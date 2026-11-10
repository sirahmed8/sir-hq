# Antigravity account rotation (Ahmed, 2026-11-09, order updated 2026-11-10): switch BEFORE the limit

## CURRENT ORDER (canonical; owner, latest 2026-11-10; replaces every order further down)
Quota is watched for ALL accounts and tools; nothing may stop. Use the first line that still has quota:
1. Free Antigravity accounts, in BOTH Chrome profiles (main profile and the second profile). For now the owner switches accounts himself; Haiku with computer use may switch Chrome profiles (click the profile picture, choose the other profile, close and reopen Chrome; else `chrome.exe --profile-directory="Profile N"`). The operator uses only the account chooser and never touches other data of those Google accounts. The restaurant account `alshikh138200` must NOT be used.
2. The free CLI agents through `scripts/cli-run2.sh <task> <project>` (Kilo auto-free, OpenCode free models, Devin CLI), reading `.sir/CHECKPOINT.md` each round. Commands and models: `plans/CLI_AGENT_INSTRUCTIONS.md`. The autopilot (`scripts/hq_autopilot.py`) starts this when a queued project is idle for 25 minutes.
3. ZCode (GLM-5.3, free Start plan): sign out and in with the owner's accounts one after another, driven by Haiku with computer use.
4. Devin: any free account switching it offers.
5. The four Pro accounts after their weekly resets (a7medorabe7 first, about 4 days; Gemini 3.8 Flash High; Gemini 3.8 weekly is 0 to 5 percent until then).
6. The paid reserve account a01083835229: Gemini 4 Argon (weekly only, no 5-hour window), then Claude Sonnet 5.5 or Opus 5.5 (burns out in minutes: ONE chat at a time, hardest tasks only). Never Claude 4.x.
7. Codex (read its reset date into `ACCOUNT_LEDGER.md`), very late.
8. HQ (Claude manager) last and sparingly.

## How switching happens without the owner (answer to Ahmed, 2026-11-10)
- CLI agents: automatic. `scripts/cli-run2.sh` moves Kilo, then OpenCode, then Devin CLI when one reports a limit; the autopilot retries every 60 minutes when all three are out. Nobody has to be awake.
- Antigravity: half automatic. It has no command-line account switch, so a Haiku operator (lowest effort) clicks Sign in and then runs `python scripts/agy-chooser.py <email>`, which picks the account in Chrome's chooser without a password. The script accepts only the owner's accounts in its `APPROVED_OWNER_ACCOUNTS` list (the four Pro accounts, the second-profile free accounts, mashoyatal3abed). Usage read at each switch goes in `ops/agy-accounts-usage.md`.
- When Claude is gone (about 2026-11-23): the CLI path keeps working alone. For Antigravity the owner taps the account himself (one tap in the chooser), or any tool with screen control follows the steps under "Steps" below.

Rotation thresholds: switch an Antigravity account at 15 percent left in the 5-hour window, or when the weekly figure is 10 percent or less, even while chats are working.
Who operates the screen: a Haiku operator at the lowest effort, never HQ itself. After a switch: type "continue" in EVERY chat and press ctrl+Return so it sends at once; press Retry on any error.
SAVE RULE (all chats, all tools): commit, push and checkpoint after every finished step, so a model switch or a quota cut never loses work.
If every option is exhausted: stop cleanly, report once on Telegram, resume at the first reset. HQ keeps `ACCOUNT_LEDGER.md` (limits, reset times) and returns to an account when its window resets.
Only Ahmed's own accounts and accounts given with his family's and friends' consent may be used (listed under the 2026-11-09 night correction below); never create accounts, never buy credits.

## Reference and history (accounts, sign-in steps, CLI model choice, owner notes; the CURRENT ORDER block wins on any conflict about order or thresholds)

Verified by hand on 2026-11-09: switching takes about 3 minutes, needs no password, and the running chats continue on the new account.

