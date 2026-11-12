# supabase

- Tool: `gemini-plugin` (plugin: `supabase`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\supabase\skills\supabase\SKILL.md`
- SKILL.md size: 14271 chars

## What it does

Use when doing ANY task involving Supabase. Triggers: Supabase products (Database, Auth, Edge Functions, Realtime, Storage, Vectors, Cron, Queues); client libraries and SSR integrations (supabase-js, @supabase/ssr) in Next.js, React, SvelteKit, Astro, Remix; auth issues (login, logout, sessions, JWT, cookies, getSession, getUser, getClaims, RLS); Supabase CLI or MCP server; schema changes, migrations, declarative schemas, security audits, Postgres extensions (pg_graphql, pg_cron, pg_vector); debugging and troubleshooting errors or unexpected behavior on Supabase projects (HTTP errors, Postgres errors, RLS surprises, permission denied, schema cache issues, timeouts, Edge Function crashes, Realtime drops, Storage failures) and reading or querying logs (Logs Explorer, ClickHouse).

## When to use (from skill text)

- If the server is reachable and `.mcp.json` is correct but tools aren't visible, the user needs to authenticate. The Supabase MCP server uses OAuth 2.1 — tell the user to trigger the auth flow in their agent, complete it in the browser, and reload the session.
- Use this when `supabase/schemas/` exists or `config.toml` sets `schema_paths`. Edit the desired schema state in those files, then generate and review the migration. Do not start by hand-writing a migration. See the [Declarative database schemas guide](https://supabase.com/docs/guides/local-developme
- Use this when the project does not use declarative schemas.

## Structure (headings inside SKILL.md)

- Supabase
- Core Principles
- Supabase CLI
- Supabase MCP Server
- Supabase Documentation
- Making and Committing Schema Changes
- Option A: Declarative schemas
- Option B: Imperative migrations
- Debugging
- Reference Guides
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server, MCP tool, MCP Server, MCP setup

## Risks / cautions found in text

- - **Deleting a user does not invalidate existing access tokens.** Sign out or revoke sessions first, keep JWT expiry short for sensitive apps, and for strict guarantees validate `session_id` against `auth.sessions` on sensitive operations.
- - **If you use `app_metadata` or `auth.jwt()` for authorization, remember JWT claims are not always fresh until the user's token is refreshed.**
- - **Never expose the `service_role` or secret key in public clients.** Prefer publishable keys for frontend code. Legacy `anon` keys are only for compatibility. In Next.js, any `NEXT_PUBLIC_` env var is sent to the browser.
- - **`SECURITY DEFINER` functions bypass RLS.** A `SECURITY DEFINER` function runs with its creator's privileges — typically a role with `bypassrls` (e.g., `postgres`). Never add `SECURITY DEFINER` to resolve a permission error; it silently removes access control without fixing the underlying cause. 

## Key rules (verbatim lines from SKILL.md)

1. - **Never use `user_metadata` claims in JWT-based authorization decisions.** In Supabase, `raw_user_meta_data` is user-editable and can appear in `auth.jwt()`, so it is unsafe for RLS policies or any other authorization logic. Store authorization data in `raw_app_meta_data` / `app_metadata` instead.
2. - **If you use `app_metadata` or `auth.jwt()` for authorization, remember JWT claims are not always fresh until the user's token is refreshed.**
3. - **Never expose the `service_role` or secret key in public clients.** Prefer publishable keys for frontend code. Legacy `anon` keys are only for compatibility. In Next.js, any `NEXT_PUBLIC_` env var is sent to the browser.
4. - **UPDATE requires a SELECT policy.** In Postgres RLS, an UPDATE needs to first SELECT the row. Without a SELECT policy, updates silently return 0 rows — no error, just no change.
5. - **UPDATE policies require both `USING` and `WITH CHECK`.** Without `WITH CHECK`, a user can reassign a row's `user_id` to another user:

## Files inside the skill

- `assets/feedback-issue-template.md` — ""
- `CHANGELOG.md` — "Changelog"
- `references/skill-feedback.md` — "Skill Feedback"
