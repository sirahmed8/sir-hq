AHome, round 14 verification (2026-11-10). Read AGENTS.md and .sir/CHECKPOINT.md first, then .sir/R14_CHECKLIST.md.

A free CLI tool ticked every item of R14_CHECKLIST.md last night. Nothing counts as done until it is seen working today. Your job is to prove or disprove each tick, and fix what is not really done.

Rules: source under apps/ only. Never open the vault, messages, notes or photos. No data leaves this machine. No pull requests: commit and push to main. Version stays 1.0.0. Run `git pull --rebase` before each item; never revert another tool's edits.

For each checklist item A to N, in order:
1. Run the app and open the screen the item is about, at widths 320, 390, 768, 1280 and 1920, in Arabic (RTL) and English, light and dark.
2. Try the exact action from the owner's complaint (swipe between tabs with a finger, open the keyboard in chat and in AI chat, long-press a message, swipe to reply, press record voice, start a video call, open the emoji and GIF panel, quiet hours time picker, the link-app window, the notification checkboxes, device detection on iPhone, the update notice shown once).
3. If it works: write "VERIFIED 2026-11-10" next to the item with one line of what you saw and the screenshot path under .sir/evidence/r14/.
4. If it does not: untick it, fix it properly (same design language as the rest of the app, spring animation like the dynamic island, no native browser pickers), run `npx tsc --noEmit` and `npm test`, verify again, then commit and push.

After the list: look for 10 more visible defects nobody reported (overlapping buttons, cards touching, tabs larger than their content, white outlines when switching tabs, leftover words the owner asked to remove), fix them, and list them under "Found without being told" in .sir/CHECKPOINT.md.

Finish: update .sir/CHECKPOINT.md (Now, exact Next step, Open promises), append one line to D:/Projects/_SIR/ops/bus/sir-hq.md with counts (verified, reopened, fixed, new defects), commit and push. Then run: python D:/Projects/_SIR/scripts/agy-done.py r17-ahome-verify
