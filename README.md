<div align="center">

<!-- ─────────────────────────  HEADER  ───────────────────────── -->

<img src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=600&size=26&duration=3200&pause=900&color=6C8EBF&center=true&vCenter=true&width=760&lines=Hi%2C+I'm+Hammad+Ahmad;AI+%2F+Machine+Learning+Engineer;LLMs+%C2%B7+RAG+%C2%B7+Knowledge+Graphs;I+build+retrieval+systems+that+cite+their+sources" alt="AI / Machine Learning Engineer — LLMs, RAG, Knowledge Graphs" />

**MSc Applied Artificial Intelligence & Data Analytics (Merit)** · University of Bradford<br>
Bradford, UK — open to relocation

<br>

<a href="https://hammadahmad.co.uk">
  <img src="https://img.shields.io/badge/Portfolio-hammadahmad.co.uk-1a1a1a?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Portfolio" />
</a>
<a href="https://www.linkedin.com/in/hammadahmad123">
  <img src="https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="mailto:hammadahmad.ml@gmail.com">
  <img src="https://img.shields.io/badge/Email-Say%20hello-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>
<a href="https://orcid.org/0009-0000-7873-4977">
  <img src="https://img.shields.io/badge/ORCID-0009--0000--7873--4977-A6CE39?style=for-the-badge&logo=orcid&logoColor=white" alt="ORCID" />
</a>
<a href="https://doi.org/10.1007/978-3-031-66854-8_1">
  <img src="https://img.shields.io/badge/Publication-Springer-0B7285?style=for-the-badge&logo=springer&logoColor=white" alt="Springer publication" />
</a>

</div>

---

## About

I build **retrieval systems that pair vector embeddings with knowledge graphs**, benchmark predictive models on large real-world datasets, and take both to production — retrieval design, backend APIs, deployment.

- 🔬 Most recent research: **FinLaw-UK**, a graph-augmented RAG system over UK financial regulation where every citation is verified against a Neo4j knowledge graph before it reaches the user.
- 📄 First-author and corresponding-author on a **peer-reviewed Springer publication** (ICSMAI 2024, Morocco).
- ⚙️ Shipped an AI voice-agent platform that handled **2,100+ outbound calls** and cut mean call latency **54%** (2.4s → 1.1s).
- 🧪 Benchmarked **11 classifiers over 253,680 CDC BRFSS records** for diabetes risk, with resampling correctly confined to training folds.
- 🎯 Currently open to **AI/ML engineering and research roles**, and applying for **PhD / postdoc positions** (including MSCA-eligible programmes) for October 2026 starts.

---

## Featured work

<table>
<tr>
<td width="50%" valign="top">

### 🏛️ [finlaw-uk](https://github.com/1oNN/finlaw-uk)
**Graph-augmented RAG over UK financial regulation**

Hybrid BM25 + BGE-small retrieval with reciprocal rank fusion, Mistral 7B-Instruct served locally via Ollama, and a Neo4j knowledge graph that verifies every citation — provisions absent from the graph are flagged as potential hallucinations.

`0.82` source accuracy · `0.81` citation quality<br>
`0.76` RAGAS faithfulness · `0.74` answer relevance<br>
*110-item benchmark · MSc dissertation*

</td>
<td width="50%" valign="top">

### 🩺 [diabetes-app](https://github.com/1oNN/diabetes-app)
**11-classifier benchmark + screening tool**

Diabetes risk on CDC BRFSS 2015, comparing random over-sampling, SMOTE and ADASYN with resampling confined to the training folds. Shipped as a lab-free, 19-question screening app.

Random Forest best on ROC-AUC and sensitivity<br>
`253,680` records · `14%` positive class<br>
*Flask + React*

</td>
</tr>
<tr>
<td width="50%" valign="top">

### 🎙️ [VoiceFlow](https://github.com/1oNN/VoiceFlow)
**Privacy-first call transcription**

Retell call exporter with **local** Whisper transcription (large-v3) — call audio never crosses another trust boundary.

Async jobs · live SSE progress<br>
One-command Docker deploy

</td>
<td width="50%" valign="top">

### 😴 [sleep-efficiency-app](https://github.com/1oNN/sleep-efficiency-app)
**The model behind my ICSMAI 2024 paper**

Four regression models compared, winner served behind a Flask form.

Random Forest `R² 0.8569` (MSE 0.0027)<br>
*First-author, corresponding author*

</td>
</tr>
<tr>
<td colspan="2" valign="top">

### 🔎 Jobzyl — [jobzyl.com](https://jobzyl.com)
**Job-search aggregator** · 20 live boards across 60+ countries, searched in parallel and streamed over SSE. First results in **~1.4s**, backed by 11 RLS-locked Supabase tables.

</td>
</tr>
</table>

<div align="center">

