# base44-troubleshooter

- Tool: `gemini-plugin` (plugin: `base44`)
- Category: ops
- Source: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-troubleshooter\SKILL.md`
- SKILL.md size: 6500 chars

## What it does

Troubleshoot production issues using backend.

## When to use (from skill text)

- an index that lags behind the invocation, so an empty result right after triggering a
- If you can trigger the failure (or it is happening now), start here rather than
- - **Never decide on a timer.** Open the stream, trigger the function, and read until

## Structure (headings inside SKILL.md)

- Troubleshoot Production Issues
- Prerequisites
- From a linked local project
- Or explicitly
- Available Commands
- Logs are not read-after-write
- Troubleshooting Flow
- 1. Watch it happen — `--follow`
- 2. Ask whether it was a scheduled run, not a request
- 3. Check Recent Errors
- 4. Drill Into a Specific Function
- 5. Inspect a Time Range
- 6. Analyze the Logs
- Reading an empty result
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - no function by that name, or the filter dropped unstamped rows (see step 3)
- - the app has not been published, when reading `--env prod`

## Key rules (verbatim lines from SKILL.md)

1. - **When output is empty, the variable to change is TIME, never a flag.** Wait and
2. - **Never decide on a timer.** Open the stream, trigger the function, and read until

## Files inside the skill

- `references/project-logs.md` — "base44 logs"
