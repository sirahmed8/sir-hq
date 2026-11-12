# vercel-storage (codex revision)

## Summary
vercel-storage is the authoritative map of Vercel storage: FIRST-PARTY — Vercel Blob (`@vercel/blob`: put/get/list/del, public vs private access, client uploads to 5TB via handleUploadUrl token endpoint, ETag conditional get, Fast Data Transfer vs Blob Data Transfer routing) and Edge Config (`@vercel/edge-config`: <1ms edge reads for flags/A-B/routing config — reads only, never user data or writes). MARKETPLACE — and the critical fact that `@vercel/postgres` and `@vercel/kv` are SUNSET: use Neon Postgres (`@neondatabase/serverless`, needs Node 19+, lazy-init DB or top-level `neon()` crashes `next build`, NEVER wrap db in a JS Proxy — breaks NextAuth inspection and hangs auth silently, drizzle-kit/tsx don't auto-load .env.local so use dotenv-cli) and Upstash Redis (`@upstash/redis` + Ratelimit), plus Supabase, Prisma, MongoDB Atlas, Convex, Turso. Provisioning preference: Marketplace integration (`vercel integration add neon`) auto-injects env vars; manual fallback requires `vercel env pull .env.local`. Includes migration diffs (@vercel/postgres→Neon with `@neondatabase/vercel-postgres-compat` drop-in, @vercel/kv→Upstash) and a decision matrix.

## When to use / when NOT
Use when choosing/provisioning/wiring any Vercel storage or database. Do NOT use Edge Config for user data/writes; don't use private Blob access for publicly-served files (slow + egress costs); don't reach for @vercel/postgres or @vercel/kv — they no longer exist.

## Inputs, outputs, tools
- Inputs: storage need (files/config/SQL/KV/docs/reactive/edge-sqlite).
- Outputs: package choice, provisioning commands, code snippets, env var handling.
- Tools: `vercel integration add/list`, `vercel env pull`, provider SDKs, dotenv-cli for scripts.

## 5 most important rules
1. @vercel/postgres and @vercel/kv are DEAD — migrate to Neon/Upstash; compat package exists for postgres.
2. Lazy-init the Neon client (`getDb()` pattern): top-level `neon()` throws at build time when DATABASE_URL isn't set yet.
3. NEVER Proxy-wrap the DB client — silently hangs NextAuth/Auth.js adapter inspection.
4. Provision via Marketplace first (auto env vars); manual provisioning means you sync env vars yourself then `vercel env pull`.
5. Only Next.js auto-loads .env.local — drizzle-kit, tsx, seed scripts need `dotenv -e .env.local --` or sourced exports.

## Risks / things needing the owner
Marketplace installs create real billed resources and inject secrets — owner-level billing/account decisions; Neon CLI fallback for Vercel-managed projects needs a Neon API key. Private blob misconfiguration leaks or breaks delivery. Env var sync mistakes cause build/runtime divergence.

## Category / tags
cloud · vercel, storage, database, marketplace, neon

## Revisions
Single source read: `C:\Users\a7med\.codex\skills\vercel-storage\SKILL.md` (363 lines). Six-tool skill; codex revision representative.