**Full case studies, with architecture diagrams and the decisions behind them → [hammadahmad.co.uk/projects](https://hammadahmad.co.uk/projects)**

</div>

---

## Publication

> **Ahmad, H.** *(first & corresponding author)*, Khan, M.U., Azam, M. (2024).<br>
> **Comparative Analysis of Machine Learning Methods for Enhancing Sleep Efficiency and Prediction.**<br>
> In: Serrhini, M., Ghoumid, K. (eds) *Advances in Smart Medical, IoT & Artificial Intelligence*, ICSMAI 2024.<br>
> Information Systems Engineering and Management, vol 12, pp. 3–15. Springer, Cham.<br>
> Presented at ICSMAI 2024, Saidia, Morocco, 18–20 April 2024.<br>
> **DOI:** [10.1007/978-3-031-66854-8_1](https://doi.org/10.1007/978-3-031-66854-8_1)

**Software & data release** — the FinLaw-UK implementation and a 110-item UK financial-regulation QA benchmark (factual questions, document tasks and case scenarios) are open at [github.com/1oNN/finlaw-uk](https://github.com/1oNN/finlaw-uk).

---

## Tech stack

<table>
<tr><td><b>ML & NLP</b></td><td>

![PyTorch](https://img.shields.io/badge/PyTorch-EE4C2C?style=flat-square&logo=pytorch&logoColor=white)
![TensorFlow](https://img.shields.io/badge/TensorFlow-FF6F00?style=flat-square&logo=tensorflow&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white)
![XGBoost](https://img.shields.io/badge/XGBoost-1B7A3D?style=flat-square)
![LightGBM](https://img.shields.io/badge/LightGBM-2C6E49?style=flat-square)
![Hugging Face](https://img.shields.io/badge/Sentence%20Transformers-FFD21E?style=flat-square&logo=huggingface&logoColor=black)
![MLflow](https://img.shields.io/badge/MLflow-0194E2?style=flat-square&logo=mlflow&logoColor=white)

</td></tr>
<tr><td><b>Retrieval & knowledge</b></td><td>

![RAG](https://img.shields.io/badge/RAG-6C8EBF?style=flat-square)
![Hybrid retrieval](https://img.shields.io/badge/BM25%20%2B%20Dense-6C8EBF?style=flat-square)
![Cross-encoder re-ranking](https://img.shields.io/badge/Cross--encoder%20re--ranking-6C8EBF?style=flat-square)
![RAGAS](https://img.shields.io/badge/RAGAS-6C8EBF?style=flat-square)
![Neo4j](https://img.shields.io/badge/Neo4j-4581C3?style=flat-square&logo=neo4j&logoColor=white)
![Ollama](https://img.shields.io/badge/Ollama-000000?style=flat-square&logo=ollama&logoColor=white)

</td></tr>
<tr><td><b>Engineering</b></td><td>

![Python](https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white)
![C++](https://img.shields.io/badge/C++-00599C?style=flat-square&logo=cplusplus&logoColor=white)
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=flat-square&logo=typescript&logoColor=white)
![SQL](https://img.shields.io/badge/SQL-336791?style=flat-square&logo=postgresql&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white)
![React](https://img.shields.io/badge/React-61DAFB?style=flat-square&logo=react&logoColor=black)
![Next.js](https://img.shields.io/badge/Next.js-000000?style=flat-square&logo=nextdotjs&logoColor=white)

</td></tr>
<tr><td><b>Data & infra</b></td><td>

![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![pandas](https://img.shields.io/badge/pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=flat-square&logo=numpy&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white)
![GitHub Actions](https://img.shields.io/badge/GitHub%20Actions-2088FF?style=flat-square&logo=githubactions&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-232F3E?style=flat-square&logo=amazonwebservices&logoColor=white)
![GCP](https://img.shields.io/badge/GCP-4285F4?style=flat-square&logo=googlecloud&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=flat-square&logo=linux&logoColor=black)

</td></tr>
</table>

---

## GitHub

<div align="center">

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api?username=1oNN&show_icons=true&hide_border=true&theme=github_dark&icon_color=6C8EBF&hide=issues" />
  <img src="https://github-readme-stats.vercel.app/api?username=1oNN&show_icons=true&hide_border=true&theme=graywhite&icon_color=1F6FEB&hide=issues" alt="GitHub stats" height="165" />
</picture>
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://github-readme-stats.vercel.app/api/top-langs/?username=1oNN&layout=compact&hide_border=true&langs_count=8&theme=github_dark" />
  <img src="https://github-readme-stats.vercel.app/api/top-langs/?username=1oNN&layout=compact&hide_border=true&langs_count=8&theme=graywhite" alt="Top languages" height="165" />
</picture>

<br>

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://streak-stats.demolab.com?user=1oNN&hide_border=true&theme=github-dark-blue" />
  <img src="https://streak-stats.demolab.com?user=1oNN&hide_border=true&theme=graywhite" alt="Contribution streak" height="165" />
</picture>

<br><br>

<!-- Requires the snake workflow (see setup notes) — delete these three lines if you skip it -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://raw.githubusercontent.com/1oNN/1oNN/output/github-snake-dark.svg" />
  <img src="https://raw.githubusercontent.com/1oNN/1oNN/output/github-snake.svg" alt="Contribution graph" />
</picture>

</div>

---

## Experience

<details open>
<summary><b>AI / Machine Learning Engineer</b> — Outlyst · Oct 2025 – Mar 2026 · Leeds, UK / Remote</summary>

<br>

*Fixed-term contract.* Built and deployed an AI voice-agent system for outbound calling (Retell AI, FastAPI): backend dialogue-flow logic, automated call flows, lead-qualification rules, gatekeeper detection and callback scheduling.

- Handled **2,100+ calls** and cut manual calling workload by roughly **50%**
- Profiled async I/O and connection pooling to reduce mean call latency **54%** (2.4s → 1.1s)
- Built an internal micro-CRM for lead tracking, removing external CRM licensing costs

</details>

<details>
<summary><b>Research Assistant, Machine Learning & LLMs</b> — University of Bradford · Jan 2025 – Sep 2025</summary>

<br>

Designed and evaluated **FinLaw-UK**, also my MSc dissertation project: Mistral 7B served locally via Ollama, paired with a Neo4j knowledge graph, over the FCA Handbook, PRA Rulebook, FRC standards and statutory sources.

- Engineered the retrieval pipeline — clause-level segmentation, Sentence Transformer embeddings, cross-encoder re-ranking, graph-grounded citation verification
- Built the evaluation harness, extending RAGAS with custom citation-precision and legal-completeness metrics
- Supervised by Dr Tillal Eldabi and Dr Irfan Mehmood

</details>

<details>
<summary><b>Research Assistant, Data Science</b> — COMSATS University Islamabad · Jul 2023 – Jul 2024</summary>

<br>

Benchmarked **11 classifiers** for diabetes risk on 253,680 CDC BRFSS records, correcting the 86/14 class imbalance with random over-sampling after comparing it against SMOTE and ADASYN, with resampling confined to the training folds.

- Analysed 20+ demographic, lifestyle and clinical indicators — age, general health, BMI, blood pressure and income emerged as the strongest correlates
- Deployed the winning model behind a REST API with SHAP-based interpretability

</details>

---

## Education

<details>
<summary><b>MSc, Applied Artificial Intelligence & Data Analytics (Merit)</b> — University of Bradford · 2024–2025</summary>

<br>

**Dissertation:** *FinLaw-UK: A Graph-Augmented Retrieval Chatbot for Reliable and Transparent UK Financial Regulation*

Modules included Artificial Intelligence and Data Science (79), Business Data Analytics (79), and Responsible AI: Ethics, Law and Governance (75).

</details>

<details>
<summary><b>BS, Bioinformatics</b> — COMSATS University Islamabad · 2020–2024</summary>

<br>

**Thesis:** *AI-Assisted Analysis and Prediction of At-Risk Diabetic Individuals* — graded A.

</details>

---

## Open to

**Full-time AI/ML engineering and research roles — available now.** Also applying for **PhD and postdoc positions**, including MSCA-eligible programmes in the EU, for start dates from October 2026.

🇬🇧 Right to work in the UK on the Graduate Route to **December 2027** — no sponsorship required.

**Research interests**<br>
`graph-augmented retrieval` · `LLM faithfulness evaluation` · `systems optimisation for high-throughput ML pipelines` · `interpretable clinical modelling`

**Languages**<br>
English (IELTS 7.0, CEFR C1) · Urdu (native) · German (A1.2)

Currently working as a Quality Control Assistant at Myton Food Group (Morrisons), Bradford, while pursuing AI/ML roles and PhD applications.

---

<div align="center">

### Let's talk

If you're working on retrieval, evaluation, or anything where a model needs to show its sources — I'd like to hear about it.

<a href="mailto:hammadahmad.ml@gmail.com">
  <img src="https://img.shields.io/badge/hammadahmad.ml@gmail.com-EA4335?style=for-the-badge&logo=gmail&logoColor=white" alt="Email" />
</a>
<a href="https://www.linkedin.com/in/hammadahmad123">
  <img src="https://img.shields.io/badge/in/hammadahmad123-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn" />
</a>
<a href="https://hammadahmad.co.uk">
  <img src="https://img.shields.io/badge/hammadahmad.co.uk-1a1a1a?style=for-the-badge&logo=googlechrome&logoColor=white" alt="Website" />
</a>

<br><br>

<img src="https://komarev.com/ghpvc/?username=1oNN&style=flat-square&color=6C8EBF&label=Profile+views" alt="Profile views" />

</div>
