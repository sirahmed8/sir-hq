# r64-telegram-first — report (devin, 2026-11-12 ~22:05)

## What was done, per brief item

### 0. Repair pass first
- `git status`/`diff`/`log` reviewed; previous models (aider, devin) left only log noise, no broken code. `node --check` + `py_compile` clean.
- Found and fixed a real crash in my own first listener rewrite (`offset` undeclared → poll loop died); committed `e503ecc`.
- Found the likely root cause of "/takeover once did not write ops/backup-manager.json": the old listener wrote the Telegram offset **before** handling each update, so a crash/restart mid-batch silently dropped the update; plus `bmSet` was a non-atomic write and `/takeover@BotName` did not match the regex. All three fixed (see item 5).

### 1. Speed
- Listener acks instantly on every burst message: `setMessageReaction 👍` + `sendChatAction typing` (fire-and-forget, < 2 s).
- `scripts/backup_manager.py` sends a quick "[تمام، قريت رسالتك. بشوف وأرد عليك.]" first, keeps typing every 4 s, then the real answer follows.
- Per-attempt timeout is now **150 s** (was 1200 s). Up to 2 pool entries race in parallel per attempt; first valid reply file wins, loser is terminated. `ops/backup-manager/latency.json` records wins/fails/avg_ms per entry (verified: `devin|swe-2-flash-medium` avg 30019 ms after the live test).
- **Live proof**: seeded a 3-message burst → job ran → reply delivered in **~30 s** (log: `22:01:20 race won by devin|swe-2-flash-medium in 30s`), well under the 60 s target.
- Note: only one racer ran because the shared pool currently has just `devin` + `aider` entries healthy (aider is not a brain tool); the race code picks up to 2 automatically as cooldowns clear.

### 2. One context per burst
- `telegram-inbox.mjs` collects messages into `ops/backup-manager/queue.json` with an **8 s debounce after the last message**; `media_group_id` albums land inside the same window. While a job runs, new messages append to the queue and start the next job on exit — never parallel jobs.
- One `job-<ts>.json` per burst → `backup_manager.py` transcribes **every** voice note and describes **every** photo **in parallel** (ThreadPoolExecutor, max 6), then builds ONE ordered numbered prompt (oldest first) with persona + chat history + all items.
- **Live proof**: seeded queue.json with 3 text items, restarted the listener → it flushed exactly ONE job file with all 3 items (`job.json {"count":3}`), queue emptied. The agent's reply proves it saw them as one context: "التلات رسايل جهوا مع بعض في نفس Burst واحد".
- Honest caveat: a live voice+photo burst could not be tested without the owner sending media; the media paths (download → parallel transcribe/describe → ordered prompt) are the same code that r67 verified live for voice (1.3 s/0.9 s Arabic) and the photo describe path is unchanged from the previous working version.

### 3. Bot API kit
- Researched the changelog: Bot API **10.4** (2026-11-09); `setMyProfilePhoto`/`removeMyProfilePhoto` exist since 9.4. Full surface list in `plans/TELEGRAM_BOT_KIT.md`.
- New shared libs: `scripts/telegram_lib.mjs` + `scripts/telegram_lib.py` — retry/backoff (429 `retry_after`, 5xx, network), HTML escape, send/edit/delete, chat action, reaction, media group, document/photo upload, callback answer, getFile/download, bot profile methods.
- Tests: `scripts/telegram_lib.test.mjs` (10 tests) + `scripts/test_telegram_lib.py` (8 tests) — all pass; plus existing `send-telegram.test.mjs`/`test-format-briefing.mjs` still green (17/17 node tests total).
- Applied:
  - HQ/backup bot: native (listener + backup_manager use the kit).
  - **SIR AI** (`apps/bot`): `HttpTelegram` rewritten on the kit pattern (backoff, `send` returns `message_id`, `editMessage`/`sendChatAction`/`setReaction` on the port); `answerWithAi` sends typing + placeholder then `editMessageText`s the final answer. Typecheck clean, **37/37 bot tests pass**, committed `d02003b` to sir-ai main.
  - SIR Jobs: notification bot already rides the shared `_SIR` sender + listener (buttons `a_`/`s_`/`reply_` routed to its handlers); no AI responder exists to edit — documented.
  - SIR Laptop Manager: no active Telegram bot in current source (only legacy/quarantine) — documented.
  - AHome: bot subsystem exists but the project has an active build worker (r57) and privacy rules; deferred to a queued follow-up task `r64-ahome-bot-kit` instead of colliding.
