# r64-telegram-first checklist

- [x] 1. Speed: ack within 2s, typing indicator, 150s per-attempt timeout, latency.json preference, two-model race for chat, quick answer first + follow-up for long work, normal reply < 60s
- [x] 2. One context per burst: ~8s collection window, media_group_id albums, voice transcribed before job, photos described in parallel, one ordered prompt, queue while running, tested (3 photos + text, voice + photo)
- [x] 3. Telegram Bot API kit: research changelog, telegram_lib.mjs + telegram_lib.py with tests, plans/TELEGRAM_BOT_KIT.md, applied to SIR AI / AHome / SIR Jobs / SIR Laptop Manager bots
- [x] 4. Bot profile picture: crisp 640x640+ from SIR AI brand assets, set via setMyProfilePhoto or BotFather, verified
- [x] 5. Robustness: restart-safe state, network retry/backoff, watchdog >3min, /status, /takeover + /handback fix, manager reads tasks/reports and hands out work via taskboard.py
- [x] 6. Persona: backup manager is the same team lead as Claude (HQ_CHECKPOINT, OWNER_REQUEST_LEDGER, tasks/reports, keeps the loop going)

Report: ops/tasks/reports/r64-telegram-first.md (also ops/agy-runs/reports/)
