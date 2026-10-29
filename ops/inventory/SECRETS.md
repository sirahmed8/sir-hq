# Secret scan summary (2026-10-29, gitleaks 8.30.1, Phase 0.4)

Scope: full git history of 20 repos + working tree of 5 non-git folders (`AI_Models_Hub` rescanned with a 2 MB file cap). Raw redacted reports: `ops/inventory/gitleaks/*.json` (values are `REDACTED`; verified 0 unredacted fields). 114 raw findings. **No secret value appears anywhere in this file or the log**; only file, rule, commit and variable names.

## Real leaks (need action)
| # | Project (visibility) | What | Where | Live? | Action |
|---|---|---|---|---|---|
| 1 | SIR ModPack (**PUBLIC**) | Xbox/Minecraft account JWTs plus account ids (uuid, display names) | tracked `accounts.json`, `ias_accounts.json`, `SIR Launcher/accounts.json`; commit 9c75793 (2026-10-22) | Tokens **expired 2026-09-05**, refresh token empty, so no live access; the personal account data is still public | **DONE 2026-10-29:** history rewritten with git-filter-repo (3 files removed, `main` + tag `v1.0.0` force-pushed, `.gitignore` updated), gitleaks rerun: no leaks. Backups: `D:\Backups\SIR-2026-10-29\SIR-ModPack-original.bundle` and `D:\Backups\SIR-2026-10-29\ModPack-account-files\`. GitHub still serves the old commit by SHA until GitHub GC (OWNER_ACTIONS, optional). Release asset `SIR_Apps_Suite.zip` (114 MB) not inspected: check it for account files in Phase 5 |
| 2 | SIR Mods for GTA V (private) | `GEMINI_API_KEY` (in `LosSantosAliveServer/.env` and `mod-distribution/staged/LosSantosAliveServer/.env`, commit 508705bc 2026-10-06) | tracked `.env` files | Probably live | **Rotate in Google AI Studio (needs Ahmed's login, Tier 2)**; then remove files from history |
| 3 | SIR Mods for GTA V (private) | `ADMIN_SECRET_KEY` (64 chars) in `web-portal/.env.production`, commit dfc7e45a (2026-10-22) | tracked | Unknown (depends on whether it is deployed) | Generate a new value and replace where deployed; remove from history |
| 4 | AhmedAndHabiba (private) | Telegram bot token as a default value in `infra-daemons/telegram_gateway_bot.py`, commit 20cd2585 (2026-10-27) | history only: verified `git grep` finds 0 token-shaped strings at HEAD (code now reads `TELEGRAM_BOT_TOKEN` from the environment); 2 untracked working-tree files hold token-shaped strings (local env files, not tracked) | Probably live | **Revoke/regenerate with BotFather `/revoke` (needs Ahmed's Telegram, Tier 2)**; then clean history |

## Not real secrets (classified, no action beyond note)
- `gcp-api-key` (about 35 hits) in Firebase client config (`firebase.ts`, `sw.js`, `google-services.json`, SIR AI JS, `.env.production`): Firebase web API keys are public by design. **Follow-up for Phase 5 security:** confirm each key is restricted (HTTP referrers/APIs) in Google Cloud.
- `private-key` (6): code that checks/wraps the `-----BEGIN PRIVATE KEY-----` header (Obour backup.mjs, firebase-admin.ts); in `SIR Restaurant/src/services/zatcaPhase2Service.ts` a **pseudo EC key is derived from a hash of serial + OTP**, which is fake crypto for ZATCA e-invoicing. Not a leak but a rule-16 problem (nothing fake): fix in Phase 5.
- `curl-auth-header` (18) in `SIR Content Creation Studio/.agents|.claude/skills/bfl-api/...`: documentation with `YOUR_API_KEY` placeholders.
- `generic-api-key`: 11Players `firestore.rules` (an admin email address compared in rules, not a key); `.env.example` files whose values are empty (`PAYMOB_API_KEY`, `VITE_PAYMOB_API_KEY`); SIR Market `superAdminService.ts` hard-coded `licenseKey` constants (seed values, not third-party secrets, but hard-coded super-admin licences are a design flaw: Phase 5); test fixtures (`subscriptions.json`, `tests/…`); `NEXT_PUBLIC_FIREBASE_VAPID_KEY` in Obour CI (a VAPID **public** key); SIR Restaurant `canaryToken.ts` (a deliberate canary); `jimeng_video.py` request-key constant.
- `jwt` in SIR ModPack: see real leak 1.
- `AI_Models_Hub`, `Jobs`, `Learning`, `Obour Institute…`: no findings (Jobs and Obour showed none; `AI_Models_Hub` capped at 2 MB per file).

## Still to check (cheap, do in Phase 5 security pass)
Untracked-but-present `.env*` files that gitleaks' history scan cannot see; run `gitleaks dir` per project after `node_modules` is excluded. Also `git grep` each private repo for the Telegram token shape at HEAD.
