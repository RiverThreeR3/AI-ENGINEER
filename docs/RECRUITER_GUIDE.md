# Engineering Evidence — Raphael Ribeiro

A short guide to **what is implemented and publicly inspectable**. This page is not a training transcript, a list of planned products or a claim of client delivery.

## Current implementations

### 1. Knowledge API — cited document retrieval

**What it does:** A FastAPI service searches five synthetic policy documents, scores lexical matches and returns source-line citations or abstains when no matching evidence is found. It is an extractive baseline, **not** an LLM-based RAG product.

**Inspect:** [Open PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2) · [code and tests at `62ccc7e`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/tree/62ccc7e4584bfcf68f07de2706a75580828c6715/projects/knowledge-api) · [GitHub Actions run for this SHA](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42366822290).

**Observed state:** CI completed successfully for the reviewed commit. The PR is open; there is no verified deployment, live customer data, tenant authorization or independent held-out quality result. Source code is maintained in AGESOMA-PROJECTS, not duplicated here.

### 2. AI Request Budget Guard — bounded cost estimation API

**What it does:** A FastAPI endpoint calculates estimated per-request cost using strict numeric contracts and `Decimal`. The proposed service includes an API-key check, request-size validation, per-process rate limiting and privacy-conscious request metrics.

**Inspect:** [Open PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) · [implementation at `6a3b11f`](https://github.com/RiverThreeR3/AIEngineer/tree/6a3b11f38e41b857326bcbf99e97ed3a34b07b65/tracks/01-python-apis) · [GitHub Actions run for this SHA](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41823927651).

**Observed state:** CI completed successfully on the reviewed commit. The PR remains open and currently has a merge conflict. It uses caller-supplied token counts and prices; it does not bill a provider, enforce distributed budgets or run in production.

### 3. InstantCloser Decision Policy Lab — rule-based action selection

**What it does:** A pure Python function proposes a next action for synthetic sales messages while applying consent, opt-out and objection priorities. It flags some instruction-override phrases and labels sensitive steps for human approval. The [evaluator](../projects/instantcloser/evaluate.py) compares actions against **11 hand-authored synthetic scenarios**.

**Inspect:** [Project explanation](../projects/instantcloser/README.md) · [policy code](../projects/instantcloser/agent.py) · [fixtures](../projects/instantcloser/scenarios.json) · [unit tests](../projects/instantcloser/tests/test_agent.py).

**Observed state:** Runnable code is present in `main`; tests and evaluation commands are documented. The [policy-regression workflow](https://github.com/RiverThreeR3/AIEngineer/actions/runs/42369898273) completed successfully on documentation PR #8 (`c112c64`): 6 unit tests and all 11 synthetic evaluator cases passed. This verifies the same unchanged lab code on that review branch, not independent real-world quality. The lab executes no external actions and does not establish real-model security, customer outcomes or production readiness.

### 4. RAG Production — retrieval and faithfulness measurement

**What it does:** A separate work-in-progress pipeline combines document ingestion, embedding retrieval over PostgreSQL/pgvector, answer providers, citations and evaluation tooling.

**Inspect:** [Public source, architecture and evaluation report](https://github.com/raphaelribeirob/rag-production).

**Observed state:** Its own README reports a prior local real-model faithfulness score of **0.647**, below the project threshold **0.85**. Those figures were **not independently rerun** in this audit. It remains work in progress, with unresolved groundedness and security/observability gaps.

## Experimental work

[Agent Benchmark](https://github.com/raphaelribeirob/agent-benchmark) is currently a scaffold for comparing agents with and without self-correction. Its documented benchmark results are **not yet available**. It is not included among validated engineering results.

## What the evidence means

| Evidence | What it establishes | What it does not establish |
| --- | --- | --- |
| Source files and tests | Inspectable implementation and specified behavior | Independent test execution, reliability or personal authorship |
| CI linked to a commit SHA | A recorded pipeline result on that revision | Production operation or real-user quality |
| Synthetic evaluations | Behavior on their stated examples and fixtures | Generalization to production inputs or customer ROI |
| Open pull request | Proposed, inspectable changes | Merge, release, deployed service or accepted customer work |

Only attributable contributions and independently supported outcomes should become individual skill or resume claims. No private code, customer information or personal assessment history is included here.

For more context, see [project status and next gates](../PROJECTS.md), [engineering standards](../ENGINEERING_STANDARDS.md) and [technical learning roadmap](../ROADMAP.md).
