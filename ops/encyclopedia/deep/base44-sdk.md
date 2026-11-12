# base44-sdk

**Source:** `C:\Users\a7med\.gemini\config\plugins\base44\skills\base44-sdk\SKILL.md` (+ `references/`)
**Category:** build
**Tags:** base44, sdk, javascript, typescript, realtime, actors, backend, ai-gateway

## Summary
The Base44 SDK skill for writing feature code inside an existing Base44 project (one that already has `base44/config.jsonc`). It documents the JavaScript/TypeScript SDK modules (entities, auth, agents, functions, actors, integrations, aiGateway, analytics, appLogs, users, and the service-role connectors and SSO), gives WRONG-vs-CORRECT method tables to prevent hallucinated APIs, and shows client setup, module selection, common patterns, and a frontend-versus-backend capability table.

## When to use / when not to
Use it to implement features, components or backend functions in an existing Base44 project. Do not use it to initialize a new project or run CLI commands (use `base44-cli`), or in an empty directory without Base44 configuration.

## Inputs, outputs, tools
Inputs: an existing `base44/config.jsonc`, `@base44/sdk` installed, and the project's entity, function, actor and agent definitions. Outputs: typed SDK code for CRUD, auth, realtime actors, AI calls and backend functions. Tools: `@base44/sdk` and the `base44-cli` skill for type generation. No MCP.

## Five most important rules
1. Verify method names against the table or `references/QUICK_REFERENCE.md`; Base44 names differ from Firebase and Supabase (for example `loginViaEmailPassword`, `functions.invoke`, `entities.Task.create`).
2. Use `appId` (not `clientId` or `id`) in `createClient` for external apps.
3. Actors: connect with `actors.Room(id).connect()`, subscribe on the connection, and expect `{unsubscribe()}`; entities `subscribe()` returns the unsubscribe function itself, so do not mix the two conventions.
4. `functions.invoke()` returns the raw axios response: the function's JSON is on `.data`, and it throws on non-2xx with the error body at `err.response.data`.
5. Use `asServiceRole` only in backend functions; never expose service-role access to the frontend.

## Risks and owner actions
The main risk is hallucinated API names, which the tables exist to prevent. `aiGateway` requires the service role and a backend. No secrets belong in client code.

## Revisions
The installed config copy (16854 bytes) and the marketplace cache 1.0.0-beta.1 have identical bodies; only the description frontmatter differs.
