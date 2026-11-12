# api-discovery

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-discovery\SKILL.md` (4.6 KB; gemini-plugin/postman) plus `reference/orbit.md`.

## Summary
Skill for finding APIs or owners, integrating public providers, locating Postman resources, and investigating consumers and change impact; routes each question to Orbit, Postman search, or the Context Graph, then verifies which source answered.

## When to use / when NOT
Use when a question is about who consumes an endpoint, provider integration, or locating Postman collections, mocks or specs. Do NOT use to implement or test the API itself; route implementation to api-engineer and testing to api-testing.

## Inputs, outputs, tools
- Inputs: discovery question; source selection (public provider, Postman resource, cross-service change).
- Outputs: resource IDs, integration guidance, consumer or change impact evidence.
- Tools: postman CLI (`postman status`, `postman search`, `postman context-graph ask`, `postman dependency add`), Orbit REST API (`POST /v1/search`, `POST /v1/integrate`; read-only, safe retries, back off on 429).

## 5 most important rules
1. Check `postman status` before search, Context Graph and dependency commands; sign in if signed out and skip with a note if that is not possible.
2. Answer each question with the source that fits; a miss in one source is not proof of absence in another; combine entity search with relationship context.
3. Pass discovered ids verbatim to integrate; never construct or edit them.
4. Treat returned leads as unverified until checked against definitions, source or telemetry; newly added calls may not be ingested yet.

## Risks / things needing the owner
Postman sign-in is required for search and Context Graph; Orbit usage is free but not unlimited, so back off on 429.

## Category / tags
Category: research. Tags: api, postman, discovery, orbit, context-graph, integration.

## Revisions
Single gemini-plugin/postman copy. No competing revisions.
