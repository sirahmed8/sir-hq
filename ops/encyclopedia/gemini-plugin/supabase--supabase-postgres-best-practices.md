# supabase-postgres-best-practices

- Tool: `gemini-plugin` (plugin: `supabase`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\supabase\skills\supabase-postgres-best-practices\SKILL.md`
- SKILL.md size: 3229 chars

## What it does

Postgres best practices maintained by Supabase, for Postgres running anywhere. Load this skill BEFORE writing or changing anything that lives in a Postgres database: creating or altering tables and columns (including choosing column types), schema design, migrations and declarative schema files, RLS policies and the tests that verify them, indexes, triggers, database functions, queues and scheduled jobs (pg_cron, pgmq), vector/semantic search (pgvector), and restoring dumps (pg_restore) or importing data. Also load it when diagnosing slow queries, high CPU, timeouts, EXPLAIN plans, connection exhaustion, locking, bloat, or rows visible to the wrong user or tenant. This is not just a performance guide — schema, migration, security, and SQL authoring tasks need these rules too, even for a one-column change or a single query.

## Structure (headings inside SKILL.md)

- Supabase Postgres Best Practices
- When to Apply
- Rule Categories by Priority
- How to Use
- References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - Writing SQL queries or designing schemas
2. - Implementing indexes or query optimization
3. - Reviewing database performance issues

## Files inside the skill

- `CHANGELOG.md` — "Changelog"
- `references/advanced-full-text-search.md` — "t"
- `references/advanced-jsonb-indexing.md` — "t"
- `references/conn-idle-timeout.md` — "pgbouncer.ini"
- `references/conn-limits.md` — "t"
- `references/conn-pooling.md` — "t"
- `references/conn-prepared-statements.md` — "t"
- `references/data-batch-inserts.md` — "t"
- `references/data-n-plus-one.md` — "t"
- `references/data-pagination.md` — "t"
- `references/data-upsert.md` — "t"
- `references/lock-advisory.md` — "t"
- `references/lock-deadlock-prevention.md` — "t"
- `references/lock-short-transactions.md` — "t"
- `references/lock-skip-locked.md` — "t"
- `references/monitor-explain-analyze.md` — "t"
- `references/monitor-pg-stat-statements.md` — "t"
- `references/monitor-vacuum-analyze.md` — "t"
- `references/query-composite-indexes.md` — "t"
- `references/query-covering-indexes.md` — "t"
- `references/query-index-types.md` — "t"
- `references/query-missing-indexes.md` — "t"
- `references/query-partial-indexes.md` — "t"
- `references/schema-constraints.md` — "t"
- `references/schema-data-types.md` — "t"
- `references/schema-foreign-key-indexes.md` — "t"
- `references/schema-lowercase-identifiers.md` — "t"
- `references/schema-partitioning.md` — "t"
- `references/schema-primary-keys.md` — "t"
- `references/security-privileges.md` — "t"
- `references/security-rls-basics.md` — "t"
- `references/security-rls-performance.md` — "t"
- `references/_contributing.md` — "Writing Guidelines for Postgres References"
- `references/_sections.md` — "Section Definitions"
- `references/_template.md` — "t"
