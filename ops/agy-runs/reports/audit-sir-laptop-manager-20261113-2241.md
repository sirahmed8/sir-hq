# Report: audit-sir-laptop-manager-20261113-2241

Worker: devin (resumed task; previous model was cut after running cycle-1 sweep).
Project: `D:/Projects/SIR Laptop Manager`
Brief: `D:/Projects/_SIR/ops/briefs/audit-sir-laptop-manager-20261113-2241.prompt.txt`
Defect log: `.sir/DEFECTS_20261113-2241.md`

## Result

Audit loop complete. Cycle-1 sweep produced 32 findings; every one traced to a
single root cause (rate limiter counting static assets) plus two latent UI
defects found while probing error states. All defects fixed at root with
regression tests, two consecutive clean full-matrix sweeps (cycles 4 and 5,
`findings: []` each), local verification fully green, everything committed and
pushed to `main`.

## What the previous model left

- Untracked `.sir/evidence/audit-20261113/sweep-cycle1-2241.json` — a full sweep
  with 32 findings: 16 `console-error` 429s on `320/light/ar/*`, and 16
  `blank-view`+`dir` findings on `390/dark/en/*`.
- `sweep-20261113-2241.json` (committed earlier) already showed 0 findings.

## Root-cause analysis of cycle 1

The `390/dark/en` blank views were not a rendering bug: `OpsRequestHandler.
do_GET` ran `_rate_ok("read")` **before** `try_serve_static`, so once the
300 GET/min sliding-window budget was exhausted, `GET /` itself was answered
`429 application/json`. The browser then rendered the raw JSON error body —
no `<html>`, no `dir` attribute, <20 chars of text. That is the worst-case
user-facing failure: refresh the dashboard during a busy minute and the app
visibly "disappears". Reproduced deterministically on a pre-fix worktree
server (commit `68f42fe`, port 8766): after ~300 API reads, `GET /` returns
`429 {"success": false, "error": "Too Many Requests"}` (screenshot
`beforeafter/before-429-blank-shell-390.png`).

## Fixes shipped

1. **Static shell exempt from the read budget** — `server.py` `do_GET` now
   runs host/identity checks, serves static assets, and only then consumes
   the `read` rate budget for non-static paths. The app shell can no longer
   be rate-limited into a JSON error page. Unknown non-static paths still
   consume budget (verified by test).
2. **Transparent GET retry on 429** — `index.html` installs a `window.fetch`
   wrapper at boot: any GET answered 429 waits `Retry-After` (capped at 8 s)
   and retries once; POSTs and persistent failures fall through to the
   existing per-view error states. Covers all ~40 API call sites at once.
3. **D4 — raw `{0}` i18n placeholder leaks (FIXED)** — `renderHealthScoreError`
   and `renderUpdatesError` called `tr()` on `trf` templates
   (`hsError`/`updError` contain `{0}`), so badges and finding titles
   rendered the literal `{0}`. Added `hsErrorTitle`, `hsErrorBadge`,
   `updErrorBadge` keys in en+ar. Before: badge text was literally
   `"Health check failed. {0}"`; after: `"Check failed"`
   (`beforeafter/before-hs-error-placeholder-390.png` vs
   `after-hs-error-clean-390.png`).
4. **D5 — FEATURE_GAPS rank 15 shipped: exportable health report** — new
   "Export report" button on the Health score card downloads the live
   snapshot as `.json` (score, band, components, findings, battery wear,
   updates) and `.md` (readable report with localized finding titles via the
   existing `HS_FINDINGS` map). Read-only; uses only data already loaded;
   fully localized en+ar. Before/after:
   `beforeafter/before-health-actions-en-390.png` vs
   `after-health-actions-en-390.png` / `after-health-actions-ar-390.png`.

## Commands run (real output)

