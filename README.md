# Hammad Ahmad

**AI / Machine Learning Engineer** · LLMs · RAG · Knowledge Graphs
MSc Applied Artificial Intelligence & Data Analytics (Merit), University of Bradford

Bradford, UK (open to relocation)
[hammadahmad.co.uk](https://hammadahmad.co.uk) · [hammadahmad.ml@gmail.com](mailto:hammadahmad.ml@gmail.com) · [LinkedIn](https://www.linkedin.com/in/hammadahmad123) · [ORCID](https://orcid.org/0009-0000-7873-4977)

I build retrieval systems that pair vector embeddings with knowledge graphs, benchmark predictive
models on large real-world datasets, and take both to production: retrieval design, backend APIs,
deployment. First-author peer-reviewed publication (Springer).

---

## Selected work

| Project | What it is | Measured result |
|---|---|---|
| **[finlaw-uk](https://github.com/1oNN/finlaw-uk)** | Graph-augmented RAG over UK financial regulation. Neo4j validates every citation; rules absent from the graph are flagged as potential hallucinations. MSc dissertation. | 0.82 source accuracy, 0.81 citation quality, 0.76 RAGAS faithfulness, 0.74 answer relevance on a 110-item benchmark |
| **[diabetes-app](https://github.com/1oNN/diabetes-app)** | 11-classifier benchmark on CDC BRFSS 2015, shipped as a lab-free 19-question screening app (Flask + React). | Random Forest: 93.15% accuracy, 98.4% sensitivity, 0.9887 AUC on 253,680 records |
| **[VoiceFlow](https://github.com/1oNN/VoiceFlow)** | Retell call exporter with **local** Whisper transcription (large-v3). Call audio never crosses another trust boundary. | Async jobs, live SSE progress, one-command Docker deploy |
| **[sleep-efficiency-app](https://github.com/1oNN/sleep-efficiency-app)** | The model from my first-author ICSMAI 2024 paper, served behind a Flask form. | Random Forest R² 0.8569 (MSE 0.0027), best of four models |
| **Jobzyl** ([live](https://jobzyl.com)) | Job-search aggregator: 20 live boards across 60+ countries, searched in parallel and streamed over SSE. | First results in ~1.4s; 11 RLS-locked Supabase tables |

Full case studies, with architecture diagrams and the decisions behind them:
**[hammadahmad.co.uk/projects](https://hammadahmad.co.uk/projects)**

---

## Experience

**AI / Machine Learning Engineer** - Outlyst (Oct 2025 - Mar 2026, Leeds, UK / Remote)
Built backend dialogue-flow logic and workflow automation for an AI voice-agent system (Retell AI,
FastAPI). Profiled async I/O and connection pooling to cut mean call latency 54% (2.4s to 1.1s),
sustained across 2,100+ concurrent stateful sessions. Gatekeeper detection and callback scheduling
lifted lead conversions ~25%. An internal micro-CRM with automated extraction pipelines reclaimed
100+ staff hours per week.

**Research Assistant, Machine Learning & LLMs** - University of Bradford (Jan 2025 - Sep 2025)
Built FinLaw-UK: Mistral 7B served locally via Ollama, paired with a Neo4j knowledge graph, over
FCA, PRA, FRC and statutory sources. Engineered the retrieval pipeline (clause-level segmentation,
Sentence Transformer embeddings, cross-encoder re-ranking, graph citation checks) and the evaluation
harness, extending RAGAS with custom citation-precision and legal-completeness metrics.

**Research Assistant, Data Science** - COMSATS University Islamabad (Jul 2023 - Jul 2024)
Benchmarked 11 classifiers for diabetes risk on 253,680 CDC BRFSS records under an 80/20 split,
correcting the 86/14 class imbalance with random over-sampling after comparing it against SMOTE and
ADASYN. Deployed the winning model behind a REST API with SHAP-based interpretability.

---

## Education

**MSc, Applied Artificial Intelligence & Data Analytics (Merit)** - University of Bradford, 2024-2025
Dissertation: *FinLaw-UK: A Graph-Augmented Retrieval Chatbot for Reliable and Transparent UK
Financial Regulation*

**BS, Bioinformatics** - COMSATS University Islamabad, 2020-2024
Thesis: *AI-Assisted Analysis and Prediction of At-Risk Diabetic Individuals*

---

## Publication

**Ahmad, H.** (first & corresponding author), Khan, M.U., Azam, M. (2024). *Comparative Analysis of
Machine Learning Methods for Enhancing Sleep Efficiency and Prediction.* In: Advances in Smart
Medical, IoT & Artificial Intelligence, ICSMAI 2024, Springer Nature, pp. 3-15.
Presented at ICSMAI 2024, Saidia, Morocco.
DOI: [10.1007/978-3-031-66854-8_1](https://doi.org/10.1007/978-3-031-66854-8_1)

---

## Technical skills

**Machine learning & NLP:** PyTorch, TensorFlow, scikit-learn, LLMs, RAG, Sentence Transformers, MLflow
**LLM & retrieval:** vector embeddings, semantic search, cross-encoder re-ranking, RAGAS evaluation, Neo4j knowledge graphs, Ollama
**Engineering:** Python, C++, SQL, FastAPI, Flask, REST APIs, React, Next.js
**Data & infrastructure:** PostgreSQL, Neo4j, pandas, NumPy, Docker, AWS, Git, Linux

---

## Open to

Full-time AI/ML engineering and research roles, and MSCA-eligible PhD or postdoc positions in the EU
(earliest start October 2026). Research interests: graph-augmented retrieval, LLM faithfulness
evaluation, systems optimisation for high-throughput ML pipelines, interpretable clinical modelling.

Languages: English (IELTS 7.0, CEFR C1) · Urdu (native) · German (A1.2)
