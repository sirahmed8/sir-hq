# supabase-postgres-best-practices (gemini-plugin)

## Summary
supabase-postgres-best-practices is Supabase's maintained Postgres performance rulebook (MIT, v1.1.1, dated January 2026), applicable to Postgres anywhere — not just Supabase. The SKILL.md is an index: 8 priority-ordered rule categories (query performance CRITICAL, connection management CRITICAL, security & RLS CRITICAL, schema design HIGH, concurrency/locking MEDIUM-HIGH, data access MEDIUM, monitoring LOW-MEDIUM, advanced features LOW), each rule living in its own reference file with wrong-vs-right SQL examples, EXPLAIN output and metrics. 30+ reference files cover missing/partial/covering/composite indexes, prepared statements, pooling, RLS basics and RLS performance, constraints, partitioning, N+1, batch inserts, upserts, keyset-style pagination, advisory locks, deadlock prevention, SKIP LOCKED, pg_stat_statements, vacuum, full-text and JSONB indexing.

## When to use / when NOT
Load BEFORE writing or changing anything that lives in Postgres: tables, columns, types, schemas, migrations, RLS policies and their tests, indexes, triggers, functions, queues (pg_cron/pgmq), pgvector search, pg_restore imports — and when diagnosing slow queries, high CPU, timeouts, EXPLAIN plans, connection exhaustion, locking, bloat or cross-tenant row visibility. Do NOT skip it for "just a one-column change"; the description explicitly says schema/migration/security/SQL tasks need these rules even for tiny changes. It is not Supabase-product guidance (auth, CLI, MCP) — that is the sibling `supabase` skill.

## Inputs, outputs, tools
- Inputs: the SQL/schema/RLS task or the symptom (slow query, lock, bloat).
- Outputs: corrected SQL, schema designs, index choices, policy patterns per the referenced rule files.
- Tools: none executable — it is a documentation skill; the agent reads the relevant `references/<prefix>-<topic>.md` file(s) and applies them. Works with any Postgres (Supabase, RDS, self-hosted).

## 5 most important rules
1. Always read the specific rule file before writing the SQL; the SKILL.md is only the index.
2. Priority order is the triage order: query performance and connection management are CRITICAL, security/RLS is CRITICAL — do not ship schema work that fails those.
3. RLS has its own performance rules (`security-rls-performance.md`): naive policies cause per-row function calls and seq scans; wrap auth checks in `(select auth.uid())`-style initplan-friendly forms.
4. Connection management rules (pooling, limits, idle timeouts, prepared statements) matter as much as query tuning on serverless/Supabase.
5. Every rule file gives incorrect AND correct SQL with reasoning — follow the correct pattern, not just the topic name.

## Risks / things needing the owner
Applying index/partition/lock changes to a production database needs care and often a maintenance window; some rules (partitioning, pg_cron) have cost implications. Nothing in the skill itself needs the owner.

## Category / tags
data · postgres, supabase, indexes, rls, performance, sql

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\supabase\skills\supabase-postgres-best-practices\` with CHANGELOG.md and ~30 reference files. No divergent copies.
