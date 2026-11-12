# base44-troubleshooter

Source read: `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-troubleshooter\SKILL.md` (gemini-plugin base44, 160 lines) plus references/project-logs.md.

## Summary
A focused runbook for diagnosing production issues in a deployed Base44 app using the Base44 CLI. It covers three tools: `base44 logs` (function logs with `--follow` realtime streaming, `--level`, `--function`, `--since/--until`, `--limit` capped at 500), `base44 workflows runs`/`list` (the automation system — cron schedules, entity triggers, connector events — where failed runs carry the failing task and underlying error, and `consecutiveFailures` flags broken workflows), and auth/app-context resolution via `npx base44 whoami`, `base44/.app.jsonc`, or `--app-id`. Its central lesson: logs are not read-after-write — one-shot fetches lag ~20-30s ingestion, so an empty result right after a run proves nothing; the variable to change is TIME, never flags.

## When to use / when NOT
Use when a deployed Base44 app has production errors, a function is failing, or "my scheduled job didn't run". Do NOT use it for local development issues (use `base44 dev`), for writing code (base44-sdk), or as a substitute for reading the function source — it diagnoses from logs and workflow runs only.

## Inputs, outputs, tools
- Inputs: app context (linked `base44/.app.jsonc`, `--app-id app_123`, or cwd), optional function name, time range, log level.
- Outputs: log lines (realtime via `--follow` or one-shot), failed workflow runs with the failing task + error, a diagnosis.
- Tools: `npx base44 whoami` (auth gate — if expired, user must run `npx base44 login`), `npx base44 logs [--follow|--level error|--function|--since|--until|--limit|--env prod|preview]`, `npx base44 workflows runs [--status failed]`, `npx base44 workflows list`. MCP: none.

## 5 most important rules
1. **Logs lag ~20-30s; empty means "not ingested yet", not "healthy"** — wait and re-run the same command; never diagnose by widening `--limit`/`--level`/`--order`.
2. **For a reproducible failure, start with `logs --follow` and trigger the function while watching** — never decide on a timer or a fixed read window; delivery is per-invocation (lines arrive when the invocation ends).
3. **"Scheduled job didn't run" → check `workflows runs`, not function logs** — function logs can't tell whether a run was dispatched; a failed run names the failing task and error. Note `manual` trigger just means no trigger type was stamped, and test runs appear tagged `(scheduled, test)`.
4. **`--function` filters stamped rows only** — legacy per-function deployments emit unstamped rows a filtered view hides; if a filtered run is empty, re-run unfiltered before concluding.
5. **Respect the stream contract**: `--since`/`--until`/`--order` are rejected with `--follow`; a mid-run stream loss exits 1 (re-run, don't change flags); `--limit` above 500 is clamped; `No logs found` is ambiguous (ingestion lag, wrong function name, unpublished app on `--env prod`).

## Risks / owner notes
`--env prod` reads live production logs — they may contain user data; don't paste raw log lines into tracked files or reports. Requires the user to be logged in (`base44 login`) when the token expires — an owner action.

## Category / tags
ops · base44, troubleshooting, logs, monitoring, workflows, debugging, production

## Revisions
Single revision (gemini-plugin base44). References sibling base44-cli workflow references — canonical and only source.
