# AIEngineer Repository Instructions for Coding Agents

This repository is Raphael's public **original engineering portfolio**, not the upstream course or a clone of private product repositories. Before editing, read [README.md](README.md), [PROJECTS.md](PROJECTS.md), [ENGINEERING_STANDARDS.md](ENGINEERING_STANDARDS.md), [docs/COURSE_MAPPING.md](docs/COURSE_MAPPING.md) and [docs/DAILY_WORKFLOW.md](docs/DAILY_WORKFLOW.md).

## Sources and scope

- **Primary curriculum:** [rohitg00/ai-engineering-from-scratch](https://github.com/rohitg00/ai-engineering-from-scratch). Use verified lesson URLs and the [Applied AI Engineer route](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/learning-paths/applied-ai-engineer.json) for role mapping. The 20 upstream phases are **not** the 11 local portfolio tracks.
- **Authorized public destinations:** this repository and AGESOMA-PROJECTS only where separately authorized; one authoritative project codebase. Do not modify or copy unrelated/private products.
- **Current flagship:** [AI Request Budget Guard PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1), an in-review deterministic API, **not** a merged or deployed LLM service. Check current PR head, tests and CI anew rather than relying on a stale SHA.
- Only one active flagship at a time. A week is for independently verified milestones, not automatically starting a new project. Respect BUILD/AUDIT separation from the existing external schedule.

## Safe editing and evidence

1. Prefer the smallest original change with typed contracts, unit/integration tests, lint and visible acceptance criteria.
2. Review existing branches and PRs first; use a focused feature branch and PR. **Never auto-merge**, silently rewrite history, commit to someone else's active feature branch or move existing code merely to rename folders.
3. Follow [templates/PROJECT_README.md](templates/PROJECT_README.md) and [templates/EVIDENCE_BUNDLE.md](templates/EVIDENCE_BUNDLE.md). Include exact commands, runtime, input/data provenance, committed SHA, test output, CI link and meaningful limitations.
4. Verify the latest commit separately from earlier CI runs. Distinguish mocked/synthetic tests, real-model evaluations and independently verified deployment. Do not publish estimated performance as measured or assume that public GitHub code has a reusable license.
5. Use outside code only with license review and attribution; **never** copy upstream solutions to claim original skills. Upstream learning exercises should be learner-owned and graded against the genuine workspace; commercial production deliverables are a separate mode.
6. Preserve secrets, personal study history, job applications/CV, interview responses and private client data outside the public repository. Do not create or publish `LEARNING.md`, `PROJECTS-LEARNING.md` or `INTERVIEW-LEARNING.md` here. No fabricated scores or certificates.
7. All repo documentation, PRs, lessons, commit messages and code comments must be **English**. If a verification is blocked, report the reason; never claim execution without observed output.

## Recruiter-facing proof and private coaching separation

- Update [docs/RECRUITER_GUIDE.md](docs/RECRUITER_GUIDE.md) when original project evidence changes. Recruiters should see a consistent path from `README.md` to `PROJECTS.md`, exact PR/commit/CI, measured outcomes, relevant skill, limitations and credible interview topics.
- Link the same stable evidence in public case studies and the **private** master CV. Do not publish the CV or its Google Drive location to public GitHub, and do not edit LinkedIn or send applications without specific authorization.
- Courses and interviews are conducted interactively with the learner in **ChatGPT**; a scheduled task can ask an unanswered question but cannot invent a reply, test pass or skill validation. Keep personal assessment answers/scores in a verified **private** progress store only. Never put a private tracking document link in this public repository.
- Upstream learning → verified learner practice → original project changes → accepted testing/evaluation → truthful resume bullet → interview explanation. Only verified, publishable evidence passes to recruiter materials.

## Definition of done

A project is **portfolio-ready** only when its relevant acceptance, reproducibility, evaluation, security, license, deployment-claim and documentation gates are satisfied. If a gate is missing, keep the honest status and define the next test. Cite original evidence; an attractive README alone is not a completion criterion.
