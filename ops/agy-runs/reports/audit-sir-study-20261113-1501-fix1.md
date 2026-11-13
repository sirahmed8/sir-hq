# Report: audit-sir-study-20261113-1501-fix1

Task: fix every item that failed verification of `audit-sir-study-20261113-1501`
(verification file: `D:/Projects/_SIR/ops/verifications/audit-sir-study-20261113-1501.md`).

## Failed items and what was done

### Item 7 — agy-done signal for audit-sir-study-20261113-1501 never verified

The original audit's report and checkpoint claimed completion, but no
`agy-done.py` output existed in the logs. This round ran the signal for real:

```
$ python D:/Projects/_SIR/scripts/agy-done.py audit-sir-study-20261113-1501 ok "Audit complete: 8 defects fixed, 2 consecutive clean cycles, report at ops/agy-runs/reports/audit-sir-study-20261113-1501.md"
signalled audit-sir-study-20261113-1501 ok
```

### Item L18 — Native-App Feel (disable browser defaults)

The verification found no evidence that default text selection / the browser
right-click context menu are disabled site-wide, and `verify.ps1` did not check
it. A previous worker round had already staged a partial implementation; this
round reviewed it, repaired the defects in it, verified it end to end, and
committed it.

What the fix does (shared lesson L18, `D:/Projects/_SIR/ops/LESSONS.md`):

- `guides/study-r11.css` — `user-select: none` (+ `-webkit-` prefix) on
  `html, body` turns off the browser default text selection for app chrome.
  Exemptions keep real editing/copying working: `input`, `textarea`,
  `[contenteditable="true"]`, and `pre, code, kbd, samp, table, .sir-selectable`
  all keep `user-select: text`. New `.sir-context-menu` / `.sir-context-item`
  styles (fixed position, z-index 950, 40px min item height, focus-visible ring,
  press scale).
- `guides/study-head.js` — new IIFE that replaces the browser context menu with
  the app's own: `role="menu"` container, `role="menuitem"` Refresh button
  (localized through `SIR_I18N.t('ctxmenu.refresh')` with a built-in fallback),
  Escape closes, ArrowUp/ArrowDown move between items, clicking outside, scrolling
  or resizing closes it, a second right-click replaces instead of stacking, and
  it never opens over `INPUT`/`TEXTAREA`/`SELECT`/contenteditable targets or when
  a real text selection exists (so select/copy/paste inside fields is untouched).
- `guides/i18n.js` — new keys `ctxmenu.title` / `ctxmenu.refresh` in both the
  English and Arabic dictionaries.
- `guides/index.html` — the zero-second redirect stub does not load
  `study-head.js`, so it carries the same `user-select: none` rule inline.
- All 8 content pages already load `study-head.js` + `study-r11.css`
  (verified by grep and by the new tests).

Guards/tests added:

- `scripts/verify_native_app_feel.py` — headless Playwright check over all 8
  pages asserting: computed `user-select` is `none` on html/body, `text` on a
  real field, `text` on every `pre/code/table`; `contextmenu` on body is
  `preventDefault`ed and opens exactly one `#sir-context-menu` with `role=menu`,
  >=1 action, keyboard focus on the item, Escape closes it, no stacking on a
  second right-click, and the app menu never opens over a real field. Exit 0 =
  pass, 1 = failures, 2 = environment skip (Playwright/Node unavailable).
- `tests/test_native_app_feel.py` — 11 source-level unittest guards pinning the
  CSS rules, the JS handler/menu/keyboard support, page script/css coverage,
  the index.html inline guard, both-language i18n keys, and sw.js precache.
- `tests/test_browser.py::test_23_audit1501fix1_native_app_feel` — the same live
  behaviour proven inside the existing Playwright suite on every page.
- `scripts/verify.ps1` — new step 18/18 runs `verify_native_app_feel.py`;
  sets `PLAYWRIGHT_NODEJS_PATH` to the system Node only when the env var is
  unset and the file exists (no-op on CI ubuntu where the pip Playwright driver
  is bundled); exit code 2 is reported as a non-blocking WARN.

## Repairs made to the inherited uncommitted work

- `scripts/verify.ps1` step numbering was broken: headers read
  `[16/20] -> [19/20] -> [20/20]` with no steps 17/20 or 18/20. Renumbered to a
  consistent 18 steps (`[1/18]` … `[18/18]`).
- `guides/study-head.js` was missing its trailing newline — added.
- `scripts/verify_native_app_feel.py` crashed with a traceback when the
  Playwright Node driver was missing; it now returns exit code 2 (skip) for
  environment limitations, matching how the unittest browser suite skips.
  `launch()` also stops the playwright instance cleanly if the chrome-channel
  fallback fails.
- First verify.ps1 run after wiring failed at step 18 for exactly that reason
  (`PLAYWRIGHT_NODEJS_PATH` unset in the PowerShell session); fixed as above.

## Commands run and real output

```
$ python scripts/verify_native_app_feel.py        # with PLAYWRIGHT_NODEJS_PATH set
  [OK] hub: app chrome unselectable, app menu, field copy/paste intact
  [OK] ds: ...  (all 8 pages identical)
NATIVE-APP FEEL: 8 pages pass lesson L18 (no browser selection, app context menu, fields copyable)
exit 0

$ python -m unittest tests.test_native_app_feel -v
Ran 11 tests in 0.012s — OK

$ PLAYWRIGHT_NODEJS_PATH="/c/Program Files/nodejs/node" python -m unittest \
    tests.test_browser.BrowserAcceptance.test_23_audit1501fix1_native_app_feel -v
test_23_audit1501fix1_native_app_feel ... ok
Ran 1 test in 9.190s — OK

$ node --check guides/study-head.js   -> OK
$ python -c "import ast; ast.parse(...)" on all touched .py files -> PY-OK x3

$ powershell -NoProfile -ExecutionPolicy Bypass -File scripts/verify.ps1
  ... all steps green ...
  [18/18] Native-App Feel (L18)...
  [OK] native-app feel verified (no browser selection, app context menu, fields copyable)
  ALL CHECKS PASSED: SIR Study is Green & Verified!   (exit 0)
```

Note: inside verify.ps1 the unittest step reports the browser suite as skipped
(`chromium unavailable ... PLAYWRIGHT_NODEJS_PATH`) because that env var is only
set for step 18; the browser tests themselves pass when run with the env var
(test_23 above, and the full browser suite ran green in the previous audit
round). This matches the project's established local pattern.

## Git / CI

- Commit `1dc4d04` "Fix audit 20261113-1501 verification: native-app feel (L18)
  + done signal" — 9 files, pushed to `main`.
- Commit `5a940e5` "Checkpoint: audit 20261113-1501-fix1 complete" — pushed.
- CI run `43501871040` (HEAD 1dc4d04) completed `failure` with **zero job
  steps** in seconds — the known GitHub Actions quota exhaustion
  (`D:/Projects/_SIR/ops/ci-quota-exhausted.flag` present, resets ~2026-12-01).
  Per WORKER_PREAMBLE rule 18 the full local verification above is the
  substitute; prior runs 43490282069 / 43485533674 show the same signature.

## Still open / notes

- M2 spaced repetition remains the only open product promise (unchanged).
- T-103 portal watcher, T-107 Drive mirror, T-023 script retirement, T-113
  owner-data step: unchanged.
- `legacy/` untouched; no secrets or private data in any change.
- L18's wider lesson text also mentions per-character bidi detection on text
  inputs and currency auto-detection; those parts belong to other lessons
  (L8/L22) already covered elsewhere and were not part of the failed item.
