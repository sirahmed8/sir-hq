# automation

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\automation\SKILL.md` (antigravity-builtin revision, the only copy).

## Summary
An interactive guide for creating scheduled background automations in Antigravity/Gemini. A scheduled automation is a background sidecar (`"builtin": "schedule"`) that runs on a cron schedule and starts a fresh agent conversation (`agentapi new-conversation`) on each run — each run has no memory of prior runs, so the prompt must be fully self-contained. The skill drives a strict 5-turn creation flow: ask cadence, confirm time/day, capture the task prompt, write `sidecar.json`, then optionally test-run to discover and record the exact permissions the automation needs.

## When to use / when NOT
Use when the user wants a recurring scheduled agent task ("summarize my emails every morning", "every Monday send me a to-do list") or invokes `/automation`. Do NOT use it for UI sidecars, continuous command/daemon sidecars, or in-turn timers — those use the `schedule` tool instead. Do NOT use it for one-shot or event-driven automation.

## Inputs, outputs, tools
- Inputs: cadence (hourly/daily/weekly/custom cron), specific time/day, the task description, the user's IANA timezone.
- Outputs: `~/.gemini/config/sidecars/<slug>/sidecar.json` with `builtin: "schedule"`, `args: ["CRON_TZ=<zone> <cron>", "agentapi", "new-conversation", "--", "<self-contained prompt>"]`, `restart_policy: "always"`, `display_name`, and `agent_permissions.access_grants` populated from a real test run.
- Tools: `ask_question` for cadence/time, `write_to_file` for sidecar.json, `agentapi new-conversation` for test runs, the Automations dashboard (`sidecar://dashboard`) for enabling. Skills/MCP tools may be consulted during the test run.

## 5 most important rules
1. **Cron must be prefixed `CRON_TZ=<IANA zone>`** — detect the host timezone, map to IANA (never abbreviations like PST or raw offsets), and don't double-prefix a user-supplied `CRON_TZ=`/`TZ=` cron.
2. **The run prompt must be self-contained** — every scheduled run is a brand-new conversation with zero memory of previous runs.
3. **Never hallucinate permissions** — only grant `command(...)`, `read_file(...)`, `write_file(...)`, `mcp(server/tool)`, `read_url(domain)` entries actually verified during a test run; never wildcards like `command(*)` or `mcp(*)`.
4. **Never enable the automation yourself** — do not set `"enabled": true` or invoke any enable RPC; the user enables `<display_name>` in the Automations dashboard.
5. **Use snake_case fields and lowercase restart_policy** (`"always"` required for schedule sidecars), absolute paths in args, `"--"` before the prompt, and never put sidecar.json in an ephemeral CitC workspace.

## Risks / owner notes
Enabling happens on the owner's machine via the dashboard — the agent must hand off with the exact `display_name`. Permissions discovered in a test run reflect that run only; a task needing new tools later will be auto-denied until grants are updated. Automations run unattended with the user's credentials — the self-contained prompt should avoid destructive actions.

## Category / tags
automation · scheduling, cron, sidecar, antigravity, background-tasks, agentapi, permissions

## Revisions
Single revision (antigravity-builtin). Not present in claude/codex/cursor/kilo skill stores — this is the canonical and only source.
