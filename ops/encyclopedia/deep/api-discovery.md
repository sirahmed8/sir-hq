# api-discovery

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-discovery\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API discovery skill that automates the exploration and documentation of REST API surfaces. It inspects endpoint URLs, HTTP methods, request/response schemas, authentication requirements, and rate limits. The skill can generate OpenAPI/Swagger documentation from living APIs, discover hidden endpoints through fuzzing, and produce a searchable catalog of API resources with their purposes and tool requirements.

## When to use / when NOT
Use when starting a new integration project, refactoring existing API consumers, or producing API documentation for a team. Do NOT rely on manually maintained docs that drift from the living API — the skill produces documentation that stays in sync with the actual endpoints. Do NOT skip the authentication discovery step; the skill will flag endpoints that require OAuth, API keys, or bearer tokens and provide the required scopes.

## Inputs, outputs, tools
- Inputs: base API URL, authentication credentials (optional), tag filters, depth limit for recursive discovery.
- Outputs: OpenAPI/Swagger YAML/JSON document, catalog of endpoints with method, path, description, auth type, rate limit, and associated tools/MCP connectors.
- Tools: Postman CLI, OpenAPI generator, API fuzzer, curl, node.js script for YAML/JSON manipulation. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always run with authentication credentials** — the skill discovers auth-protected endpoints that are invisible without valid credentials.
2. **Use tag filtering to limit scope** — without filtering, the discovery can produce thousands of endpoints and be impractical to read.
3. **Review the generated OpenAPI for accuracy** — the skill is highly accurate but may misinterpret non-standard endpoints; manual review of edge cases is recommended.
4. **Catalog discovered tools/MCP connectors** — the skill maps each endpoint to the tools or connectors that can consume it; this is essential for the skills index.
5. **Run discovery on a staging environment first** — the skill will attempt to connect to the provided URL; ensure you have permission and that staging is isolated.

## Risks / owner notes
The skill may discover endpoints that are not intended for public consumption or that have undocumented breaking changes. The owner should review the catalog for sensitive endpoints (internal admin APIs) and either document them properly or exclude them from the public index. Over-discovery (without depth limits) can produce noisy output that is difficult to maintain.

## Category / tags
api · discovery, openapi, rest, documentation, fuzzing, catalog, developer-experience

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.