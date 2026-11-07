# Daily AI Engineer Learning, Delivery and Interview Workflow

This document describes how to apply [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) to Raphael's learning and professional portfolio. It does **not** prove any local skills have been installed or any scheduled run has produced code.

## One combined daily routine

The existing external ChatGPT automation is scheduled for **08:00 America/Sao_Paulo**; this repository only documents its intended behavior. Keep **one daily report**, not separate notifications for lessons, coding and interviews.

| Mode | Learning | Engineering | Evidence |
| --- | --- | --- | --- |
| BUILD | One verified upstream lesson or prerequisite; explanation, prediction, from-scratch exercise, production-library comparison, unanswered quiz | One bounded original implementation stage for the **same active flagship** project | Exact branch/PR/SHA, commands and outcomes actually observed |
| AUDIT | Review an earlier lesson and learning gap; do not invent quiz scores | Inspect the active PR at its actual SHA; test behavior, security, dependency licenses and regressions; fix only with reviewable changes | Tests, CI and deployment distinctly labeled; blockers and next gate |
| SUNDAY | Same lesson and interview obligations | Project status and acceptance-gate audit | **One** private, accurate English master resume generated from verified evidence, preserving prior version when supported |

The scheduled routine alternates BUILD and AUDIT by local calendar days from 2026-11-05 (BUILD) and 2026-11-06 (AUDIT). Sundays do not cancel either part of the learning routine.

## Two separate progress indicators — course vs engineering portfolio

