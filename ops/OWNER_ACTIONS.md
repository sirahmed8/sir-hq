# NEEDS AHMED (only what an agent truly cannot do; it never blocks any work)

Format: `- [ ]` open, `- [x]` done. The SIR Control Room dashboard and pane read this file, so keep it true: tick or remove an item the moment it is done.

## Open
- [ ] **AHome first sign-in (you only, 5 minutes).** Open http://127.0.0.1:8090/login, choose "First time here", enter the code in `D:\Projects\AHome\local-vault\auth-setup-ahmed.txt` (agents never read it), pick a password, add the key to an authenticator app, save the 10 recovery codes, delete the file. Habiba does nothing: her account is switched off on purpose (surprise, ADR-002); she keeps using the hosted site and the bot.
- [ ] **AHome, optional: Tailscale for your own PC and phone only** (free personal plan; not needed for Habiba). Needs administrator approval to install.
- [ ] **AHome: move `local-vault/vault-recovery-key.txt` to your password manager, then delete it** (run `python scripts/vault_key_export.py` first; without this a Windows reinstall would lock the sealed vault).
- [ ] **Move the account passwords out of the two TickTick notes into a password manager and change them.** Why only you: agents cannot type or handle your passwords. Bitwarden is free.
- [ ] **Study portal (optional): sign in once to https://elearning.oi.edu.eg in Chrome** when you want the read-only digest of new uploads, deadlines and quiz dates in SIR Study. Quizzes and assignments are never done by agents.
- [ ] **Decide when you like: publisher name SIR, domains, store developer accounts, payment gateway keys (Paymob, Fawry, Stripe).** Free pages.dev addresses and the Launching Soon billing fallback cover it until then.

## Done (latest first)
- [x] 2026-11-01 AHome Firebase check done by the AHome chat in your Chrome: only Google sign-in is on (Email/Password already off); the web API key is now limited to the hosted site, the Firebase domains and localhost (a foreign referrer gets 403, the site gets through); the Gemini key that shipped in the old web build is deleted (restorable 30 days).
- [x] 2026-11-01 Vercel CLI signed in on this PC (Ahmed, with 2FA); the AHome chat can deploy the hosted site.
- [x] 2026-10-30 Telegram bot tokens of the AHome AI bot and the SIR AI bot revoked in BotFather (HQ, your Telegram Web).
- [x] 2026-10-30 Wrangler signed in (Google one-click and Authorize in your Chrome).
- [x] 2026-10-30 Leaked GTA Gemini key and four stale Gemini keys deleted; six old OpenRouter keys deleted; Sourcery AI removed from GitHub; 30 old repos archived; five security fixes merged.
- [x] 2026-10-30 TickTick plans refreshed (wave tasks, goals text, one note); Habiba notes and personal lists untouched.
