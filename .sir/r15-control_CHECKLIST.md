# r15-control checklist

- [x] 1. Telegram `/menu` sends status, disk clean, and games off buttons through `scripts/deliver/send-buttons.mjs`; Control Room shows sanitized autopilot state, queue, log tail, and account ledger in Arabic and English.
- [x] 2. Owner approvals flow: `scripts/deliver/ask-approval.mjs <id> <text>` sends `approve_ok` / `approve_no` buttons with the id, and `telegram-inbox.mjs` stores answers in `ops/bus/approvals.json` for other chats.
- [x] 3. Republish helper keeps `ops/artifact/control-room.html`, `ops/dashboard.html`, `ops/artifact/CHANGED.txt`, and `ops/artifact/PUBLISHED.txt` state truthful and current.
  - FIXED (2026-11-12, task ci-sir-20261112-0901-fix1-fix1): the generator writes the page and both mirrors byte for byte (`ops/artifact/control-room.html`, `ops/dashboard.html`, `ops/public/dashboard.html`) and records the content hash in `ops/artifact/CHANGED.txt`. The local site and the artifact can no longer drift.
  - The publish helper only counts a publish when the reply starts with `published`; the old check matched "not published", so a failed run wrote a false hash into `ops/artifact/PUBLISHED.txt`. The file now holds the last hash that was really published (`20ee1159`) and the publish log keeps the time.
  - The refresh worker compares the two hashes by value (not as whole strings) and checks the mirrors against the artifact.
  - Proof: refresh log `Artifact OUT OF SYNC: changed=b33226b8 vs published=20ee1159; mirrors match the artifact (b33226b8)`; `curl http://127.0.0.1:8899/dashboard.html` returns the same 73962 bytes as `ops/artifact/control-room.html`.
- [x] 4. CI failure check is green (`python -m compileall plans scripts`, dashboard generation, GitHub Actions after push).
  - GREEN (2026-11-12, task ci-sir-20261112-0901-fix1-fix1, commit `bdd3383`): `python -m compileall plans scripts` exit 0; `python plans/generate_dashboard.py` exit 0; `python -m pytest tests -q` = 62 passed (MSYS python, Chromium present) and 57 passed, 5 skipped (pythoncore python, no Chromium build for it); GitHub Actions on `bdd3383`: verify `43249115760` success, test `43249115784` success.
