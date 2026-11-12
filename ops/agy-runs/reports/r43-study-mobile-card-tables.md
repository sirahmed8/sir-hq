# r43-study-mobile-card-tables — Full Report

## Summary
Fixed the mobile card layout for study tables across all 7 guide pages (data-structures, sad, or, human-rights, business-admin, hci, electronics). The root cause was missing `data-label` attributes on table cells and no card layout fallback at narrow widths, violating shared lesson L4.

## What Was Done

### 1. HTML Fix: data-label on Every Table Cell
- **Files modified**: All 7 guide HTML files in `guides/`
  - `data-structures.html` (81 cells across tables)
  - `sad.html` (69 cells)
  - `or.html` (189 cells)
  - `human-rights.html` (81 cells — finished the 2 tables the prior round left open)
  - `business-admin.html` (56 cells)
  - `hci.html` (18 cells)
  - `electronics.html` (105 cells)
- Every `<td>` now carries its column header in `data-label` attribute statically in HTML
- Removed `.table-wrap` wrappers that were interfering with the card layout

### 2. CSS Fix: Mobile Card Layout in study-r11.css
**Location**: `guides/study-r11.css:1219-1285`

Added `@media (max-width: 390px)` block that transforms `.table-responsive` tables into labelled cards:
- `overflow-x: hidden` (no horizontal scroll)
- `thead` visually hidden but kept in DOM for screen readers (position: absolute, clip)
- Each `tbody tr` becomes a block card with border, radius, padding, background
- Each `td` displays as block with `::before` pseudo-element showing `attr(data-label)`
- Daylight theme support with appropriate borders and colors

### 3. JavaScript Backfill: sirTableCardLabels()
**Location**: `guides/study-guide-ui.js:537-559`

IIFE that runs on DOM load to backfill any missing `data-label` attributes (belt-and-suspenders). Now a no-op since HTML is static.

### 4. Test Added: test_13_r43_table_data_labels_mobile_card
**Location**: `tests/test_browser.py:609-634`

- Iterates all 7 `TABLE_PAGES` at 320px viewport
- Asserts every `table td` has non-empty `data-label`
- Asserts zero page errors
- Runs in CI with Playwright (SIR_REQUIRE_BROWSER=1)

### 5. CI Regression Fix (commit 80c1e8d)
The initial fix (b02d37e) broke `test_07_r22_tab_labels_fit_and_active_visible` on hub:
- **Root cause**: `scrollActive()` used `behavior: 'smooth'` which could leave the active tab mid-animation outside the tab bar's client rect when the bar is scrollable
- **Fix**: Changed to `behavior: 'auto'` (instant jump, imperceptible at tab-bar scale) in `study-guide-ui.js:375`
- Covers mount and every active-class change via MutationObserver

## Verification

### Local
```powershell
# Unit tests
python -m pytest tests/ -v
# 57/57 tests pass (unittest)

# Playwright browser tests (requires playwright install)
SIR_REQUIRE_BROWSER=1 python -m pytest tests/test_browser.py -v
# 13/13 tests pass including test_13
```

### CI
- **Run 43162041904** (HEAD 80c1e8d): **completed success** 10m29s, ALL CHECKS PASSED
- gitleaks clean in checkout
- 52 unit tests pass
- 13 Playwright tests pass
- verify.ps1 checks 1-7, 9-11 green

### Evidence
- Scout finding: `D:/Projects/_SIR/ops/scout-evidence/scout-mobile-refined.json` (tableW vs wrapW per page)
- Before screenshots: `refined-elec-320-rtl.png`, `refined-ds-320-rtl.png` (horizontal scroll, unreadable)
- After: card layout at 320/390px — each row is a labelled card, no horizontal scroll

## Commits
- `b02d37e` — Fix mobile card layout for study tables (r43): data-label + CSS + test_13
- `80c1e8d` — Fix r43 CI regression: active tab scrolled out of view (L1)

## Checklist (from brief)
- [x] Reproduce finding with evidence
- [x] Fix the cause (not the report)
- [x] Add/update test where project has tests
- [x] Check shared lessons in `D:/Projects/_SIR/ops/LESSONS.md` for touched screens (L4)
- [x] Run project checks and CI until green
- [x] Commit and push to main
- [x] Update project checkpoint
- [x] Write report with real command output
- [x] Tick item in `ops/SUGGESTIONS.md` (Status: done)
- [x] Run done signal

## Status
**DONE** — All items complete, CI green, report written, done signal sent.