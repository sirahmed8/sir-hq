# Deliver to Ahmed's iPhone (Telegram)

`node send-telegram.mjs <file|text> [caption]` sends from @PersonalAI_1Bot ("SIR AI") to Ahmed's private chat.
Text goes through sendMessage (split at 4000 chars); other files go through sendDocument (50 MB limit).
Prints `sent <name> message_id=N` or `FAILED <reason>` (exit 1). It never prints the token or chat id.

- Credentials: user env vars `SIR_TELEGRAM_BOT_TOKEN` and `SIR_TELEGRAM_CHAT_ID`. If a console started before
  they were set, the script reads them from the Windows user scope itself. Never put them in git or logs.
- Refuses paths inside the private home project and any text, file name or caption that names the private couple project.
- Tests: `node --test` (local mock server, override with `SIR_TELEGRAM_API_BASE`).
- Owner approvals: `node ask-approval.mjs <id> "<text>"` sends `approve_ok:<id>` and `approve_no:<id>` buttons. `telegram-inbox.mjs` stores pending and answered requests in `ops/bus/approvals.json` for other chats to read. Ids are limited to 50 chars so callback data stays under Telegram's 64-byte limit. Never put AHome or Habiba content in the text.
- Rotate the token: @BotFather > /mybots > @PersonalAI_1Bot > API Token > Revoke, then store the new one
  with `[Environment]::SetEnvironmentVariable('SIR_TELEGRAM_BOT_TOKEN', <new>, 'User')`.

Fallback if Telegram stops working (not built, tools are connected to the manager):
- Gmail: send or draft to a7medorabe7@gmail.com with the Gmail connector (`create_draft` / `send_message`).
- Google Drive: upload with the Drive connector (`create_file`) and send the link by Gmail.
