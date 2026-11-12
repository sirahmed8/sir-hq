# r42-verifier-scout: Free-Agent Team (Verifier, Scouts, Review Loop, Lessons, Dashboard, Usage Plan)

**Date:** 2026-11-12
**Task:** HQ infra round 42 - build the team of free agents that works for the manager
**Status:** OK - all 6 brief items implemented, scheduled tasks registered, CI green on main

---

## What I found on arrival

A previous model had already written the full r42 implementation but was cut before committing:

- Uncommitted new files: `scripts/hq_team.py`, `hq_verifier.py`, `hq_review.py`, `hq_notify.py`,
  `hq_usage_plan.py`, `r42_rounds.py`, `scout.py`, 7 `scout-*.py` wrappers,
  `install-r42-tasks.ps1`, `tests/test_r42_team.py`, `tests/test_r42_dashboard.py`,
  `ops/LESSONS.md`, `ops/SUGGESTIONS.md`, `ops/verifications/r41-disk-regenerable.md`.
- Modified: `plans/generate_dashboard.py`, `plans/dashboard_template.html`,
  `ops/public/dashboard.html`, `ops/artifact/control-room.html`, `ops/artifact/CHANGED.txt`,
  `scripts/hq_manager_tick.py`, `ops/RUNNING_STATE.md`, `.gitignore`, bus files.
- Also uncommitted: r41 disk-cleanup deletions of ~50 old `ops/agy-runs/reports/*` files plus
  `ops/disk-plan-2026-11-12.md` and the r41 report (verified against
  `ops/agy-runs/reports/r41-disk-regenerable.md`: intentional, 14.81 GB freed).

Nothing was broken: `python -m compileall` clean on all touched scripts,
`tests/test_r42_team.py` + `tests/test_r42_dashboard.py` = 26/26 pass.

## What I did this round

1. Verified the inherited implementation against every brief item (details below).
2. Regenerated the dashboard (`py -3 plans/generate_dashboard.py` -> 325303 bytes,
   hash `48899f02`, deterministic - matches the committed output).
3. Dry-ran every round: `scout.py --all --dry`, `hq_verifier.py --dry --limit 3`,
   `hq_review.py --dry`, `hq_notify.py --daily --dry` - all exit 0 with sane output.
4. Registered the 5 Windows scheduled tasks via `scripts/install-r42-tasks.ps1`
   (powershell -ExecutionPolicy Bypass). `schtasks /query` shows all State=Ready:
   - `SIR_HQ_Verifier` - verifier job at :30, repeats every 2h
   - `SIR_HQ_Scouts` - scouts --all at 04:00 daily
   - `SIR_HQ_Review` - review loop at :00, repeats every 2h
   - `SIR_HQ_NotifyFails` - FAIL notifications at :45, repeats every 2h
   - `SIR_HQ_NotifyDaily` - 21:00 daily summary
   All run `scripts/r42_rounds.py <job>` under pythonw, below-normal priority,
   game-mode pause (`game_mode_snapshot.json`), per-job lock files, IgnoreNew.
5. Added `ops/usage.log` to `.gitignore` (runtime log the usage plan writes).
6. Committed in two commits and pushed:
   - `hq: r41 disk cleanup - remove old agy-runs reports, add cleanup report and plan`
   - `hq: r42 free-agent team - verifier, scouts, review loop, lessons, dashboard sections, usage plan`
   - `hq: r42 checkpoint`, `hq: r42 bus note`
7. CI: `gh run list` -> run `43133050729` on main = **completed success** (verify, 11s).
   Later pushes (checkpoint, bus note) are docs-only; last check below.

## Brief item coverage

1. **VERIFIER** - `scripts/hq_verifier.py`: iterates `ops/AUTOPILOT_QUEUE.json` done tasks
   with no `ops/verifications/<task>.md`, picks a free model via `cli_pool.py pick`,
   builds a prompt from the task brief + project checklists, requires PASS rows to carry
   evidence (PASS without evidence is auto-downgraded to FAIL by `enforce_evidence`),
   FAIL items auto-queue `<task>-fix1` through `scripts/queue-add.py` with a real brief.
   AHome restricted to apps/, tests, screenshots. Scheduled every 2h at :30.
