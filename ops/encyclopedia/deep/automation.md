# automation

**Source:** `C:\Users\a7med\.gemini\antigravity\builtin\skills\automation\SKILL.md`
**Category:** automation
**Tags:** antigravity, scheduling, cron, sidecar, agent-automation, permissions

## Summary
An Antigravity built-in skill that interactively designs and creates a scheduled background automation: a cron sidecar that starts a fresh agent conversation on each run. It walks the user through five turns: cadence (hourly, daily, weekly or custom cron), the exact time and day with a real timezone, the self-contained task prompt, writing `sidecar.json` with `"builtin": "schedule"`, and an optional test run that discovers the exact permissions the automation needs. The skill never enables the automation itself; the user enables it in the Automations dashboard.

## When to use / when not to
Use it when the user wants a recurring scheduled task ("summarize my emails every morning", "every Monday send me a to-do list") or invokes `/automation`. Do not use it for UI sidecars, continuous generic command/daemon sidecars, or in-turn timers; those use the `schedule` tool instead.

## Inputs, outputs, tools
Inputs: cadence, time or day, an IANA timezone, and the task description. Outputs: `<configDir>/sidecars/<slug>/sidecar.json` containing the cron args, a display name, a description, and `agent_permissions` access grants. Tools: `ask_question`, `write_to_file`, `agentapi new-conversation`, and the Automations dashboard (`sidecar://dashboard`). MCP servers or tools only when they are real and verified.

## Five most important rules
1. Always prefix the cron with `CRON_TZ=<IANA zone>` and use a real timezone name, never an abbreviation or a raw offset.
2. Put the full cron string in `args[0]`, place `--` immediately before the prompt, and use absolute paths for any local script arguments.
3. Never hallucinate tools or permissions: grant only `mcp(server/tool)` or `command(prefix)` you verified exist, and never use wildcards such as `command(*)` or `read_file(/)`.
4. Never enable the automation yourself: do not edit `user_config.json` and do not start the sidecar; point the user to the Automations dashboard.
5. If test-running, record every permission actually required, scoped as narrowly as possible, and update the prompt with the exact skill paths and CLI flags that worked.

## Risks and owner actions
Scheduled automations run unattended with inherited permissions, so wrong grants or a bad prompt can fail silently. Enabling the automation and granting permissions require the owner. No secrets belong in the sidecar file.

## Revisions
`.gemini/antigravity/builtin` and `.gemini/antigravity-cli/builtin` are byte-identical (12572 bytes); the antigravity copy is the source.
