# r64-ahome-bot-kit — AHome Telegram bot: vendor telegram_lib.py + edit-own-message

## Context

The brief arrived as `/proc/self/fd/0` (stdin was empty/lost). The task queue entry and title were used as the brief:

> AHome Telegram bot: vendor telegram_lib.py and add edit-own-message support

Source of truth for intent: `D:/Projects/_SIR/plans/TELEGRAM_BOT_KIT.md` (r64) and `ops/agy-runs/reports/r64-telegram-first.md`, which deferred this exact task to AHome "to avoid colliding with the active AHome worker". Kit rules applied: rule 1 (import the kit, never hand-roll Bot API calls without retry/backoff) and rule 2 (edit the ack/placeholder message into the answer when the reply may take > ~5 s).

## What changed (all in `D:/Projects/AHome`, working tree — NOT committed)

Worker instruction for this round said "Commit nothing unless the brief says so"; the recovered brief contains no commit instruction, so everything is left uncommitted for the next worker/manager to review and commit.

### 1. `infra-daemons/telegram_lib.py` (new, vendored)

Verbatim copy of `D:/Projects/_SIR/scripts/telegram_lib.py` (the shared SIR Bot API kit: retries + exponential backoff, 429 `retry_after` honoured, HTML escape, send/edit/delete/reaction/media-group/document/photo/callback/getFile/profile methods, stdlib only). Added a 4-line header noting it is vendored for AHome's sync scripts and that the async daemon surface lives in `telegram_lib.py`'s sibling `telegram_api.py`.

Real consumer wired: `infra-daemons/send-update.py`.

### 2. `infra-daemons/telegram_api.py` (rewritten)

The daemon's async httpx surface now enforces the same kit retry policy (it previously made single attempts and silently returned False):

- `_post()` retries `httpx.HTTPError`, HTTP 429 (honours `parameters.retry_after`, capped at 30 s) and 5xx with exponential backoff (`0.8 * 2^(n-1)`, 4 retries). Returns the Bot API `result` payload or `None`; logs method + error type only (token never logged, as before).
- `send_message_id()` — new; like `send_message` but returns Telegram's `message_id` (needed for edit-own-message). Still auto-attaches the yes/no keyboard for questions via `telegram_format`.
- `send_message()` — now a thin bool wrapper over `send_message_id()`; signature and truthiness contract unchanged, so `telegram_gateway_bot.claim_telegram_notifications` and all test fakes keep working.
- `edit_message()` — unchanged payload, now rides the retrying `_post`.
- `delete_message()` — new; removes a bot message (used to clean up a stuck placeholder).
- `set_message_reaction()` — new; kit-parity reaction acknowledgement.
- `answer_callback()` — retrying `_post` with `retries=1`, 8 s timeout (was single attempt).
- `send_chat_action()` — unchanged single attempt (cosmetic, called every ~4.5 s by `_keep_typing`; retrying would stack delays).
- `send_document()` — same multipart upload, now with the same retry loop (re-opens the file per attempt).

### 3. `infra-daemons/telegram_dispatch.py` (edit-own-message)

Assistant path (free text that is not a command/reminder request) now follows the SIR AI pattern:

1. `_keep_typing` task starts (unchanged).
2. `api.send_message_id(..., "…", reply_to_id=msg_id)` posts a placeholder threaded to the owner's message.
3. `ask_assistant()` runs (n8n → local-core fallback, unchanged).
4. On success the placeholder is `editMessageText`-ed into the final answer — one bubble, no spam. If the edit fails, the placeholder is deleted and the answer is sent as a normal message (previous behaviour) so delivery is never lost.

Command replies, reminder drafts, callbacks and notifications are unchanged (they answer in < ~5 s or already edit in place via `process_callback`).

### 4. `infra-daemons/send-update.py` (rewritten on the kit)

Was hand-rolled `httpx` + `asyncio` with a single-attempt `sendDocument`. Now a synchronous script using `TelegramBot(TOKEN, chat_id).send_document(apk, caption=...)` per recipient — same retry/backoff as every other SIR bot, same CLI (`<apk> <version> [changelog]`), same `.env` loading (`TELEGRAM_BOT_TOKEN`, `AHMED_CHAT_ID`, `HABIBA_CHAT_ID`), same exit codes (2 usage, 1 missing config/send failure, 0 ok) and same stdout/stderr messages.

### 5. `apps/local-core/tests/test_bot_gateway.py` (+2 tests, +51 lines)

- `test_assistant_answer_edits_its_own_placeholder` — paired chat, free text → asserts `ask_assistant` got `("55", "ahmed", text)`, placeholder `…` was sent, `editMessageText` carried the answer to message_id 501, and **no** second `sendMessage` bubble was posted.
- `test_assistant_falls_back_to_a_new_message_when_the_edit_fails` — edit returns False → placeholder deleted (`deleteMessage` on 501) and answer delivered via `sendMessage`.
- Shared `_assistant_stubs()` helper stubs `send_chat_action`, `send_message_id`, `edit_message`, `delete_message`, `ask_assistant`.

## Commands run and real output

```
$ python -m py_compile infra-daemons/telegram_lib.py infra-daemons/telegram_api.py infra-daemons/telegram_dispatch.py infra-daemons/send-update.py
COMPILED

$ cd apps/local-core && ./.venv/Scripts/python.exe -m pytest tests/test_bot_gateway.py tests/test_bot_hardening.py tests/test_bot_snooze_flow.py tests/test_agenda_briefing_engine.py tests/test_telegram_contact_pin.py tests/test_telegram_gender_and_commands.py -x -q
73 passed in 13.43s

$ cd apps/local-core && ./.venv/Scripts/python.exe -m pytest tests -x -q
1058 passed in 131.68s (0:02:11)        # was 1056 before this round (+2 new tests)

$ python infra-daemons/send-update.py
usage: send-update.py <apk-path> <version> [changelog]

$ .venv python -c "import telegram_lib, telegram_api, telegram_dispatch"   (from infra-daemons/)
imports ok
```

## Not verified / open

- **No live Telegram round-trip.** Everything is proven against mocks/MockTransport; a real `editMessageText` against the live bot needs the daemon running with `TELEGRAM_BOT_TOKEN` (owner machine). The code path is identical in shape to the already-live SIR AI bot pattern.
- **CI**: `ops/ci-quota-exhausted.flag` still governs (GitHub Actions minutes exhausted until ~2026-12-01); local full-suite green is the gate per worker rule 18.
- **Uncommitted**: `git status` shows modified `infra-daemons/{telegram_api,telegram_dispatch,send-update}.py`, `apps/local-core/tests/test_bot_gateway.py`, new `infra-daemons/telegram_lib.py`, plus unrelated pre-existing web/probe files from other rounds (`.gitignore`, `next-env.d.ts`, `folder.ico`, `apps/web/scripts/_*.mjs`, `audit_cycle_0051.mjs`) that I did not touch.
- `telegram_profile.py` still uses its own raw httpx for `setMyProfilePhoto`/`setMyCommands` (works, out of scope; could adopt `telegram_api._post` later).
- `set_message_reaction` is added for kit parity but not yet called by any flow (typing indicator already acks); flagged honestly rather than silently wired into UX.

## Recommendation for next worker

Review `git diff infra-daemons apps/local-core/tests/test_bot_gateway.py`, commit as e.g. `feat(telegram): vendor bot kit, retry/backoff API layer, edit-own-message answers`, push to main, then optionally do one live smoke test (send the bot a free-text message, confirm the `…` bubble becomes the answer).
