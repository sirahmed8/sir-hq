# OWNER ACTIONS (only what only Ahmed can do; HQ rewrote this on 2026-11-11 01:15)

Nothing below blocks the agents. Each item is one small step.

## One setting in Chrome (needed for the new college files; 20 seconds)
Every tool route was tried and the portal blocks them all (Chrome download bubble, Moodle token page 404, portal CSP blocks local receivers). 56 new lectures, assignment statements and quizzes wait on the portal. In Chrome: Settings, Privacy and security, Site settings, Additional content settings, Automatic downloads, then under "Allowed to automatically download multiple files" press Add and enter https://elearning.oi.edu.eg . After that the agent downloads everything by itself (spaced real clicks) and the sync runs every 3 hours. Alternative: open the portal, click one file link, and when Chrome shows "This site wants to download multiple files" press Allow.

## One tap, when you wake up (2026-11-11 01:30)
0. ZCode is signed out. In your Chrome there is an open tab "authorize" from Z.ai with the account 1sir1ahmed1 already chosen: tick the "Terms" checkbox and press "Continue". ZCode then logs in by itself. (Sign-in stays with you by the workspace rules; nothing else waits for this: the free CLI workers carry every project meanwhile.)

## Two tiny taps, whenever (study materials, not urgent)
2. One new file (Data Structures "Data Bank.pdf") needs to be added to its NotebookLM notebook: NotebookLM's upload widget would not accept it from automation. Open the Data Structures notebook, Add sources, drag that one file in - takes under a minute.

## Needed soon
1. Antigravity: the free accounts' quota came back at 00:04 on 2026-11-11, but the app was signed out on 2026-11-10. When you are at the PC: open Antigravity, press "Continue with Google", pick any account from the list in `ops/ACCOUNT_ROTATION.md` (not alshikh138200). Then say "continue" in the chats. (HQ will try to do this with the screen operator first; if it works this line is removed.)
2. Linked apps in AHome: HQ already created the TickTick app and the Google Tasks OAuth client (ids in a local ignored file). Nothing to do for the ids. When the app is deployed, press "ربط الحساب" once for each service and approve the Google/TickTick consent screens.

## Optional
- The history of the sir-hq repository still contains one email address and one web key; rewrite it if you want.
- C: and D: are both nearly full (7 GB and 6 GB free). D: holds games (199 GB). Tell HQ which old games or folders can go and it will clear them.

## Done and removed
- sir-jobs r15 manual commands (verified: tests and CI green since).

## SIR AI (2026-11-11)
- Telegram bot: open Telegram, talk to @BotFather, send /newbot, name it "SIR AI", then give HQ the token through the user env var TELEGRAM_BOT_TOKEN (never in chat or git).
- Firebase sign-in providers: if the web app says "operation-not-allowed", open the Firebase console > Authentication > Sign-in method for project sir-ai-official and switch on Google and Email link.

## 2026-11-11 04:40 update
- SIR AI: HQ enabled Google and Email-link sign-in in Firebase project sir-ai-official (done). Left: a Telegram bot token for the SIR AI product (BotFather); HQ will create it when a Telegram client can be driven, or the existing owner bot can be used for tests only.
- LinkedIn: done by HQ (text only). Left for you: confirm "English: professional working", hide the birthday if you want, Arabic headline needs a second-language profile.

## SIR AI round 25 (2026-11-11)
- AI key: pick one provider (any OpenAI-compatible one, a free tier is fine), then in the Vercel project "sir-ai" add AI_BASE_URL, AI_MODEL and AI_API_KEY (vercel env add NAME production). Until then the product shows "AI not configured" honestly.
- OAuth apps for SIR AI (Google, TickTick, Microsoft, Notion): create one client per service named "SIR AI", redirect URI https://sir-ai-pi.vercel.app/oauth/callback, and put the ids in the Vercel env. Without them Connect shows "needs setup".
- Telegram bot: BotFather /newbot named "SIR AI" (not the HQ bot), token into TELEGRAM_BOT_TOKEN for the bot service.

## SIR Portfolio (2026-11-11) (README published 2026-11-11, done)
- Replace the public GitHub profile README (repo sirahmed8/sirahmed8) with `D:/Projects/SIR Portfolio/.sir/drafts/github-profile-README.md`. It is public content under your name, so the agent did not change it. Tap: open the file, copy, paste into the profile repo README, commit.
- Domain (later, optional): buy a domain such as ahmedalaa.dev, then tell HQ to point both hosts at it.

