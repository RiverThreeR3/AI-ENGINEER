# AI Engineer — Verified Completion Meter

**Mission:** bring the personal applied AI Engineering portfolio to **100% on the 11 local tracks** documented in [README.md](../README.md). This is **not** the upstream 20-phase course / 542 lessons; upstream reading is an independent personal learning activity, never auto-marked complete.

**Curriculum alignment:** this is only the **engineering portfolio** meter; the separate [20-phase / 542-lesson AI Engineering From Scratch alignment](AI_ENGINEERING_FROM_SCRATCH_ALIGNMENT.md) has a distinct private learner-progress measure. Do not present 66/66 as graduating the complete upstream curriculum.

## What the meter measures

One original, demonstrable and recruiter-defensible outcome must satisfy **six technical acceptance gates per track**:

| Gate | Required evidence |
| --- | --- |
| `implementation` | Actual runnable original code or attributable, authorized implementation, with exact commit and an intended outcome |
| `tests_ci` | Positives, negatives, regressions and **passing CI on the exact revision**, with real logs and no runner failure |
| `evaluation` | Relevant held-out/baseline evaluation, observed metrics and limitations; avoid invented customer or model performance |
| `security` | Security/privacy and permission review, relevant negative tests, safe credentials and dependency attribution |
| `reproducibility` | Reviewer-reproducible setup, versioned dependencies, commands, evidence bundle and limitations |
| `demo` | Actually executed task/artifact and independent review; no mock/demo claim promoted to deployed without proof |

**Total denominator: 11 tracks × 6 gates = 66.** One gate contributes **1/66 ≈ 1.5 percentage points**. A track counts as **concluded only when all its six gates are verified**.

**Formula:** `progress = ROUND(100 × verified_gates / 66, 1)`; `tracks_completed = count(tracks with six verified gates)`. Do not count files, directories, copied tutorials, commits, drafted tests, unmerged PRs, failed CI, fictional ROI or study lessons as completed engineering gates.

The ledger [`data/ai-engineer-progress.json`](../data/ai-engineer-progress.json) starts conservatively at **0/66 VERIFIED and 0/11 completed tracks**. This does **not** claim that no work has been written; it means historical evidence has not yet been reassessed against **all six current gates**. The [Budget Guard PR #1](https://github.com/RiverThreeR3/AIEngineer/pull/1) remains open and may earn credit **only after** independent review and exact-SHA test evidence.

## Progress visualization

```text
AI ENGINEER | ░░░░░░░░░░░░░░░░░░░░ 0.0%
Verified gates: 0/66 | Pending: 66
Finished tracks: 0/11 | Remaining: 11
```

The percentage increases only after a `PENDING` gate becomes `VERIFIED` with a link to reviewable evidence. The renderer checks that evidence entries have a GitHub HTTPS URL, full 40-character SHA, `PASS` result, review date and explanation; **it cannot independently verify GitHub CI status or the authenticity of the evidence merely from a JSON entry**. The daily agent must **open the cited source and CI at the exact SHA** before crediting the gate. A link with no independent readback remains PENDING/BLOCKED.

### Recompute locally

```sh
node scripts/ai-engineer-progress.mjs
node --test tests/ai-engineer-progress.test.mjs
```

The script uses Node.js built-ins and has no install-time dependencies. Unit tests use synthetic fixture evidence **only to validate the percentage arithmetic**, not to prove any real track complete.

### Daily scheduled report

Each daily 08:00 São Paulo run of **AGESOMA + AI Engineer · Pesquisar → Implementar → Auditar** should display:

```text
AI ENGINEER — [████░░░░░░░░░░░░░░░░] 20.0%
Gates verified: 13/66 | Remaining: 53
Tracks fully complete: 2/11 | Remaining: 9
Δ vs yesterday: +1/66 gate (+1.5 pp), only if independently verified
Next missing gate: <track + exact acceptance criterion>
Evidence: <PR/commit/CI run>
```

This is an **illustrative format**, not actual 20% progress. Read the current repository and evidence each day; if the ledger is unavailable, clearly state **PERCENTUAL NÃO VERIFICADO** rather than reuse a stale figure. If the repo is unchanged, show **Δ 0**. If a previously accepted gate regresses, **remove credit** and report the lower percentage: the meter measures current proof, not cumulative effort.

### Clear separation from InstantWork

- `AGESOMA/InstantWork`: private company product and the execution engine for AGESOMA services. The public `AGESOMA-PROJECTS` is its product evidence showcase.
- `RiverThreeR3/AIEngineer`: Raphael's **separate personal professional portfolio** and the source of this 11-track progress meter.
- Work done in private InstantWork can inform individual career progress **only** if contribution, technical acceptance and safe public attribution are verified, without copying private code or customer data.
- CV and recruiter claims require their own evidence; completing a lesson does not count as commercial experience.

### Completion criterion

**ZERADO / 100%** is only reached when **all 66 gates are independently backed by real evidence** and all eleven tracks meet their particular project acceptance criteria. This means the **defined current backlog** is completed; future new projects/versions should be tracked as a subsequent cycle, not silently used to move the denominator or rewrite past progress.
