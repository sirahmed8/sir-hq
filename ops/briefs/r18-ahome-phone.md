AHome, round 15 finish (2026-11-10 evening). Read AGENTS.md, .sir/CHECKPOINT.md and .sir/R15_CHECKLIST.md first.

Situation: the Antigravity agent did items 1 to 23 of .sir/R15_CHECKLIST.md today (commits cdb8237 to 447db7c on main) and then ran out of quota. It stopped in the middle. Left behind: one unpushed commit, an uncommitted edit in apps/web/tests/webkit_keyboard.test.mjs, an untracked apps/web/scripts/audit_390_defects.mjs, and items 24 to 27 not done. You finish the round.

Rules: source under apps/ only. Never open the vault, messages, notes or photos. No private data leaves this machine or goes into commits, logs or screenshots sent anywhere. No pull requests: commit and push to main after every step. Version stays 1.0.0. Never revert another tool's edits. No emoji in code or copy.

Step 1. Save the interrupted work.
- `git status` and `git diff`. Read the uncommitted test edit and the untracked script. If they are sound, keep them; if the test edit is half-written, finish it. Run `npx tsc --noEmit` and `npm test` in apps/web. Fix every error (fix the code, never delete or skip a test). Commit and push.

Step 2. Item 24: `npx tsc --noEmit` and `npm test` pass with zero errors across the repo. Tick it with the exact output counts.

Step 3. Prove items 1 to 23, do not trust the ticks. The previous agent ticked them fast. For each item, run the app, open the screen at 390 px in Arabic (RTL) and English, light and dark, and try the exact action written in the item. Items that need special care because the owner reported them twice already:
- 10 and 11: message box above the keyboard and not cropped (AI page and chat page).
- 13 to 17: emoji, stickers and GIF panel follows the theme, is calm, box stays visible.
- 18 to 20: context menu stays open after the finger lifts and animates from the bubble.
- 21 and 22: reply preview and voice recorder grow from the message box and close smoothly.
If an item works, write "VERIFIED 2026-11-10" next to it with one line of what you saw and a screenshot path under .sir/evidence/r15/ (UI only, no private content). If it does not, untick it, fix it properly, test, verify again, commit and push.

Step 4. Item 25: `gh run list --limit 10`. Every workflow on main must be green. Fix a failing workflow, do not disable it.

Step 5. Item 26: deploy the web app to Firebase Hosting and to Vercel using the project's existing deploy scripts and config. Open both live addresses and confirm the new build is served (the page title "حياتنا" must be present). Write both addresses and the result in the checkpoint. If a deploy needs a sign-in that is missing, write the one exact command the owner must run in the checkpoint and continue.

Step 6. Item 27: build the Android app and install it on the phone connected to this laptop: `adb devices`, then `adb install -r <apk>`. Open the app and check items 1, 10, 16 and 18 on the device. If no device is listed, say so in the checkpoint and continue.

Finish: update .sir/CHECKPOINT.md (Now, exact Next step, Open promises), append one line to D:/Projects/_SIR/ops/bus/sir-hq.md with counts (items verified, reopened, fixed, deploy results, install result), commit and push.
