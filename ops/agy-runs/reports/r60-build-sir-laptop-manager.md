# r60-build-sir-laptop-manager — worker report

Date: 2026-11-12. Worker: devin (continued an interrupted r60 round). Project: `D:/Projects/SIR Laptop Manager`. Branch: `main`.

## Result

FEATURE_GAPS rank 4 (uninstall manager with leftover detection) is implemented, tested, committed and pushed. Local verification is fully green. GitHub Actions is still quota-blocked (flag `ops/ci-quota-exhausted.flag` present); the new CI run failed in 4 s with 0 job steps, which is the quota signature, not a code failure. Per WORKER_PREAMBLE rule 18, local verification substitutes for CI.

Commits pushed to `main`:

- `c591fe0` r60: uninstall manager leftover review - guarded quarantine cleanup
- `8f7449c` r60: refresh regenerated r46 evidence screenshots and icon metadata

## What I found on resume

The previous worker left a nearly complete rank-4 implementation uncommitted: `care/uninstall.py`, `ops_ui/routes_uninstall.py`, route wiring, an 8th "Installed Apps" SPA tab, en/ar strings, and tests. I did not revert it; I repaired and finished it.

Real defects I fixed this round:

1. `loadApps()` rendered the list while `appsLoading` was still true, so the Apps tab stayed on skeletons forever even though `/api/uninstall/apps` returned data. Reproduced live (141 apps returned, list still skeleton), then moved `renderAppsList()` after the `finally` that clears `appsLoading`.
2. The previous worker raised the global POST body cap from 4096 to 65536 for every route. I restored 4096 globally and scoped 65536 to `/api/uninstall/clean` only, with a regression test proving other routes still reject >4 KB bodies.
3. `loadLeftovers()` now resets stale scan state and hides the clean button while rescanning, so a failed rescan cannot leave a clean action armed on old data.
4. The leftovers badge no longer shows "Not scanned" after a successful scan that found zero items; it shows the real `0 folders selected` state.
5. `post_uninstall_clean` validates `app_id` length and converts unexpected cleanup exceptions into a JSON error instead of dropping the connection.
6. Browser test fixes: per-context helper (ruff B023), typed mocks (mypy), hidden leftovers card handled before selection, mobile navigation via shortcut `8` at <=768 px.

## Files changed (feature commit c591fe0)

- `src/sir_laptop_manager/care/uninstall.py` (new): registry inventory HKLM64/HKLM32/HKCU, token-matched leftover scan, protected-path and install-location exclusion, caps `MAX_DIR_FILES=20000` / `MAX_CLEAN_FILES=5000`, dry-run vs confirmed cleanup, restore point first, quarantine + manifest + `uninstall_report.json`.
- `src/sir_laptop_manager/ops_ui/routes_uninstall.py` (new): `GET /api/uninstall/apps`, `GET /api/uninstall/leftovers?id=`, `POST /api/uninstall/clean` (`confirm` must be JSON `true`).
- `src/sir_laptop_manager/ops_ui/routes_cycle8.py`, `routes_extended.py`, `server.py`, `tailnet.py`: route wiring; scoped body cap; allowlists.
- `src/sir_laptop_manager/ops_ui/static/index.html`: 8th tab, search, five states, escaped interpolation, keyboard/a11y, en/ar counted nouns, dry-run -> confirm -> quarantine flow.
- `tests/test_r60_uninstall.py` (new, 21 tests), `tests/test_r60_apps_browser.py` (new, 3 tests), `tests/test_ops_ui_server.py` (+1 body-cap test), `tests/test_ops_ui_a11y.py` (7 -> 8 tabs).
- `.sir/evidence/r60/` (new): 16 layout screenshots (320/390/768/1280 x en/ar x light/dark) + 2 clean-flow screenshots.
- `.sir/CHECKPOINT.md`: Now / Next step / Done evidence / Decisions updated.

Second commit `8f7449c` only refreshes regenerated `.sir/evidence/r46/*.png` (rerun by the suite against the 8-tab shell) and `assets/brand/icon.png` (PNG metadata only; decompressed IDAT hash identical to HEAD: `2fa76950a6b0454e`).

## Safety model (as implemented)