## Accounts (Ahmed's own, all signed in in his Chrome; never use any other account)
| Order | Account | Notes |
|---|---|---|
| 1 | a7medorabe7@gmail.com | Google AI Pro. Read 03:50: Gemini 5 h 100%, weekly 35% (resets in 4 d 23 h) |
| 2 | a01083835229@gmail.com | Google AI Pro. Read 03:40: Gemini 5 h 59% (resets in 4 h 25 m), weekly 45% (6 d 5 h); Claude/GPT models weekly 50% |
| 3 | 1sir1ahmed1@gmail.com | Google AI Pro. Read earlier: Gemini weekly 95% left, 5 h 81% left |
| 4 | ahmedalaa2006.7.6@gmail.com | Pro per the owner; plan and quota not read yet |
Keep this table updated after every read (percent left and the reset times).

## When to rotate (the 30 percent figure is superseded by 15 percent, see CURRENT ORDER)
Read Settings > Models & Usage (bottom-left Settings, then Models). Switch when the CURRENT account's Gemini five-hour limit shows 15% or less left (was 30%), or the weekly limit shows 10% or less. Pick the account with the most five-hour AND weekly quota left (from the table; read it after switching). If the new account is also low, switch again. A chat showing a quota/limit error that clears on Retry does not need a switch. The manager checks at every wake-up; chats that stall with a real quota error trigger an immediate check.

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

## Model and account order (Ahmed, 2026-11-09, final) [SUPERSEDED by CURRENT ORDER at the top]
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

## FINAL ORDER (owner, 2026-11-09, replaces the order above) [SUPERSEDED by CURRENT ORDER at the top]
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
Lessons (2026-11-09): the OAuth callback listener of Antigravity dies after about a minute, so do steps 2 and 3 FAST: after the Continue click run the script, then ONE claude-in-chrome browser_batch: navigate to the URL, wait 3, click the account row (second row (640,257), third (640,316), fifth (640,450) in the 1095x772 frame), wait 4, click Sign in (845,508), wait 3; the tab then shows 'Google Antigravity Auth Success'. Do not call open_application for Antigravity during the flow (it hides Chrome). After a rotation every chat shows 'Agent terminated' with Retry: Haiku clicks Retry on each.

## OWNER CORRECTION 2026-11-09 night (supersedes the order above) [SUPERSEDED by CURRENT ORDER at the top]
- The PAID reserve account is a01083835229@gmail.com: it has Gemini 4 Argon (Medium, weekly only, no 5h window), Claude Opus 5.5 / Sonnet 5.5, GPT-OSS. All six chats now use Gemini 4 Argon Medium on it (Argon weekly 100% at 23:20; Claude/GPT group weekly 50%, resets in 1d14h).
- ORDER NOW: 1) Argon on a01083835229 until exhausted. 2) Claude Sonnet 5.5 (or Opus 5.5) on the same account, burns very fast: ONE chat at a time for the hardest tasks. 3) Free accounts, including the accounts the owner took from family and friends WITH THEIR CONSENT (mashoyatal3abed, partner, Rasha Alaa, Rasha x2, Ibrahim Hamdy, and any others in the chooser): rotate with the fast sequence; read each one's Models page and ledger it; never read or touch anything else in those Google accounts. 4) OpenCode and Kilo CLIs with the free model chosen in ops/CLI_MODEL_BENCH.md. 5) Codex (read its reset date). 6) HQ last.
- The four Pro-promo accounts have Gemini 3.8 weekly at 0 to 5% until their resets (4 to 6 days): a7medorabe7 4d6h, a01083835229 5d6h, ahmedalaa2006.7.6 5d3h, 1sir1ahmed1 5d9h.

## CLI free-model choice (benchmark 2026-11-09, ops/CLI_MODEL_BENCH.md; small smoke test, not a quality ranking)
1) opencode/glm-5.3-flash-free (19 s, 6/6 tests passed), 2) opencode/deepseek-v4.1-flash-free (29 s, passed), 3) opencode/big-pickle (36 s, 8/8 tests, most thorough), 4) kilo/kilo-auto/free (needs --auto; tries pip install), kilo/meta/muse-spark-1.3 is NOT usable (asks for credits). Start: `cd "D:/Projects/<project>" && opencode run -m opencode/glm-5.3-flash-free "$(cat <brief-file>)"`; use big-pickle for tasks that need thorough tests. Always commit after each step (save rule).

