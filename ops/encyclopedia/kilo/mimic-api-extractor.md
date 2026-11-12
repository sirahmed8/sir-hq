# mimic-api-extractor

Source read: `C:\Users\a7med\.claude\skills\mimic-api-extractor\SKILL.md` (2 KB; claude revision; codex/cursor/gemini-plugin/kilo/opencode/windsurf listed).

## Summary
Traffic-to-code reverse engineering: turn captured network traffic (HAR archives, mitmproxy dumps, Chrome DevTools logs via `list_network_requests`) into typed Python/TypeScript client SDKs. Pipeline: Parser (pattern & auth extraction) → Schema (data contract & endpoint mapper) → SDK (typed client library). Protocol: identify base URLs, versioned endpoints, methods, dynamic route params vs query params; extract auth schemes (Bearer JWT, OAuth refresh, cookies, CSRF, custom headers like x-api-key/device fingerprints) into a pluggable AuthHandler/token-refresh manager — never hardcode credentials; infer JSON schemas into Pydantic v2 models (Python) or Zod schemas/TS interfaces; generate a modular client (`client.py/ts` with retries+backoff+logging, `models.*`, `endpoints/` per resource) using `httpx` (Python) or `fetch` (TS) against live endpoints with zero mock data.

## When to use / when NOT
Use when the user has a HAR/proxy/DevTools capture and wants a typed SDK for that API. Do NOT use for APIs with public docs (use the official SDK), for credential harvesting, or to bypass access controls — it reverse-engineers observed traffic for interoperability.

## Inputs, outputs, tools
- Inputs: HAR file, mitmproxy dump, or DevTools network log; target API base.
- Outputs: `client.py|ts`, `models.py|ts` (Pydantic v2/Zod), `endpoints/` resource methods with docstrings.
- Tools: traffic captures, `httpx`/`fetch`, Pydantic v2, Zod, TypeScript; Chrome DevTools MCP `list_network_requests`.

## 5 most important rules
1. Distinguish dynamic route params (`/users/{id}`) from static query params when mapping endpoints.
2. Extract auth into a pluggable handler with token refresh — credentials are never hardcoded into generated code.
3. Infer strict types for every request/response (Pydantic v2 / Zod / TS interfaces).
4. Client must include retries, exponential backoff, and logging.
5. Zero mock data — generated SDK calls live endpoints.

## Risks / owner notes
Reverse-engineering third-party APIs may violate their ToS; generated clients embed the user's session tokens' SCHEME (not values). Captured HARs can contain live credentials/secrets — sanitize before writing files.

## Category and tags
Category: build. Tags: reverse-engineering, har, api-client, sdk-generation, pydantic, typescript, httpx.