- Never executes `UninstallString`; this is a leftover review/cleanup tool, not an uninstaller.
- Registry keys are detected and shown as review-only; never auto-deleted.
- Filesystem cleanup accepts only paths produced by a fresh server-side scan, strictly inside approved roots (Program Files, Program Files (x86), AppData Local/Roaming, ProgramData, install-location parent), never the install location itself, never protected/system paths.
- `confirm` must be JSON `true`; string `"true"` stays dry-run (tested).
- Confirmed cleanup: file-count cap check, restore point required (failure aborts before any change), then quarantine with manifest; restore available from the Quarantine tab.
- Dry-run creates/moves/deletes nothing (tested).

## Commands run and real output

- `git status --short`, `git diff --stat`, `git log -5` at start: showed the interrupted uncommitted feature; repaired, not reverted.
- Live repro of the skeleton bug: `/api/uninstall/apps` returned `{"avail":true,"n":141}` while `#apps-list` still held skeleton HTML.
- Targeted: `uv run --offline pytest -q tests/test_r60_uninstall.py tests/test_r60_apps_browser.py tests/test_ops_ui_server.py tests/test_ops_ui_a11y.py` -> `66 passed, 1 skipped` after fixes (67 collected).
- `uv run --offline pytest -q tests/test_ops_ui_server.py -x` -> `32 passed in 5.06s`.
- `uv run --offline pytest -q tests/test_r60_apps_browser.py -x -vv` -> `3 passed in 24.78s`.
- Authoritative local verification (CI quota flag present): `.\scripts\verify.ps1`
  - `[1/4] ruff format` -> `135 files already formatted`
  - `[2/4] ruff check` -> `All checks passed!`
  - `[3/4] mypy` -> `Success: no issues found in 116 source files`
  - `[4/4] pytest` -> `320 passed, 1 skipped in 259.26s (0:04:19)`
  - Final: `[OK] All verification checks passed with zero errors!`
- `git push origin main` -> `7d14912..8f7449c main -> main`.
- `gh run list --limit 5` -> new run `43314557237` queued then `completed failure` in 4 s.
- `gh run view 43314557237 --json conclusion,status,jobs` -> `{"conclusion":"failure","jobs":[{"name":"Verify Quality Bar (Windows)","steps":0}]}`: zero steps = Actions quota exhaustion, matching `ops/ci-quota-exhausted.flag` and prior 4 s failures. No CI fix loop attempted per rule 18.

## Screenshots / evidence

- `.sir/evidence/r60/apps-{320,390,768,1280}-{en,ar}-{light,dark}.png` (16)
- `.sir/evidence/r60/apps-clean-{en-light,ar-dark}.png` (2)
- `.sir/evidence/r46/cards-*.png` refreshed by the suite (committed separately).

## Checklist reconciliation (honest)

- The brief's named checklist `ops/briefs/sir-laptop-manager-tasks.md` (Tasks 1-10) was already judged superseded in `.sir/PLAN_REFRESH.md`: each item maps to verified milestone work (M0-M10, rounds R8-R46). I did not falsely tick it.
- `.sir/TASKS.md` still has older unchecked items unrelated to this checkpoint's next step: `T-026` (move legacy folders to `D:\Projects\old projects\`, depends on M6 retirement), `T-027` (release docs/tag v1.0.0), and `T-061` (audio guard daemon, owner request). These remain open future work; they are not part of FEATURE_GAPS rank 4 and were not attempted in this round.
- `.sir/PLAN.md` section 8 checkboxes are stale relative to `.sir/TASKS.md`/CHECKPOINT (milestones are recorded as verified there); left for a docs pass rather than edited blindly.

## Uncertainties

- Rank-4 acceptance mentions "last-used date"; the Windows uninstall registry exposes no reliable per-app last-used timestamp. The UI shows publisher, version, install date and size and never fakes a last-used value (recorded in CHECKPOINT Decisions).
- Leftover detection scans immediate children of the standard data roots; deeply nested vendor folders (e.g. `AppData\Vendor\App`) are out of scope for this safe slice.
- EstimatedSize is KB from the registry; size is shown as an estimate.

## Recommendations / remaining work

- Next exact step (in CHECKPOINT): FEATURE_GAPS rank 5 duplicate-file finder (SHA-256 grouping, user-chosen folder, keep one per group, quarantine rest behind dry-run + restore point + confirm).
- Then ranks 6-24 in `.sir/plans/FEATURE_GAPS.md`.
- SIR-KIT lesson already logged in PLAN_REFRESH: dev-script sync must skip non-`package.json` projects or emit the Python launcher.
- When `ops/ci-quota-exhausted.flag` is removed, re-run CI on `main` per rule 4.
