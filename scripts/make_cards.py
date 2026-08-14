#!/usr/bin/env python3
"""
Generates GitHub profile stat cards as SVG, no personal access token needed.

Runs inside GitHub Actions using the built-in GITHUB_TOKEN, which is enough
because every endpoint used here reads PUBLIC data only.

Outputs six files (light + dark for each card):
    metrics.svg              metrics-dark.svg
    metrics.languages.svg    metrics.languages-dark.svg
    streak.svg               streak-dark.svg
"""

import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timedelta, timezone
from xml.sax.saxutils import escape

USER = os.environ.get("GH_USER", "1oNN")
TOKEN = os.environ.get("GITHUB_TOKEN", "")
API = "https://api.github.com"

ACCENT = "#6C8EBF"

THEMES = {
    "light": dict(bg="#ffffff", border="#d0d7de", text="#1f2328",
                  muted="#656d76", track="#eaeef2"),
    "dark":  dict(bg="#0d1117", border="#30363d", text="#e6edf3",
                  muted="#8b949e", track="#21262d"),
}

# GitHub's own language colours for the ones most likely to show up here.
LANG_COLORS = {
    "Python": "#3572A5", "Jupyter Notebook": "#DA5B0B", "TypeScript": "#3178c6",
    "JavaScript": "#f1e05a", "HTML": "#e34c26", "CSS": "#563d7c",
    "C++": "#f34b7d", "C": "#555555", "C#": "#178600", "Java": "#b07219",
    "Shell": "#89e051", "Dockerfile": "#384d54", "Makefile": "#427819",
    "R": "#198CE7", "Rust": "#dea584", "Go": "#00ADD8", "Ruby": "#701516",
    "PHP": "#4F5D95", "Swift": "#F05138", "Kotlin": "#A97BFF",
    "SCSS": "#c6538c", "Vue": "#41b883", "Svelte": "#ff3e00",
    "TeX": "#3D6117", "Cypher": "#4581C3", "MDX": "#fcb32c",
    "PowerShell": "#012456", "Batchfile": "#C1F12E", "Procfile": "#a91e50",
}
FALLBACK_PALETTE = ["#6C8EBF", "#8FBF6C", "#BF6C8E", "#BFA36C", "#6CBFB8",
                    "#9A6CBF", "#BF7A6C", "#6C7ABF"]

FONT = ("-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif")


# ───────────────────────────── data ──────────────────────────────

def api(path):
    req = urllib.request.Request(API + path)
    req.add_header("Accept", "application/vnd.github+json")
    req.add_header("User-Agent", "profile-cards")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        return json.loads(r.read().decode())


GRAPHQL = "https://api.github.com/graphql"

CALENDAR_QUERY = """
query($user:String!, $from:DateTime!, $to:DateTime!) {
  user(login:$user) {
    contributionsCollection(from:$from, to:$to) {
      contributionCalendar {
        weeks { contributionDays { date contributionCount } }
      }
    }
  }
}
"""


def graphql(query, variables):
    body = json.dumps({"query": query, "variables": variables}).encode()
    req = urllib.request.Request(GRAPHQL, data=body, method="POST")
    req.add_header("Content-Type", "application/json")
    req.add_header("User-Agent", "profile-cards")
    if TOKEN:
        req.add_header("Authorization", f"Bearer {TOKEN}")
    with urllib.request.urlopen(req, timeout=30) as r:
        payload = json.loads(r.read().decode())
    if payload.get("errors"):
        raise RuntimeError(payload["errors"][0].get("message", "graphql error"))
    return payload["data"]


def contribution_days(created_at):
    """Merge every year's calendar into one {date: count} map.

    contributionsCollection caps each query at one year, so walk year by year
    from signup. Weeks straddle year boundaries, hence the dict rather than a
    running total: duplicated days collapse instead of counting twice.
    """
    start = datetime.strptime(created_at, "%Y-%m-%dT%H:%M:%SZ").replace(tzinfo=timezone.utc)
    today = datetime.now(timezone.utc)
    days = {}

    for year in range(start.year, today.year + 1):
        frm = max(start, datetime(year, 1, 1, tzinfo=timezone.utc))
        to = min(today, datetime(year, 12, 31, 23, 59, 59, tzinfo=timezone.utc))
        if frm > to:
            continue
        data = graphql(CALENDAR_QUERY, {
            "user": USER,
            "from": frm.strftime("%Y-%m-%dT%H:%M:%SZ"),
            "to": to.strftime("%Y-%m-%dT%H:%M:%SZ"),
        })
        weeks = data["user"]["contributionsCollection"]["contributionCalendar"]["weeks"]
        for week in weeks:
            for day in week["contributionDays"]:
                days[day["date"]] = day["contributionCount"]

    cutoff = today.strftime("%Y-%m-%d")
    days = {d: c for d, c in days.items() if d <= cutoff}
    if not days:
        # Better to fail the run and keep yesterday's committed card than to
        # publish a card full of zeroes because the token lost calendar access.
        raise RuntimeError("contribution calendar came back empty")
    return days


