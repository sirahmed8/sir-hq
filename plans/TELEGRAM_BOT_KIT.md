# Telegram Bot Kit (r64)

Shared Bot API layer for every SIR bot. Current Bot API: **10.4** (Nov 9, 2026). Research notes below; code in `scripts/telegram_lib.mjs` (Node) and `scripts/telegram_lib.py` (Python, stdlib only). Tests: `scripts/telegram_lib.test.mjs` (node --test), `scripts/test_telegram_lib.py` (unittest).

## What the kit gives you

One client per bot: `new TelegramBot({ token, chatId })` / `TelegramBot(token, chat_id)`. Every call retries network errors, HTTP 429 (`retry_after` honoured) and 5xx with exponential backoff (4 tries, base 0.8 s, cap 30 s). Other API errors raise with the Bot API description.

Methods wrapped: `sendMessage` (4096 cap, HTML escape helper `escapeHtml`/`escape_html`), `editMessageText`, `editMessageReplyMarkup`, `deleteMessage`, `sendChatAction`, `setMessageReaction`, `sendMediaGroup`, `sendPhoto`, `sendDocument` (multipart), `answerCallbackQuery`, `getFile`/`downloadFile`, `setMyCommands`, `setMyDescription`, `setMyShortDescription`, `setMyProfilePhoto`.

## Bot API surface that matters for SIR bots (verified against core.telegram.org/bots/api-changelog)

- **editMessageText / editMessageReplyMarkup / deleteMessage** — the AI edits or retracts its own answers instead of spamming new messages. Used by the backup manager pattern and SIR AI bot.
- **setMessageReaction** — instant acknowledgement on the owner's message (< 2 s) without a chat bubble.
- **sendChatAction** — typing/uploading indicators; refresh every ~4-5 s while working.
- **reply_parameters / reply_to_message_id** — reply-to the owner's message.
- **inline keyboards** — AI-decided buttons; `callback_data` (<= 64 bytes) comes back as `callback_query`, answer with `answerCallbackQuery` (toast, `show_alert` for important), then route the data back to the AI or a handler.
- **sendMediaGroup** — albums (2-10 items) for photo sets.
- **sendDocument / sendPhoto** — files and APKs (upload <= 50 MB via multipart, or by file_id/URL).
- **sendPoll** — quick polls when a decision needs structured input.
- **setMyCommands** — the `/` menu (already set for the HQ bot).
- **setMyDescription / setMyShortDescription** — profile text shown in bot profile and forwarded messages.
- **setMyProfilePhoto / removeMyProfilePhoto** — Bot API 9.4+ (Feb 2026); manages the bot picture directly, no BotFather needed. InputProfilePhoto `{type:"static", photo:"<file_id|attach://>"}`.
- **getUserProfilePhotos** — verify what picture a user/bot shows (used to verify item 4).
- **MessageEntity / formatting** — `parse_mode` HTML or MarkdownV2; the kit escapes HTML for you. The HQ bot deliberately sends plain text (owner wants zero markdown surprises).
- **Ephemeral messages (Bot API 10.x)** — `ephemeral_message_parameters` on send methods hides a reply to a single user in groups; not needed for the private HQ chat but available in the kit's raw `call()`.
- **Widgets / sendWidget, stories repost, chat join requests, forum topics in private chats (9.4)** — newer surfaces; not used yet, listed for completeness.
- **Drafts/streaming**: `sendMessageDraft` exists (Bot API 9.3) for streaming-style drafts in supported clients; not wired — the edit-into-final pattern covers the need today.

## Per-bot application status (r64)

| Bot | Where | Kit status |
|---|---|---|
| HQ / backup manager (`PersonalAI_1Bot`) | `scripts/deliver/telegram-inbox.mjs`, `scripts/backup_manager.py` | Native: burst queue, reaction+typing ack, watchdog, /status, latency table, model racing |
| SIR AI bot | `SIR AI/apps/bot` (`telegramClient.ts`, `ports.ts`, `handlers.ts`) | Applied: retry/backoff client, `editMessage`/`sendChatAction`/`setReaction` on the port; AI answers send typing + placeholder then `editMessageText` the final reply |
| SIR Jobs | sends via `_SIR/scripts/deliver/send-telegram.mjs` + `send-buttons.mjs`; button callbacks handled by the HQ listener (`a_`, `s_`, `reply_` routes) | Uses the shared kit infra; notification-only bot, no AI responder to edit |
| SIR Laptop Manager | no active Telegram bot in current source (only `legacy/` and `.quarantine/`) | Kit ready; wire when a bot exists |
| AHome | `apps/local-core` bot subsystem (`bot_router`, `bot_service`, `assistant_router`, `telegram_router` pairing API) | Deferred to the AHome worker: private project with an active build task (r57); vendoring `telegram_lib.py` + `editMessage` support is queued as a follow-up task so two workers do not collide |

## Rules for new bots

1. Import the kit; never hand-roll `fetch('https://api.telegram.org/...')` without retry/backoff.
2. Ack first (reaction or chat action), then work; edit the ack message into the answer when the reply may take > ~5 s.
3. Inline keyboards: keep `callback_data` short and namespaced (`<bot>:<action>:<id>`), always `answerCallbackQuery`, route unknown data to the AI.
4. Escape user/AI text before `parse_mode=HTML`; or send plain text like the HQ bot.
5. Profile: `setMyProfilePhoto` needs a square image (>= 640 px recommended); verify with `getUserProfilePhotos`.
