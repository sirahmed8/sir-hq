# resolving-mcp-region-configs

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills\resolving-mcp-region-configs\SKILL.md`
- SKILL.md size: 4150 chars
- Identical content to: `encyclopedia/gemini-plugin/data-agent-kit-plugin--resolving-mcp-region-configs.md`

Auto-generated stub: this SKILL.md is byte-identical to `encyclopedia/gemini-plugin/data-agent-kit-plugin--resolving-mcp-region-configs.md`. Read that digest for full details.

Description: Mandatory Step 0 pre-flight check for regional Google Cloud MCP servers (e.g. Dataproc) before using MCP tools or falling back to gcloud/bq CLI. Use whenever interacting with Dataproc clusters, Spark batches, jobs, sessions, or regional GCP resources. Fixes regional MCP servers whose endpoint URL still has an unreplaced $GCP_REGION / ${REGION} placeholder across Claude Code, Codex, and Antigravity. Trigger: an expected mcp__*_{service}_* tool is missing entirely (not just failing), or a call to one fails/hangs on a malformed host. Check via ToolSearch/deferred-tools listing before falling back to gcloud/bq CLI. Asks the user for a region, patches the live MCP config file(s), and tells the user how to restart without losing session context.