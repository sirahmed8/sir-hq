# OWNER ACTIONS (only what only Ahmed can do; HQ rewrote this on 2026-11-11 01:15)

Nothing below blocks the agents. Each item is one small step.

## One tap, when you wake up (2026-11-11 01:30)
0. ZCode is signed out. In your Chrome there is an open tab "authorize" from Z.ai with the account 1sir1ahmed1 already chosen: tick the "Terms" checkbox and press "Continue". ZCode then logs in by itself. (Sign-in stays with you by the workspace rules; nothing else waits for this: the free CLI workers carry every project meanwhile.)

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
