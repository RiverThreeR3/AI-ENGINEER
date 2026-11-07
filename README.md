# Raphael Ribeiro — AI Engineering

**Python APIs · Retrieval systems · Evaluations · Safety-conscious automation**

This portfolio highlights inspectable engineering implementations and their current evidence. Each project links to source code, tests or a pull request. A **passing CI run is not a production deployment**, and an open pull request is not merged work.

## Featured engineering work

| Project | What is implemented | Evidence | Current state |
| --- | --- | --- | --- |
| **[Knowledge API](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2)** | A FastAPI document search/answer service using deterministic lexical retrieval, source-line citations, abstention and synthetic evaluation cases. Source code lives in the separate public AGESOMA-PROJECTS repository. | [Implementation and tests](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/tree/62ccc7e4584bfcf68f07de2706a75580828c6715/projects/knowledge-api) · [CI at the reviewed SHA](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/actions/runs/42366822290) | **Open PR**, CI passed on `62ccc7e`; no LLM, private-document ingestion or deployment |
| **[AI Request Budget Guard](https://github.com/RiverThreeR3/AIEngineer/pull/1)** | A typed FastAPI endpoint that estimates per-request model cost with `Decimal`, validates input, requires an API key and applies a process-local rate limiter. | [Source and tests in PR](https://github.com/RiverThreeR3/AIEngineer/tree/6a3b11f38e41b857326bcbf99e97ed3a34b07b65/tracks/01-python-apis) · [CI at the reviewed SHA](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41823927651) | **Open PR**, CI passed on `6a3b11f`; merge conflict pending; no provider billing or production enforcement |
| **[InstantCloser Decision Policy Lab](projects/instantcloser/README.md)** | Side-effect-free Python rules for consent, opt-out, objections, scheduling requests, pricing requests and an illustrative injection-pattern check, with 11 hand-authored synthetic scenarios. | [Decision engine](projects/instantcloser/agent.py) · [Regression tests](projects/instantcloser/tests/test_agent.py) · [Evaluator](projects/instantcloser/evaluate.py) | **Code in main**; reproducible demo, not a deployed agent or real-model evaluation |
| **[RAG Production](https://github.com/raphaelribeirob/rag-production)** | A separate work-in-progress retrieval pipeline using FastAPI, PostgreSQL/pgvector, embeddings, citations and evaluation tooling. | [Code and project evaluation notes](https://github.com/raphaelribeirob/rag-production) | **Work in progress**; repository reports real-model faithfulness below its target; not independently rerun in this review |

### Experimental, not yet a demonstrated result

[Agent Benchmark](https://github.com/raphaelribeirob/agent-benchmark) contains a proposed comparison framework for agent self-correction. Its own README identifies it as a **scaffold with no completed benchmark runs or measured results**. It is not presented as a finished project.

## How to review the work

1. Open the linked code or pull request and inspect the actual inputs, outputs and tests.
2. For a CI claim, compare the workflow run's commit SHA with the project revision.
3. Read the documented limitations: synthetic tests, local demonstrations and production systems are different levels of evidence.

These are public engineering artifacts, not claims of customer delivery, verified commercial outcomes or individual authorship of every commit. Contribution and ownership should be checked against the relevant Git history and reviews.

## Technical approach

**Define the contract → implement a deterministic baseline → test failure modes → evaluate quality and safety → document what was actually observed.**

Current focus: completing the acceptance and security/evaluation checks for [Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2). [Budget Guard PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) remains in the maintenance/audit queue.

## More detail

- [Project evidence and remaining gaps](PROJECTS.md)
- [Engineering evidence guide](docs/RECRUITER_GUIDE.md)
- [Engineering standards](ENGINEERING_STANDARDS.md)
- [Learning tracks and future work](ROADMAP.md)
- [Course-to-practice mapping](docs/COURSE_MAPPING.md)

Learning-track folders document requirements and intended work; they do **not** represent completed projects. No live deployment or client outcome is implied by an architectural design, a tutorial or a passing CI badge.
