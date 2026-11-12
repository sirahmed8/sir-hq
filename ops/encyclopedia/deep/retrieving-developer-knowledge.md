# retrieving-developer-knowledge

Tools: codex (also claude/cursor/opencode/windsurf; codex chosen). Source: C:\Users\a7med\.codex\skills\retrieving-developer-knowledge\SKILL.md (101 lines) + references/{mcp-usage,api-fallback,supported-domains}.md

## Summary
Fetches OFFICIAL Google developer docs (Cloud, Gemini/ai.google.dev, ADK, TensorFlow, Android, Chrome, Web, Flutter, Go, Firebase) via the Developer Knowledge MCP (`answer_query`, `search_documents`, `get_documents`) or REST fallback at developerknowledge.googleapis.com/v1 — preferring existing gcloud credentials, then DEVELOPERKNOWLEDGE_API_KEY. Output is a complete executable solution, never recalled docs presented as retrieved.

## When to use / not use
Use for any technical question about Google platforms where doc accuracy matters (CLI flags, IAM permissions, configs). NOT for non-Google topics, general programming, or when offline; also not a substitute for reading the project's own code.

## Inputs, outputs, dependencies
Input: a technical query. Output: grounded documentation + complete self-contained solution (commands with all flags, YAML/JSON, code) with placeholders like PROJECT_ID. Needs: MCP tools if present, else curl + gcloud auth or API key; references/ for details.

## Key rules
1. MCP first, REST fallback — but a DECLARED server may not be CONNECTED; absent tools are normal, use REST.
2. Verify the lookup SUCCEEDED: PERMISSION_DENIED/401/403/empty results = failed lookup even if the tool reported no error; never answer as though it worked.
3. On HTTP 429 quota exhaustion of answer_query/:answerQuery, switch to search endpoint (search_documents or documents:searchDocumentChunks) with 2-5 focused keywords — don't fall back to memory.
4. Credential order for REST: gcloud user token → gcloud application-default token → DEVELOPERKNOWLEDGE_API_KEY; a 401/403 on one credential means try the next, not failure.
5. Output the FULL executable solution in the reply with standard placeholders — official doc conventions override memorized defaults.

## Risks / owner items
- Quota-limited generative endpoint; heavy use hits 429 — search endpoint is the fallback path.
- Requires gcloud auth or an API key the owner must provision (quickstart link provided); no credential = must say so rather than answer ungrounded.
- Answer quality depends on query phrasing; keyword search needs focused terms, not sentences.

## Category and tags
research, cloud, ai — google, documentation, gcp, gemini, firebase, grounded-answers.

## Revision note
Single codex revision (v1.0.1); the doc-grounding counterpart used across the ecosystem.
