# automation-engineer (Gemini 3.8 Flash, Antigravity, AgentsRoom)
Role: automation-engineer for SIR Life (D:\Projects\SIR Life) and SIR ecosystem automation. Builds calendar, task bridges, Telegram notification & reminder engine, daily briefs, and triage systems.

## Current task
SIR Life organiser (T-100 to T-104):
- T-100: Calendar bridge (read/write Google Calendar & Tasks, import SIR Study schedule, daily plan builder)
- T-101: Telegram reminder engine (on SIR AI bot, quiet hours, snooze/done buttons, escalation)
- T-102: Gmail triage (read-only summary, labels, drafts)
- T-103: Daily brief (morning/evening in Telegram + page)
- T-104: Test suite (calendar sync, duplicates, time zone Cairo, snooze/escalation, quiet hours)

## Last actions
- 2026-11-08: Accepted assignment `asg-0mw7bj7nl-82bd87f0`. Read all instructions (START_ANY_AI, AGENTS, SIR Life AGENTS, PLAN, TASKS, SCHEDULE, MANAGER_BRIEF). Initialized READ_LOG and tracker.

## Lessons
- Google Calendar events must use stable deterministic event IDs to ensure idempotency across sync runs.
- Quiet hours (Cairo time 23:30 - 07:00) must strictly silence non-urgent alerts unless an imminent exam escalation triggers during study windows.
- Telegram tokens must be dynamically loaded from local config/env, never logged or committed.

## Owes
- T-100 to T-104 implementations, test suites, and evidence files in `SIR Life/.sir/evidence/`.
