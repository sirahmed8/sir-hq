# HQ CHECKPOINT (updated 2026-11-10, instructions audit)
Older blocks (2026-10-29 to 2026-11-10) are in `ops/archive/HQ_CHECKPOINT_until_2026-11-10.md`. Read that file only when you need history. This file stays under 6 KB.

## Now
**2026-11-10 (HQ).** The Claude subscription ends around 2026-11-23, so the instruction files are being made self-sufficient for weaker models (audit report: `ops/reviews/2026-11-10/instructions-audit.md`).
- AUTOPILOT runs without Claude: scheduled task SIR_HQ_Autopilot (`scripts/hq_autopilot.py`, at logon, hidden). Every 5 minutes it pauses in game mode, keeps the Telegram listener alive (buttons: `scripts/deliver/send-buttons.mjs`, actions in `ops/telegram-actions.json`), takes the first unfinished task in `ops/AUTOPILOT_QUEUE.json` and, when that project has had no commit or edit for 25 minutes, starts `scripts/cli-run2.sh` (Kilo, OpenCode, Devin CLI rotation). It tells Ahmed once on Telegram and backs off 60 minutes when free limits are hit. State: `ops/autopilot_state.json`; log: `ops/autopilot.log`.
- The autopilot now works two tasks at once (two different project folders) and ignores `ops/` runtime files when it checks whether `_SIR` is idle. Add work with `python scripts/queue-add.py <name> <brief.md> <folder> "<title>"`.
- Overnight, with Claude out of usage, the free CLIs reported done: r14-ahome (05:13), r15-laptop (05:43), r15-jobs (06:13), r16-laptop (08:43). These are CLAIMS, not verified. Still open in the queue: r15-control (starts when `_SIR` has no commit for 25 minutes), plus what the reviewers queue (r16-jobs, r16-study, r16-control).
- AHome: every box in `AHome/.sir/R14_CHECKLIST.md` is ticked by a free CLI. Verification brief for Antigravity: `ops/briefs/PASTE_AHOME_4.txt` (done marker r17-ahome-verify). Antigravity is still signed out: operator18 failed at 09:45 (`agy-chooser.py` found no Google sign-in tab, the SIR Autonomy extension is disconnected, Chrome computer-use access was denied). The task went to the free CLIs instead (queue: r17-ahome-verify); the one tap is on `OWNER_ACTIONS.md`.
- Reviews of 2026-11-10 are complete in `ops/reviews/2026-11-10/` (Laptop Manager, Jobs, Study, Control Room). Worst: Control Room server on 8899 serves all of `ops/` with no check (C1), typed-in "verified today" numbers (C2), 4 to 9 server copies; Jobs CSS selectors broken and POST routes accept cross-site requests. Queue open: r15-control, r16-jobs, r16-study, r16-control, r17-ahome-verify. Private AHome task names were removed from `plans/generate_dashboard.py` and the artifact republished (version 20).
- Runner logs, autopilot state and `scratch/` are gitignored (a 223 MB installer in `scratch/` blocked a push).
- Mode: low usage (`plans/LOW_USAGE_MODE.md`). At most two chats work at once.
- Installed and logged in by the owner: Devin CLI (free model swe-2-flash-medium) and ZCode (GLM-5.3, free Start plan). Gemini CLI free tier is discontinued; Antigravity (`agy`) and the free CLI agents are the builders.
- Claude Fable reset reminder: scheduled task SIR_Reminder_Claude_Reset, Wed 2026-11-11 13:00. Press Reset once when weekly usage is about 90%, never later than 2026-11-16.

- 14:10: r15-control, r16-study, r16-control reported done by free CLIs (unverified); r16-jobs and r17-ahome-verify running; Antigravity signed in by the owner and working AHome; Chrome extensions (Claude, SIR Autonomy) installed. Details: `.sir/CHECKPOINT.md` HQ note.

