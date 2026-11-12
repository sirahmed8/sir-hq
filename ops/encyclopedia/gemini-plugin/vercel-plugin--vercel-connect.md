# vercel-connect (gemini-plugin: vercel)

## Summary
vercel-connect manages short-lived, scoped third-party credentials via Vercel Connect: apps authenticate with their project OIDC token (or a scoped Vercel access token in external CI) and request provider tokens (Slack, GitHub, Linear, 100+ services) WITHOUT storing provider API keys or refresh tokens in env vars. Connectors are team-owned with stable UIDs like `slack/acme-slack`; a project+environment must `vercel connect attach` before requesting tokens. Four subject types: `user` (on-behalf-of, needs stable server-side user id — never from request body), `app` (bot/installation), `jwt-bearer` (federated), `token` (exchange). SDK: `@vercel/connect` `getToken()` at use-time with built-in caching; eve-agent helpers (`connect()`, `connectSlackCredentials`, `connectGitHubCredentials`, `connectLinearCredentials`) wire tokens AND webhook verification (Vercel OIDC-signed forwards) so no SLACK_BOT_TOKEN/GITHUB_APP_PRIVATE_KEY env vars are needed; framework adapters for AI SDK/MCP, TanStack AI, Chat SDK, Better Auth, Auth.js; plain HTTP API `POST /v1/connect/token/<uid-url-encoded>` for other languages. CLI: `vercel connect list/create/attach/detach/token` with `--format=json`; creation/attach are distinct steps; browser auth flows need a human.

## When to use / when NOT
Use when an app needs provider API credentials without managing OAuth refresh tokens itself, MCP client auth, or eve agent channels. Do NOT use for signing users INTO your app (that's the betterauth/authjs adapters' different job — they don't return provider tokens), and do NOT store raw provider tokens in logs.

## Inputs, outputs, tools
- Inputs: connector UID, subject type/id, scopes/audience/resources; CLI commands; HTTP POST body.
- Outputs: short-lived provider tokens; eve channel credential objects; connector metadata.
- Tools: `vercel connect` CLI, `@vercel/connect` SDK (+ `/eve`, `/ai-sdk`, `/mcp`, `/chat`, `/betterauth`, `/authjs` subpaths), `@vercel/passport` identity, Vercel OIDC token, HTTP API.

## 5 most important rules
1. Server-side only: getToken, Connect auth providers and MCP clients never run client-side; subject.id comes from the authenticated session, never request input.
2. Full lifecycle: list → create (check `create <service> --help` for connection methods) → attach to project+environments → token. Creating does NOT authorize the project.
3. Call getToken() immediately before provider use; let SDK cache; scope each request (installationId, scopes, audience, authorizationDetails).
4. Multi-tenant: never guess installationId — resolve trusted mapping; separate connectors for prod vs non-prod provider isolation.
5. Triggers are opt-in and separate; forwarded webhooks arrive as Vercel-OIDC-signed requests verified by the helpers, not raw provider secrets.

## Risks / things needing the owner
Connector creation/authorization opens a browser OAuth flow — a human must finish it; `--yes` only permits auto-opening. Access tokens can only mint `app` or own-user subjects; user subjects for others need project OIDC. Token requests without attach fail. Nothing else needs the owner.

## Category / tags
cloud · vercel, oauth, credentials, mcp, agents

## Revisions
Single revision read: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-connect\SKILL.md` (320 lines). Gemini-plugin only per slice.
