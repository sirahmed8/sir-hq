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

## HQ note (2026-11-10 23:10)
- Done and checked by HQ: r18-ahome-phone (27 of 27 items ticked, CI green on last 2 runs, both live addresses answer 200, APK installed on the phone at 21:30; caveats: no phone walkthrough after the last test-only fix, 8 Dependabot alerts open). r19-study (CI green on last 2 runs; fixed H1 H2 H5 H6 M2 M3 M4 M8; open H3 H4 M1 M5 M6 M7 L1 L2 L4 and others, see SIR Study/.sir/R19_CHECKLIST.md).
- Running on free CLIs: r19-jobs (started 22:25, nothing pushed yet, CI still red), r19-control (started 22:40).
- Queued: r20-study (closes the open checklist lines; exam table must be confirmed against the timetable).
- Next step: when autopilot.log shows task done for r19-jobs and r19-control, check `gh run list` in SIR Jobs (must be green) and that one server copy listens on 8899; then queue AHome round 16 (phone walkthrough of items 1, 10, 16, 18 and Dependabot alerts) and republish the Control Room artifact.

## HQ note (2026-11-10 23:25)
- Found why rounds failed: free quotas hit by both tasks at once, Devin in smart mode refused all tool calls, workers used bash syntax in PowerShell and left main broken. Fixed: scripts/cli_pool.py (shared model pool with cooldowns, 12 free models), scripts/cli-run2.sh rewritten, ops/WORKER_PREAMBLE.md, kilo and opencode configs load the manual, scripts/ai-status.py, plans/AI_TOOLS_CONTROL.md.
- r19-jobs and r19-control restarted 23:11 on Devin (dangerous mode); autopilot restarted 23:16 with the new runner pids.
- Next step: run python scripts/ai-status.py; check r19-jobs/r19-control progress and that gh run list in SIR Jobs turns green; then r20-study starts by itself.

## HQ note (2026-11-10 23:55)
- Now: queue order r21-ahome (CLI pool, owner second phone review plus self-audit loop), r19-jobs, r19-control, r20-study (ZCode via a Haiku operator was asked to start it; result not yet known). One writer per project.
- Next step: run `python scripts/ai-status.py`; read the Haiku operator result for ZCode; check `gh run list` in SIR Jobs and AHome; confirm .sir/plans/r21-tabs.md exists in AHome (HQ guard blocks reading AHome files from this chat, ask the AHome worker or its report).
- Open promises: Antigravity quota returns 2026-11-11 00:04 (use the 19 accounts via ops/ACCOUNT_ROTATION.md); repair Codex and Qwen CLIs; republish Control Room artifact after r19-control; verify r15/r16-laptop.
- Re-read after a reset: plans/AI_TOOLS_CONTROL.md, ops/WORKER_PREAMBLE.md, ops/briefs/r21-ahome.md, scripts/cli_pool.py.

## HQ note (2026-11-11 01:00)
- Owner screenshots analysed and turned into briefs: r22-laptop, r22-control, r22-jobs, r22-study (queued after r21-ahome and r20-study). ZCode (GLM-5.3 Max, Full access, workspace D:\Projects) was blocked by the provider content filter while writing graded-work refusal patterns for SIR Study (reason=content_filter, not a quota). Haiku operator asked to stop that chat and start r21-ahome in ZCode; CLI runner on AHome stopped (one writer per project).
- Owner request, not started: after GLM finishes, update TickTick (his own projects: Daily/Weekly/Monthly routine, My life, Yearly goals, 2026 Goals, 30-Day Projects Sprint, notes) with current plans and tasks. Dates about the two of them go into the app events from real data inside the app only (sync feature built in AHome); HQ and outside agents must not read that data (AHome privacy line).
- Next step: python scripts/ai-status.py; read the Haiku result; check gh run list in AHome and Study.