- Bot profile text improved (was Vietnamese by mistake, corrected to Egyptian Arabic): description + short description set, both `true`.

### 4. Bot profile picture
- Built `ops/telegram-media/bot-avatar-640.png` (640x640 PNG) from `SIR AI/assets/brand/source.png` (1024x1024) via ImageMagick.
- `setMyProfilePhoto` → `true` (Bot API 9.4+, no BotFather needed). Verified: `getUserProfilePhotos` on the bot id returns `total_count: 1`.

### 5. Robustness
- Restart-safe state: `queue.json` (pending items), `job.json` (running pid+startedAt), `job-state.json` (stage for /status), all written tmp+rename. Verified live: killed the listener mid-queue → restarted → it adopted/resumed and flushed the queue into one job.
- Listener adopts a still-running python job after restart (pid liveness check every 5 s) instead of double-dispatching.
- Network drops: poll errors now back off exponentially 15 s → 120 s max (was fixed 15 s); the kit retries each API call too.
- Watchdog: if a job runs > 3 min the owner gets one "لسه بشغال" message with the current stage.
- `/status` while backup mode is on reports queue depth, job elapsed + stage, and the 3 fastest models from latency.json.
- `/takeover` + `/handback`: commands matched before the backup branch, `@BotName` suffix stripped, `bmSet` is atomic (tmp+rename) and runs before any await — the state flip cannot be lost to a crash or a half-written file.
- Persona (`ops/BACKUP_MANAGER_PROMPT.md`) now states the backup manager is the SAME team lead as Claude and must read `ops/tasks/reports` + `ops/verifications` each call and hand out work via `scripts/taskboard.py`/`queue-add.py` (new step 3 under "First, every time").

### 6. Persona — covered above.

## Commits (all pushed to main)
- `3f5ecbf` r64: telegram burst queue, model racing, shared Bot API kit
- `e503ecc` r64 fix: declare offset in telegram-inbox
- `8113881` r64: TELEGRAM_BOT_KIT.md
- SIR AI repo: `d02003b` feat(bot): telegram kit

## CI
- `gh run list`: latest main (`8113881`) `test` 43295934113 success, `verify` 43295934066 success. One earlier `verify` on `e503ecc` failed while the C: drive was 100% full (gh couldn't even download the log: "not enough space on the disk"); superseded by the green run on the tip. `ops/ci-quota-exhausted.flag` exists but runs are completing — treated as informational; r67-c-drive-space owns the disk issue.

## Verification commands run (real output)
- `node --test telegram_lib.test.mjs` → 10/10 pass; `python test_telegram_lib.py` → 8/8 OK
- `node --test deliver/send-telegram.test.mjs deliver/test-format-briefing.mjs telegram_lib.test.mjs` → 17/17 pass
- `python -m py_compile scripts/backup_manager.py scripts/taskboard.py scripts/cli_pool.py` → clean
- `node --check scripts/deliver/telegram-inbox.mjs` → clean
- SIR AI: `npx tsc --noEmit -p apps/bot/tsconfig.json` → exit 0; `npx vitest run apps/bot` → 37/37 pass
- Live Telegram: burst job answered in ~30 s (log + reply file + chat.jsonl evidence above); `setMyProfilePhoto`/`getUserProfilePhotos`/`setMyDescription`/`setMyShortDescription` all returned true/verified.

## Still open / honest caveats
- Live photo+text and voice+photo bursts await a real owner message (media file_ids can't be fabricated); code path is shared with the verified voice pipeline.
- Model racing degrades to a single runner while the pool is mostly in cooldown — by design, it widens automatically.
- AHome bot kit application is queued as `r64-ahome-bot-kit` (inbox) to avoid colliding with the active AHome worker.
- The quick ack "[تمام، قريت رسالتك...]" is an extra message per burst; if the owner finds it noisy it can be switched to reaction-only in `backup_manager.py` (`send(...)` call at stage "queued").
