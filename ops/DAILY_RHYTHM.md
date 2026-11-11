# Daily rhythm: HQ as Ahmed's personal assistant (owner request 2026-11-11)
Everything Ahmed types or taps in Telegram lands in `ops/bus/ahmed-telegram.md` (the listener `scripts/deliver/telegram-inbox.mjs`). Read it first in every run. Buttons: `scripts/deliver/send-buttons.mjs`; actions in `ops/telegram-actions.json`. Message format: `ops/WORKER_PREAMBLE.md` rule 12.

| When | Duty | Sources |
|---|---|---|
| Fajr + 3 min (real time of that day) | Plan of the day + one outside recommendation (video, article, tool, habit) | Google Calendar, Gmail, TickTick, WhatsApp digest, `ai-status.py`, git logs |
| every 2 h (:43) | WhatsApp digest, read only: batch groups, archive, work and job groups; only new items | WhatsApp Web in his Chrome |
| Asr + 10 min and Isha + 75 min | Health and sport check-in with buttons, adapt to answers | `ahmed-telegram.md`, `_local/health_log.jsonl` |
| Isha + 15 min | Day summary: what projects and agents did, health, tomorrow, one suggestion | git, CI, TickTick, logs |
| every hour (:17) | Watch: workers, CI, disk, queue | `ai-status.py`, watchdog |
| 00:20 daily | Scheduler: fetch the day's real prayer times (get_prayer_times, Egyptian method, lat 30.2 lon 31.47, Africa/Cairo) and create the one-shot jobs above for that day | prayer-times tool |

Prayer times are never fixed clock times: they change every day.

These run today as Claude session crons. For a successor manager (Antigravity or any agent with Google, TickTick and browser tools): create the same schedule in that tool, same prompts (summarised in the table), same output files. The OS-level parts (autopilot, watchdog, manager tick) do not depend on any manager.
Standing duties: suggest, advise and think with Ahmed instead of waiting for orders; keep TickTick and the calendar current; never read the TickTick note "Accounts".