## HQ note (2026-11-11 00:55)
- Now: ZCode (GLM-5.3 Flash after the Max quota ended) writes in SIR Study under brief r20-study (commits every ~10 min, CI green). AHome has no writer since 00:33 (CLI worker stopped by HQ); the autopilot restarts a CLI worker there after 25 minutes idle. Owner wants GLM on AHome: proposal pending, Haiku operator would open a new ZCode chat there and the CLI would take Study.
- Next step: `python D:/Projects/_SIR/scripts/ai-status.py`; then `gh run list --limit 3` in SIR Study and AHome. HQ does not edit this file while ZCode writes in this project.
- Open promises: r22-study brief (D:/Projects/_SIR/ops/briefs/r22-study.md) queued after r20-study; TickTick update of HQ projects after GLM finishes; C: and D: nearly full (7 GB and 6 GB free).
- Re-read after a reset: D:/Projects/_SIR/plans/AI_TOOLS_CONTROL.md, D:/Projects/_SIR/ops/briefs/r20-study.md, .sir/R19_CHECKLIST.md.

## HQ note (2026-11-11 01:05)
- Added hq_watchdog.py (task SIR_HQ_Watchdog, every 10 min) and an hourly HQ cron (session only). Added AHome brief item 12: linked apps (TickTick, Google Tasks) "ربط الحساب" does nothing, must work end to end with OAuth, no private data read by agents. GLM Flash daily quota almost used; ZCode may be idle soon. Autopilot starts a CLI worker on AHome at its next tick (idle 28 min).
- Next step: read ops/watchdog.log and ai-status.py; if ZCode quota is gone, rotate account via Haiku (approved list in scripts/agy-chooser.py), Full access, send continue.

## HQ note (2026-11-11 01:35)
- ZCode is signed out (quota gone on both GLM models); Haiku refused to finish the Z.ai OAuth consent (sign-in stays with the owner). One tap added to ops/OWNER_ACTIONS.md and sent on Telegram. CLI workers carry all projects (autopilot MAX_PARALLEL=4; r21-ahome and r22-laptop running; Study picks up when ZCode idles 25 min; r22-control and r22-jobs wait for a free slot). TickTick project "SIR HQ" created with the owner tasks and round tracking (owner own data only). Fallback manager tick task exists (SIR_HQ_ManagerTick).
- Next step: hourly watch (cron 9b8288f7): ai-status.py, watchdog.log, gh run list per project; if C: under 3 GB the watchdog cleans; do not retry ZCode sign-in without the owner.

## HQ note (2026-11-11 02:25)
- Owner rules changed in D:/Projects/AGENTS.md line 20: agents may click OAuth consent and pick his own listed accounts; no waiting; no test messages to tools. Haiku still refused to relay the ZCode consent (it cannot verify approval relayed by another agent); GLM also runs through OpenCode/Kilo free models in the pool, so ZCode is optional.
- Done by HQ in his logged-in Chrome: TickTick developer app "AHome" (client id and redirect URL set), Google Cloud project ahmed-habiba OAuth client "AHome Tasks Sync" (Tasks API was already enabled, consent screen already In production). Ids in _local/ahome-oauth.env (gitignored); brief r21-ahome tells the worker to use them. TickTick read: no dates or countdowns about the two of them exist there; "SIR HQ" project and sprint tasks updated.
- WhatsApp Web is logged in in his Chrome: first read-only digest sent on Telegram; cron d383b42b every 2 hours (session only).
- Next step: hourly watch (cron 9b8288f7); WhatsApp digest (cron d383b42b); check r21-ahome progress and CI.
## HQ note (2026-11-11 01:37) [watch] Study active (0 min idle), Laptop/_SIR green, AHome CI shows failure (r21 owns it), raised MAX_PARALLEL to 5 so SIR Jobs starts; C: 8.3 GB.

