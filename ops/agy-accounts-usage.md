# Antigravity accounts and usage (labels only, never passwords or tokens)
Updated 2026-11-08 07:58 by pm. Source: Ahmed's orders (4 Antigravity Pro accounts, about 15 free ones), `plans/MANAGER_BRIEF_2026-11-08.md` section 5, `plans/AGENTSROOM_SETUP.md`.

## Accounts (labels from earlier notes; verify in Antigravity Settings > Models)
| Label | Tier | Use |
|---|---|---|
| a7medorabe7 | Pro | default account on this PC |
| ahmedalaa2006.7.6 | Pro | switch target |
| 1sir1ahmed1 | Pro | switch target |
| a01083835229 | Pro (paid, has Claude models) | design, review, security, hard debugging only |
| about 15 free accounts | Free | overflow for small tasks; labels not recorded yet: add them when seen |

## Rules
- Switch only at 85 percent of the 5 h meter or 90 percent weekly. Each agent that runs long gets its own login folder when the CLI allows it; otherwise switch the account in the Antigravity app by computer use (SIR Autonomy bridge or desktop engine). Never type a password, 2FA code or solve a CAPTCHA: those go to `OWNER_ACTIONS.md`.
- AgentsRoom quota rule `qr-1794116165046-ld9wg3` moves running agents to OpenCode when any Antigravity gauge reaches 95 percent (Ahmed: if all agy accounts are used, go to OpenCode or Kilo). Kilo is the second fallback.
- AgentsRoom `usage_overview` shows Antigravity as `http_error` (no gauge) on 2026-11-08: read the meter from Antigravity Settings > Models by computer use instead.
- Claude (pm) showed `rate_limited` at 07:40 local; the Gemini manager `manager-gemini` takes over via the 30-minute watch trigger.

## Readings (add a row each time)
| Time | Account | 5 h meter | Weekly | Note |
|---|---|---|---|---|
| 2026-11-08 07:58 | default (system) | not readable (http_error) | not readable | needs a computer-use read of Settings > Models |

## Read from the app 2026-11-08 08:52 (EST, shell clock)

Source: Antigravity Settings (Account, Models & Usage, General). Read only, nothing signed out or switched.

### Accounts
- Account 1 (active): email shown as "1sir1ahmed1@gmail.com" (display name "Sir Ahmed"). Plan: "Google AI Pro". Upgrade button shown (Google AI Ultra offered; not clicked).
- No other signed-in account is listed in Settings. Only one account was visible.

### Usage (Models & Usage page, as shown)
- Gemini models: Weekly limit remaining 95% ("fully refresh in 6 days, 23 hours"). Five-hour limit remaining 81% ("fully refresh in 4 hours, 27 minutes").
- Claude and GPT models: Weekly limit remaining 100%. Five-hour limit remaining 100%.
- Model Credits: "Enable AI Credit Overages" toggle is OFF. Left OFF (no purchase or overage enabled).

### Switching accounts
- No account switcher is shown in Settings. The Account page has only "Sign Out" next to the email.
- Switching would mean Sign Out, then signing in to the other Google account. That needs the owner's password or 2FA, so it needs the owner. Not done.

## Permissions

Settings > General (read only, nothing changed in this run):
- Permission Preset: "Turbo" (before: Turbo, after: Turbo, unchanged).
- Tool Permissions: "Open" button, 118 entries (Modify permissions for file, terminal and MCP tools). Not opened: the click failed twice (user interrupt). Before: not read in detail. After: unchanged.
- Network Access Rules: "Open" button, 25 entries (allowed and denied URLs for reading). Not opened. After: unchanged.
- Plan Review Policy: "Always Proceed" (unchanged).
- Queued Messages: "Queue" selected (unchanged).

Result: no permission was changed. The Tool Permissions page (browser, terminal, file, JavaScript, allowlist) was not reached because two clicks were aborted by user interrupt. Owner or the next operator run should open Tool Permissions and set the per-tool options to always allow for this app.

## Read 2026-11-08 (operator run)
- Gemini 5-hour quota: BLOCKED. Chat "Laptop Scan Prompt Execution" shows "Individual quota reached. Resets in 4h25m28s." (error banner, Retry button).
- Weekly % left and reset time: not readable. Settings and the model-chip menu did not open on two clicks each (Antigravity UI did not respond to the clicks).
- Part B skipped: quota block message present, so no continue lines were sent and the duplicate chat was not deleted.

## Google accounts in Chrome
- Ahmed Alaa <a7medorabe7@gmail.com>
- Sir Ahmed <1sir1ahmed1@gmail.com>
- Ahmed Alaa <ahmedalaa2006.7.6@gmail.com>
- mashoyatal3abed@gmail.com
- Ahmed Alaa <a01083835229@gmail.com>
- Habiba Gamal <habiba.2011.gsht@gmail.com>
- Rasha Alaa <rashaalasy40807@gmail.com>
- Rasha <rashakhalay87@gmail.com>
- Rasha <rashakhalasi@gmail.com>
- Ibrahim Hamdy <ih9568719@gmail.com>
2026-11-09 03:42 | account 1sir1ahmed1@gmail.com (switched from a01083835229, quota exhausted) | Gemini 5h 100% | Gemini weekly 72% (refresh 6d 4h) | Claude/GPT 5h 100%, weekly 100%
- 2026-11-09 06:26 operator6: 1sir1ahmed1 read 5h 21% / weekly 50% (chats hit real quota errors on continue, rotated). a7medorabe7 read 5h 12% / weekly 10% (below threshold, skipped). a01083835229 read 5h 100% / weekly 28% (now active, chosen).
2026-11-09 06:57 | operator7 | account a01083835229@gmail.com | Gemini weekly 28% left (resets 5 d 23 h), 5h 100% left | Claude/GPT weekly 50% left, 5h 100% left | no rotation (threshold 15%)
2026-11-09 09:06 | operator8 | account a01083835229@gmail.com | Gemini weekly 18% left (resets 5 d 23 h), 5h 67% left (resets 4 h 28 m) | Claude/GPT weekly 50% left, 5h 100% left | no rotation (threshold 15%, 18% is above it)
2026-11-09 12:47 | operator10 (power-cut recovery) | account 1sir1ahmed1@gmail.com | Gemini weekly 42% left (resets 5 d 19 h), 5h 93% left (resets 4 h 56 m) | Claude/GPT weekly 100%, 5h 100% | no rotation (threshold 15%) | AI overages left OFF
- 2026-11-09 operator11: account 1sir1ahmed1@gmail.com, Gemini weekly 31% left (resets 5d 14h), 5h 96% left (resets 4h 26m). No rotation (above 15%). Sent r10 briefs to laptop, jobs, ahome, control, study: all Working.
2026-11-09 18:52 operator12: account 1sir1ahmed1@gmail.com, Gemini weekly 21%, five-hour 65% (no rotation; above 15%)
- 2026-11-09 18:59 operator13: account 1sir1ahmed1@gmail.com (Google AI Pro) read in Settings > Models: Gemini weekly 16% left (resets 5d 13h), 5h 49% left (resets 3h 52m). Above 15% threshold, no rotation.
2026-11-09 operator14: signed in a7medorabe7@gmail.com (Google AI Pro). Models & Usage: Gemini weekly 10% left (refresh in 4 d 6 h), Gemini 5 h 100%; Claude and GPT weekly 100%, 5 h 100%. Picker: Gemini 3.8 Flash High, Claude Sonnet 4.6 (Thinking), Claude Opus 4.6 (Thinking), GPT-OSS 120B (Medium), Gemini 4 Argon (Unavailable). No switch done.