## Next step (exact)
1. If Claude is running: read `ops/autopilot.log`, `git log -5` in the queue's project folders and `ops/agy-runs/done/`; review new reports in `ops/agy-runs/reports/`; keep going down the queue.
2. If a fresh session of any model starts: read this file, `ops/AUTOPILOT_QUEUE.json`, `ops/autopilot.log`, then `plans/CLI_AGENT_INSTRUCTIONS.md`.
3. Verify the overnight claims (truth rule): AHome through `PASTE_AHOME_4.txt` in Antigravity; Laptop and Jobs by running their tests and opening the app. If Antigravity is signed out, `ops/ACCOUNT_ROTATION.md` section "How switching happens without the owner".
4. After the queue: ZCode (GLM-5.3) through a Haiku computer-use operator, Pro accounts after their resets, Claude 5.5, then HQ itself (order: `ops/ACCOUNT_ROTATION.md`).
5. Review r14 on the phone (screenshots) when it finishes, then stay in low-usage mode.

## Open promises
- AHome r14 items A to N verified on screen (r17-ahome-verify); r15-laptop, r15-jobs, r16-laptop claims verified; `plans/INBOX_ASSISTANT.md` phases 2 and later; Laptop "update all programs" (`ops/briefs/queued-laptop-updates.md`).
- Codex reset date read and written in `ops/ACCOUNT_LEDGER.md`; SIR Autonomy extension reconnected.
- Independent verification of earlier chat claims (truth rule: nothing is called working until a reviewer saw it today).
- Instruction audit follow-ups listed in `ops/reviews/2026-11-10/instructions-audit.md` under "Left for the manager".

## Owner actions listed (never blocking)
See `ops/OWNER_ACTIONS.md` (sign-ins, 2FA, CAPTCHA, payment, identity only).

## Re-read after a reset
`D:/Projects/AGENTS.md` · `_SIR/NEXT.md` · `ops/OWNER_STANDING_REQUESTS.md` · `ops/ACCOUNT_ROTATION.md` · `plans/CLI_AGENT_INSTRUCTIONS.md` · `plans/LOW_USAGE_MODE.md` · `ops/AUTOPILOT_QUEUE.json` · `AHome/.sir/R14_CHECKLIST.md`

## History
`ops/archive/HQ_CHECKPOINT_until_2026-11-10.md` (full old file, 131 KB, including the 2026-10-29/30 phase notes, wave 0 PR notes and the old Open promises list). Mission log: `ops/MISSION_LOG.md`.

## Done (r16-control)
- 0da1e8c r16-control task 1: serve only ops/public with host gate
- 42cf9d7 r16-control task 2: redact private email and key patterns from ops


- 14:50 r16-jobs reported done 14:20 (commit d07076a, claim, unverified). Owner phone review of AHome written as ops/briefs/PASTE_AHOME_5.txt (27 items, done signal r18-ahome-phone); owner pastes it into the Antigravity AHome chat. Still open: verify today claims; Control Room worker files in _SIR are uncommitted (generate_dashboard.py, dashboard_template.html, agy-worker.py and outputs): review then commit.

- 19:30 Antigravity free accounts all out. AHome r15 items 1-23 committed by Antigravity (claims), 24-27 open: queued r18-ahome-phone for CLIs. Control Room C1 verified fixed after stopping 11 stale server copies (404 on ops files). Worker files committed. Details: .sir/CHECKPOINT.md 19:30 note.

## HQ note (2026-11-10 21:10)
- Now: AHome round 15 finish runs on a free CLI (task r18-ahome-phone, started 19:35; local tests 930 pass; it is fixing the red `verify` workflow, then deploy and phone install). Antigravity quota is out on every free account until 2026-11-11 00:04.
- Verified by HQ today: SIR Jobs r16 (local tests pass, H1 H3 H4 M1 M3 fixed; CI RED on windows Theme Dropdown test, M6 cookie open, 6 files over 300 lines, 66 lint warnings). SIR Study r16 (M2 M4 H1 fixed; CI RED: hard-coded D:/Projects path in button wiring check; exam weekday for 2026-11-12 is Thursday, checkpoint says Wednesday). Control Room: 11 stale server copies killed, one listener now, /OWNER_ACTIONS.md 404.
- Queued for the CLIs (autopilot, 2 at once): r19-study, r19-jobs, r19-control (briefs in ops/briefs/r19-*.md).
- Next step: when ops/autopilot.log shows "task done: r18-ahome-phone", read its report, run `gh run list` in AHome, open both live addresses. Then verify each r19 task the same way (CI green is the gate) and queue r20.
- Open promises: republish Control Room artifact after r19-control; verify r15/r16-laptop; ZCode via Haiku operator before 2026-11-14; Telegram approval end-to-end check.
- Owner plan: this chat returns to Sonnet 5.5 medium after the weekly reset.
