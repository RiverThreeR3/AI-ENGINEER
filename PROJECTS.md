# Engineering Projects — Evidence Index

**Reviewed:** 2026-11-07. This page distinguishes code that can be inspected today from open PRs, planned work and results that have not been independently reproduced.

## Work with inspectable implementations

| Project | Problem and current implementation | Evidence inspected | State and next gate |
| --- | --- | --- | --- |
| **[Knowledge API](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2)** | Retrieve relevant passages from a fixed synthetic policy corpus and return verbatim answers with source-line citations. FastAPI endpoints use typed validation, whole-word lexical scoring and explicit abstention for unsupported queries. No LLM is used. | [Code/test directory at `62ccc7e`](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/tree/62ccc7e4584bfcf68f07de2706a75580828c6715/projects/knowledge-api) · [CI success for exact SHA](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42366822290) | **Open PR, not deployed.** Synthetic evaluation only. Next: independent holdout questions, false-positive retrieval analysis, security and access-control design. |
| **[AI Request Budget Guard](https://github.com/RiverThreeR3/AIEngineer/pull/1)** | Estimate a theoretical per-request model cost using Decimal arithmetic and caller-supplied prices/tokens. API-key check, input/body limits, basic request telemetry and a single-process rate limiter are included in the proposal. | [Code/tests at `6a3b11f`](https://github.com/RiverThreeR3/AIEngineer/tree/6a3b11f38e41b857326bcbf99e97ed3a34b07b65/tracks/01-python-apis) · [CI success for exact SHA](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41823927651) | **Open PR, not mergeable at inspection and not deployed.** Next: review conflict and independently verify safety and updated CI; do not equate estimated cost with provider billing. |
| **[InstantCloser Decision Policy Lab](projects/instantcloser/README.md)** | Evaluate a deterministic, side-effect-free policy that proposes actions based on consent, opt-out, objection, booking, pricing and suspicious instruction patterns. | [Code](projects/instantcloser/agent.py) · [11 synthetic scenarios](projects/instantcloser/scenarios.json) · [Tests](projects/instantcloser/tests/test_agent.py) · [Evaluator](projects/instantcloser/evaluate.py) | **Public demo committed to main.** No model calls, real integration, authentication or deployed service. Next: independent holdout and security/failure evaluation. |
| **[RAG Production](https://github.com/raphaelribeirob/rag-production)** | Separate WIP document ingestion/retrieval and question-answering pipeline using FastAPI, pgvector, embeddings and a configurable answer provider. Includes documented retrieval and faithfulness evaluation. | [Source and reported evaluation](https://github.com/raphaelribeirob/rag-production/blob/main/README.md) | **Work in progress.** README reports 0.647 real-model faithfulness against a 0.85 gate on a prior local evaluation; not independently rerun here. Next: investigate false grounding/abstention and add reliable security/telemetry gates. |

## Early-stage work — not a completed project

[Agent Benchmark](https://github.com/raphaelribeirob/agent-benchmark) describes an agent-with/without-self-correction experiment and includes an early aggregation scaffold. Its README reports **no benchmark runs or measured results**. It belongs in the experimental backlog until task suites, reproducible runs and evaluation evidence exist.

## One active engineering focus

The [Knowledge API](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2) is the current cross-repository technical focus. Its authoritative code lives **only** in AGESOMA-PROJECTS; this personal index links to the same public evidence rather than cloning the implementation. Contributions must be verified before being attributed as personally authored.

The [Budget Guard](https://github.com/RiverThreeR3/AIEngineer/pull/1) remains a maintenance/audit item, not a parallel expanding feature track. Work in other repositories is shown for context only; this combined workflow does not modify those repositories.

## Evidence standard

An engineering claim needs a source revision, reproducible commands, tests or evaluations with their data provenance, security boundaries and limitations. Passing tests on synthetic inputs do not establish real-world accuracy. CI does not establish deployment. An open PR does not establish a merged deliverable.

The 11 topic tracks and proposed future implementations are maintained in the [roadmap](ROADMAP.md), **not counted as existing projects**. The [engineering evidence guide](docs/RECRUITER_GUIDE.md) explains how to inspect the featured work.
