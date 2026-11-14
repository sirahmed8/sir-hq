# resolving-mcp-region-configs

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\resolving-mcp-region-configs\SKILL.md`
- SKILL.md size: 4150 chars

## What it does

>- Mandatory Step 0 pre-flight check for regional Google Cloud MCP servers (e.g. Dataproc) before using MCP tools or falling back to gcloud/bq CLI. Use whenever interacting with Dataproc clusters, Spark batches, jobs, sessions, or regional GCP resources. Fixes regional MCP servers whose endpoint URL still has an unreplaced $GCP_REGION / ${REGION} placeholder across Claude Code, Codex, and Antigravity. Trigger: an expected mcp__*_{service}_* tool is missing entirely (not just failing), or a call to one fails/hangs on a malformed host. Check via ToolSearch/deferred-tools listing before falling back to gcloud/bq CLI. Asks the user for a region, patches the live MCP config file(s), and tells the user how to restart without losing session context.

## When to use (from skill text)

- Treat a missing `mcp__*__<service>__*` tool as the trigger, not just a failed

## Structure (headings inside SKILL.md)

- Regional MCP Server Configuration
- Mandatory Step 0 Pre-Flight Check
- When to use
- Supported services
- Locating the live config
- Procedure
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP Server, MCP tools, MCP configuration, MCP servers, MCP connections

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  You MUST NOT call the regional tools yet — there likely aren't any to call.
2. 2.  You MUST ask the user for their GCP region (e.g. `us-central1`). You MUST
3. 3.  You MUST edit the placeholder to that region in the config file(s) above.
4. 4.  You MUST tell the user to restart — MCP connections load once at startup and

## Files inside the skill

- (SKILL.md only)
