# base44-troubleshooter

**Source:** `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-troubleshooter\SKILL.md` (+ `references/project-logs.md`)
**Category:** ops
**Tags:** base44, debugging, logs, workflows, production, observability

## Summary
A focused Base44 skill for diagnosing production issues using function logs and workflow run history. Its central insight is that logs are not read-after-write: a one-shot `base44 logs` fetch lags about 20-30 seconds, so an empty result right after triggering a function is expected, not evidence of a problem. It teaches a six-step flow: watch it happen with `--follow`, decide whether it was a scheduled workflow run (use `workflows runs`, not function logs), check recent errors, drill into a function, inspect a time range, and analyze the output.

## When to use / when not to
Use it to investigate Base44 app errors, debug function calls, or diagnose failed scheduled jobs and automations. Do not use it to write features (use `base44-sdk`) or to set up deployments.

## Inputs, outputs, tools
Inputs: an authenticated CLI and an app context (a linked project or `--app-id`). Outputs: live or historical logs, workflow run statuses, and an error analysis. Tools: `npx base44 logs` (with `--follow`, `--function`, `--level`, `--since`, `--until`, `--env`, `--limit`) and `npx base44 workflows runs/list`. No MCP.

## Five most important rules
1. When output is empty, change TIME, never a flag: wait and re-run the same command instead of widening `--limit` or switching `--order`.
2. Never decide on a timer: open `--follow`, trigger the function, and read until the lines arrive; silence mid-invocation is normal because delivery is per-invocation.
3. For "my scheduled job did not run", start with `workflows runs --status failed`, then drop into function logs once you know which task failed.
4. `--follow` mode is decided once at startup; a lost stream exits 1 and the fix is to re-run the same command, not to change flags. `--since`, `--until` and `--order` are rejected with `--follow`.
5. Treat `No logs found matching the filters.` as ambiguous (not ingested yet, no such function, unstamped legacy rows, or an unpublished prod app), never as healthy.

## Risks and owner actions
Debugging production needs access to the owner's Base44 app, and `--env prod` requires a published app. No secrets should appear in log output.

## Revisions
The installed config copy (6522 bytes) and the marketplace cache 1.0.0-beta.1 have identical bodies; only the description frontmatter differs.