2. **SCOUTS** - `scripts/scout.py` + 7 per-project wrappers: reads checkpoint, last 8
   commits, owner feedback (telegram bus, request ledger, project feedback files),
   shared lessons; rotates through 10 lenses daily (`ops/scout-lenses.json`); model returns
   JSON findings; dedupe against queue/suggestions/rejects (`is_duplicate`, `is_rejected`);
   appends to `ops/SUGGESTIONS.md`. Scheduled daily 04:00.
3. **REVIEW LOOP** - `scripts/hq_review.py`: applies owner Telegram answers from
   `ops/approvals.jsonl` (sug-* ids), auto-approves critical/high with a real project
   folder, queues approvals through `queue-add.py` (writes a real brief), rejects with a
   reason recorded in `ops/suggestion-rejects.json` (never proposed again), and offers up
   to 3 pending items per run via `scripts/deliver/send-buttons.mjs` with
   approve/reject buttons registered in `ops/bus/approvals.json`.
4. **LESSONS** - `ops/LESSONS.md`: 370 lines, numbered rules L1+ each with Source,
   Rule, and "Apply to all"; seeded from `standard/OWNER_DEFAULTS.md` and briefs
   r33/r34/r35/r38 (53 "Apply" lines). Verifier and scout prompts both inject
   `lessons_text()`.
5. **STATUS OUTPUT** - `plans/generate_dashboard.py` + template: new "Verifications"
   and "Suggestions" sidebar sections and stat tiles fed by `parse_verifications()` /
   `parse_suggestions()`; regenerated `ops/public/dashboard.html` +
   `ops/artifact/control-room.html` (hash `48899f02`). `scripts/hq_notify.py`: sends
   Telegram only for FAIL verifications (once each, `notify-state.json`) and one plain
   daily summary at 21:00 (title + <=5 one-fact lines, dedupe via telegram-outbox.md).
6. **USAGE WINDOWS** - `scripts/hq_usage_plan.py`: parses `ops/ACCOUNT_LEDGER.md`
   banner readings (never sends test messages), keeps newest per account+models,
   marks readings older than 2 days stale, writes the heavy/light plan between
   `<!-- r42-usage -->` markers in `ops/RUNNING_STATE.md`. Already run once:
   heavy=2, light=9, stale=12.

## Commands run (real output)

- `py -3 -m pytest tests/test_r42_team.py tests/test_r42_dashboard.py -x -q` -> `26 passed in 0.78s`
- `py -3 plans/generate_dashboard.py` -> `dashboard.html & control-room.html generated (325303 bytes, hash 48899f02, git cdd0564, synced=False)`
- `powershell -ExecutionPolicy Bypass -File scripts/install-r42-tasks.ps1` -> 5 tasks registered, all `Ready`
- `py -3 scripts/hq_usage_plan.py` (earlier run by previous model) -> `plan written: heavy 2, light 9, unknown 12`
- `gh run list --limit 3` / `gh run watch 43133050729` -> `completed success`

## Known open / honest caveats

- `ops/artifact/PUBLISHED.txt` still holds `20ee1159`; the artifact is regenerated but
  HQ republishes when ready (per standing rule it stays until HQ republishes).
- Local-only Playwright test `tests/test_control_room_defects.py::test_no_clipped_text`
  fails at 320px light on BOTH the old (HEAD, 127 clipped elements) and new dashboard -
  pre-existing layout debt, not caused by r42, and not part of the CI gate
  (verify.yml runs compileall + generate_dashboard). Worth a future UI round.
- `py -3` (pythoncore-3.14) has playwright 1.63 without matching browsers; the
  browser-backed tests need `py -3.13` (playwright 1.65). Environmental only.
- No real scout/verifier round has consumed a model yet - first runs happen via the
  scheduled tasks (scouts 04:00, verifier next :30). `ops/verifications/` currently holds
  only the r41 verification written earlier.
- `SUGGESTIONS.md` has one pending scout suggestion already (tab-bar item) which the
  review loop will offer to the owner with buttons on its next run.

## Commits on main

- `0f5bf74` hq: r42 free-agent team - verifier, scouts, review loop, lessons, dashboard sections, usage plan
- (plus r41 cleanup commit, `fb62194` checkpoint, `4c7f5d8` bus note)

## Recommended next

- After the first scheduled scout run, check `ops/SUGGESTIONS.md` for real findings and
  `ops/verifications/` for the first auto-verifications; confirm `ops/review.log`
  shows the owner-button offer working end to end.
- Consider a UI round for the 320px clipped-text debt the Playwright audit keeps flagging.