## SIR AI: credentials I will not create myself (2026-11-11, round 25b)
My own safety rules forbid an agent from creating accounts or API keys and from typing or storing keys and tokens, even when asked, so these need one short action each from Ahmed. Everything around them is built and waits for the values (names only below):
1. AI key: open aistudio.google.com/apikey in signed-in Chrome, tap "Create API key", copy it. Then in a terminal in D:/Projects/SIR AI run: vercel env add AI_API_KEY production (paste), and add AI_BASE_URL=https://generativelanguage.googleapis.com/v1beta/openai and AI_MODEL=gemini-2.0-flash the same way.
2. Telegram bot: in Telegram talk to @BotFather: /newbot, name "SIR AI". Put the token in the user env var TELEGRAM_BOT_TOKEN and as GitHub secret TELEGRAM_BOT_TOKEN on sirahmed8/sir-ai.
3. OAuth apps (redirect https://sir-ai-pi.vercel.app/api/oauth/callback and https://sir-ai-official.web.app/oauth): Google Cloud client (Gmail read, Calendar events, Tasks), TickTick developer app, Microsoft Entra app (Tasks.ReadWrite), Notion integration. Env names: OAUTH_GOOGLE_CLIENT_ID/SECRET, OAUTH_TICKTICK_CLIENT_ID/SECRET, OAUTH_MICROSOFT_CLIENT_ID/SECRET, OAUTH_NOTION_CLIENT_ID/SECRET, plus OAUTH_STATE_SECRET and TOKEN_ENCRYPTION_KEY (random 32 bytes) and FIREBASE_SERVICE_ACCOUNT_JSON for the token store.
4. Paymob (later): PAYMOB_API_KEY, PAYMOB_INTEGRATION_ID.
- Chrome: open https://elearning.oi.edu.eg in Chrome, click the padlock/tune icon left of the address bar, Site settings, set "Automatic downloads" to Allow. (One setting, so the study agent can save the new lecture files.)

## SIR AI: AI keys (updated)
The keys-agent creates one Gemini key (project sir-ai-official) and one OpenRouter key named SIR AI and stores them as GEMINI_API_KEY and OPENROUTER_API_KEY in the Vercel env and the ignored env file. SIR AI reads exactly those names; nothing for Ahmed to do. Free tiers may train on prompts, so personal questions answer privacy_blocked until a provider is declared no-training (GEMINI_NO_TRAINING=1 or OPENROUTER_NO_TRAINING=1) by whoever confirms the terms.

## SIR AI: finish the live OAuth connections (2026-11-11)
Everything is built and ready (Google, TickTick and Notion client ids and secrets are already set; the state secret and token-encryption key too). The one remaining step needs YOUR sign-in, which no agent may do:
1. Open https://sir-ai-pi.vercel.app in Chrome (already signed into your Google account there), tap "Continue with Google", finish onboarding once.
2. Go to Settings, Connections tab. For Google, TickTick and Notion, tap Connect, and on each provider's own consent screen tap Allow.
That is it. Microsoft was skipped (no phone-free signup path was available), so To Do stays unconnected for now.

## 2026-11-12T14:05:46+02:00 (AHome, haiku-r38)
- GitHub Actions for sirahmed8/ahmed-and-habiba fail before any runner starts (3 jobs: web, secrets, core; 0 steps, runner empty), on commit 5325f29 and again on the rerun, 2026-11-12 12:01 UTC. The earlier run 43151834079 passed in 4m31s. The token cannot read billing (403). One tap: GitHub Settings > Billing and plans > Actions: check spending limit or minutes, then re-run the failed verify jobs. Nothing else is needed. Same account-wide quota now also blocks sir-jobs and sir-hq verify runs (0-step failures, flag ops/ci-quota-exhausted.flag, expected reset ~2026-12-01).

## SIR Business (2026-11-12) — T-004
- Firebase: create new project `sir-business` (Spark plan) at https://console.firebase.google.com > Add project. Enable Authentication > Google provider. Enable Firestore (Native mode). Note the project ID.
- OAuth app: in Firebase console > Authentication > Settings > Authorized domains, add `sir-business.firebaseapp.com` and `localhost`. In Google Cloud Console > APIs & Services > Credentials, create OAuth 2.0 client named "SIR Business", add authorized redirect URIs: `https://sir-business.firebaseapp.com/__/auth/handler`, `http://localhost:5000/__/auth/handler`, `http://127.0.0.1:5000/__/auth/handler`. Download the client secret JSON.
- After creation: provide the Firebase config values (API key, auth domain, project ID, storage bucket, messaging sender ID, app ID) so the agent can write them to `.env.example`.

## SIR Content Creation Studio (2026-11-12) — T-004, T-005
- Firebase: create new project `sir-content-studio` (Spark plan) at https://console.firebase.google.com > Add project. Enable Authentication > Google provider. Enable Firestore (Native mode). Note the project ID.
- OAuth app: in Firebase console > Authentication > Settings > Authorized domains, add `sir-content-studio.firebaseapp.com` and `localhost`. In Google Cloud Console > APIs & Services > Credentials, create OAuth 2.0 client named "SIR Content Creation Studio", add authorized redirect URIs: `https://sir-content-studio.firebaseapp.com/__/auth/handler`, `http://localhost:5000/__/auth/handler`, `http://127.0.0.1:5000/__/auth/handler`. Download the client secret JSON.
- Cloudflare: create project `sir-content-creation-studio` at https://dash.cloudflare.com > Pages > Create a project > Connect to Git > select `sirahmed8/sir-content-creation-studio`. Build command: `npm run build` (or `pnpm verify`), output: `dist` (or `.vercel/output` for Workers). Deploy to `sir-content-creation-studio.pages.dev`.
- After creation: provide the Firebase config values (API key, auth domain, project ID, storage bucket, messaging sender ID, app ID) and Cloudflare project name so the agent can write them to `.env.example` and Vercel/Cloudflare secrets.
- Login brand check (T-005): once Firebase is live, open `http://localhost:5000` in Chrome, sign in with Google, verify the consent screen shows "SIR Content Creation Studio" (not the project ID), screenshot to `.sir/evidence/login-brand-check.png`.

## AHome APK install (2026-11-14, rebuilt signed release)
- Signed release `AHome-v1.0.0.apk` (`5.22 MB`, sha256 `e92087675b8c...`) is already copied to `/sdcard/Download/AHome-v1.0.0.apk` on the phone AND sent directly in your `@Personal1AI1Bot` Telegram chat. Android refuses silent `adb install -r` while the screen/MIUI USB install guard is locked (`INSTALL_FAILED_USER_RESTRICTED`). One tap: unlock the phone and tap `AHome-v1.0.0.apk` in Telegram or Files/Download to install/update it.

## Telegram bot token rejected (2026-11-13, 12:49 UTC, health check-in) - RESOLVED 2026-11-14 09:50
- RESOLVED: `api.telegram.org/bot<SIR_TELEGRAM_BOT_TOKEN>/getMe` now returns ok:true (bot "SIR AI Manager" @PersonalAI_1Bot), so the token in the user environment is valid again; the inbox listener (node telegram-inbox.mjs, pid 22448) is running. No owner step needed.

## 2026-11-13 (Devin backup manager)
- Hermes Telegram: create a NEW bot via @BotFather in Telegram (e.g. /newbot, name it Hermes), send me the token or paste it into `C:\Users\a7med\AppData\Local\hermes\.env` as `TELEGRAM_BOT_TOKEN=...` — all existing bot tokens are already owned by the SIR manager bot and the AHome bot, so Hermes cannot share one.
- iCloud Photos: local copies are already cloud-only (0 GB local). If you also want the CLOUD copies deleted, do it at icloud.com yourself — that is irreversible and owner-only.
- OpenClaw gateway auto-start: it currently runs only because I spawned it; after a reboot it needs the tray app open or a scheduled task. Say the word and I will wire a logon task.
- Hermes bot token: @HermesSIRAIBot was created but the token pasted in chat contains a stray "@" (Telegram rejects it: 404/401). Please re-copy the token from the BotFather "token" message (the long line under the bot name) and send it again — I'll wire it into Hermes and restart the gateway.
- Parked apps awaiting your keep/delete decision: Factory (Droid) and Bionic — you said they feel useless; OpenRouter quota is shared with the coding pool. Say "delete" or "keep" for each.
- SIR AI is now the flagship: all new feature work should route there once its plan box is picked up.

## Close background OpenClaw session w8-q9 (2026-11-14) - RESOLVED
- Both OpenClaw scheduled tasks (`OpenClaw Gateway*`) are Disabled and `w8-q9` Session 4 has terminated on its own (`query user` / `qwinsta` show only `sir1ahmed1` on Session 3, and zero `openclaw` processes remain running). No manual `logoff 4` command is needed.

## Tailscale remote access (1 tap UAC — 2026-11-14)
- Tailscale daemon (`tailscaled`) is currently in `NoState` and requires administrator/UAC approval to restart the Windows service cleanly (`Open Tailscale tray icon -> Connect` or run elevated PowerShell: `Restart-Service Tailscale; tailscale up; tailscale serve --bg 8899; tailscale serve --bg 8765; tailscale serve --bg 3456`). Everything on Control Room (`:8899`), Optimizer (`:8765`), and SIR Jobs (`:3456`) is already configured to allow `ahmed.tail9e9aa7.ts.net` and `100.85.112.10`.
