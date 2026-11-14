# r82-study-drawer-hidden-from-taborder — report

## Finding (reproduced)
The closed `.side-drawer` was hidden only by `transform: translateX(±100%)` in `guides/study-r11.css`. With no `visibility:hidden`, `aria-hidden` or `inert`, all drawer links/buttons stayed in the keyboard Tab order and the accessibility tree on every page (hub, data-structures, sad, or, electronics, etc.). Scout evidence: `D:/Projects/_SIR/ops/scout-evidence/scout-a11y-20261114.json` `tab_first15` showed drawer-brand / drawer-close-btn / drawer-nav-items as Tab stops 9-15+.

## Fix (cause, not the report)
`guides/study-r11.css` — `.side-drawer` now mirrors the existing `.settings-modal` pattern (lines ~206-241):

- Closed state: `visibility: hidden; pointer-events: none;` added; transition is now `transform 0.32s var(--spring-modal-bezier), visibility 0s linear 0.32s` so visibility flips to hidden only after the slide-out finishes.
- `.side-drawer.open`: `visibility: visible; pointer-events: auto;` with `visibility 0s linear 0s` so focus can land inside immediately on open (the existing `focusFirstIn()` in `study-shell.js` relies on this).

`visibility:hidden` removes the subtree from both sequential focus navigation and the accessibility tree in all supported browsers — no JS/`inert` changes needed. No HTML changes: the drawer markup is shared markup duplicated across the 8 guide pages and the CSS is the single shared `study-r11.css`, so one rule covers every page. No page renders the drawer statically open (verified: no `class="side-drawer open"` in any HTML; the only `display:none` rule for it is inside the print media block, unaffected).

## Test added
`tests/test_browser.py::test_25_r82_closed_drawer_leaves_tab_order` — on hub (`/START_HERE.html`) and one guide (`/or.html`):
- asserts closed drawer computed style is `visibility:hidden` + `pointer-events:none` and does not have `.open`;
- presses Tab 30 times and asserts `document.activeElement` is never inside `#side-drawer`;
- opens via `#btn-menu-drawer`, asserts `visibility:visible`, `pointer-events:auto`, `.open` present, and focus moved inside.

## Commands run (real output)

- `PLAYWRIGHT_NODEJS_PATH="C:\Program Files\nodejs\node.exe" python -m pytest tests/test_browser.py -k "test_25" -v`
  → `test_25_r82_closed_drawer_leaves_tab_order PASSED` — `1 passed, 24 deselected in 3.88s`
- `... pytest tests/test_browser.py -k "test_11 or test_06 or test_02" -v`
  → `test_02_click_every_visible_button PASSED`, `test_06_r22_no_horizontal_scroll_and_header_clearance PASSED`, `test_11_r24_overlays_focus_in_escape_returns PASSED` — `3 passed in 630.86s` (confirms every visible button still works, header clearance unaffected, overlay focus-in/Escape-returns still correct for both drawer and settings modal).
- `powershell -File scripts/verify.ps1`
  → `ALL CHECKS PASSED: SIR Study is Green & Verified!` — all 18 steps: core files, HTML validity, shared assets drift guard (8 assets, 9 precached), search-index freshness, data-integrity guards (unguarded localStorage, flashcard reset keys, progress reset scope, i18n backup keys), integrity eval (refusal gate + legitimate explanations, 105/105), dev server scripts, gitleaks (2 known false positives in gitignored `.env`, non-blocking), unit tests all OK, native-app feel 8/8 pages.
- `git status` before work: clean tree; `git diff --stat`: no stray edits. After: only `guides/study-r11.css`, `tests/test_browser.py`, `.sir/CHECKPOINT.md` changed (`.sir/evidence/r20/browser_report.json` churn from the filtered test run was restored, not committed — it would have recorded quiz/search as false from the partial run).

## Commits / push
- `2a416eb` `fix(guides): hide closed side drawer from tab order and AT tree (r82)` — pushed to `main` (`68da78e..2a416eb`).
- `2e0c254` `chore(sir): checkpoint r82 drawer tab-order fix` — pushed (`2a416eb..2e0c254`).
- `D:/Projects/_SIR` `7e148bd` `suggestions: mark r82 study drawer tab-order fix done` — pushed to `main`.

## CI status
`gh run list`: run `43564111967` on `2a416eb` completed `failure` in **3 seconds** with no steps — this is the GitHub Actions quota exhaustion, not the code (`D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists, expected reset ~2026-12-01). Prior runs on `main` (`43559217487`, `43559175332`) failed identically in 3s. Per WORKER_PREAMBLE rule 18, "CI green" is replaced by full local verification while the flag exists — verify.ps1 18/18 + targeted Playwright tests all pass and are pasted above.

## Checklist / bookkeeping
- `ops/SUGGESTIONS.md` item `sug-the-closed-side-drawer-is-hidden-b425c23f`: `Status: done` with fix summary (committed in `_SIR` `7e148bd`).
- `.sir/CHECKPOINT.md` updated with the r82 entry.
- `ops/LESSONS.md` checked: L52 (dialog/drawer focus in/out) already satisfied — `toggleSideDrawer` moves focus inside on open and back to `#btn-menu-drawer` on close; the new test asserts this still holds. No new lesson needed (this was a CSS state bug, covered by existing patterns).

## Open / unsure
- Nothing open for this item. When Actions quota resets (~2026-12-01), the next push will exercise the full CI suite including `test_25`.
- Note: `test_25` presses Tab 30 times per page; on pages with very long tab orders the drawer links (previously stops ~9-15) are well inside that window, so the assertion is meaningful.
