# HQ CHECKPOINT (updated 2026-11-10, instructions audit)
Older blocks (2026-10-29 to 2026-11-10) are in `ops/archive/HQ_CHECKPOINT_until_2026-11-10.md`. Read that file only when you need history. This file stays under 6 KB.

## Now
**2026-11-10 (HQ).** The Claude subscription ends around 2026-11-23, so the instruction files are being made self-sufficient for weaker models (audit report: `ops/reviews/2026-11-10/instructions-audit.md`).
- AUTOPILOT runs without Claude: scheduled task SIR_HQ_Autopilot (`scripts/hq_autopilot.py`, at logon, hidden). Every 5 minutes it pauses in game mode, keeps the Telegram listener alive (buttons: `scripts/deliver/send-buttons.mjs`, actions in `ops/telegram-actions.json`), takes the first unfinished task in `ops/AUTOPILOT_QUEUE.json` and, when that project has had no commit or edit for 25 minutes, starts `scripts/cli-run2.sh` (Kilo, OpenCode, Devin CLI rotation). It tells Ahmed once on Telegram and backs off 60 minutes when free limits are hit. State: `ops/autopilot_state.json`; log: `ops/autopilot.log`.
- Queue (all unfinished): r14-ahome, r15-laptop, r15-jobs, r15-control.
- Mode: low usage (`plans/LOW_USAGE_MODE.md`). At most two chats work at once. Pro Gemini accounts reset in about 4 days; Claude 5.5 on a01083835229 in about 1 day 14 hours.
- AHome r14 (27 screenshot findings, items A to N): A, parts of B, C, D, E, F and the J spelling fix are done; the list is in `AHome/.sir/R14_CHECKLIST.md`. OpenCode (autopilot runner) works the checklist from the top; a Haiku operator pastes `ops/briefs/PASTE_AHOME_3.txt` into the Antigravity AHome chat on a free account so Antigravity works it from the bottom (04:25: sirahmedalaa2006 exhausted until 11/17, operator16 rotating).
- Installed and logged in by the owner: Devin CLI (free model swe-2-flash-medium) and ZCode (GLM-5.3, free Start plan). Gemini CLI free tier is discontinued; Antigravity (`agy`) and the free CLI agents are the builders.
- Claude Fable reset reminder: scheduled task SIR_Reminder_Claude_Reset, Wed 2026-11-11 13:00. Press Reset once when weekly usage is about 90%, never later than 2026-11-16.

## Next step (exact)
1. If Claude is running: read `ops/autopilot.log`, `git log -5` in the queue's project folders and `ops/agy-runs/done/`; review new reports in `ops/agy-runs/reports/`; keep going down the queue.
2. If a fresh session of any model starts: read this file, `ops/AUTOPILOT_QUEUE.json`, `ops/autopilot.log`, then `plans/CLI_AGENT_INSTRUCTIONS.md`.
3. When `ops/agy-runs/done/r14-ahome.done` is missing and `scripts/cli-run.sh` has ended, run `bash scripts/cli-run2.sh r14-ahome /d/Projects/AHome` in the background.
4. After the queue: ZCode (GLM-5.3) through a Haiku computer-use operator, Pro accounts after their resets, Claude 5.5, then HQ itself (order: `ops/ACCOUNT_ROTATION.md`).
5. Review r14 on the phone (screenshots) when it finishes, then stay in low-usage mode.

## Open promises
- AHome r14 items B to N verified on screen; `plans/INBOX_ASSISTANT.md` phases 2 and later; Laptop "update all programs" (`ops/briefs/queued-laptop-updates.md`).
- Codex reset date read and written in `ops/ACCOUNT_LEDGER.md`; SIR Autonomy extension reconnected.
- Independent verification of earlier chat claims (truth rule: nothing is called working until a reviewer saw it today).
- Instruction audit follow-ups listed in `ops/reviews/2026-11-10/instructions-audit.md` under "Left for the manager".

## Owner actions listed (never blocking)
See `ops/OWNER_ACTIONS.md` (sign-ins, 2FA, CAPTCHA, payment, identity only).

## Re-read after a reset
`D:/Projects/AGENTS.md` · `_SIR/NEXT.md` · `ops/OWNER_STANDING_REQUESTS.md` · `ops/ACCOUNT_ROTATION.md` · `plans/CLI_AGENT_INSTRUCTIONS.md` · `plans/LOW_USAGE_MODE.md` · `ops/AUTOPILOT_QUEUE.json` · `AHome/.sir/R14_CHECKLIST.md`

## History
`ops/archive/HQ_CHECKPOINT_until_2026-11-10.md` (full old file, 131 KB, including the 2026-10-29/30 phase notes, wave 0 PR notes and the old Open promises list). Mission log: `ops/MISSION_LOG.md`.
