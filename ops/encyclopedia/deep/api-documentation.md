# api-documentation

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-documentation\SKILL.md` (2.8 KB; gemini-plugin/postman) plus `reference/rest-api-best-practices.md`.

## Summary
Skill that keeps API contracts documented: starts from the existing source of truth (OpenAPI or Postman collection), generates the other when both are needed, describes what changes affect callers, saves examples including error paths, and chooses delivery.

## When to use / when NOT
Use when defining or improving an API contract, generating docs from a collection or OpenAPI spec, or publishing docs. Do NOT use for implementing endpoints or running tests; route implementation to api-engineer and testing to api-testing.

## Inputs, outputs, tools
- Inputs: OpenAPI spec or Postman collection, contract changes, examples.
- Outputs: documentation, generated collection, saved examples.
- Tools: `postman spec generate collection`, collection-schema-v3 for local edits, variables for credentials, postman-mcp-server docs workflow.

## 5 most important rules
1. Keep one source of truth; when both spec and collection matter, maintain both with an explicit generation direction.
2. Inspect generated collections before replacing an existing one; maintained scripts and examples carry knowledge beyond endpoint shapes.
3. Describe caller impact: required vs optional inputs, auth and scopes, response guarantees, pagination, retries, side effects; label unresolved design choices instead of inventing them.
4. Save examples for consequential cases including errors; a success-only example hides failure paths callers must handle.

## Risks / things needing the owner
Public docs publishing requires an audience decision; a workspace push does not publish public docs by itself.

## Category / tags
Category: research. Tags: api, documentation, openapi, postman, contracts, examples.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
