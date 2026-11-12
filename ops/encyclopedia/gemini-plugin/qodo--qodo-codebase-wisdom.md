# qodo-codebase-wisdom

- Tool: `gemini-plugin` (plugin: `qodo`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-codebase-wisdom\SKILL.md`
- SKILL.md size: 15724 chars

## What it does

Understand how code works, how a change was done before, and which repos are coupled — to answer a question, plan a code change, debug a regression, or scope a fix, using Qodo managed tools through MCP or the CLI. Use when a task needs to understand a codebase, its history, or how its repos relate — especially for a repo you don't have checked out or work spanning repos — "how does X work", "where is X defined", "who changed X", "explain this service", "plan the change for X", "what would changing X affect", "which repos depend on X", "why did X regress / when did it break", "has this been fixed before", "how did we solve X".

## Structure (headings inside SKILL.md)

- Codebase Wisdom
- Description
- Prerequisites
- Instructions
- Choose the execution path
- Handle a skill update notice
- Execution
- Runtime compatibility gate
- Quick start
- Preflight
- Route to a tool group
- Narrow, then fetch
- Examples
- Deliver
- Configuration
- Error Handling
- Guardrails
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tools, MCP path, MCP does, MCP Task, MCP capability

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - The required tools are available through a connected QAR managed-tools MCP server or the Qodo CLI.
2. - The workspace exposes the required read-only Codebase, pull-request, or cross-repo tools.
3. - Windows CLI: read [shell guidance](references/windows-shells.md) before the first call; [launcher recovery](references/windows-launcher.md) only if invocation fails. Reuse the resolved invocation.
4. - **Empty or `truncated: true` → narrow once and retry** (tighter query / path / repo) before
5. - On CLI, call reads through the fail-closed `qodo read` gateway; on MCP, require a read-only

## Files inside the skill

- `agents/openai.yaml`
- `references/skill-updates.md` — "Manual enterprise skill updates"
- `references/windows-launcher.md` — "Windows launcher recovery"
- `references/windows-shells.md` — "Windows shells"