```text
$ node scripts/audit-20261113.mjs http://127.0.0.1:8765 .sir/evidence/audit-20261113/sweep-cycle1-2241.json
sweep complete: 32 findings   (pre-fix state, inherited)

$ node scripts/audit-20261113.mjs http://127.0.0.1:8765 .sir/evidence/audit-20261113/sweep-cycle2-2241.json
sweep complete: 0 findings

$ node scripts/audit-20261113.mjs http://127.0.0.1:8765 .sir/evidence/audit-20261113/sweep-cycle3-2241.json
sweep complete: 2 findings  (self-inflicted: this audit's own evidence burst
>300 GETs at /api/health on the same server while the sweep ran; documented
in DEFECTS as a tooling artifact, not a product defect)

$ node scripts/audit-20261113.mjs http://127.0.0.1:8765 .sir/evidence/audit-20261113/sweep-cycle4-2241.json
sweep complete: 0 findings

$ node scripts/audit-20261113.mjs http://127.0.0.1:8765 .sir/evidence/audit-20261113/sweep-cycle5-2241.json
sweep complete: 0 findings
```

Two consecutive clean cycles (4 and 5) across the full matrix: 8 tabs x
320/390/768/1280 px x dark/light x en/ar.

```text
$ node scripts/touch_targets_check.mjs
OK   320px..1920px all tabs
ALL CHECKS PASSED
```

Interactive probe (`scripts/audit-20261113-2241-probe.mjs`, Playwright
headless Chromium, `--mute-audio`, all pages closed): settings sheet, drawer,
command palette, shortcuts modal, offline state, dead-button scan — all clean,
0 console errors; offline correctly shows the localized "Connection Lost"
banner with Retry.

```text
$ uv run --project . pytest tests/test_audit_20261113_2241.py -x -q
5 passed in 15.10s
```

New tests: static shell survives exhausted read budget; unknown paths still
rate-limited; browser GET retries once on 429 (route-intercepted, asserts
exactly 2 hits); health-score error shows no raw `{0}`; export downloads real
`.md` + `.json` with correct payload.

```text
$ powershell -NoProfile -File scripts/verify.ps1
[1/4] ruff format: 144 files already formatted
[2/4] ruff check: All checks passed!
[3/4] mypy: Success: no issues found in 125 source files
[4/4] pytest: 352 passed, 1 skipped in 347.96s
[OK] All verification checks passed with zero errors!
```

## Browser work (per preamble rule 55)

Tool: Playwright (`playwright` Node package, headless Chromium, `--mute-audio`,
`speechSynthesis.speak` stubbed, every context closed). URLs opened:
`http://127.0.0.1:8765` (current build) and `http://127.0.0.1:8766`
(pre-fix worktree at `68f42fe`, removed after capture; `git worktree list`
clean). No tabs left open.

## Evidence

- `.sir/evidence/audit-20261113/sweep-cycle{1,2,3,4,5}-2241.json`
- `.sir/evidence/audit-20261113/probe/probe-report.json` + 6 overlay shots
- `.sir/evidence/audit-20261113/beforeafter/`:
  - `before-429-blank-shell-390.png` vs `after-429-shell-still-loads-390.png`
    vs `after-429-api-retry-recovers-390.png`
  - `before-hs-error-placeholder-390.png` vs `after-hs-error-clean-390.png`
  - `before-health-actions-en-390.png` vs `after-health-actions-en-390.png`
    vs `after-health-actions-ar-390.png`
- Refreshed `.sir/evidence/r46/cards-*.png` (verify's browser tests re-captured
  with the new Export button present).

## Commits pushed to main

- `8541911` audit-2241: exempt static shell from read rate limit; retry GETs once on 429
- `3c1922f` audit-2241: fix raw {0} i18n leaks in error badges; add health report export
- `3f1f9ec` audit-2241: checkpoint + clean sweep evidence (cycles 4-5) + refreshed r46 shots

## CI status

`ops/ci-quota-exhausted.flag` is still present; GitHub Actions runs fail in
~4 s with zero steps (runs 43523856741, 43525215883 — quota, not code).
Per WORKER_PREAMBLE rule 18, the full local verification above is the gate.

## Still open / notes

- Sustained overload (>60 s of continuous 429s) still surfaces each view's
  normal error state with Retry — by design; the wrapper only absorbs
  transient bursts.
- `sweep-cycle3-2241.json`'s 2 findings were caused by this audit's own
  evidence burst hitting the live server mid-sweep; documented in the defect
  log. Future evidence scripts should target a separate port.
- FEATURE_GAPS ranks 6-14, 16-24 remain in `.sir/plans/FEATURE_GAPS.md`
  (rank 16 first-run sheet already shipped in R70; rank 15 shipped here).
