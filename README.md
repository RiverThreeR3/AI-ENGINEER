# AI Engineer

**Build reliable AI systems. Measure results. Ship usable products.**

This is the applied AI Engineering portfolio of [@raphaelribeirob](https://github.com/raphaelribeirob). It is organized around hands-on projects, reproducible evaluations, software quality, security and deployment.

**Current status:** learning tracks and project requirements are organized. A folder does **not** mean its project is complete.

## Primary learning repository

The **canonical upstream curriculum** for this portfolio is [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT license). Its lessons, hands-on exercises, and practical projects provide the default learning sequence. This repository remains Raphael's **original work and evidence portfolio**, not a fork or mirror of the upstream course. 

Each daily lesson should cite the relevant upstream phase and exact lesson URL, connect it to a real weekly project, and record independently verified tests. The weekly project is still selected from current client demand. Other open-source repositories are secondary references; see [RESOURCES.md](RESOURCES.md) and [ROADMAP.md](ROADMAP.md).

## Curriculum-to-portfolio workflow

The **main curriculum** is [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch). Its [Applied AI Engineer / LLM Product Engineering career route](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json) sets the professional evidence targets. The **20 upstream course phases** and the **11 local application tracks** are different systems; no lesson or track is implied complete by being listed.

- [Official 20-phase → local 11-track map](docs/COURSE_MAPPING.md)
- [Daily learning, BUILD/AUDIT and interview flow](docs/DAILY_WORKFLOW.md)
- [Evidence-based project and resume template](templates/EVIDENCE_BUNDLE.md)
- [Agent and Codex project instructions](AGENTS.md)

**Cadence:** one original flagship project until its acceptance gates pass, with verifiable weekly milestones—not a prescribed number of new projects per week. Quiz/interview answers, personal progress and the professional resume stay private.

## Navigate

- [Learning path](ROADMAP.md): foundations → LLM systems → production.
- [Project portfolio](PROJECTS.md): existing evidence, planned builds and next steps.
- [Engineering quality standard](ENGINEERING_STANDARDS.md): definition of done.
- [Open-source project references](RESOURCES.md): external examples to learn from.
- [Project template](templates/PROJECT_README.md): standard README for every new build.

## Hands-on tracks

| # | Track | Main deliverable | State |
| --- | --- | --- | --- |
| 01 | [Python & APIs](tracks/01-python-apis/README.md) | Tested FastAPI service | Planned |
| 02 | [Machine Learning](tracks/02-machine-learning/README.md) | Measured ML prediction API | Planned |
| 03 | [Deep Learning](tracks/03-deep-learning/README.md) | Reproducible PyTorch training loop | Planned |
| 04 | [LLM Engineering](tracks/04-llm-engineering/README.md) | Structured-output LLM gateway | Planned |
| 05 | [RAG & Search](tracks/05-rag-search/README.md) | Evaluated document question-answering API | Existing WIP project |
| 06 | [AI Agents & MCP](tracks/06-agents-mcp/README.md) | Tool-using agent with action controls | Existing scaffold |
| 07 | [Evaluations](tracks/07-evaluations/README.md) | Repeatable eval and regression suite | Planned in this track |
| 08 | [Fine-tuning & Model Choices](tracks/08-model-adaptation/README.md) | Baseline vs fine-tuned model comparison | Planned |
| 09 | [MLOps & Deployment](tracks/09-mlops-deployment/README.md) | Containerized observable AI API | Planned |
| 10 | [AI Security & System Design](tracks/10-security-system-design/README.md) | Threat model and multi-tenant safety tests | Planned |
| 11 | [Capstone Products](tracks/11-capstones/README.md) | End-to-end real-world AI application | Planned |

## Existing public code

The [InstantCloser AI Engineering case](projects/instantcloser/README.md) includes a safe public decision-policy lab, regression tests and a synthetic evaluation benchmark. The complete commercial InstantCloser source remains in its separate private repository and is **not** published here.


| Repository | What it demonstrates | Honest status |
| --- | --- | --- |
| [rag-production](https://github.com/raphaelribeirob/rag-production) | FastAPI, pgvector, grounded Q&A and retrieval evaluation | **Work in progress.** The repository documents a real-model faithfulness score below its target. |
| [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) | Agent benchmarking architecture and result aggregation | **Scaffold.** No completed benchmark or performance measurements claimed. |

Existing projects remain independent. This hub links to them instead of copying code. Private repositories are not represented here as accessible public portfolio projects.

## What counts as a finished project?

A project is portfolio-ready **only after** a reviewer can reproduce it, inspect measured results, verify tests, understand security controls and see limitations. See [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md).

## Working principle

**Build → test → evaluate → secure → measure cost/latency → document → deploy → verify.**

All source and results should be original or correctly attributed, with upstream licenses respected. No unverified production-readiness claims.
