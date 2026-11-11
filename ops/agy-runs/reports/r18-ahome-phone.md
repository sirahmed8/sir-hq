# r18-ahome-phone: AHome: finish the mobile round and deploy (R15)

- Date: 2026-11-10
- Folder: D:/Projects/AHome
- Brief: finish Round 15 (r15-ahome mobile feedback round) and ship it (CI green, Firebase Hosting + Vercel deployed, APK installed on the phone "ronf6d5hrkqsuoaa")
- Signalled: `agy-done.py r18-ahome-phone ok` at 2026-11-10 22:18 local
- Status: done (CI-verified)

## What shipped

- Round 15 checklist `.sir/R15_CHECKLIST.md` Section I items 24-27 annotated with verified evidence; all 27 items ticked.
- CI on `main` green on commit `d0e8c45` (`verify` run 42893143542):
  - `web` job 3m41s: npm ci, eslint, `tsc --noEmit`, `npm test` (929 passed, 1 skipped — all three R15 WebKit suites included), privacy-audit
  - `secrets` job 11s: gitleaks 361 commits, 0 leaks
  - `core` job: pytest green (previous local run: 1,007 passed)
- Outbox race fix (commit `ee03e07`, prior session): `confirm()` enqueue dedup/insert moved into the same SQLite transaction as the confirm UPDATE in `bot_store.py` / `reminder_outbox.py`.
- Flaky fixed-deadline WebKit assertions replaced with polling (`page.waitForFunction`, 6s timeout, `getComputedStyle`):
  - `apps/web/tests/r15_chat_keyboard.test.mjs` — dock opacity must become "0" while keyboard open (2 spots)
  - `apps/web/tests/r15_emoji_panel.test.mjs` — panel fade-out after outside tap
  - `apps/web/tests/r15_reply_voice.test.mjs` — reply preview expand/collapse, voice recorder open/dismiss
  - Commits: `7cfefd7`, `d0e8c45`
- Firebase Hosting (`https://ahmed-habiba.web.app`) and Vercel (`https://ahmed-and-habiba.vercel.app`) verified serving the live v1.0.0 build (page title "AHome — أحمد وحبيبة"; Arabic strings present in immutable chunk `327x7hrru52wh.js`).
- APK installed on physical phone `ronf6d5hrkqsuoaa` (package `app.sir.ahome`) at 2026-11-10 21:30 local time.
- Checklist "Found without being told": 15 prior items + 2 new (outbox race; CI fixed-wait WebKit assertions) = 17.

## Verification counts

- `npm test` local: 929 passed / 0 failed (1 skipped)
- `npx tsc --noEmit`: 0 errors
- Core pytest (local venv): 1,007 passed
- GitHub Actions: 1 verify run green (`42893143542`); earlier 3 runs red (fixed)
- Smoke evidence: `.sir/evidence/r15/r15-vercel-check.html`

## Known gaps

- Section I item 26/27 evidence is from the prior session; no new redeploy was needed for the WebKit test fix (test-only change; production build unchanged).
- 8 Dependabot vulnerabilities open on the repo (2 high, 4 moderate, 2 low) — not part of this brief.
- Device re-verification of items 1/10/16/18 on the physical phone was done at install time; no fresh on-device walkthrough after the test-only change (it does not touch the app bundle).

## Commits this round

- `ee03e07` fix(outbox): confirm-to-done atomic
- `9f6154d` R15: mark items 24-27 complete (CI green, Firebase/Vercel deployed, APK installed)
- `9f29527` chore(deploy): track firebase-hosting chunks
- `7cfefd7` / `d0e8c45` fix(web/tests): poll computed styles for WebKit timings
- `7c31f3c` docs(r15): annotate checklist items 24/25 with verified evidence
