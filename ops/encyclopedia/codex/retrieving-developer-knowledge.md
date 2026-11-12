# retrieving-developer-knowledge

- Tool: `codex`
- Category: data
- Source: `C:\Users\a7med\.codex\skills\retrieving-developer-knowledge\SKILL.md`
- SKILL.md size: 7719 chars

## What it does

Search and retrieve official Google developer documentation across Google Cloud, Gemini, Android, Chrome, Web, Flutter, and Firebase.

## Structure (headings inside SKILL.md)

- Google Developer Knowledge
- Workflow
- Tool Selection & Usage
- 1. Developer Knowledge MCP Tools (Preferred)
- 2. REST API Fallback
- Synthesis & Output Guidelines
- References
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tools, MCP handshake, MCP Tools, MCP Usage

## Risks / cautions found in text

- 2. **Confirm the lookup succeeded before using it**: A response that arrives is not automatically an answer. `PERMISSION_DENIED`, `UNAUTHENTICATED`, HTTP 401 or 403, an empty result set, or any error payload is a FAILED lookup even when the tool itself reported no error. On a failed lookup, do not a
- - **`answer_query(query="...")`**: Use for conceptual guides, architectural comparisons, product choice overviews, and multi-step workflows. This tool has limited quota. If you get a 429 out of quota error, use `search_documents` instead.
- - **`search_documents(query="...")`**: Use for granular CLI flags, exact syntax, parameter names, and IAM permissions (`service.resource.verb`). Use 2–5 focused keywords (e.g., `cloud run filestore nfs mount gcloud`) rather than full conversational sentences.
- 2. **Exact Parameter Formatting**: Format CLI flags, composite keys (e.g. `location=IP:PATH`), and IAM permission strings according to official Google specifications.

## Key rules (verbatim lines from SKILL.md)

1. 1. **Direct Retrieval**: When answering a technical question, execute a single documentation lookup directly within your current conversation context (do not delegate retrieval to subagents):
2. - **A declared server is not always a connected server.** Some clients cannot complete the MCP handshake with this server and expose no `answer_query`, `search_documents` or `get_documents` tool at all, even though the plugin declares one. Treat their absence as normal and use the REST fallback belo
3. 2. **Confirm the lookup succeeded before using it**: A response that arrives is not automatically an answer. `PERMISSION_DENIED`, `UNAUTHENTICATED`, HTTP 401 or 403, an empty result set, or any error payload is a FAILED lookup even when the tool itself reported no error. On a failed lookup, do not a
4. 3. **Immediate & Complete Solution Output**: Immediately upon receiving the documentation response, output the complete, self-contained, and executable technical solution (commands with all required flags and placeholders, YAML/JSON configurations, or code snippets) directly in your response text.
5. 3. **Complete Solutions in Final Response**: Always output the full, self-contained, executable technical solution (commands, configurations, or code snippets) with clear standard placeholders (e.g. `PROJECT_ID`, `SERVICE_NAME`, `REGION`) directly in your final message, even if previously referenced

## Files inside the skill

- `references/api-fallback.md` — "Developer Knowledge REST API Fallback Guide"
- `references/mcp-usage.md` — "MCP Tool Usage & API Details"
- `references/supported-domains.md` — "Supported Developer Domains"