def streaks(days):
    if not days:
        return dict(total=0, current=0, current_from="", current_to="",
                    longest=0, longest_from="", longest_to="", first="")

    dates = sorted(days)
    today = datetime.now(timezone.utc).strftime("%Y-%m-%d")

    longest = run = 0
    longest_from = longest_to = run_from = ""
    for d in dates:
        if days[d] > 0:
            run = run + 1 if run else 1
            if run == 1:
                run_from = d
            if run > longest:
                longest, longest_from, longest_to = run, run_from, d
        else:
            run = 0

    # A quiet today does not break the streak yet, so start counting at
    # yesterday in that case. Two quiet days in a row and it is over.
    cursor = datetime.strptime(today, "%Y-%m-%d").replace(tzinfo=timezone.utc)
    if days.get(today, 0) == 0:
        cursor -= timedelta(days=1)

    current = 0
    current_to = cursor.strftime("%Y-%m-%d")
    while days.get(cursor.strftime("%Y-%m-%d"), 0) > 0:
        current += 1
        cursor -= timedelta(days=1)
    current_from = (cursor + timedelta(days=1)).strftime("%Y-%m-%d") if current else ""

    return dict(
        total=sum(days.values()),
        current=current,
        current_from=current_from,
        current_to=current_to if current else today,
        longest=longest,
        longest_from=longest_from,
        longest_to=longest_to,
        first=dates[0],
    )


def gather():
    user = api(f"/users/{USER}")

    repos, page = [], 1
    while True:
        batch = api(f"/users/{USER}/repos?per_page=100&type=owner&page={page}")
        repos.extend(batch)
        if len(batch) < 100:
            break
        page += 1

    owned = [r for r in repos if not r.get("fork")]
    stars = sum(r.get("stargazers_count", 0) for r in owned)

    langs = {}
    for r in owned:
        if r.get("size", 0) == 0:
            continue
        try:
            for name, count in api(f"/repos/{r['full_name']}/languages").items():
                langs[name] = langs.get(name, 0) + count
        except urllib.error.HTTPError:
            continue

    return dict(
        name=user.get("name") or USER,
        repos=len(owned),
        stars=stars,
        followers=user.get("followers", 0),
        langs=langs,
        streak=streaks(contribution_days(user["created_at"])),
    )


def mock():
    return dict(
        name="Hammad Ahmad", repos=14, stars=27, followers=9,
        langs={"Python": 812_000, "Jupyter Notebook": 402_000,
               "TypeScript": 233_000, "HTML": 96_000, "CSS": 61_000,
               "JavaScript": 40_000, "Dockerfile": 9_000, "Shell": 6_500},
        streak=dict(total=1994, current=12, current_from="2026-08-03",
                    current_to="2026-08-14", longest=48,
                    longest_from="2025-02-11", longest_to="2025-03-30",
                    first="2021-10-21"),
    )


# ───────────────────────────── render ────────────────────────────

def shell(w, h, t, title, body):
    return f"""<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" role="img" aria-label="{escape(title)}">
  <style>
    .t {{ font-family:{FONT}; }}
    .title {{ font-size:14px; font-weight:600; fill:{ACCENT}; }}
    .big {{ font-size:26px; font-weight:700; fill:{t['text']}; }}
    .lbl {{ font-size:11px; font-weight:500; fill:{t['muted']}; letter-spacing:.3px; }}
    .lang {{ font-size:12px; font-weight:500; fill:{t['text']}; }}
    .pct {{ font-size:12px; font-weight:400; fill:{t['muted']}; }}
    .date {{ font-size:10px; font-weight:400; fill:{t['muted']}; }}
    .accent {{ fill:{ACCENT}; }}
  </style>
  <rect x="0.5" y="0.5" width="{w-1}" height="{h-1}" rx="8"
        fill="{t['bg']}" stroke="{t['border']}"/>
  <text x="24" y="34" class="t title">{escape(title)}</text>
{body}
</svg>
"""


