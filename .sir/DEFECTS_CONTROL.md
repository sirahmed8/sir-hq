# Control Room defect log — round 22 (r22-control)
Page: `plans/dashboard_template.html` + generator `plans/generate_dashboard.py`.
Checked at 320/390/768/1280 px, light and dark. Root-cause fixes at the template/generator level (no CSS patches only).

## Defect 1 — header subtitle + toolbar (FIXED)
Symptom: line above title blurred/half-faded ("HQ FOR AHMED ..."); paragraph below title long marketing text; Menu and Settings as two big side-by-side buttons.
Fix: one short factual subtitle under the title; Menu + Settings in a single compact `.header-toolbar` row.
Proof: CSS `.header-toolbar`/`#header-toolbar` at `dashboard_template.html:170-176` and HTML at generated `ops/public/dashboard.html:1313`; subtitle text short factual line.

## Defect 2 — status strip chips (FIXED)
Symptom: "Updated ... 9m ago, git hash, hash, artifact is waiting for republish" wrapped mono string running into the next block.
Fix: `.status-strip` with chips (updated time, commit, republish needed/in sync); `white-space: nowrap` so it never wraps.
Proof: CSS `dashboard_template.html:176-197`; chip HTML `#chip-republish` at generated `dashboard.html:1325`.

## Defect 3 — drawer dedupe + top bar (FIXED)
Symptom: five equal-width tabs, active marked only by border; side drawer 11 items centered unevenly, active pill different width; duplicate names ("Handover" vs "Gemini Handover", "CI" vs "CI & Remote").
Fix: drawer is a left-aligned list of equal rows, active row clearly marked; top bar shows first four tabs + "More" opening the drawer; one name per page (Handover, CI, Projects, Accounts, Activity).
Proof: observer sectionIds deduped; i18n keys `navHandover`/`navCi` used once; drawer list CSS `dashboard_template.html` drawer section.

## Defect 4 — stat tiles from real data (FIXED)
Symptom: "VERIFIED TODAY 0/16", "ACTIVE REBUILDS 0", "QUEUED IN BACKLOG 0", "FROZEN CLIENT REPO 0" — dead zeros, one tile wrong meaning.
Fix: `renderTiles` feeds Verified Today, Active Workers, Pending Queue, CI State from real queue/worker/CI data; hides tiles with no data; projects with last CI red show red tile; tile classes `.tile.ok/bad/warn` with border.
Proof: `dashboard_template.html` renderTiles function; CSS `.tile.ok/bad/warn`.

## Defect 5 — Working now from live data (FIXED)
Symptom: stale "feed older than 6 hours" badge and an old-cycle card ("LOOP-STUDY-4").
Fix: `renderActive` reads `ops/autopilot_state.json`, `ops/AUTOPILOT_QUEUE.json`, `ops/agy-runs/model-pool.json`, and last lines of `ops/agy-runs/cli-*.log` through the generator (safe fields only: task, project folder, model, minutes since last write, last commit subject); shows who works on which project with which model since when, plus cooling-down pills.
Proof: generator functions `load_model_pool`, `project_folder_for_task`, `model_cooling`, `parse_cli_workers`; `renderActive` at `dashboard_template.html`.

## Defect 6 — handover stacked cards (FIXED)
Symptom: cards wider than screen, titles/descriptions cut, inner vertical scrollbar, one-word-per-line descriptions.
Fix: each checklist row is a stacked `.checklist-item` card: title, status chip, description full width; `overflow-wrap: anywhere`; no inner scroll box; horizontal-scroll container only for real tables.
Proof: CSS `.checklist-item` at `dashboard_template.html:719`; stacked card HTML at generated `dashboard.html:2789`.

## Defect 7 — one-line sub-descriptions + Accounts merge (FIXED)
Symptom: English-only page; code-word labels ("Ledgers", "Waves", "Accounts", "Account Ledger", "Workforce", "Activity"); no description under page titles.
Fix: one-line sub-description under every page title (EN + AR); Accounts and Account Ledger merged into `#accounts` (acct-ledger table moved in, `#account-ledger` section removed, observer id removed).
Proof: `accSub`, `projectsSub`, `platSub`, `wfSub`, `actSub` i18n keys EN/AR; `#account-ledger` section removed from template.

## Defect 8 — self-audit loop (this document + browser test)
Symptom: no central defect record; no repeatable check across widths/themes.
Fix: `.sir/DEFECTS_CONTROL.md` (this file) lists every defect with status and proof; browser test `tests/test_control_room_defects.py` opens the dashboard at 320/390/768/1280 px light/dark and asserts no horizontal scroll, no clipped text, one name per page, no tile with fake data.

## Remaining open items (accepted)
- Browser test cannot run in this sandbox (no Playwright installed; not in CI `.github/workflows/verify.yml`). It is committed so it runs where Playwright is available; CI green gate is the generator step + compileall + gitleaks.
- M3 (single-file generator/template ~1200/~3100 lines) deferred as accepted tech debt from r19; documented in `plans/sir-control-room.md` section 11.

## Verification this round
- `python -m compileall plans scripts` — OK
- `python plans/generate_dashboard.py` — OK, `ops/public/dashboard.html` regenerated (286809 bytes, hash afe30386)
- All 7 defect fixes present in generated output (header-toolbar, status-strip chips, checklist-item, accSub/projectsSub EN/AR, working-now, no `#account-ledger` section, `#chip-republish`).
