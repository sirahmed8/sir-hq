# OWNER ACTIONS (Tier 2: only Ahmed can do these; never blocks any work)

Updated 2026-10-29 after Ahmed asked for as few as possible. Everything the agent could do itself, it did. What is left cannot be done by an agent because it needs his own account login or changes a system/security setting, and the rules forbid the agent from doing those even when asked.

## Real items (2)
- [ ] **Revoke the AHome Telegram bot token.** Telegram → @BotFather → `/mybots` → pick the AHome gateway bot → API Token → Revoke current token → paste the new token only into the local `.env` of `AhmedAndHabiba` (the code already reads `TELEGRAM_BOT_TOKEN` from the environment). Why only you: it needs your Telegram account. Closes leak #4 (old commit 20cd2585 in the private repo). After that, the agent cleans the history by itself.
- [ ] **Rotate the Gemini API key used by the GTA V mod server.** https://aistudio.google.com/apikey → delete the key named in `LosSantosAliveServer/.env` (`GEMINI_API_KEY`), create a new one, keep it only in a local untracked `.env`. Why only you: needs your Google login and a permanent key deletion. Closes leak #2 (private repo `sir-mods-for-gta-v`, commit 508705bc). Leak #3 (`ADMIN_SECRET_KEY`) the agent regenerates itself once the deploy target is known.

## Optional (nothing depends on them)
- [ ] Windows power plan: sleep "Never" when plugged in; lid close "Do nothing" on AC. Not done by the agent (system setting). The Claude app already holds the laptop awake while a session works, and `scripts/rc-hq.ps1` starts at logon from the Startup folder, so this is only for phone sessions started while the laptop is idle.
- [ ] Standing permissions for the safety classifier (`autoMode.allow`, extra `additionalDirectories`). Not done by the agent (security setting). Everything works without it.
- [ ] Ask GitHub Support to purge the cached old SIR-ModPack commit `9c757935` (https://support.github.com/contact → "Remove sensitive data"). The tokens in it expired on 2026-09-05; this only removes leftover account ids.

## Done by the agent instead of asking (2026-10-29)
- Off-laptop backup: private repo `sirahmed8/sir-backups`, release `backup-2026-10-29` (Jobs, Learning, Obour Institute, old projects zips and the model list). Replaces the Google Drive step.
- HQ Remote Control starts at logon from the Startup folder (`SIR-HQ-RemoteControl.vbs`).
- Antigravity credit overages off in the CLI (`useG1Credits: false`); Output.ai plugin and 55 other unneeded plugins disabled; 22 unused claude.ai connectors disconnected; 77 unneeded account plugins removed.
- Vercel login dropped: earning products use Cloudflare Pages or Firebase Hosting (rule 17).