def card_overview(d, t):
    w, h = 460, 195
    cells = [(f"{d['repos']}", "PUBLIC REPOS"), (f"{d['stars']}", "TOTAL STARS"),
             (f"{d['followers']}", "FOLLOWERS"), (f"{len(d['langs'])}", "LANGUAGES")]
    out = []
    for i, (val, lab) in enumerate(cells):
        x = 24 + (i % 2) * 220
        y = 88 + (i // 2) * 62
        out.append(f'  <text x="{x}" y="{y}" class="t big">{escape(val)}</text>')
        out.append(f'  <text x="{x}" y="{y+18}" class="t lbl">{escape(lab)}</text>')
    out.insert(0, f'  <text x="24" y="56" class="t lbl">{escape(d["name"].upper())}</text>')
    return shell(w, h, t, "GitHub overview", "\n".join(out))


def card_languages(d, t):
    w, h = 460, 195
    total = sum(d["langs"].values()) or 1
    top = sorted(d["langs"].items(), key=lambda kv: -kv[1])[:8]
    shown = sum(v for _, v in top) or 1

    bar_x, bar_y, bar_w, bar_h = 24, 56, w - 48, 10
    out = [f'  <clipPath id="bar"><rect x="{bar_x}" y="{bar_y}" width="{bar_w}" '
           f'height="{bar_h}" rx="{bar_h/2}"/></clipPath>',
           f'  <rect x="{bar_x}" y="{bar_y}" width="{bar_w}" height="{bar_h}" '
           f'rx="{bar_h/2}" fill="{t["track"]}"/>',
           '  <g clip-path="url(#bar)">']

    cursor = float(bar_x)
    for i, (name, val) in enumerate(top):
        seg = bar_w * (val / shown)
        colour = LANG_COLORS.get(name, FALLBACK_PALETTE[i % len(FALLBACK_PALETTE)])
        out.append(f'    <rect x="{cursor:.2f}" y="{bar_y}" width="{seg:.2f}" '
                   f'height="{bar_h}" fill="{colour}"/>')
        cursor += seg
    out.append("  </g>")

    for i, (name, val) in enumerate(top):
        col, row = i % 2, i // 2
        x = 24 + col * 220
        y = 100 + row * 24
        colour = LANG_COLORS.get(name, FALLBACK_PALETTE[i % len(FALLBACK_PALETTE)])
        label = name if len(name) <= 17 else name[:16] + "…"
        out.append(f'  <circle cx="{x+5}" cy="{y-4}" r="5" fill="{colour}"/>')
        out.append(f'  <text x="{x+18}" y="{y}" class="t lang">{escape(label)}</text>')
        out.append(f'  <text x="{x+196}" y="{y}" text-anchor="end" class="t pct">'
                   f'{val/total*100:.1f}%</text>')

    return shell(w, h, t, "Most used languages", "\n".join(out))


MONTHS = ["Jan", "Feb", "Mar", "Apr", "May", "Jun",
          "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]


def pretty(iso):
    # %-d is not portable to Windows, so build it by hand.
    if not iso:
        return ""
    d = datetime.strptime(iso, "%Y-%m-%d")
    return f"{MONTHS[d.month - 1]} {d.day}, {d.year}"


def card_streak(d, t):
    # Wider than the other cards: three date ranges need the room, and at 460
    # the longest of them sits ~5px off the divider rules.
    w, h = 495, 195
    s = d["streak"]

    span = f"{pretty(s['first'])} - {pretty(s['current_to'])}" if s["first"] else ""
    cur = f"{pretty(s['current_from'])} - {pretty(s['current_to'])}" if s["current"] else pretty(s["current_to"])
    lng = f"{pretty(s['longest_from'])} - {pretty(s['longest_to'])}" if s["longest"] else ""

    cells = [
        (f"{s['total']:,}", "TOTAL CONTRIBUTIONS", span, False),
        (f"{s['current']}", "CURRENT STREAK", cur, True),
        (f"{s['longest']}", "LONGEST STREAK", lng, False),
    ]

    col = (w - 48) / 3
    out = []
    for i, (val, lab, sub, hot) in enumerate(cells):
        cx = 24 + col * i + col / 2
        klass = "t big accent" if hot else "t big"
        out.append(f'  <text x="{cx:.1f}" y="{100}" text-anchor="middle" class="{klass}">{escape(val)}</text>')
        out.append(f'  <text x="{cx:.1f}" y="{124}" text-anchor="middle" class="t lbl">{escape(lab)}</text>')
        if sub:
            out.append(f'  <text x="{cx:.1f}" y="{146}" text-anchor="middle" class="t date">{escape(sub)}</text>')

    for i in (1, 2):
        x = 24 + col * i
        out.append(f'  <line x1="{x:.1f}" y1="70" x2="{x:.1f}" y2="160" stroke="{t["border"]}"/>')

    return shell(w, h, t, "Contribution streak", "\n".join(out))


def main():
    data = mock() if "--mock" in sys.argv else gather()
    outdir = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else "."

    files = {
        "metrics.svg":               card_overview(data, THEMES["light"]),
        "metrics-dark.svg":          card_overview(data, THEMES["dark"]),
        "metrics.languages.svg":     card_languages(data, THEMES["light"]),
        "metrics.languages-dark.svg": card_languages(data, THEMES["dark"]),
        "streak.svg":                card_streak(data, THEMES["light"]),
        "streak-dark.svg":           card_streak(data, THEMES["dark"]),
    }
    for name, svg in files.items():
        with open(os.path.join(outdir, name), "w") as f:
            f.write(svg)
        print("wrote", name)


if __name__ == "__main__":
    main()