## Owner notes 2026-11-10
- Muse Spark 1.3: use it through OpenCode (not Kilo). In Kilo use only the auto-free router (kilo/kilo-auto/free, with --auto).
- A SECOND Chrome profile holds about 9 more free Google accounts (owner's own, seen in its account list: sirahmed0115757, sirahmedalaa2006, sir1ahmed2006, ahmed1orabi2006, ahmedalaaorabi2006, ahmedalaaorabe2006, ahmedalaaorabe, ahmedalaaeldinorabe (all @gmail.com), plus alshikh138200 which belongs to the restaurant and must NOT be used). They are the reserve after the free accounts in the main profile; to use them the sign-in must run in that Chrome profile (ask the owner once which profile folder; claude-in-chrome works on the browser instance it is connected to).
- Claude (HQ) usage: weekly 54% used, resets Sunday 02:00; 'Fable reset' (free weekly reset) expires Nov 17 09:59 GMT+2. Best use: when weekly usage reaches about 90% (forecast: Wednesday afternoon), press Reset for free once; never later than Nov 16. Telegram reminder scheduled for Wed 2026-11-11 13:00.
- OpenCode id for Muse Spark 1.3: openrouter/meta/muse-spark-1.3 (also -contributor); check that it is free before relying on it: opencode run -m openrouter/meta/muse-spark-1.3 "say OK".

## ORDER OF 2026-11-10 (owner, latest; supersedes earlier orders) [SUPERSEDED by CURRENT ORDER at the top]
The second Chrome profile still holds FREE Antigravity accounts: they are the EMERGENCY reserve. Now: 1) OpenCode (big-pickle, glm-5.3-flash-free, deepseek-v4.1-flash-free, Muse Spark 1.3 via openrouter) runs the work through scripts/cli-run.sh; do not interrupt it, only monitor (live log tab in the Terminal panel, ops/agy-runs/cli-<task>.log). 2) When OpenCode runs out or a task needs more: the free Antigravity accounts (second profile), one after another. 3) Then Kilo (auto-free). 4) Then Codex, then the Pro accounts as they reset (a7medorabe7 first, ~4 days), then Claude 5.5 on a01083835229 (resets in ~1d14h), HQ last.

## Tools beyond Antigravity (2026-11-10)
Devin CLI (free model only: swe-2-flash-medium) and ZCode (GLM-5.3 free Start plan, owner is signed in) are installed and the owner logged in. Instructions for all free agents: plans/CLI_AGENT_INSTRUCTIONS.md. Runner: scripts/cli-run2.sh <task> <project> rotates kilo, opencode (big-pickle, nemotron ultra, glm, deepseek, openrouter free) and devin, reading .sir/CHECKPOINT.md each round. The older runner scripts/cli-run.sh is running r14-ahome now (kilo and opencode only); when it ends, start cli-run2.sh.

## Browser profiles and ZCode accounts (owner, 2026-11-10; the order is folded into CURRENT ORDER)
- Order now: 1) finish the free Antigravity accounts in BOTH Chrome profiles (the owner switches accounts himself for now); 2) then Kilo, OpenCode, Devin CLI and the other free sources through scripts/cli-run2.sh; 3) then ZCode: sign out and in with the owner's accounts one after another (ZCode can sign out like Antigravity); 4) Devin: any free account switching it offers; 5) Pro accounts after their resets, Claude 5.5, then HQ.
- Profile switching is done by HAIKU with computer use (click the Chrome profile picture and choose the other profile; close and reopen Chrome so it takes effect; if that does not work find another way, for example chrome.exe --profile-directory="Profile N"). Not by claude-in-chrome. After the switch the OAuth sign-in for Antigravity or ZCode opens in that profile; the operator uses only the account chooser and never touches other data of those Google accounts.
- Web research is allowed for all agents (plans/CLI_AGENT_INSTRUCTIONS.md rule 3).