The official [AI Engineering From Scratch](https://github.com/rohitg00/ai-engineering-from-scratch) has **20 phases / 542 lessons** on the version checked 2026-11-07. The learner's course progress is a **PRIVATE measure** and may only advance with user-confirmed lesson evidence; if no permitted study tracker is accessible, show `PERCENTUAL CURRICULAR NÃO VERIFICADO`. Follow [course alignment](AI_ENGINEERING_FROM_SCRATCH_ALIGNMENT.md) and the public [phase map](../data/ai-engineering-from-scratch-curriculum.json), which stores NO personal lesson completions. This course measure never adds to the **11 tracks × 6 gates = 66** professional project measure. Print both on each daily report, with evidence and remaining work; review upstream changes before shifting the course denominator. Keep the user's requested fully solved explanatory lessons rather than inventing interactive quiz scores.

## AI Engineer completion percentage in every scheduled report

For the personal `RiverThreeR3/AIEngineer` repository, print a progress meter at the top of each daily report, separate from AGESOMA/InstantWork release gates: **verified engineering gates / 66 × 100** and **fully completed tracks / 11**. Follow [the evidence ledger and acceptance contract](PROGRESS_METER.md). Only count one of six gate types per track after exact-SHA and CI/evaluation evidence have been independently checked. Show the difference since the prior verified report and the next unclosed acceptance gate. If the ledger or evidence is inaccessible, show `PERCENTUAL NÃO VERIFICADO` rather than recycling a guessed number. No lesson-read count, course title, planned project, failed CI or open PR automatically earns completion credit. The prior BUILD/AUDIT calendar alternation in this document is superseded for the **scheduled AGESOMA + AI Engineer automation** by its required daily **research → implement → audit** cycle.

## ChatGPT as the interactive classroom

**Location of interactive practice:** ChatGPT conversation. The scheduled report prepares a complete English lesson, 10–20-minute practical exercise, and one unanswered authentic interview-bank question. The learner must **reply in ChatGPT** to practice. The assistant then asks follow-ups, marks real responses against verified rubrics, and revisits misunderstandings. A scheduled report cannot independently complete a live mock interview, grade unanswered questions, or assume a response in a different thread is visible.

**Private persistence:** The user's restricted-access Google Drive learning tracker can be read and updated only via successful, explicitly verified connected Drive actions. It may summarize actual lesson responses, phase checks and interview gaps with timestamps; the tracker is not publicly linked here. If cross-chat or automated retrieval cannot see a real learner response, record `Pending / not verified`, request that response in the active ChatGPT lesson, and never invent completion. The full curriculum's `LEARNING.md` and course project's `PROJECTS-LEARNING.md` are optional private local state files, not public portfolio files.

**Public career proof:** The sanitized [recruiter-facing evidence map](RECRUITER_GUIDE.md) links each project to real GitHub code, acceptance criteria, reproducible checks and honest limitations. The private professional resume and its weekly refinements reference the **same stable project/CI links**. Interview coaching targets these same technical decisions, but personal answers/scores do not become recruiter-visible content.

**Weekly reconciliation:** Match the official `applied-ai-engineer.json` readiness criteria to: upstream lesson → real learner exercise → project PR/commit SHA → reproducible test/evaluation → employer-safe CV bullet → interview deep-dive. Flag missing steps and do not promote learning-only accomplishments to CV experience.

## Official learning contracts

- [`start-learning`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/start-learning/SKILL.md) and [`find-your-level`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/find-your-level/SKILL.md): initial questions, ten-question placement and a genuine learner-owned plan.
- [`learn`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/learn/SKILL.md): one lesson per interactive session, prior-lesson recall when progress exists, code walkthrough, quiz and targeted review.
- [`check-understanding`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/check-understanding/SKILL.md): eight-question phase review **after** real learner responses.
- [`build-project`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/build-project/SKILL.md): **one project stage per learning session**, with learner-written attempts, staged grader and feedback. This does **not** establish a new-projects-per-week quota.
- [`interview-prep`](https://github.com/rohitg00/ai-engineering-from-scratch/blob/main/skills/interview-prep/SKILL.md): authentic prompts from the bank, answers withheld until Raphael responds, measured feedback and linked learning gaps.

Interactive course practice is **not** equivalent to agent-generated client-facing code. Commercial BUILD tasks may use coding agents subject to separate verification; study exercise completion requires genuine learner participation.

## Where information belongs

| Artifact | Destination | Publication status |
| --- | --- | --- |
| Original code, public demo, reproducible commands, safe evaluations | `RiverThreeR3/AIEngineer` or the authorized AGESOMA-PROJECTS implementation | Public **only when safe and authorized** |
| Public case study and sanitized acceptance evidence | `PROJECTS.md` and the project's README/evidence bundle | Public if no secrets, contact details, private client data or proprietary material |
| `LEARNING.md` | Learner's **private** persistent workspace after real placement | Do not publish |
| `PROJECTS-LEARNING.md` | Learner's **private** persistent workspace after genuine stage work | Do not publish |
| `INTERVIEW-LEARNING.md` | Learner's **private** persistent workspace after real responses | Do not publish |
| Weekly professional resume and personal contact details | Existing **private Google Drive Resume folder** | Never upload to public GitHub without explicit approval |

The three learning state files above are intentionally excluded from this repository via `.gitignore`. A link to a private store does **not** prove write access; verify real persistence before saying progress was saved.

## Daily report — required fields, in English

1. **Source check:** exact upstream phase/lesson/route, URL, checked revision if actually available, relevant changes or `unverified`.
2. **Career alignment:** LLM Product Engineering route stage and why it relates to a current verified client need.
3. **Lesson:** concept, tiny tested example or explicitly labeled hand trace/pseudocode, trade-off, 10–20-minute exercise and unanswered questions.
4. **Interview:** one bank-linked question without the solution; feedback only after Raphael answers in English.
5. **Project stage:** current flagship, original files/PR/SHA, independent tests, CI for the **same** commit, failures and next acceptance gate.
6. **Portfolio evidence delta:** new reproducible measurements and limitations; `none verified` if there was no new proof.
7. **Audit and next action:** planned vs delivered, security/quality gap, blockers, and an achievable next step.

Do not describe planned activity as delivered, a locally completed tutorial as professional experience, or a passing test as production deployment. Verify a source before asserting a new upstream version or license.
