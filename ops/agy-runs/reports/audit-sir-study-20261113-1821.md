# Audit report: audit-sir-study-20261113-1821 (SIR Study)

Date: 2026-11-13
Worker: kilo (resumed the round after the previous model's quota cut)
Repo: D:/Projects/SIR Study, branch main
Commits this round: 2dd6a9f (fixes, tests, evidence), 0f9d195 (checkpoint)

## 1. What the round was asked to do

Brief: D:/Projects/_SIR/ops/briefs/audit-sir-study-20261113-1821.prompt.txt

Open every page, tab, sheet and flow at 320/390/768/1280 px, light and dark, in
every supported language, in a real browser; log every defect in
.sir/DEFECTS_20261113-1821.md; fix each at its root; add a browser test; commit
and push after each fix; ship at least 10 visible improvements with before/after
screenshots under .sir/evidence/; repeat until two cycles in a row find nothing;
write this report and run agy-done.

The brief allows only SIR Study files; AHome/Habiba data was never opened. All
browser work was headless Playwright (py -3, scripts/sir_browser.py, system
Chrome fallback), closed in a finally block. No visible browser tab was opened.
URLs opened: http://127.0.0.1:3300 (current tree) and http://127.0.0.1:3301
(git worktree D:/Projects/sir-study-before-audit1821 at 1c9475c, used only to
capture the "before" half of the evidence pairs).

## 2. State at resume (what the previous model had done)

- Commit 20e0b97 "fix swallowed quiz markup and localize JS-generated chrome".
- D1: 35 quiz buttons in guides/data-structures.html and guides/electronics.html
  were missing the `>` between the last attribute and the label, so the browser
  swallowed the option/check labels into attributes (`<button ... data-index="0"
  أ) المصفوفات (Arrays)</button>`). Fixed; test_21 added.
- D2: JS-generated chrome (score, mastery count, check/copy buttons, question-pill
  titles, exam countdowns, review sheet, subtitle bar, OR graph point labels, toast
  icon) was hard-coded Arabic inside inline scripts and stayed Arabic in EN. Fixed
  with new i18n keys + a `sirDynamicI18n` painter in guides/study-guide-ui.js.
- D3: exam countdowns flipped to "exam over" at exam start instead of during the
  live hour. Fixed with examEnd = start + duration and a live state.
- D4: confirm dialogs / review sheet / subtitle bar strings localized.
- Evidence: 12 before/after pairs, but 3 of them (e05 copy button, e07 SAD hero,
  e10 DS timer) were pixel-identical on both sides (MD5 equal), so only 9 were
  real. Cycle 3 found 16 page-weight defects on or.html ("701 KB transferred");
  cycle 4 was 0 but was captured before the page-weight root was fixed.

Untracked at resume: .sir/evidence/20261113-1821/audit/cycle4-defects.json.

## 3. Defects found and fixed this round

### D5 - DFD lab default diagnosis panel stayed Arabic in English mode

- Page: guides/sad.html.
- Symptom: `#dfd-diag-status`, `#dfd-diag-desc` and `#dfd-diag-exam-rule` are
  static Arabic markup. `simulateDfdRule()` localizes them, but it only runs on a
  tab click, so on load and after switching to English the panel read
  `الحالة: نموذج سليم 100%`.
- Root cause: no repaint at load and no `sir:i18n-applied` listener; the event is
  dispatched on `document` with `bubbles: false`, so a `window` listener never
  fires (the first fix attempt used window and did nothing - verified).
- Fix (guides/sad.html): `simulateDfdRule()` now records `window.__dfdCurrentRule`
  and `window.__dfdCurrentBtn`; `sirDfdRepaint()` runs at the end of the script
  (default markup state) and on `document.addEventListener('sir:i18n-applied', ...)`,
  so the panel follows the language and keeps the learner's selected rule.
- Regression test: tests/test_browser.py::test_22 asserts EN default
  `Status: model 100% valid`, English Black Hole violation text, and AR
  `الحالة: نموذج سليم 100%`.
- Before/after: .sir/evidence/20261113-1821/improvements/{before,after}/e07-sad-dfd-en.png

### D6 - Heaviest guide transferred 701 KB (no compression)

- Symptom (cycle 3, 16 findings): or.html transferred 701 KB at every width,
  theme and language. Root cost: 370,028 bytes of HTML (82 inline SVGs) plus
  ~120 KB CSS/JS, all uncompressed.
- Root cause: scripts/serve.py is a plain SimpleHTTPRequestHandler with no
  Content-Encoding. Production static hosts gzip these files; the local server
  did not.
- Fix (scripts/serve.py): when the request has `Accept-Encoding: gzip`, text
  assets (.html .htm .css .js .mjs .json .svg .txt .xml .map) are gzipped on the
  fly with `gzip.compress(..., 6)`, served with Content-Encoding: gzip, a correct
  Content-Length and `Vary: Accept-Encoding`; clients without gzip still get the
  plain file. Measured: or.html 370,028 -> 70,659 bytes (5.2x); whole-page
  transfer 701 KB -> 266 KB in Chromium.
- Regression tests: tests/test_server_gate.py::test_text_assets_are_gzipped_and_intact
  and ::test_clients_without_gzip_get_the_plain_file; tests/test_browser.py::test_22
  asserts the or.html page weight is under 300 KB.

### Evidence pairs repaired (not new defects)

- e05-ds-copybtn-en: recaptured; before `.btn-copy-code` = `نسخ الكود`,
  after = `Copy code`.
- e07-sad-dfd-en: recaptured; before = `الحالة: نموذج سليم 100%`,
  after = `Status: model 100% valid`.
- e10-elec-checkbtn-en: recaptured; before `.btn-check` = the whole explanation
  paragraph (D1 malformed markup), after = `Check answer`.
- Tool: scripts/audit_1821_pairs.py (takes base URL + out dir, asserts the
  visible text of the changed control). All 12 pairs now differ (MD5 check:
  pairs=12, different=12). The two stale identical files
  (e07-sad-hero-en.png, e10-ds-timer-en.png) were removed.

## 4. Cycles (scripts/audit_20261113.py, 144 combos per cycle)

- cycle3 (before D6 fix): 16 defects, all page-weight on or.html
  (.sir/evidence/20261113-1821/audit/cycle3-defects.json).
- cycle4 (after D5+D6): `Cycle 4: 0 defects -> .../cycle4-defects.json` (exit 0).
- cycle5 (final code): `Cycle 5: 0 defects -> .../cycle5-defects.json` (exit 0).
- Two consecutive clean cycles on the final code. The sweep covers 9 pages x
  320/390/768/1280 x light/dark x ar/en, plus tab panels, dead controls,
  reduced motion and performance probes.

## 5. Commands and real output

```
> powershell -NoProfile -ExecutionPolicy Bypass -File scripts\verify.ps1
...
[15/17] Running Unit Tests...
Ran 53 tests in 1.441s
OK (skipped=2)            # browser tests skipped without PLAYWRIGHT_NODEJS_PATH
...
[17/17] Search Index Freshness & Data Integrity...
search-index.json is fresh (228 headings)
DATA INTEGRITY: all checks passed
==========================================================
     ALL CHECKS PASSED: SIR Study is Green & Verified!
==========================================================
```

```
> $env:PLAYWRIGHT_NODEJS_PATH='C:\Program Files\nodejs\node'; py -3 -m unittest tests.test_browser
Ran 22 tests in 837.982s
OK
(exit 0)
```

```
> $env:SIR_AUDIT_TAG='20261113-1821'; py -3 scripts/audit_20261113.py 4
Cycle 4: 0 defects -> .../cycle4-defects.json   (exit 0)

> $env:SIR_AUDIT_TAG='20261113-1821'; py -3 scripts/audit_20261113.py 5
Cycle 5: 0 defects -> .../cycle5-defects.json   (exit 0)
```

```
> curl.exe -s -o NUL -D - -H "Accept-Encoding: gzip" http://127.0.0.1:3300/or.html
HTTP/1.0 200 OK
Content-Type: text/html
Content-Encoding: gzip
Content-Length: 70659
Vary: Accept-Encoding
```

```
> py -3 -m unittest tests.test_server_gate -v
Ran 8 tests in 0.841s
OK
```

Integrity eval inside the suite: 73/73 refusals, 32/32 explanations with
citations, 105/105 checks passed.

Gitleaks: only the two known hits in the gitignored, untracked .env (never
committed); CI checkout is clean. verify.ps1 treats it as non-blocking.

## 6. CI

- Run 43485533674 (HEAD 2dd6a9f) completed failure in 3s with 0 job steps.
- D:/Projects/_SIR/ops/ci-quota-exhausted.flag exists: GitHub Actions minutes are
  exhausted (3000/month, reset expected 2026-12-01). This is the billing/quota
  signature, not a code failure. Per WORKER_PREAMBLE rule 18, the full local
  verification above (verify.ps1 17/17, 53 unit tests OK, 22 browser tests OK in
  838s, integrity 105/105) is the substitute. No CI fix was attempted.
- The previous run 43478415287 (20e0b97) also failed in 4s with 0 steps, same cause.

## 7. Evidence index

- .sir/DEFECTS_20261113-1821.md - D1-D6, root causes, fixes, tests, accepted notes.
- .sir/evidence/20261113-1821/improvements/before|after/ - 12 pairs:
  e01-ds-quiz-ar, e02-ds-quiz-en, e03-elec-quiz-ar, e04-elec-quiz-en,
  e05-ds-copybtn-en, e06-or-hero-en, e07-sad-dfd-en, e08-hr-hero-en,
  e09-ba-hero-en, e10-elec-checkbtn-en, e11-or-quiz-en, e12-or-review-en.
- .sir/evidence/20261113-1821/audit/cycle3-defects.json (16, before D6),
  cycle4-defects.json (0), cycle5-defects.json (0).
- scripts/audit_1821_pairs.py - repeatable evidence capture with text assertion.

## 8. What is still open / unsure

- M2 spaced repetition (flashcards + SRS scheduling) is still OPEN. Not part of
  this brief; do not claim it.
- T-103 portal watcher needs one real portal read while Chrome is closed; the
  sync currently skips cleanly on a locked profile. T-107, T-023, T-113 unchanged.
- The 7 subject guides still carry a hardcoded per-guide exam countdown that can
  say "exam over" inside the exam hour (the hub got the live-state treatment in
  an earlier round). This is the same class as D3 but outside this round's
  captured pages; recommend a follow-up task.
- serve.py still binds with SO_REUSEADDR, so two instances can share port 3300
  (known optional item; this round had to stop three stale instances before the
  gzip server could be verified).
- The audit page-weight threshold is 700 KB; or.html is now 266 KB, but the
  other 8 pages were always below it, so the margin is wide.

## 9. Recommendations

1. Delete ops/ci-quota-exhausted.flag only after 2026-12-01, then confirm one run
   is green before trusting CI again.
2. Port the hub's live exam-hour countdown state to the 7 guide pages (one shared
   helper instead of per-page copies).
3. Add the serve.py gzip behaviour to the production host check (Firebase/
   Vercel already gzip) so local and production page weight stay comparable.

## 10. Done signal

`python D:/Projects/_SIR/scripts/agy-done.py audit-sir-study-20261113-1821 ok "<one line>"` - run after this report was written.