# netlify-database (netlify plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\netlify\agent-plugin\skills\netlify-database\SKILL.md`. Zero-config managed Postgres via `@netlify/database`.

## Summary
Managed Postgres: install `@netlify/database`, write migrations under `netlify/database/migrations/` (SQL files or subdirs with `migration.sql`), deploy — Netlify provisions the DB and applies migrations automatically. Queryable from Functions, Edge Functions, Builds, Agent Runners. Modern client: `getDatabase()` auto-selects connection per runtime; `db.sql` tagged template auto-parameterizes (`sql`User`` → rows, `execute()`/`stream()`/`chunked(n)`/`toSQL()`); helpers `sql.identifier` (safe names), `sql.values` (bulk insert), `sql.default`, `sql.raw` (UNPARAMETERIZED — trusted constants only, never user input), `sql.unsafe` ($1 params). Own driver/ORM: `getConnectionString()` returns correct per-branch connection string. Transactions require `db.pool` (pg.Pool) — BEGIN/queries/COMMIT on the same `pool.connect()` client. Legacy `@netlify/neon`/`neon()` and `NETLIFY_DATABASE_URL` are superseded by `@netlify/database`/`NETLIFY_DB_URL`. Drizzle convention: schema `db/schema.ts`, client `db/index.ts` with the `netlify-db` adapter. Local dev via `netlify dev` with local Postgres; database branches isolate deploy previews.

## When to use / when NOT
Use for adding a database, contact forms/CRUD APIs, SQL migrations, Drizzle wiring, `netlify database` commands, local Postgres testing, migrating off Neon/Supabase/RDS. NOT for new code on legacy `@netlify/neon` or for object storage needs (→ netlify-blobs).

## Inputs, outputs, tools
- Inputs: schema/migrations, query code, optional Drizzle schema.
- Outputs: provisioned Postgres, applied migrations, per-branch DBs for previews.
- Tools: `@netlify/database` (`getDatabase`, `getConnectionString`, `db.sql`, `db.pool`), `netlify database` CLI, `netlify dev`, Drizzle ORM.

## 5 most important rules
1. Migrations live in `netlify/database/migrations/` — auto-applied on deploy.
2. `db.sql` tagged templates auto-parameterize; `sql.raw` bypasses injection protection — trusted constants only.
3. Transactions MUST use `db.pool.connect()` — same connection for BEGIN…COMMIT.
4. Legacy `@netlify/neon`/`NETLIFY_DATABASE_URL` → migrate to `@netlify/database`/`NETLIFY_DB_URL`.
5. Deploy-preview DBs are branch-scoped — previews don't touch production data.

## Risks / owner notes
`sql.raw`/`sql.unsafe` are injection footguns if misused. Migration failures block deploys. Connection string handling differs per runtime — use `getConnectionString()`, not env spelunking.

## Category and tags
Category: cloud. Tags: netlify, postgres, database, migrations, drizzle, sql, transactions, deploy-previews.
