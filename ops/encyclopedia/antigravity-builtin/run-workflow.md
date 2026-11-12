# run-workflow

- Tool: `antigravity-builtin`
- Category: automation
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\run-workflow\SKILL.md`
- SKILL.md size: 10311 chars

## What it does

>- How to write and run a dynamic workflow script with the `run_workflow` tool: a Python script that orchestrates many agents with `agent`, `parallel`, `pipeline`, and `phase`. Use when a task splits into many independent or staged pieces of agent work (fan out over files, modules, bugs, or review angles, then aggregate), or when the user asks for a workflow. Don't use for a single delegated task (use a subagent) or for legacy workflow files (see migrate-workflows).

## Structure (headings inside SKILL.md)

- Dynamic workflows with `run_workflow`
- Steps
- Script rules
- Primitives
- Agents that keep their context
- Calling tools from the script
- Reading earlier conversation steps
- Behavior to know
- Example
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   `schema` (required): a JSON schema (dict or string) for the agent's result.
2. -   Agents do not see the script or each other. Put all the context an agent

## Files inside the skill

- (SKILL.md only)
