# migrate-agent-settings

- Tool: `antigravity-builtin`
- Category: security
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\migrate-agent-settings\SKILL.md`
- SKILL.md size: 10468 chars

## What it does

Migrates the user's MCP servers, skills, slash commands, subagents, and instruction files from other coding agents (Claude Code, Codex, Cursor, Gemini CLI) into one new Antigravity plugin. Use when the user wants to bring over, import, or migrate their setup or config from another agent or tool. Don't use for installing Marketplace plugins or authoring a new plugin from scratch (use the plugin skill).

## When to use (from skill text)

- trigger: always_on
- triggers: `alwaysApply: true` to `always_on`; non-empty `globs` to
- `trigger: glob`; a non-empty `description` to `trigger: model_decision`;

## Structure (headings inside SKILL.md)

- Migrate agent settings into an Antigravity plugin
- Step 1: Discover
- Step 2: Confirm the plan
- Step 3: Write the plugin
- Step 4: Hand back
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP servers, MCP server, MCP configs

## Risks / cautions found in text

- -   Claude Code `hooks` and `permissions` in `settings.json`: their tool names
- -   Keep literal secret values exactly as they were in the source file; the
- -   Drop `model` and `color`.

## Key rules (verbatim lines from SKILL.md)

1. -   The `name` in frontmatter must match the folder name.
2. -   `description`: required; write one from the body if missing.
3. -   `tools`: always write it, since an omitted `tools` gets only a small

## Files inside the skill

- (SKILL.md only)
