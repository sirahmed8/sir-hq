# Fix laptop manager evidence gaps

## Context
Task `audit-sir-laptop-manager-20261114-0722` shipped 6 visible improvements but lacks before/after screenshots for 2 of them:
- Copy path button per largest-file row
- Drive health refresh button

## Required
1. Launch SIR Laptop Manager dashboard in Chrome.
2. Navigate to the Drive tab.
3. For the "Largest files" card:
   - Capture a "before" screenshot showing the list.
   - Click the copy button on one row.
   - Capture an "after" screenshot showing the copy action (e.g., button state or notification).
4. For the "Drive health (SMART)" card:
   - Capture a "before" screenshot.
   - Click the refresh button.
   - Capture an "after" screenshot showing the refresh result.
5. Save all 4 screenshots to `D:/Projects/SIR Laptop Manager/.sir/evidence/audit-20261114-0722/`.
6. Write a short report to `ops/agy-runs/reports/6-fix-laptop-manager-evidence.md` listing the files and what they show.

## Done when
- 4 PNG files exist in the evidence dir with clear names (e.g., `largest-files-before.png`, `copy-action-after.png`, `drive-health-before.png`, `drive-refresh-after.png`).
- Report file is written and committed.
- `ops/verifications/6-fix-laptop-manager-evidence.md` confirms PASS.

## Notes
- Use SIR Autonomy CLI: `sir_ctl.py browser open`, `sir_ctl.py browser screenshot`.
- No code changes; only evidence collection.