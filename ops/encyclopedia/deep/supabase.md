# supabase (gemini-plugin)

## Summary
supabase is Supabase's own official skill (author: supabase, v0.1.2): the single entry point for ANY task touching Supabase — database, Auth, Edge Functions, Realtime, Storage, pgvector, Cron/Queues, the supabase-js/@supabase/ssr client libs, the CLI, the MCP server, RLS, migrations, and debugging. Its core doctrine is "verify, don't trust training data": fetch the changelog before implementing, verify fixes with test queries, stop looping after 2-3 failed attempts, and always check docs via MCP `search_docs` or `.md`-suffixed doc URLs. It carries a serious Supabase-specific security checklist (user_metadata is user-editable and must never drive authorization; service_role keys never in public clients; views bypass RLS unless security_invoker; UPDATE needs SELECT+USING+WITH CHECK; SECURITY DEFINER functions are public API endpoints) and documents both schema workflows (declarative `supabase/schemas/` vs imperative migrations via `supabase db pull`).

## When to use / when NOT
Use for literally any Supabase task: schema changes, auth bugs, RLS policies, Edge Functions, CLI/MCP operations, performance issues, log reading. Do NOT use for non-Supabase Postgres (use supabase-postgres-best-practices for pure Postgres rules, or other DB skills), and do not rely on it for other BaaS providers.

## Inputs, outputs, tools
- Inputs: the Supabase task plus project context; credentials via env or the Supabase MCP server (`https://mcp.supabase.com/mcp`, OAuth 2.1 or scoped PAT).
- Outputs: working code/migrations/policies plus verified query results.
- Tools: Supabase CLI (discover via `--help`, never guess; `db query` needs v2.79+, `db advisors` v2.81.3+), the Supabase MCP server tools (execute_sql, get_advisors, search_docs), `psql` fallback, and docs fetched as markdown. Scoped personal access tokens preferred over classic full-access tokens.

## 5 most important rules
1. Check `supabase.com/changelog.md` for breaking changes before implementing; training data is stale.
2. RLS on every table in exposed schemas; `TO authenticated` alone is BOLA — always pair with an ownership `USING` predicate; UPDATE policies need both `USING` and `WITH CHECK`.
3. Never use `user_metadata`/`raw_user_meta_data` for authorization; use `app_metadata`. Never expose service_role keys; use publishable keys.
4. Imperative projects: iterate with `execute_sql`/`db query`, NOT `apply_migration` (it writes history every call and breaks `db diff`); commit via `supabase db pull <name> --local`.
5. SECURITY DEFINER functions in `public` are callable by everyone — keep them in unexposed schemas with auth.uid() checks, prefer SECURITY INVOKER.

## Risks / things needing the owner
Auth to the MCP server is OAuth in browser or a scoped PAT the owner must create; `supabase login` browser flow creates a full-access classic token (CI should use SUPABASE_ACCESS_TOKEN scoped token). Production schema changes and `db push` are high-impact. New tables may be invisible to the Data API depending on dashboard settings — check grants, not just RLS.

## Category / tags
cloud · supabase, postgresql, rls, auth, migrations, backend

## Revisions
Only one revision exists: the gemini-plugin supabase skill folder (SKILL.md, CHANGELOG.md, references/skill-feedback.md, assets). No divergent copies.
