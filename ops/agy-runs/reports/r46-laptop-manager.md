# r46-laptop-manager report: competitor matrix and feature-gap round

Date: 2026-11-12. Project: `D:\Projects\SIR Laptop Manager`. Branch: `main`. Commit: `7331784`.

## What the brief asked

1. Find the best direct competitors or best-in-class apps for what this product does, with strongest 3 features, weakest 3 flaws, what to copy and what to do better.
2. Write `.sir/plans/COMPETITOR_MATRIX.md` and `.sir/plans/FEATURE_GAPS.md` with at least 20 ranked gaps and an acceptance test each.
3. Implement the 3 highest-value, lowest-risk gaps, verified on screen at 320/390/768/1280 px, Arabic and English, light and dark.
4. Update `.sir/CHECKPOINT.md`, add one line to `D:/Projects/_SIR/ops/bus/sir-hq.md`, never open AHome, no emoji, no em-dashes, truth rule.

## What changed

### Research documents

- `.sir/plans/COMPETITOR_MATRIX.md` (new): 10 products in the main table and 5 open-source or adjacent tools in a second table.
  - Microsoft PC Manager, CCleaner, Glary Utilities Pro, Razer Cortex, MSI Center, Dell Optimizer, BleachBit, Bulk Crap Uninstaller, Windhawk, Sysinternals Autoruns.
  - Prices are from the official pages on 2026-11-12. Third-party figures are marked unverified. GitHub licence and star counts come from the GitHub REST API on 2026-11-12: BleachBit GPL-3.0 7,465; BCUninstaller Apache-2.0 22,429; Windhawk GPL-3.0 9,792.
- `.sir/plans/FEATURE_GAPS.md` (new): 24 ranked gaps, each with a competitor reference, a concrete acceptance test, risk and effort. The first three are the ones implemented this round. The next three are the uninstall manager (rank 4), duplicate-file finder (rank 5) and largest-files browser (rank 6).

### Code

- `src/sir_laptop_manager/care/health_score.py` (new): pure weighted score, no I/O. Weights: CPU 20, memory 20, disk 25, GPU 15, battery 10, startup 10. Unavailable components are removed and the remaining weights renormalized. A critical finding caps the score at 69 so a machine with a critical issue cannot show "excellent". Findings: `low_disk`, `high_memory`, `high_cpu`, `hot_gpu`, `battery_wear`, `many_startup`, `stale_startup`.
- `src/sir_laptop_manager/ops_ui/routes_health.py` (new): `GET /api/health/score`. Reads the existing health telemetry, battery analytics and startup entries once, then returns score, band, components, findings and `checked_at`.
- `src/sir_laptop_manager/ops_ui/routes_cycle8.py`: registered `/api/health/score` and `/api/updates`.
- `src/sir_laptop_manager/ops_ui/routes.py`: new `get_updates_telemetry()`. Returns `winget_available`, `upgradable_count`, `upgradable_packages`, `checked_at` and the NVIDIA driver version. It never installs anything.
- `src/sir_laptop_manager/care/updates.py`: winget check now has a 10 minute TTL cache and a `force_refresh` parameter. Package names are parsed by splitting each winget line on two or more spaces, instead of slicing the first 30 characters.
- `src/sir_laptop_manager/ops_ui/static/index.html`:
  - Health tab: new score ring card with band, component chips, prioritized findings, a "Run check" button and a one-tap jump to the tab that fixes the finding.
  - Health tab: new Battery Care card with health, wear, design capacity, full charge capacity, cycle count, a plain recommendation and a no-battery empty state.
  - Health tab: new Updates card that starts at "Not checked", shows a loading state, then the update list or an honest unavailable/empty/error state.
  - New CSS tokens and classes for the ring, finding rows, battery cells and update list. Added Arabic and English strings for all new copy. Added bindings for the new static labels. Added command-palette entries for "Run health check" and "Check app updates".

### Tests

- `tests/test_r46_health_score.py`: 25 tests. Pure-function scoring, critical cap, missing battery, startup findings, route registration, i18n keys in both languages, markup presence, binding ids.
- `tests/test_r46_updates_cache.py`: 4 tests. Winget parsing and cache, winget absent, route payload has no install action, route registration.
- `tests/test_r46_browser_cards.py`: 3 tests. Real server and real Chrome, 16 layout contexts (320/390/768/1280 x en/ar x light/dark), score in range, card boxes inside the viewport, no card or page overflow, Arabic labels in Arabic mode, no Arabic in English mode, health check button refresh, updates card initial state.
- `tests/test_r25_i18n.py`: two `networkidle` waits replaced with `domcontentloaded` plus an attached `#lbl-tab-health` wait. The old wait was flaky because the dashboard keeps polling telemetry; the assertions are unchanged.

