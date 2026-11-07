# AI Engineer Career Roadmap

This is a **project-first** path for applied AI engineering; phases represent skills and gates, not promises about hiring timelines.

| Phase | Tracks | Hands-on outcome |
| --- | --- | --- |
| Foundations | 01–03 | Python service + ML baseline + PyTorch training |
| GenAI systems | 04–05 | LLM interface with schemas + evaluated RAG |
| Agent engineering | 06–07 | Permissioned tool-use agent + repeatable benchmark |
| Advanced AI | 08 | Compare prompting, retrieval and fine-tuning on one task |
| Production engineering | 09–10 | Deploy, observe, secure and cost-control an AI system |
| Capstone | 11 | Deliver a full customer-oriented application |

## Canonical learning backbone

**Primary upstream:** [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch) (MIT). Use its 20-phase curriculum as the **default learning source**, not as an assertion that all 542 lessons have been completed. Select the exact lesson and phase for each daily lesson and link it in the daily report.

**Market-first execution:** The single active engineering project is selected from verified current freelance demand. In the combined daily routine the permitted opportunity source is **LinkedIn only**; archived Workana/Upwork citations are historical, not actively monitored. The current flagship is [AGESOMA Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2), whose source stays in AGESOMA-PROJECTS. [AI Request Budget Guard PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) is maintenance/audit-only. A new week sets a new milestone for that same flagship; it does not require starting another project. Map that project to the closest upstream phase and exercise; prioritize Phase 0 (tooling), Phase 11 (LLM engineering), Phase 13 (tools/protocols), Phase 14 (agent engineering), Phase 17 (infrastructure/production), Phase 18 (safety), and Phase 19 (capstone) when relevant. Learn prerequisite phases when gaps are evident; do not force a linear 542-lesson sequence ahead of client-relevant delivery.

**Daily evidence contract:** Upstream lesson URL + phase + concept, original implementation or exercise, test commands with actual outcomes, interview practice, and next learning gap. Do not equate reading upstream material, cloned examples, or mock evaluations with verified professional production experience.

## Project cadence — upstream-aligned

The upstream [build-project skill](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/build-project/SKILL.md) prescribes **one project stage per learning session**, not a fixed number of new projects each week. Its [career practice guide](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/CAREER-PRACTICE.md) recommends deepening one coherent project across product, implementation, independent verification and iterative improvement.

**Raphael portfolio policy (our adaptation, not an upstream quota):**
- **One active flagship project at a time.** Do not start a new one just because Monday arrives; continue for as many weeks as verification requires.
- **At least one auditable milestone per week when feasible**, expressed as a tested increment or a documented blocker, not a promise of a finished project. A BUILD session targets one bounded implementation stage; an AUDIT session verifies and repairs earlier work. Do not claim a passing stage without observed grader/test output.
- Map each project to an upstream phase/lesson and, where relevant, a **related** upstream exercise, but keep all original portfolio code separate from upstream examples. Record the exact upstream reference and limits of the analogy.
- Promote a project to portfolio-ready only after the acceptance checklist, security review, independent run/evaluation and honest limitations are documented. Record a follow-up iteration and feedback where available.
- Keep **education/quiz records private** and only publicly share appropriate original code and non-sensitive evidence. Skills added to the professional CV require verified independent evidence; completing a tutorial alone is insufficient.

## Applied AI Engineer readiness gates

The canonical route is upstream [`learning-paths/applied-ai-engineer.json`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json): **common core** (prompts, schemas, retrieval/tools), **role practice** (evals, cost, guardrails), **proof project** (bounded production-style service), and **interview/readiness evidence** (rollout and recovery decisions). Use the [crosswalk](docs/COURSE_MAPPING.md) to link each local track to relevant upstream phases and lessons; do not confuse 20 phase IDs with the 11 local track IDs.

**Proof before promotion:** user contract, grounded tool/retrieval boundaries where relevant, held-out evaluation, latency-and-cost scorecard, security, and only independently verified deployment or rollout claims. Follow the [daily workflow](docs/DAILY_WORKFLOW.md); learner scores and private resume data do not belong in public GitHub.

## Learning loop

1. Define user problem, inputs, outputs and success criteria.
2. Build the cheapest deterministic baseline first.
3. Add the AI component only where it brings measured improvement.
4. Test timeouts, invalid responses, malicious inputs and authorization boundaries.
5. Evaluate accuracy, latency, tool correctness, cost and failure rate.
6. Publish run commands, exact environment, measured results and limitations.
7. Ship a reproducible demo; independently verify deployment before claiming it.

## Next concrete work

1. Inspect the [AGESOMA Knowledge API PR #2](https://github.com/RiverThreeR3/AGESOMA-PROJECTS/pull/2) at its current head SHA, independently test retrieval grounding, abstention, negative/security cases and holdout evaluation, and advance one reviewable stage per BUILD day **in its authoritative commercial repository**.
2. Audit the [AI Request Budget Guard PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) for current-SHA CI, conflicts, security and evidence as a **maintenance task**, not a second ongoing feature build.
3. Reconcile both public evidence indices without copying application code, implying agent-authored work proves personal mastery, or promoting a portfolio item before its gates pass.
4. Consider additional project candidates only after verified flagship acceptance and a documented decision. Do not write in legacy or private repositories.

## Status definitions

- **Planned** — requirements documented, no implementation claimed.
- **Scaffold** — initial code or structure, not end-to-end validated.
- **In progress** — important requirements still missing.
- **Verified locally** — reproducible run and test evidence exists.
- **Verified deployed** — a live environment was independently checked.
- **Portfolio-ready** — documentation, quality, safety and evidence gates are satisfied.

Do not confuse third-party labels such as “production-ready” with independent verification.
