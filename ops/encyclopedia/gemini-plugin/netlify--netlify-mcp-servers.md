# netlify-mcp-servers (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-mcp-servers\SKILL.md`. Build/deploy/secure MCP servers on Netlify Functions.

## Summary
Disambiguation first: "Netlify MCP" can mean Netlify's OWN hosted MCP server (lets agents operate the Netlify platform — you don't write it, point clients at Netlify's docs; see netlify-agent-runner) vs building YOUR OWN MCP endpoint exposing your app's tools to agents — this skill covers the latter. An MCP server on Netlify = ONE Netlify Function speaking MCP over HTTP. Two shapes: standalone repo (wraps third-party API) or added to existing app (tools call the SAME service/data layer as UI/REST routes — no duplicated logic). Decide auth up front: single-user → shared secret; multi-user → per-user API keys via Netlify Identity (start with secret, layer later). Stack: official MCP SDK + `WebStandardStreamableHTTPServerTransport` — web-standard Request/Response primitives, no Node bridge needed (older guides' `fetch-to-node`+`StreamableHTTPServerTransport` is unnecessary on Netlify); `@modelcontextprotocol/sdk` + `zod`. Server pattern: `buildServer()` creates `McpServer`, `server.tool(name, desc, zod-schema, handler)`; default export checks bearer auth → rejects non-POST (405 — GET opens SSE stream that never closes → 502 on serverless) → transport handles JSON-RPC/version handshake. HTTP 406 = client's Accept header lacks both `application/json` and `text/event-stream` (MCP-spec requirement — fix client, not server). Covers auth (references/authentication.md), read/write tool safety, file uploads, client connections.

## When to use / when NOT
Use when exposing app tools/data to AI agents (Claude Desktop/Code, Cursor) via MCP, wrapping third-party APIs as tools, or adding MCP to an existing Netlify site. NOT for operating Netlify itself via MCP (that's Netlify's hosted server) or non-HTTP transports.

## Inputs, outputs, tools
- Inputs: tools to expose (name/desc/zod schema/handler), auth choice (shared secret vs Identity keys).
- Outputs: MCP endpoint at a function path serving JSON-RPC over Streamable HTTP.
- Tools: `@modelcontextprotocol/sdk` (`McpServer`, `WebStandardStreamableHTTPServerTransport`), `zod`, Netlify Functions, `@netlify/identity` for per-user keys.

## 5 most important rules
1. Web-standard transport only — no Node req/res bridge on Netlify.
2. POST-only: reject GET (SSE never closes → 502 on serverless); 406 = client Accept header problem.
3. Decide auth first: shared secret for single-user, Identity-backed keys for multi-user.
4. Tools should reuse the app's existing service layer — don't duplicate logic.
5. Stateless JSON mode — don't hold SSE sessions in a serverless function.

## Risks / owner notes
Auth is the whole security story — a public MCP endpoint exposes your tools to anyone. Write tools need explicit safety review. Stateless transport limits some MCP features (no persistent SSE). Version drift in SDK transport behavior.

## Category and tags
Category: cloud. Tags: netlify, mcp, ai-agents, streamable-http, tools, authentication, serverless.
