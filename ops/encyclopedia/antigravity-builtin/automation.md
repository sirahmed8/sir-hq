# automation

- Tool: `antigravity-builtin`
- Category: design
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\automation\SKILL.md`
- SKILL.md size: 12548 chars

## What it does

Interactive guide to design and create a scheduled background automation. Use this skill when the user wants to create an automated or recurring scheduled task (e.g. "summarize my emails every morning", "every Monday send me a to-do list"). Also triggered by the /automation slash command.

## Structure (headings inside SKILL.md)

- Scheduled Automations
- Quick Start (5-Turn Creation Flow)
- Interactive Creation Workflow
- Turn 1: Ask for the Cadence
- Turn 2: Confirm the Specific Time / Day
- Turn 3: Ask What the Task Should Do
- Step 4: Create `sidecar.json` & Offer a Test Run to Configure Permissions
- 1. Translate Schedule & Author Self-Contained Run Prompt
- 2. Announce Automation Creation & Write `<configDir>/sidecars/<sidecar-id>/sidecar.json`
- 3. Point to the Dashboard (with Automation Name) & Ask to Test-Run for Reliable Permissions
- Step 5: If the User Chooses to Test-Run the Task Now
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP servers, MCP tools

## Risks / cautions found in text

- -   `(Recommended) Yes, execute a test run now to configure permissions`
- -   `No, I'll review permissions and enable '<display_name>' in the
- 2.  **Update `sidecar.json` with the exact verified permissions**:
- -   Record every permission grant actually required during the test run,

## Key rules (verbatim lines from SKILL.md)

1. -   Use lowercase string literals for **`restart_policy`** (`"always"` is
2. -   Never place `sidecar.json` or scripts inside an ephemeral CitC workspace
3. -   `args[0]` **must** be the full cron schedule as a single string, including
4. -   Always use **absolute paths** for any local script arguments in `args`
5. -   Always include `"--"` immediately before the prompt string in `args` so the

## Files inside the skill

- (SKILL.md only)
