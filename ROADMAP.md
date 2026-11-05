# AI Engineer — Project-First Career Roadmap

**Goal:** prepare for international AI Engineer interviews by building systems that can be run, reviewed, measured and explained. Milestones represent engineering evidence—not promised employment dates or assumed professional experience.

## Authoritative learning and career framework

**Primary course:** [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch). Its **20 phases** are learning subjects; they do **not** correspond numerically to the 11 portfolio tracks below. See the [phase-by-phase mapping](docs/COURSE_MAPPING.md).

**Official specialization:** [Applied AI Engineer — LLM Product Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json). Prioritize typed user contracts, retrieval/tool grounding, repeatable evaluation, safety, latency, cost and rollout evidence. These are career readiness gates, not claims that all work is already complete.

**Official study process:** [start-learning](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/start-learning/SKILL.md) → [learn](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/learn/SKILL.md) → [build-project](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/build-project/SKILL.md) → [interview-prep](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/interview-prep/SKILL.md), with genuine learner-owned answers, private progress tracking and no fictional test passes. See [DAILY_WORKFLOW.md](docs/DAILY_WORKFLOW.md).

## Learning sequence

| Phase | Tracks | Evidence to produce |
| --- | --- | --- |
| Software foundations | 01–03 | Tested Python API, measured ML baseline, reproducible PyTorch training |
| LLM applications | 04–05 | Structured model gateway, evaluated retrieval and grounded responses |
| Agents & evaluation | 06–07 | Permissioned tool execution, deterministic and model-based regressions |
| Model choices | 08 | Fixed-dataset comparison of prompts, retrieval and fine-tuning |
| Production engineering | 09–10 | Verified deployment, observability, auth, budgets, security and recovery |
| Capstone | 11 | Demonstrable product solving a scoped user problem |

Track-specific scopes live under [`tracks/`](tracks/) and current implementation evidence lives in [PROJECTS.md](PROJECTS.md). Some older public experiments exist in other repositories; they are references, not completed tracks in this repository.

## Current work: Track 01

**AI Request Budget Guard — [PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1)**

The FastAPI implementation is **in an open PR, not in `main`**. The [2026-11-04 CI run](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41823927651) passed on commit `6a3b11f38e41b857326bcbf99e97ed3a34b07b65`. This is a deterministic service and no real-model usage or production deployment is claimed.

**Immediate priorities:**
1. Review the PR, tests, Docker and privacy-metrics behavior against [engineering standards](ENGINEERING_STANDARDS.md).
2. Resolve security and deployment/operability gaps proportionate to its declared **demo** or **deployed** scope; document any deferred production controls precisely.
3. Decide repository-level licensing before asserting open-source redistribution rights.
4. Merge the reviewed PR only after its acceptance criteria and current-commit CI are satisfied. Keep project and status documentation in sync.

**Candidate later learning tracks:** Track 02 classical ML service, Track 03 PyTorch training, Track 04 LLM gateway and other market-relevant outcomes. Start the next flagship only once the active project's acceptance gates are met (or a documented stop/pivot decision is made); the current market demand determines priority. External [rag-production](https://github.com/raphaelribeirob/rag-production) and [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) can inform learning, but do not replace acceptance gates.

## Daily build + lesson + interview loop

One bounded stage on BUILD days and verification on AUDIT days for the **same active** project; the upstream course prescribes one learning stage per interactive session, **not a new project per week**:

1. **Build:** define the smallest useful change, implement and link exact source/PR evidence.
2. **Verify:** unit/integration tests, lint, risk checks and accurately labeled benchmarks where applicable.
3. **Teach:** cite the exact upstream lesson and phase; explain a real excerpt or clearly labeled pseudocode, quiz only after real learner responses, and compare from-scratch logic to production libraries.
4. **Interview (English):** ask a verified question from the official interview bank without exposing its answer until the learner responds, then assess the same technical decision as a realistic interview answer. Practice Python/APIs first, then ML, LLMs, RAG, agents, evaluation, MLOps, security and system design as the projects progress.
5. **Review:** record weaknesses and the next acceptance gate; do not invent interview scores, code runs or production results.

For interview feedback, score technical accuracy (30%), clarity (20%), trade-offs (20%), production considerations (20%) and spoken/written English (10%). A weekly mock interview can test architecture, troubleshooting and explaining portfolio decisions. Keep draft answers separate from verified engineering evidence.

## Status vocabulary

- **Planned:** requirements only; no committed implementation claimed.
- **Scaffold:** starter code; no complete end-to-end validation.
- **In progress:** working components exist but declared acceptance gates remain open.
- **Locally verified:** reproducible local checks and evidence attached.
- **CI verified:** automated checks passed on an identified commit; not a deployed service.
- **Deployed verified:** independently checked live environment with identified version.
- **Portfolio-ready:** relevant reproducibility, evaluation, documentation and safety gates satisfied.

**Evidence first:** build → test → evaluate → secure → measure cost/latency → document → demonstrate. Never present a CI badge, synthetic eval or design document as proof of production AI performance.