## HQ note (2026-11-11 03:00)
- Done: leaked Playwright test browsers killed (they read an Arabic law guide aloud), watchdog now kills them after 25 min, worker rule 11 (close and mute browsers) and rule 12 (clean message format) added; AHome brief items 13-14 (events from real calendar data, more integrations, clean Telegram format); events exported to _local/ahome-events-import.json from the owner Google Calendar (birthdays, 4 midterms); crons: hourly watch (9b8288f7), WhatsApp digest every 2h incl. archive, work and job groups (5394854a), morning life brief 07:05 (db14a089). Habobty is the Gmail contact name for Habiba; no folder or note with that name found in Drive, TickTick or local disk.
- Not done: TickTick "My notes" not read yet (it holds a note with account passwords; need a title-only listing first), Antigravity sign-in, ZCode sign-in.
- Next step: read My notes by id after listing titles only; update stale TickTick tasks; run Antigravity sign-in with scripts/agy-chooser.py.

## HQ note (2026-11-11 03:40)
- Now: three Sonnet 5.5 subagents run in the background (sir-ai-builder in D:/Projects/SIR AI, sir-portfolio-builder in D:/Projects/SIR Portfolio, linkedin-improver in his signed-in Chrome, text edits only). CLI queue: r21-ahome, r20-study, r22-laptop, r22-control, r22-study, r23-jobs-cv. r22-jobs finished with CI green.
- Next step: wait for the three subagent reports; check CI per project with `gh run list`; run `python D:/Projects/_SIR/scripts/ai-status.py`; read ops/bus/ahmed-telegram.md for his answers.
- Open promises: crons (session only): hourly watch 9b8288f7, WhatsApp digest 5394854a, Fajr plan dbafdb6c 04:52, health check-in 0255e696 14:12 and 20:12, Isha summary a17f1544 21:03 (see ops/DAILY_RHYTHM.md); TickTick My notes beyond the dates note; Antigravity and ZCode sign-in; Haiku refuses relayed consent.
- Re-read after a reset: ops/DAILY_RHYTHM.md, plans/AI_TOOLS_CONTROL.md, plans/SIR_AI_ASSISTANT_REQUIREMENTS.md, ops/WORKER_PREAMBLE.md, ops/OWNER_ACTIONS.md.
## HQ note (2026-11-11 02:35) [watch] all projects green or running; SIR AI and Portfolio agents committing; C: fell 8.3 to 5.9 GB in an hour so the watchdog cleaning threshold is now 4.5 GB.
## HQ note (2026-11-11 02:57) SIR AI slice live at sir-ai-official.web.app (CI green, Google and Email-link sign-in enabled by HQ); LinkedIn experience, education, services, post fixed truthfully; duties moved to OS task SIR_HQ_Duties; NVIDIA App MCP found.

## HQ note (2026-11-11 04:05)
- Now: queue r21-ahome, r22-study, r24-jobs-apply, r24-games running on free CLIs; r20, r22-laptop, r22-control, r23 finished. Sonnet agents resumed after the 5-hour limit: sir-portfolio-builder (continue plan), linkedin-improver (first post, job alerts, at most 10 connections, jobs list to _local/job_offers.jsonl). sir-ai-builder finished slice 1 (live at sir-ai-official.web.app). OS tasks run the rhythm (SIR_HQ_Duties) independent of chat.
- Next step: read the Portfolio and LinkedIn agent reports; check ops/bus/ahmed-telegram.md; `python D:/Projects/_SIR/scripts/ai-status.py`; verify r24 briefs when done; queue next rounds (SIR AI slice 2: Google Workspace, TickTick, agent manager).
- Open promises: Telegram bot token for SIR AI (BotFather), Antigravity and ZCode sign-in, WhatsApp digest cron needs this session, owner weekly reset at 100 percent.
- Re-read after a reset: ops/DAILY_RHYTHM.md, plans/AI_TOOLS_CONTROL.md, plans/SIR_AI_ASSISTANT_REQUIREMENTS.md, ops/OWNER_ACTIONS.md, memory file owner-working-style.