## Commands and real output

### Verify gate (final run)

Command: `powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify.ps1`

Output (final lines):

```
[1/4] Checking code formatting (ruff format)...
131 files already formatted

[2/4] Linting codebase (ruff check)...
All checks passed!

[3/4] Strict typecheck (mypy)...
Success: no issues found in 112 source files

[4/4] Running automated tests (pytest)...
======================= 294 passed in 258.60s (0:04:18) =======================

==========================================================
 [OK] All verification checks passed with zero errors!
==========================================================
```

The previous run had one flaky `networkidle` timeout and 52 pytest temp-directory setup errors (`FileNotFoundError` on `pytest-of-sir1ahmed1\pytest-26`). The rerun after fixing the flaky wait was fully green. The temp-directory errors were environmental, not code: they appeared only in the interrupted run and did not recur.

### Direct endpoint call

Command:

```
uv run python -c "from sir_laptop_manager.ops_ui.routes import get_updates_telemetry; import json; d=get_updates_telemetry(); print(json.dumps({k:v for k,v in d.items() if k!='upgradable_packages'}, ensure_ascii=False)); print('packages:', len(d['upgradable_packages']))"
```

Output:

```
{"winget_available": true, "upgradable_count": 0, "checked_at": "2026-11-12T13:50:03.322805+00:00", "gpu": {"available": true, "name": "NVIDIA GeForce RTX 4050 Laptop GPU", "driver_version": "617.42"}}
packages: 0
```

This is real machine data: winget is present and reports no pending upgrades, and the NVIDIA driver is 617.42.

### Health score latency

Command:

```
uv run python -c "import time; from sir_laptop_manager.ops_ui.routes_health import get_health_score_data; t=time.perf_counter(); d=get_health_score_data(); print('latency_ms', round((time.perf_counter()-t)*1000,1), 'score', d['score'], 'findings', len(d['findings']))"
```

Output:

```
latency_ms 637.1 score 45 findings 4
```

The score is real on this machine: 4 findings and a fair/poor band. That is expected on a working laptop with a nearly full C: drive and several startup apps, not a fake "excellent".

## Screen proof

Screenshots written to `.sir\evidence\r46\`:

- `cards-320-en-light.png`, `cards-320-en-dark.png`, `cards-320-ar-light.png`, `cards-320-ar-dark.png`
- `cards-390-en-light.png`, `cards-390-en-dark.png`, `cards-390-ar-light.png`, `cards-390-ar-dark.png`
- `cards-768-en-light.png`, `cards-768-en-dark.png`, `cards-768-ar-light.png`, `cards-768-ar-dark.png`
- `cards-1280-en-light.png`, `cards-1280-en-dark.png`, `cards-1280-ar-light.png`, `cards-1280-ar-dark.png`

The browser test asserts for every context: `data-theme` and `lang` match the requested context, the score is an integer 0 to 100, the three cards have non-zero boxes fully inside the viewport, no card or page overflow, Arabic labels in Arabic mode and no Arabic in English mode.

## Truth and status

- The app is a local desktop dashboard. The health score, battery card and update card read real host data through existing endpoints.
- The update card never installs. `GET /api/updates` only reads winget output and the NVIDIA driver version.
- No invented prices or users were written into the product. Prices live only in the research matrix and are snapshots.
- No AHome or Habiba material was opened or written.
- GitHub Actions minutes are exhausted (`D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists). Rule 18 applies: local verification is the gate, and the full local verify is green above. The commit is pushed to `main` (`88939bf..7331784`).

## What is unsure or open

1. The battery card uses the existing `battery_wear.py` parser. On a machine where WMI does not expose `DesignCapacity`, the card shows charge level only and says capacity counters are not available. That is the honest fallback, but it was not exercised on such a machine this round.
2. The update card was verified with winget reporting zero pending updates. The package list path was proven by a mocked winget output in `tests/test_r46_updates_cache.py`, not by a live pending update.
3. The health score is instantaneous at the moment of the fetch, like Task Manager. It is not a 24 hour average. A short CPU spike can lower the score for one refresh. A future smoothing window is a gap item, not a defect.
4. `test_r25_i18n.py` was made deterministic by waiting for attached DOM instead of `networkidle`. That is a test-stability fix, not a product change.

## Recommendation for the next round

Start with gap rank 4, the uninstall manager: a read-only installed-app list, leftover preview, restore point, then quarantine, then removal. It is the highest-value gap that is still missing, but it is destructive, so it needs its own dry-run and restore tests before any UI copy. Gap rank 5 (duplicate files) is the next lowest-risk read-only scan.