# enforcing-resource-attribution

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\enforcing-resource-attribution\SKILL.md`
- SKILL.md size: 4219 chars

## What it does

| Enforces resource attribution for CLI commands. Use this skill whenever you are running `bq` or `gcloud` commands via `run_command`. It ensures mandatory labeling for supported `bq` operations while avoiding invalid flags on read-only commands.

## Structure (headings inside SKILL.md)

- Resource Attribution Enforcement
- Applicability
- 🚫 When to Omit
- BigQuery CLI (`bq`)
- Examples
- Google Cloud SDK (`gcloud`)
- Examples
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tools

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  **DAK Tooling**: You are executing Python scripts, running MCP tools, or
2. 2.  **Domain Relevance**: You are operating on BigQuery datasets, GCS
3. -   **Flag Form**: `--label key:value`

## Files inside the skill

- (SKILL.md only)
