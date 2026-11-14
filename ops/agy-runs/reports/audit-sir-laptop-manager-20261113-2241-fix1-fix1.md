# Report: audit-sir-laptop-manager-20261113-2241-fix1-fix1

Task: fix the failed verification of `audit-sir-laptop-manager-20261113-2241-fix1`
(item 7: >=10 visible improvements with before/after screenshots).

## What was broken (from the verification file)

1. `src/sir_laptop_manager/ops_ui/static/index.html` lines ~3055-3060 held
   literal `${tr('suFilterAll')}` etc. in static HTML - never evaluated, so the
   startup impact filter/sort buttons rendered raw template text (improvement 3
   visibly broken).
2. `after-health-ar-390.png` showed raw server log lines
   (`GET /api/health/history ... 200`) above the health score card.
3. `conn-dot` before/mid/after PNGs were byte-identical; `tabbar` and
   `focus-ring` before==mid; `startup`/`apps` before==mid - not 10 clean
   working improvements.

## Fixes (cause, not report)

### index.html

- Startup filter chips + sort button and the apps sort button now use the
  existing `data-i18n-text` binding mechanism with English fallback text
  (lines ~3055-3060, ~3395). `toggleLanguage()` re-syncs the two dynamic sort
  labels after `applyI18nBindings` so a language switch cannot reset a
  non-default sort label (lines ~5526-5530).
- `#daemon-log-tail` moved inside the collapsed
  `<details class="dev-details">` disclosure (was a sibling rendered directly
  above the health score card); CSS margin adjusted. Raw daemon log lines now
  only appear when the user opens Details.

### tests/test_audit_20261113_2241_fix1.py (+4 tests)

- `test_static_markup_has_no_unevaluated_tr_placeholders` - strips every
  `<script>` block and fails on `${tr(`/`${trf(` in real markup.
- `test_startup_filter_buttons_use_i18n_bindings` - the six sort/filter
  buttons carry the expected `data-i18n-text` keys.
- `test_daemon_log_tail_hidden_inside_details` - log tail sits between
  `<details class="dev-details">` and its `</details>`.
- `test_data_i18n_text_keys_exist_in_both_dicts` - every `data-i18n-text`
  key exists in both the en and ar dictionaries.

### Evidence re-capture

New script `scripts/audit-20261113-2241-fix1-fix1-evidence.mjs`. The ops server
reads `static/index.html` from disk per request, so the script swaps in three
variants (`variants/before.html` = 3c1922f, `variants/mid.html` = cd73814,
`variants/after.html` = working tree), captures all scenarios per variant,
and restores the working file in `finally`.

Scenario fixes versus the previous capture:

- `tabbar` captured at 1280px (the `.tab-btn.active::after` indicator only
  exists in the desktop tab bar; the 390px bottom bar has none).
- `conn-dot` captured as a `footer` element screenshot while hovering the dot
  after `conn-dot-ok` is confirmed (previous clip at y=800 captured body
  content because the footer is below the fold on a tall page).
- `focus-ring` uses keyboard `Tab` + `body:focus-visible`; verified
  `getComputedStyle(document.body).outline` = `none` on before vs
  `auto 3px rgb(16,185,129)` on after.
- `toast` screenshot taken ~120ms after trigger to catch the slide-in.

30 PNGs in `.sir/evidence/audit-20261113-2241-fix1/`; `IMPROVEMENTS.md`
rewritten to list 13 improvements, each with an MD5-verified differing pair.

## Verification output (real)

- `ruff format --check src tests`: 1 file reformatted -> fixed, now clean.
- `ruff check src tests`: `All checks passed!`
- `mypy src tests`: `Success: no issues found in 131 source files`
- `pytest tests -x -q`: `392 passed, 1 skipped in 399.09s`
- Targeted: `pytest tests/test_audit_20261113_2241_fix1.py tests/test_r25_i18n.py` -> `29 passed in 9.67s`
- Live probe (Playwright, ar/dark/390px on http://127.0.0.1:8765):
  `su-filter-all` = "الكل", `btn-sort-startup` = "ترتيب: التأثير",
  `btn-apps-sort` = "ترتيب: الاسم"; `daemon-log-tail` parent = DETAILS,
  `detailsOpen` = false, `tailVisible` = false; health view innerText
  contains no `GET /api` lines.
- CI: `ops/ci-quota-exhausted.flag` still present; `gh run list` shows the
  push run `43578957203` failed in 4s with zero steps = Actions quota, not
  code (rule 18). Local verification above is the gate and is green.

## Commits pushed to main

- `33a0da3` fix1-fix1(2241): repair i18n placeholder leaks and health log
  tail; recapture verified evidence pairs
- `2429cc6` chore: commit refreshed r46/r60/r70 browser evidence screenshots
  (pre-existing uncommitted evidence refreshes from the previous round)

## Notes / leftovers

- `_shot_r70fix.py` (untracked, repo root) is a previous round's scratch
  screenshot probe writing into `_SIR/ops/verifications/evidence`; left
  untracked.
- `variants/*.html` inside the evidence folder are intentional provenance for
  the three served index.html versions.
- Browser use this round: headless Playwright chromium via the capture
  script and two small node probes against http://127.0.0.1:8765; all browser
  instances closed (`browser.close()` in `finally`). No tabs left open.
