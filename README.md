# AI Engineer — Applied AI Engineering Portfolio

**Build reliable AI systems. Measure results. Explain the trade-offs.**

A project-first portfolio focused on Python services, LLM engineering, RAG, tool-using agents, evaluation, security and deployment. Each example is labeled by what has actually been implemented and verified; planned work is not presented as shipped software.

**Repository:** [RiverThreeR3/AIEngineer](https://github.com/RiverThreeR3/AIEngineer) · **Last portfolio review:** 2026-11-04

## Primary curriculum and professional route

The **main learning source** is [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch), with the official [Applied AI Engineer / LLM Product Engineering career route](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json). The upstream course has **20 phases**; this original portfolio has **11 applied tracks**. They are mapped, not copied or considered completed.

- [Full 20-phase to 11-track mapping](docs/COURSE_MAPPING.md) — official phases, skill targets, active project correspondence and evidence gates.
- [Daily lesson, BUILD/AUDIT and interview workflow](docs/DAILY_WORKFLOW.md) — no invented completion grades or new-projects-per-week quota.
- [Project evidence bundle template](templates/EVIDENCE_BUNDLE.md) — project outcomes, measured quality, costs, security, feedback and resume-safe claims.
- [Coding agent rules](AGENTS.md) — code ownership, review requirements, permission boundaries and public/private data separation.

**Working cadence:** one active flagship project until its real acceptance gates pass. Aim for an auditable weekly milestone, not an artificial weekly project count. Learner assessment scores and the professional CV remain private.

## Featured work

Start with the implementation, evidence and limitations—not the number of folders.

| Project | What a reviewer can inspect | Evidence and current status |
| --- | --- | --- |
| **[AI Request Budget Guard — Track 01](https://github.com/RiverThreeR3/AIEngineer/pull/1)** | FastAPI, strict validation, exact decimal estimates, API-key guard, rate limits, Docker, request metrics and tests | **In progress in PR #1; not in `main`.** [CI passed on its Nov 4 code commit](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41823927651). Deterministic demo; no model calls or verified production deployment. |
| **[InstantCloser — public policy lab](projects/instantcloser/README.md)** | Side-effect-free decision rules, permission/opt-out handling, synthetic scenarios and regression tests | **Demo code on `main`.** [CI passed](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41309522674). No customer results, real-model benchmark or production integration claimed. |
| **[RAG Production (external)](https://github.com/raphaelribeirob/rag-production)** | Separate RAG implementation, retrieval/evaluation design and documented gaps | **Work in progress in another repository.** Reported model-groundedness gap remains unresolved; not presented as portfolio-ready. |

**Other reference:** [agent-benchmark (external)](https://github.com/raphaelribeirob/agent-benchmark) — scaffold only; not a completed benchmark.

> **Branch distinction:** `main` contains the public InstantCloser lab and the learning-track outlines. The active FastAPI implementation, updated tests and observability are proposed in [PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) until reviewed and merged. A successful CI run is not proof of production deployment.

## What I am building

The applied portfolio follows 11 tracks. They are aligned with the upstream curriculum; completion must be established from independent, reproducible evidence rather than folder existence:

| Track | Focus | Status in this repository |
| --- | --- | --- |
| [01](tracks/01-python-apis/README.md) | Python & APIs | **Implementation in open PR #1** |
| [02](tracks/02-machine-learning/README.md) | Classical ML | Planned |
| [03](tracks/03-deep-learning/README.md) | Deep Learning / PyTorch | Planned |
| [04](tracks/04-llm-engineering/README.md) | LLM Engineering | Planned |
| [05](tracks/05-rag-search/README.md) | RAG & Search | Track planned; separate external WIP reference |
| [06](tracks/06-agents-mcp/README.md) | Agents & MCP | Track planned; separate external scaffold reference |
| [07](tracks/07-evaluations/README.md) | Evaluations | Planned |
| [08](tracks/08-model-adaptation/README.md) | Fine-tuning & model choices | Planned |
| [09](tracks/09-mlops-deployment/README.md) | MLOps & deployment | Planned |
| [10](tracks/10-security-system-design/README.md) | AI Security & system design | Planned |
| [11](tracks/11-capstones/README.md) | Capstones | Planned |

## How to review this portfolio

- **[Project evidence and current gates](PROJECTS.md):** what was built, links to CI and what is still missing.
- **[Learning roadmap](ROADMAP.md):** career-aligned project sequence and verified next steps.
- **[Curriculum crosswalk](docs/COURSE_MAPPING.md)** · **[Daily learning and delivery method](docs/DAILY_WORKFLOW.md)**.
- **[Engineering standards](ENGINEERING_STANDARDS.md):** reproducibility, security, evaluation and definition of done.
- **[Contributor workflow](CONTRIBUTING.md)** · **[Project README template](templates/PROJECT_README.md)** · **[External resources](RESOURCES.md)**.

For a runnable example on `main`, follow the [InstantCloser public lab quickstart](projects/instantcloser/README.md). For Track 01, review the setup and commands in [PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1); they do not describe files already merged to `main`.

## Repository boundaries and evidence policy

- This repository is maintained under **RiverThreeR3**. Links under **raphaelribeirob** refer to separate public repositories, not folders or mirrored implementations here.
- The full commercial InstantCloser application remains private. This public lab is a limited educational demonstration, not its production source.
- **Planned ≠ implemented; passing CI ≠ live deployment; synthetic evaluations ≠ model or customer performance.** Each project should link to an exact commit/run, setup, measurements, limitations and license/attribution decisions.
- Repository-level license selection is **pending**; no blanket open-source license is implied by a public repository.

**Working principle:** Define a problem → build a deterministic baseline → test → evaluate → secure → measure cost/latency → document → verify.
