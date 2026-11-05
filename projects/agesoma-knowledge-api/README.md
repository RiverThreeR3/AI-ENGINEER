# Applied AI Engineering — AGESOMA Knowledge API

**Status:** Cross-referenced learning case. The implementation lives in **one public source repository**, [AGESOMA-PROJECTS](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2). No code is duplicated here. It remains in an open PR and has not been independently deployed to production.

## What the project demonstrates

- Building a typed FastAPI interface for search and document-grounded responses.
- Engineering a transparent lexical retrieval baseline before using embeddings or LLMs.
- Reporting document name and line number as auditable source evidence.
- Abstaining when source terms do not support an answer.
- Creating regression tests and a synthetic evaluation set with explicit acceptance thresholds.
- Running CI, Python lint, tests, Docker build and smoke checks.

## Verified evidence

The original AGESOMA-PROJECTS branch produced **25 passing tests, Ruff lint success, synthetic recall@1 1.0 (9 known cases), synthetic unknown-question abstention 1.0 (3 cases), and successful Docker smoke** in [GitHub Actions run 41942623996](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/41942623996). These are *small synthetic tests* and do not demonstrate real-world RAG model quality, operational security or production deployment.

**Implementation source:** [Knowledge API project](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/tree/feat/knowledge-api-baseline-20261104/projects/knowledge-api)

## Lesson — What is a retrieval baseline?

A retrieval baseline is a simple, measurable search system against which more expensive architectures can be compared. Here we normalize words, remove common stop words and score sentence-level passages by shared terms weighted using inverse document frequency. Unlike a language model, this system cannot generate new claims. It returns source text verbatim or abstains.

**Trade-off:** deterministic lexical retrieval is cheap, interpretable and reproducible, but struggles with synonyms, paraphrases, ambiguous requests and multi-document synthesis. Evaluating these failures should precede adding an embedding model or agent framework.

## Practical exercise (10–20 minutes)

Read `projects/knowledge-api/retrieval.py` in the linked repository and design two new synthetic questions: one using a synonym not appearing in the corpus and one mixing legitimate terms with an unrelated malicious instruction. Predict the output, add tests, and explain how you would measure a fix without changing the evaluation answers.

## Interview practice (answer in English)

**Question:** "How would you demonstrate that adding vector search improves an existing deterministic knowledge-retrieval API without introducing hallucinations or unacceptable latency?"

Evaluation rubric: technical correctness 30%, clarity 20%, trade-offs 20%, production considerations 20%, English communication 10%.

## Next gate

Recheck the current AGESOMA-PROJECTS PR CI status, then create a separately authored evaluation set, document failure modes, and compare against an embeddings/pgvector option only if the market demand and evaluation justify it.
