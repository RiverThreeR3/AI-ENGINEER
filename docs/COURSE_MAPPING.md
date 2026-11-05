# AI Engineering From Scratch — Curriculum Alignment

**Primary upstream:** [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT licensed course).
**Career overlay:** [Applied AI Engineer / LLM Product Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json).
**Purpose:** map upstream learning to original, evidence-backed engineering work in this repository. This is a crosswalk, **not a fork, mirror, completed course, or automatic certification**.

## Two layers: learning vs professional delivery

- **Upstream:** the 20-phase curriculum, lessons, quiz bank, project starters/graders, and interview bank are the teaching reference.
- **This repository:** 11 applied engineering tracks, original code, reproducible engineering evidence, README/case studies and PR review. Track numbers are **not** upstream phase numbers.
- **Commercial cases:** when original public work is developed in AGESOMA-PROJECTS, reference its authorized public case and the exact implementation; do not duplicate a product merely to populate this repository.
- **Private study records:** keep learner scores, lesson progress, interview answers and professional CV outside public repositories; see [DAILY_WORKFLOW.md](DAILY_WORKFLOW.md).
- **Market-first milestones:** choose one active flagship project by demonstrable market need; keep it active beyond a calendar week until acceptance criteria pass.

## Upstream 20 phases → local 11 tracks

The source names below are from the upstream [ROADMAP.md](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/ROADMAP.md). Multiple upstream phases can support one local project; this table is a topic map, **not** individual completion status.

| Upstream phase | Official upstream topic | Closest applied portfolio track(s) |
| --- | --- | --- |
| 00 | Setup & Tooling | 01 Python & APIs; 09 MLOps |
| 01 | Math Foundations | 02 Machine Learning; 03 Deep Learning prerequisites |
| 02 | ML Fundamentals | 02 Machine Learning; 07 Evaluations |
| 03 | Deep Learning Core | 03 Deep Learning |
| 04 | Computer Vision | Optional specialization; 03 Deep Learning foundations |
| 05 | NLP | 04 LLM Engineering; 05 RAG & Search |
| 06 | Speech & Audio | Optional specialization; no completed local track implied |
| 07 | Transformers Deep Dive | 03 Deep Learning; 04 LLM Engineering |
| 08 | Generative AI | 04 LLM Engineering; 08 Model Adaptation |
| 09 | Reinforcement Learning | Optional specialization; not a current delivery claim |
| 10 | LLMs from Scratch | 03 Deep Learning; 04 LLM Engineering |
| 11 | LLM Engineering | 04 LLM Engineering; 05 RAG; 07 Evaluations |
| 12 | Multimodal AI | Optional specialization; not yet represented by a shipped track |
| 13 | Tools & Protocols | 06 Agents & MCP; 10 Security |
| 14 | Agent Engineering | 06 Agents & MCP; 07 Evaluations |
| 15 | Autonomous Systems | 06 Agents & MCP; 10 Security |
| 16 | Multi-Agent & Swarms | 06 Agents & MCP; 07 Evaluations |
| 17 | Infrastructure & Production | 09 MLOps & Deployment; 10 Security |
| 18 | Ethics, Safety & Alignment | 10 Security & System Design |
| 19 | Capstone Projects | 11 Capstone Products |

## Primary career route: LLM Product Engineering

The official route [applied-ai-engineer.json](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json) specifies practical evidence for an Applied AI Engineer / LLM Engineer / AI Product Engineer:

1. **Common core:** prompts, structured outputs, embeddings, context, RAG and tool calling.
2. **Role practice:** evaluation, cost-aware engineering and guardrails.
3. **Proof project:** an operational LLM application, bounded interfaces and service controls.
4. **Interview/readiness evidence:** controlled rollout choices and reasoned trade-offs.

### Portfolio proof gates

- Typed user-facing contract and structured output schema.
- Grounded retrieval or tool use with failure controls.
- Versioned evaluation cases and guardrail report.
- Quality, latency **and** cost scorecard measured under described conditions.
- Verified deployment or staged rollout record **only if deployment is actually performed**.

A deterministic API or mock-only demo can still be a useful engineering project, but it is **not** automatically a deployed LLM product.

## Current active mapping (reviewed 2026-11-04)

| Work | Upstream lessons / related exercise | Honest status |
| --- | --- | --- |
| [AI Request Budget Guard — PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) | [LLM caching/cost](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/11-caching-cost/docs/en.md), [FinOps for LLMs](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/17-infrastructure-and-production/27-finops-llms/docs/en.md); related [Token Counter and Cost Meter](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/projects/token-counter-and-cost-meter) | In open PR; deterministic budget estimator, not actual billing/tokenizer/provider inference |
| [InstantCloser public policy lab](../projects/instantcloser/README.md) | [Tools & Protocols](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/13-tools-and-protocols), [Agent Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering) | Public deterministic/synthetic demo only |
| [rag-production (external)](https://github.com/raphaelribeirob/rag-production) | [RAG](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/phases/11-llm-engineering/06-rag/docs/en.md), [Retrieval Evaluation Lab](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/projects/retrieval-evaluation-lab) | External work in progress, not completed here |
| [agent-benchmark (external)](https://github.com/raphaelribeirob/agent-benchmark) | [Agent Engineering](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/phases/14-agent-engineering), [Agent Trace Debugger](https://github.com/rohitg00/ai-engineering-from-scratch/tree/main/projects/agent-trace-debugger) | External scaffold only |

**Reusing upstream code:** assess license, keep required notices, and never submit copied reference solutions as original portfolio engineering. Related upstream projects are teaching references, not identical implementations.

See [PROJECTS.md](../PROJECTS.md) for current project claims and [ENGINEERING_STANDARDS.md](../ENGINEERING_STANDARDS.md) for the definition of done.
