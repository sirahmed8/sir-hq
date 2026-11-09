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
