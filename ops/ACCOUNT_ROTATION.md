# Antigravity account rotation (Ahmed, 2026-11-09): switch BEFORE the limit, automatically

Verified by hand on 2026-11-09: switching takes about 3 minutes, needs no password, and the running chats continue on the new account.

## Accounts (Ahmed's own, all signed in in his Chrome; never use any other account)
| Order | Account | Notes |
|---|---|---|
| 1 | a7medorabe7@gmail.com | Google AI Pro. Read 03:50: Gemini 5 h 100%, weekly 35% (resets in 4 d 23 h) |
| 2 | a01083835229@gmail.com | Google AI Pro. Read 03:40: Gemini 5 h 59% (resets in 4 h 25 m), weekly 45% (6 d 5 h); Claude/GPT models weekly 50% |
| 3 | 1sir1ahmed1@gmail.com | Google AI Pro. Read earlier: Gemini weekly 95% left, 5 h 81% left |
| 4 | ahmedalaa2006.7.6@gmail.com | Pro per the owner; plan and quota not read yet |
Keep this table updated after every read (percent left and the reset times).

## When to rotate
Read Settings > Models & Usage (bottom-left Settings, then Models). Switch when the CURRENT account's Gemini five-hour limit shows 30% or less left, or the weekly limit shows 10% or less. Pick the account with the most five-hour AND weekly quota left (from the table; read it after switching). If the new account is also low, switch again. A chat showing a quota/limit error that clears on Retry does not need a switch. The manager checks at every wake-up; chats that stall with a real quota error trigger an immediate check.

## Steps (computer use, Antigravity app; screen frame 1456x819)
1. Settings (bottom-left) > click the account name at the bottom-left of the Settings list > 'Sign Out' (button right of the email).
2. 'Welcome to Antigravity': click 'Continue with Google' (centre, about (728,309)).
3. Run `python D:/Projects/_SIR/scripts/agy-chooser.py <email>`: it clicks the account in Chrome's account chooser and 'Sign in' on the confirmation page (no password). It prints OK when Google says 'successfully authenticated'. If it prints that Google asks for a password or 2FA, stop and put the account on OWNER_ACTIONS.md.
4. Back in Antigravity a 'Security Notice & Data Use' page appears: UNCHECK the data-sharing checkbox (about (462,346)), click 'Get started' (about (728,687)).
5. Settings > Models: read the five-hour and weekly numbers, update the table above and ops/agy-accounts-usage.md.
6. Nudge every chat that stopped with 'continue'.

## Owner update 2026-11-09 (Ahmed)
- Switch the Antigravity account when ANY quota (5h Gemini window or weekly) reaches 15% left or less, even while chats are working. Do not wait for 30% or for a stall.
- After signing in on the new account, send "continue" to EVERY chat and make it go out at once: type it, then press ctrl+Return (or alt+Return) so it is sent immediately and not queued as a waiting message. If a chat shows an error with a Retry button, press Retry.
- Who does it: a Haiku 5.5 operator at the lowest effort, never the HQ model (saves Claude tokens).

## Model and account order (Ahmed, 2026-11-09, final)
Quota is watched for ALL accounts; nothing may stop. Order of use:
1. Gemini 3.8 Flash High on the Pro accounts, one after another (a7medorabe7, a01083835229, 1sir1ahmed1, ahmedalaa2006.7.6), switching at 15% left (5h window) or when the weekly figure is 10% or less. Drain Gemini 3.8 on every Pro account first.
2. Then Gemini 3.8 on the free accounts (about 15 of them), same switching rule.
3. Then, on the account that offers Claude models (Opus/Sonnet 5.5, shown in its model menu): Claude Sonnet 5.5 / Opus 5.5. NEVER Claude 4.x (4.6 is too old).
4. Then OpenCode and Kilo with the strongest cheap model available (the Haiku operator or the manager checks what they offer; Gemini-3.8-class strength, low cost).
5. Last: the Claude manager (HQ) does the work itself, sparingly.
If every option is exhausted, the operator must report it to HQ at once, and HQ tells Ahmed on Telegram.
Ledger: ops/ACCOUNT_LEDGER.md holds, for every account, the 5h and weekly % left, the reset times (read from Models and Usage: 'resets in ...'), and the last read time; the operator appends a row at each rotation and HQ returns to an account when its window has reset.

## Open item (owner, 2026-11-09)
The signed-in account a7medorabe7 offers only Claude 4.6 (too old) and shows 'Gemini 4 Argon: Unavailable'. The owner says ANOTHER account offers Argon, Sonnet 5.5 and Claude 5.5 models. At the next rotation the operator signs in to the accounts in order, opens Settings > Models for each, and records its full model list and numbers in ACCOUNT_LEDGER.md (note which account has Argon and the 5.5 models); that account is held in reserve per the order above. Current numbers (a7medorabe7): Gemini 3.8 5h 100%, weekly 10% (resets in 4 d 6 h); next switch target: the Pro account with the highest weekly %, then free accounts.

## FINAL ORDER (owner, 2026-11-09, replaces the order above)
1. Gemini 3.8 Flash High on the Pro accounts (promotion Pro, not paid), one after another, switching at 15% (5h) or weekly 10% or less.
2. Gemini 3.8 on the free accounts (about 15).
3. The ONE PAID account (the only one that shows Claude Sonnet 5.5, Opus 5.5 and Gemini 4 Argon; the Pro accounts are promotions, so Google hides Argon there). Warnings: Claude 5.5 burns out in about two minutes when several chats use it, so use it for ONE chat at a time or for hard tasks only; Gemini 4 Argon has NO 5-hour window (weekly only), so prefer Argon on this account and keep Claude 5.5 for the hardest work. Never Claude 4.x.
4. OpenCode and Kilo: they have daily limits and often offer unnamed or stealth models from strong companies that test with users: use them (they are free and strong). Before switching to them, every chat must have committed and checkpointed (see the save rule below).
5. Codex (OpenAI): the Pro Google accounts also have free Codex accounts. Haiku opens Codex, reads when the monthly usage returns, records it in ACCOUNT_LEDGER.md; use them very late.
6. Other AI tools worth a free-tier check and monitoring: Devin, Windsurf, GLM (Z.ai), Cursor. Haiku surveys them once; HQ decides what to add after Antigravity, OpenCode, Kilo and Codex.
7. HQ (Claude manager) last and sparingly.
SAVE RULE (all chats, all tools): commit and push after every finished step and write the checkpoint after each step, so a model switch or a quota cut in the middle never loses work; the next tool reads the checkpoint, the plan file and the last commit and continues.
HQ keeps the ledger of every account and tool (limits, reset times) and returns to an account when its window resets, so nothing ever has to stop.

## Sign-in without the SIR Autonomy extension (works, used 2026-11-09 night)
1) In Antigravity: Settings > profile > Sign Out, then Continue with Google. 2) `python D:/Projects/_SIR/scripts/agy-oauth-url.py 90 > /tmp/oauth_url.txt` waits for Chrome to log the new accountchooser URL and prints it. 3) Open that exact URL in a claude-in-chrome tab (it keeps the localhost callback), wait for it to load, click the wanted account (find 'account link <email>'), wait, click Sign in at about (845,508) on the 'Make sure you downloaded this app' page. 4) Back in Antigravity untick the data-sharing box (click at about (462,346), verify) and click Get started (727,686). The owner authorised this by instruction on 2026-11-09 (act, do not wait for him). Settings > General > Queued Messages: set 'Send Immediately' so messages are not queued.
