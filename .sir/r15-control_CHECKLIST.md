# r15-control checklist

- [x] 1. Telegram `/menu` sends status, disk clean, and games off buttons through `scripts/deliver/send-buttons.mjs`; Control Room shows sanitized autopilot state, queue, log tail, and account ledger in Arabic and English.
- [x] 2. Owner approvals flow: `scripts/deliver/ask-approval.mjs <id> <text>` sends `approve_ok` / `approve_no` buttons with the id, and `telegram-inbox.mjs` stores answers in `ops/bus/approvals.json` for other chats.
- [x] 3. Republish helper keeps `ops/artifact/control-room.html`, `ops/dashboard.html`, `ops/artifact/CHANGED.txt`, and `ops/artifact/PUBLISHED.txt` state truthful and current.
- [ ] 4. CI failure check is green (`python -m compileall plans scripts`, dashboard generation, GitHub Actions after push).
