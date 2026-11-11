# r22-control report — Control Room mobile UI hardening

Task: finish SIR Control Room round 22 (mobile UI) per brief `ops/briefs/r22-control.md`. Fix all 8 dashboard defects in
`plans/dashboard_template.html` + `plans/generate_dashboard.py`, regenerate `ops/public/dashboard.html`, commit and push to
`main` with green CI, then write this report, update `.sir/CHECKPOINT.md`, append a line to `ops/bus/sir-hq.md`, run `agy-done.py`.

## What was done

### Repair / carry-forward
- Previous worker's (r19-control) uncommitted changes were committed as `6abb8a9` and pushed (8 files including `ops/public/dashboard.html`, `ops/artifact/control-room.html`, `.gitignore`, bus files).

### Defect 1 — header subtitle + compact toolbar
- One short factual subtitle under the title (replaced long marketing text / blurred line).
- Menu + Settings in a single compact `.header-toolbar` row.
- CSS `.header-toolbar` / `#header-toolbar` added; `#stamp` removed.

### Defect 2 — status strip chips
- `.status-strip` with chips: updated time, git commit, republish needed / in sync (ok-warn chip).
- `white-space: nowrap` so it never wraps into the next block.
- `#chip-republish` renders "republish needed" or "in sync".

### Defect 3 — drawer dedupe + top bar
- Drawer is a left-aligned list of equal rows; active row clearly marked.
- Top bar shows first four tabs + "More" opening the drawer.
- Duplicate names removed: "Gemini Handover"→"Handover", "CI & Remote"→"CI"; one name per page.
- Observer sectionIds and i18n nav keys updated (en/ar).

### Defect 4 — stat tiles from real data
- `renderTiles` rewritten: Verified Today (bar), Active Workers (runner_count), Pending Queue (pending_count), CI State (red if any failure).
- Hides tiles with no data; dynamic grid columns.
- `.tile.ok/bad/warn` border CSS added.

### Defect 5 — Working now from live data
- Generator extended: `import time`, `load_model_pool`, `project_folder_for_task`, `model_cooling`, `parse_cli_workers`.
- `renderActive` lists workers from cli logs: model, folder, minutes ago, commit subject, cooling-down pills.
- Autopilot data includes `workers`.

### Defect 6 — handover stacked cards
- Each checklist row is a stacked `.checklist-item` card: title, status chip, description full width.
- `overflow-wrap: anywhere`; no inner scroll box.
- Horizontal-scroll container only for real tables.

### Defect 7 — one-line sub-descriptions + Accounts merge
- One-line sub under every page title: `accSub`, `projectsSub`, `platSub`, `wfSub`, `actSub` (EN + AR).
- Accounts and Account Ledger merged into `#accounts`; `#account-ledger` section removed; observer id removed.
- `navAccountLedger` i18n keys and applyLang line removed.

### Defect 8 — self-audit loop
- `.sir/DEFECTS_CONTROL.md` written: all 8 defects with status, root-cause fix, file:line proof.
- `tests/test_control_room_defects.py` written (Playwright): opens dashboard at 320/390/768/1280 px light/dark; asserts no horizontal scroll, no clipped text, one name per page, no tile with fake data. Skips where Playwright absent.

## Regeneration
- `python -m compileall plans scripts` — OK
- `python plans/generate_dashboard.py` — OK, `ops/public/dashboard.html` regenerated (286809 bytes, hash afe30386, git 869176b)
- All 7 defect fixes present in generated output (header-toolbar, status-strip chips, checklist-item, accSub/projectsSub EN/AR, working-now, no `#account-ledger` section, `#chip-republish`).

## Privacy spot-check
- No AHome private data or Habiba names in dashboard text. `habiba` absent (case-insensitive). `ahome` appears only as intended project label.

## Open items (accepted)
- Browser test cannot run locally (no Playwright installed; not in CI `.github/workflows/verify.yml`). Committed so it runs where Playwright is available. CI green gate is compileall + generator + gitleaks.
- M3 (single-file generator/template ~1200/~3100 lines) deferred as accepted tech debt from r19; documented in `plans/sir-control-room.md` section 11.

## Files changed
`.sir/DEFECTS_CONTROL.md` (new), `.sir/CHECKPOINT.md`, `ops/agy-runs/reports/r22-control.md` (new), `ops/bus/sir-hq.md`, `ops/public/dashboard.html`, `plans/dashboard_template.html`, `plans/generate_dashboard.py`, `tests/test_control_room_defects.py` (new).
