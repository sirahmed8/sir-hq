# Audit report: audit-sir-study-20261114-0541 (SIR Study)

Date: 2026-11-14
Worker: devin
Repo: D:/Projects/SIR Study, branch main
Commits this round: d8bc649 (CLS fixes + regression test), 807ba1e (checkpoint),
0754301 (evidence pairs), 76f55c6 (clean-cycle audit JSONs)

## 1. What the round was asked to do

Brief: D:/Projects/_SIR/ops/briefs/audit-sir-study-20261114-0541.prompt.txt
(checklist: .sir/PLAN.md audit loop; team lens: layout/overflow/clipping +
standard probes).

Open every page, tab, sheet and flow at 320/390/768/1280 px, light and dark, in
every supported language (ar RTL, en LTR), in a real browser; log every defect
in .sir/DEFECTS_20261114-0541.md; fix each at its root; add a browser
regression test; commit and push after each fix; ship at least 10 visible
improvements with before/after screenshots under .sir/evidence/; repeat until
two cycles in a row find nothing; write this report and run agy-done.

All browser work was headless Playwright (scripts/sir_browser.py Chromium with
system-Chrome fallback, `PLAYWRIGHT_NODEJS_PATH=C:/Program Files/nodejs/node.exe`,
`--mute-audio`), every browser/context closed in finally blocks. No visible
tab was opened. URLs: http://127.0.0.1:3300 (current tree) and
http://127.0.0.1:3301 (git worktree D:/Projects/sir-study-before-0541 at a60d497,
used only for the "before" half of evidence pairs; removed after capture).
legacy/ untouched; no private data opened.

## 2. Cycle 1 findings and root causes

Raw audit (`scripts/audit_20261113.py`, 9 pages x 4 widths x 2 themes x 2
languages = 144 combos + tab/dead-control/copy/reduced-motion probes):
**13 layout-shift defects, CLS 0.24-0.74**, on sad/or/hci/elec/ba at
320/768/1280 px in both themes and languages
(.sir/evidence/20261114-0541/audit/cycle1-defects.json).

Investigation tooling added under scripts/audit_0541_*.py:
cls_sweep (flagged-combo replay), cls_bisect (script blocking), font_test,
mutation_probe (DOM mutation timeline), nav_probe/nav_rows/nav_widths (header
geometry), rect_diff, shift_capture, late_shift, shift_rects (layout-shift
source previousRect/currentRect - the decisive instrument), pairs (evidence).

### D1 - CLS: late-inserted chrome grew the sticky header (root-fixed)

- `guides/study-guide-ui.js` injects `.sir-read-progress` into `.nav-actions`
  ~190 ms after first paint, widening it 52 px -> 164 px.
- Below 900 px `.nav-content` wraps. The `.tab-bar` flex-basis (~829 px
  max-content) takes its own line, and the wider `.nav-actions` no longer fit
  on the tab bar's line, so it wrapped to a THIRD nav row. Proven with
  shift-rect attribution on or.html 768 light en: `#main-content` moved
  y=159->209 and shrank h=685->635; `.nav-actions` w=52->164.
- At >=900 px the always-on `flex-wrap: wrap` let the same chip push a second
  row at borderline widths.

Fixes in `guides/study-r11.css`:
- `.nav-content` wraps only below 900 px; `nowrap` at >=900 px.
- Below 900 px explicit `order` keeps `.nav-brand-group` + `.nav-actions` on
  row 1 and `.tab-bar` on row 2, so chip widening stays inside row 1 and the
  row count never changes. Verified: nav-actions top=0 / tab-bar top=50 at
  320/390/700/768/850 px; nav height identical before and after JS.
- <=400 px: chip drops its mini progress bar and tightens padding
  (104 px -> 62 px) so it fits the brand row on the narrowest phones.
- <=350 px: `.nav-brand-text` hidden (logo carries the brand) - the wordmark
  was the last slack at 320 px.

### D2 - CLS: empty `.sir-match-count` pill rendered under every search box

`.sir-match-count` is created with `hidden = true`, but its class sets
`display: inline-block`, beating the UA `[hidden] { display: none }` rule, so
an empty pill painted under every `.search-box-wrap` on load.
Fix: `.sir-match-count[hidden] { display: none; }`.

