# AI Engineer — Project-First Career Roadmap

**Goal:** prepare for international AI Engineer interviews by building systems that can be run, reviewed, measured and explained. Milestones represent engineering evidence—not promised employment dates or assumed professional experience.

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

**Following projects:** Track 02 classical ML service → Track 03 PyTorch training → Track 04 LLM gateway. External [rag-production](https://github.com/raphaelribeirob/rag-production) and [agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark) can inform learning, but do not replace acceptance gates.

## Daily build + lesson + interview loop

One increment per day for the **current** project, not a new project every day:

1. **Build:** define the smallest useful change, implement and link exact source/PR evidence.
2. **Verify:** unit/integration tests, lint, risk checks and accurately labeled benchmarks where applicable.
3. **Teach:** explain a real code excerpt, why it was designed this way, alternatives and trade-offs.
4. **Interview (English):** explain the same technical decision as a realistic interview answer. Practice Python/APIs first, then ML, LLMs, RAG, agents, evaluation, MLOps, security and system design as the projects progress.
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
