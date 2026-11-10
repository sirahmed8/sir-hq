# OWNER ACTIONS (only what only Ahmed can do; HQ rewrote this on 2026-11-11 01:15)

Nothing below blocks the agents. Each item is one small step.

## One tap, when you wake up (2026-11-11 01:30)
0. ZCode is signed out. In your Chrome there is an open tab "authorize" from Z.ai with the account 1sir1ahmed1 already chosen: tick the "Terms" checkbox and press "Continue". ZCode then logs in by itself. (Sign-in stays with you by the workspace rules; nothing else waits for this: the free CLI workers carry every project meanwhile.)

## Needed soon
1. Antigravity: the free accounts' quota came back at 00:04 on 2026-11-11, but the app was signed out on 2026-11-10. When you are at the PC: open Antigravity, press "Continue with Google", pick any account from the list in `ops/ACCOUNT_ROTATION.md` (not alshikh138200). Then say "continue" in the chats. (HQ will try to do this with the screen operator first; if it works this line is removed.)
2. Linked apps in AHome (TickTick, Google Tasks): the buttons need two ids that only your accounts can create. The agents build everything else. Steps, each takes 5 minutes and can wait:
   - TickTick: open developer.ticktick.com, sign in, "Manage Apps", "New App". Name: AHome. Redirect URL: the one the app shows on its "ربط الحساب" screen (the agent will print it in `.sir/OWNER_ACTIONS` of AHome). Copy "Client ID" and "Client Secret" into the AHome environment file the agent names.
   - Google Tasks: open console.cloud.google.com, create a project named AHome, "APIs and services", enable "Google Tasks API", set up the "OAuth consent screen" (external, add your account as test user), then "Credentials", "Create credentials", "OAuth client ID", type "Web application", add the same redirect URL. Copy the client ID and secret into the same file.
   - If you prefer, tell HQ "do the ids": the screen operator can click through these pages with your signed-in Chrome; you only approve the consent screens.

## Optional
- The history of the sir-hq repository still contains one email address and one web key; rewrite it if you want.
- C: and D: are both nearly full (7 GB and 6 GB free). D: holds games (199 GB). Tell HQ which old games or folders can go and it will clear them.

## Done and removed
- sir-jobs r15 manual commands (verified: tests and CI green since).
