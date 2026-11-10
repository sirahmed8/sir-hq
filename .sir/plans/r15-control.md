# Task Plan: r15-control

Goal: Finish the Control Room and Telegram menu brief without losing the prior worker's uncommitted changes.

## Files touched
- `plans/generate_dashboard.py`: sanitize autopilot telemetry before embedding it, parse `ops/ACCOUNT_LEDGER.md` robustly.
- `plans/dashboard_template.html`: fix the new Autopilot and Account Ledger renderers, bilingual labels, responsive queue rows.
- `scripts/deliver/telegram-inbox.mjs`: keep `/menu` buttons and record `approve_ok` / `approve_no` answers in `ops/bus/approvals.json`.
- `scripts/deliver/ask-approval.mjs`: make the helper reliable and enforce Telegram callback limits.
- `scripts/deliver/README.md`: document the approval store for other chats.
- `.sir/CHECKPOINT.md`, `.sir/r15-control_CHECKLIST.md`, `ops/agy-runs/reports/r15-control.md`: handover state and report.

## Order
1. Audit and repair the dashboard data pipeline and renderers.
2. Repair and verify the Telegram menu and approval helper/inbox flow.
3. Regenerate `ops/dashboard.html` and `ops/artifact/control-room.html`.
4. Run compile, generation, and CI checks; commit and push each finished item.

## Acceptance
- `/menu`, `/start`, and `/help` send status, disk clean, and games off buttons through `send-buttons.mjs`.
- Control Room shows sanitized autopilot state, queue, and log tail plus the account ledger in Arabic and English.
- `ask-approval.mjs <id> <text>` sends `approve_ok:<id>` and `approve_no:<id>`; answers land in `ops/bus/approvals.json`.
- `python -m compileall plans scripts` and `python plans/generate_dashboard.py` pass; GitHub CI is green after push.
