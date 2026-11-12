# Report: r61-plan-sir-life (planning-only refresh, rule 20)

Date: 2026-11-12. Tool: devin (continuation; an earlier worker this round had already expanded `ops/briefs/sir-life-tasks.md` but left everything else untouched).

## Scope kept

Planning only. Nothing was written inside `D:/Projects/SIR Life`, no repos created, no code written. All edits are under `D:/Projects/_SIR` in `plans/`, `ops/competitors/`, `ops/briefs/`, `ops/bus/` and this report.

## What I found on arrival (repair first)

- `git status` showed many unrelated modified files from other workers; the only file belonging to this task was `ops/briefs/sir-life-tasks.md` (+171 lines, uncommitted).
- The previous worker's expansion was half-done and partly wrong:
  - `plans/sir-life.md` unchanged (no research, no new detail sections).
  - `ops/competitors/sir-life.md` unchanged (still the r52 single pass).
  - No `plans/sir-life-REFRESH-LOG.md`.
  - No report file.
  - Copy-paste defects inside the tasks file: T29's exit check mentioned "visit code and ETA" (access-map leftover); T38-T42 were handyman/access-map tasks in disguise (completed jobs with escrow releases, lawyer review of an eKYC contract, 301 redirects from old hosts, domain setup framed for a services product). None of that belongs to SIR Life.
- Nothing was broken at runtime (docs-only task), so "repair" meant finishing and correcting the half-written planning artifacts.

## What I did

1. **Team bus**: appended START line to `ops/bus/team.md` (the earlier START lines from autopilot/opencode for this task are already there).
2. **Competitor research, second pass** (`ops/competitors/sir-life.md`, new section 5): opened/search-verified on 2026-11-12 -
   - Muslim Pro: Premium now bundles Qalbox streaming, ships "AiDeen" Islamic AI bot, gamified quests/streaks, whole Quran free; prices still "(unsourced, verify)".
   - Sahibukum: Regimen planner inside prayer windows, Privacy PIN encrypting on-device before sync, official-timetable badges (MUIS/Kemenag/JAKIM), halal scanner, 12 languages, no ads.
   - Barakah Planner: niyyah tasks, Quran streaks, family shared lists, medication lists, iOS+Android.
   - Salah Home, Just Pray (app-blocking at prayer + AI coach), Deeny, Salah Focus, Islamic Tracker, Pillars recorded as second ring.
   - Conclusion written into the file: "life around the salah" is now an occupied position; SIR Life's edge narrows to whole-day breadth (medicine/food/gym/expenses/mood), local-first privacy, Arabic-first + EGP.
3. **Plan detail** (`plans/sir-life.md`): header updated for r61; added section 15 (category delta), section 16 (19-route screen inventory with milestone map), section 17 (API/integration surface table), section 18 (launch and marketing: 20-50 user consent beta, Arabic-first SEO, pricing interviews), section 19 (risks R8-R12 + open questions Q6-Q7 with recommended answers).
4. **Tasks file** (`ops/briefs/sir-life-tasks.md`): rewrote to 42 tasks. T1-T10 keep the exact r52 order so nothing queued breaks; milestone headings corrected to M0-M6; every task now has an explicit **Acceptance test** and a **Skills** line from `ops/SKILLS_INDEX.md` (verified: 42 `### T` headings, 42 `Acceptance test:`, 42 `Skills:`). Fixed T29 payload bug; rewrote T38-T42 for this product (domain + dual-hosting go-live, store-readiness drafts, backup/restore drills, consent beta, legal + paid-launch gate). Removed all escrow/lawyer/301-redirect content.
5. **Refresh log**: `plans/sir-life-REFRESH-LOG.md` written with what was re-read, research added, plan/task changes and the date.

## Commands run (real output)

- `git status -sb`, `git log -5 --oneline`, `git diff --stat` - see session; only `ops/briefs/sir-life-tasks.md` belonged to this task.
- `grep -c "^### T" ops/briefs/sir-life-tasks.md` -> 42; `grep -c "Acceptance test:"` -> 42; `grep -c "Skills:"` -> 42; grep for `visit code|escrow|lawyer|301` -> no matches.
- `git diff --stat` on the three edited files: `ops/briefs/sir-life-tasks.md` +195/-28 region, `ops/competitors/sir-life.md` +36, `plans/sir-life.md` +85.
- Web research via web_search (Muslim Pro premium/features pages, Sahibukum, Barakah Planner, salah-habit-app roundups) - sources listed in competitor file section 5 with open dates.

## Verification

- Docs-only change; no build/test applies. `ops/ci-quota-exhausted.flag` exists, so per WORKER_PREAMBLE rule 18 local verification substitutes for CI; the "verification" here is structural: task count, per-task acceptance/skills coverage and grep checks above, all pasted with real output.
- No product-folder files touched, so the SIR Life `pnpm verify` state (65/65 tests, recorded in the plan truth rule) is unaffected.

## What is still open / honest caveats

- Muslim Pro, Headspace, Fabulous and Athan exact prices remain "(unsourced, verify)" - pages did not expose numbers today; listed as sourcing tasks in competitor file section 4.
- Sahibukum/Barakah feature claims are vendor claims from their own pages, not audited.
- The product folder still has the uncommitted `.sir` doc reversions noted in the plan; that is build-task T1's job, not this planning round's.
- Building is still forbidden for free tools (owner order, rule 22); the 42 tasks queue only after the owner lifts planning-only for SIR Life.

## Recommended next

- HQ queues T1-T10 from `ops/briefs/sir-life-tasks.md` when SIR Life leaves planning-only.
- Owner decisions needed (recorded in plan section 19 and section 12): domain purchase, Firebase project `sir-life` confirmation, store account purchases, legal review, pricing validation interviews.
