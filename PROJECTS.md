# Project Portfolio — Evidence Register

**Reviewed:** 2026-11-04 · **Canonical repository:** [RiverThreeR3/AIEngineer](https://github.com/RiverThreeR3/AIEngineer)

This page separates **merged code**, **work in an open pull request**, **separate external repositories** and **planned projects**. Do not count a roadmap folder as an implemented project.

## Current project index

| Project | Location / tracks | Demonstrated evidence | Status / next gate |
| --- | --- | --- | --- |
| **[AI Request Budget Guard](https://github.com/RiverThreeR3/AIEngineer/pull/1)** | Track 01 · **PR #1**, not merged to `main` | FastAPI endpoints, strict inputs, Decimal estimates, API-key validation, process-local rate limits, Docker, tests and privacy-conscious metrics in PR | **In progress.** Review PR and CI; distributed controls, real deployment/rollback, real provider usage and license decision remain open. |
| **[InstantCloser public policy lab](projects/instantcloser/README.md)** | `projects/instantcloser/` · tracks 01/06/07/10/11 | Synthetic scenarios, deterministic action policy, regression tests and [successful CI run](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41309522674) | **Demo on `main`.** Add held-out evaluation, authorized tool simulation and measured real-model comparison before broader claims. |
| **[rag-production](https://github.com/raphaelribeirob/rag-production)** | Separate public repository · related to 05/07/09/10 | Existing RAG code and documented evaluation limitations | **External WIP.** Address reported faithfulness/groundedness gap and independently validate current tests and controls. |
| **[agent-benchmark](https://github.com/raphaelribeirob/agent-benchmark)** | Separate public repository · related to 06/07 | Benchmark scaffold, without a verified end-to-end benchmark | **External scaffold.** Implement a runnable suite with independently measured results. |

The commercial InstantCloser app is **not** published here. Its capabilities, customers or production readiness must not be inferred from the public policy lab.

## Course alignment and project progression

The active project follows the [official Applied AI Engineer career route](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json), mapped in [docs/COURSE_MAPPING.md](docs/COURSE_MAPPING.md). The upstream [Career Practice](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/CAREER-PRACTICE.md) guide recommends iterating on one coherent problem, not generating a fixed number of new repositories per week.

- **One active flagship at a time** and at least one independently checkable milestone each week when feasible; a blocker is a legitimate result, not a fabricated completed project.
- **One learning project stage per interactive session** per the upstream [build-project skill](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/build-project/SKILL.md); never claim grader success without observing it.
- Use [templates/EVIDENCE_BUNDLE.md](templates/EVIDENCE_BUNDLE.md) for a reproducible problem/baseline, tested original implementation, observed results, risks, customer/peer feedback where available, and a truthful CV-safe bullet.
- The upstream reference implementation and local course certificate are **not** proof of original professional experience.

## Track 01 — AI Request Budget Guard

**Source under review:** [PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) on branch `feat/track01-budget-guard-20261101`.

**Implementation reported and inspectable in the PR:** typed FastAPI request/response contracts, bounded request payloads, key-based demonstration auth, process-local quota, non-root Docker image, regression tests, an in-process and loopback HTTP benchmark, and JSON application request metrics that omit user payloads and credentials.

**Verified CI evidence:**
- [2026-11-02 run](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41440781850): pytest, Ruff, Docker build and HTTP smoke check successful for that commit.
- [2026-11-03 run](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41625097153): pytest, Ruff, benchmark and Docker smoke checks successful for that commit.
- **[2026-11-04 run](https://github.com/RiverThreeR3/AIEngineer/actions/runs/41823927651): completed successfully on commit `6a3b11f38e41b857326bcbf99e97ed3a34b07b65`**, including the privacy-metrics increment. These checks exercise the demo and do **not** prove a deployed production API.

**Measurement scope:** the 2026-11-03 local loopback benchmark documented in the PR reports 40 sequential HTTP requests, p50 2.252 ms / p95 3.783 ms / p99 4.813 ms. These are local loopback measurements without model/provider latency, concurrency or public network traffic—not production SLOs. The PR README is the source for test commands and detailed caveats.

**Current limitations:** caller supplies token counts and prices; the service makes **no LLM calls** and does **not** enforce actual provider spending. API-key handling and rate limiting are only demonstration controls; quotas are per process. No external deployment, multi-tenant auth, distributed quota, telemetry backend or rollback is verified. License decision and immutable action/image pinning are pending.

**Next review gate:** preserve the passing CI result, review code and security, resolve open quality gates, make a deliberate decision about whether the service is a learning demo or a deployed portfolio service, and merge only after review.

## Planned builds (not implementations)

| Track | Intended artifact |
| --- | --- |
| 02 | ML baseline, holdout evaluation and inference API |
| 03 | Reproducible PyTorch train/evaluate/save/reload loop |
| 04 | LLM gateway with schemas, bounded retries, streaming and usage/cost records |
| 05 & 07 | Retrieval comparison with fixed evaluation cases and source-grounding metrics |
| 06 | Tool-using agent with allowlist, approvals and auditable actions |
| 08 | Prompting vs RAG vs fine-tuning evaluation |
| 09 & 10 | Deployment, tenant isolation, monitoring, threat model and rollback |
| 11 | End-to-end product capstone with verified demonstration |

Follow [ROADMAP.md](ROADMAP.md) for sequence, not an assumption that all tracks have working software.

## Evidence required before saying “portfolio-ready”

- Stable commit SHA, source path, tested runtime and reproducible commands.
- Test/CI link for **the same commit**; distinct local, CI and production claims.
- Baseline, held-out data, real-model measurements where relevant, and known failure cases.
- Latency, utilization, token/cost measures **with measurement environment labeled**.
- Security boundaries, secret/PII handling, provider authorization and threat model.
- Verified demo/deployment (if claimed), rollback/operation details, limitations and license.

**Operating rule:** do not advance the active project merely to fill the next track. Close its declared evidence gates or state clearly why it remains in progress.
