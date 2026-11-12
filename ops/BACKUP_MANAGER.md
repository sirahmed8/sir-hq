# Backup manager through Telegram (owner order 2026-11-12)
- Switch on: send the bot `/takeover` (or the menu button). Switch off: `/handback`. State file: ops/backup-manager.json.
- While on, every text, voice message and photo from Ahmed goes to scripts/backup_manager.py: voice is transcribed (Groq whisper, Cloudflare whisper second), photos are described (Gemini vision) and saved in ops/telegram-media/, then the first free tool of the pool that can use tools (kilo, opencode, devin, agy) reads ops/BACKUP_MANAGER_PROMPT.md plus the recent chat, does the work, and its reply file is sent back. Chat memory: ops/backup-manager-chat.jsonl. Logs: ops/agy-runs/backup-manager.log.
- Order of managers: Claude, then Antigravity (when it is available again), then the free tools.
- The backup manager uses the computer and Chrome through the SIR Autonomy MCP server (registered in opencode and kilo) and the skills library.
