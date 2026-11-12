# qodo-review-notes

- Tool: `gemini-plugin` (plugin: `qodo`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\qodo\skills\qodo-review-notes\SKILL.md`
- SKILL.md size: 31593 chars

## What it does

Preserve reasoning for independent review of plans and PRs through Qodo notes tools. Use during substantive planning and development, when decisions, scope or validation change, when resuming or handing off work, and before opening or updating a PR. Tracks hold the evolving plan across issues and repositories; PR notes explain one change. Also use to read or maintain reviewer context. This skill does not review or approve a plan or code, implement it, or open a PR.

## Structure (headings inside SKILL.md)

- Development Tracks and PR Review Notes
- Description
- Capture reasoning as work develops
- Prerequisites
- Instructions
- Handle a skill update notice
- Execution
- Choose the available tools
- Find the track at intake or when resuming
- Maintain Development Track Notes
- Publish PR Review Notes before opening a PR
- Associate an existing or newly opened PR
- Configuration
- Error Handling
- Report the result
- Read every page before editing
- Tool access
- CLI
- Example input for local CLI preparation
- Git providers and repository identities
- MCP
- Operations
- Manual enterprise skill updates
- Runtime recovery
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP connection, MCP server, MCP remains, MCP with, MCP
tools, MCP performs, MCP schema, MCP call

## Risks / cautions found in text

- - The chosen approach, scope, assumptions, dependencies or a significant risk changes.
- 5. Create a track when the task has overall product/delivery context worth maintaining and no
- - Product decisions and their reasons; business impact when known.

## Key rules (verbatim lines from SKILL.md)

1. - A plan has concrete goals, constraints, proposals or decisions worth reviewing, before coding.
2. - Windows CLI: read [shell guidance](references/windows-shells.md) before the first call; [launcher recovery](references/windows-launcher.md) only if invocation fails. Reuse the resolved invocation.

## Files inside the skill

- `agents/openai.yaml`
- `references/windows-launcher.md` — "Windows launcher recovery"
- `references/windows-shells.md` — "Windows shells"
