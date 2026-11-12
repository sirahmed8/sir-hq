# vercel-connect

- Tool: `gemini-plugin` (plugin: `vercel-plugin`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\vercel-plugin\skills\vercel-connect\SKILL.md`
- SKILL.md size: 18879 chars

## What it does

Securely obtain and manage scoped credentials.

## When to use (from skill text)

- - Forward provider events to applications through Vercel Connect triggers
- The CLI also supports `detach`, `update`, `remove`, and `open`. Run `vercel connect <command> --help` before using optional installation, scope, trigger, branch, or custom-environment flags.
- Use this whenever the project is on eve + Vercel Connect. It is the one-liner for both outbound posts and inbound webhook auth.

## Structure (headings inside SKILL.md)

- Vercel Connect Skill
- Overview
- When to Use Vercel Connect
- Modes of tokens
- CLI
- Inspect connectors linked to the current project, or all team connectors
- Inspect supported setup options, then create a connector
- Link the connector to the current project and selected environments
- Request a scoped provider token
- JavaScript/TypeScript SDK (`@vercel/connect`)
- HTTP API
- Get a token via HTTP
- Get token from Vercel Connect
- Use the token
- Framework adapters
- Better Auth and Auth.js
- Project links, installations, and environments
- Triggers and observability
- Recommended workflow
- Sources of truth
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP clients, MCP server, MCP servers, MCP connection, MCP runtime, MCP client

## Risks / cautions found in text

- - Connect to any third-party system that requires OAuth tokens or API credentials
- - Obtain scoped, short-lived provider credentials for authenticated API calls
- - **`token`**: token exchange. Pass `{ token }` with an existing subject token; the SDK infers `type: "token"` in `@vercel/connect` 2.4.0+.
- - `getTokenResponse()` for token metadata such as expiry and connector details.

## Key rules (verbatim lines from SKILL.md)

1. - Connect to any third-party system that requires OAuth tokens or API credentials
2. - **`user`**: actions performed on behalf of a specific end user (e.g., post a Slack message as the user). Requires a user `id` and optional `issuer`.
3. - **`app`**: actions performed as the app itself (e.g., post as a Slack bot or use a GitHub installation). It skips per-user consent but may still require a provider installation or supported app grant.
4. - **`jwt-bearer`**: federated identity through the OAuth JWT-bearer grant. Pass `sub` (required), plus optional `iss`, `aud`, and `additionalClaims`.
5. - `startAuthorization()` after `UserAuthorizationRequiredError` to begin user consent.

## Files inside the skill

- (SKILL.md only)