### D3 - CLS: read-toggle gutter unreserved before JS runs

`study-guide-ui.js` adds `.sir-has-read` + an absolutely positioned 44 px
`.sir-read-btn` to every `h2/h3.card-title` after first paint. Static CSS now
reserves `padding-inline-end: 52px` on those headings so no heading gains a
wrapped line post-paint.

## 3. Regression coverage

`tests/test_browser.py::test_24_audit0541_header_stability_no_cls` installs a
layout-shift PerformanceObserver, loads or.html at 320 and 768 px and
electronics.html at 1280 px, waits past the late-injection window, and asserts
total CLS < 0.05, the read-progress chip exists, and the header keeps its
two-row order below 900 px. Passes (7.2 s standalone).

## 4. Evidence - 12 visible improvement pairs

`.sir/evidence/20261114-0541/improvements/{before,after}/` + `contact-sheet.png`
+ `pairs.json`. Captured by `scripts/audit_0541_pairs.py` against the pre-fix
worktree (a60d497) on :3301 vs the fixed tree on :3300 with identical
prefs/theme/lang application.

Pixel-verified with the project's pair verifier (COMPARE_JS): all 12 pairs
non-blank and non-identical. diffPct: e01-e05 (320 px headers) 36-41% (whole
page moves up ~50 px because the header lost its third row); e08-e10 (768 px)
43-54%; e06/e07/e12 (390 px chip slimming) 0.7-16.7%; e11 search-region 37.5%.

## 5. Audit cycles

| Cycle | Result | Artifact |
|-------|--------|----------|
| 1 | 13 defects (CLS 0.24-0.74) | audit/cycle1-defects.json |
| 2 | 0 defects | audit/cycle2-defects.json |
| 3 | 0 defects | audit/cycle3-defects.json |

Two consecutive clean cycles - the brief's repeat-until-clean loop is met.
Defect log: .sir/DEFECTS_20261114-0541.md.

## 6. Verification (real command output)

- `PLAYWRIGHT_NODEJS_PATH="C:/Program Files/nodejs/node.exe" python -m
  unittest discover -s tests -p "test_*.py"` -> **Ran 92 tests in 855.140s -
  OK** (includes new test_24; integrity eval 105/105 printed inside suite).
- `scripts/verify.ps1` -> **ALL CHECKS PASSED: SIR Study is Green & Verified!**
  18/18 steps (htmlhint/prettier warnings are the known non-blocking ones;
  browser-dependent subtests skip inside verify.ps1 without
  PLAYWRIGHT_NODEJS_PATH, covered by the standalone run above).
- Flagged-combo CLS re-sweep after fixes: cls <= 0.002 on all 13 previously
  flagged combos (residual = audit-harness prefs reflow, excluded by design;
  standalone page loads show zero shifts >= 0.01).
- `git status` clean; all commits pushed to main: d8bc649, 807ba1e, 0754301,
  76f55c6.

## 7. CI status

`D:/Projects/_SIR/ops/ci-quota-exhausted.flag` is present (Actions minutes
exhausted, resets ~2026-12-01 per prior rounds). Per WORKER_PREAMBLE rule 18
the full local verification above is the substitute; no CI-green claim is
made. First push attempt failed once on a transient connect error; retry
succeeded.

## 8. Uncertainties / notes

- The 0.24-0.74 CLS values only reproduced inside the audit harness's
  sequential 144-combo sweep and after its own prefs-forcing step; standalone
  loads showed the same header-wrap mechanism via shift-rect attribution, and
  the fix removes the mechanism itself (row count can no longer change).
- e11/e12 "search" pairs required activating the Question Bank tab first
  (search boxes live in a non-default panel); both sides got identical
  treatment.
- `.sir/evidence/r20/browser_report.json` is regenerated by
  tests/test_browser.py tearDownClass on every suite run; the committed diff
  is the fresh run's output, not hand edits.

## 9. Open promises (unchanged)

M2 spaced repetition OPEN; T-103 portal watcher, T-107 Drive mirror, T-023
retirement, T-113 rotation items unchanged; legacy/ untouched.
