# alloydb-omni-performance

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-performance\SKILL.md` (gemini revision; only source).

## Summary
A Google-published AlloyDB Omni skill for analyzing query performance and monitoring database activity. It ships Node.js scripts that connect to a PostgreSQL-compatible AlloyDB Omni instance and run diagnostics: execute SQL, estimate column cardinality, generate EXPLAIN plans (without executing), list active/long-running queries, database stats, query stats (pg_stat_statements) and table stats (sequential scans, index usage, bloat, vacuum times).

## When to use / when NOT
Use when tuning AlloyDB Omni (PostgreSQL-compatible) queries, inspecting execution plans, finding missing indexes, spotting table bloat, or monitoring active queries. Do NOT use against production without care on `execute_sql` (it runs arbitrary SQL), and do NOT treat estimated cardinality as exact (run ANALYZE first). Requires pg_stat_statements for query stats.

## Inputs, outputs, tools
- Inputs: SQL statements, schema/table/column names, filters (min duration, application names, limits, sort fields), connection via .env.
- Outputs: JSON/text query results and EXPLAIN plans.
- Tools: Node.js scripts under the skill's `scripts/` folder; environment variables loaded from .env files. No MCP.

## 5 most important rules
1. **Run ANALYZE on a table before cardinality estimates** or results are stale.
2. **`get_query_plan` does not execute the query** (safe for production plan inspection); `execute_sql` does execute arbitrary SQL.
3. **Query stats require pg_stat_statements** installed/enabled or the call fails.
4. **Table stats surface index effectiveness** via `idx_scan_ratio_percent` and bloat via `dead_row_ratio_percent`; low index ratio signals missing/ineffective indexes.
5. **Scripts auto-load .env**; only ask the user for env vars if execution fails due to missing variables.

## Risks / owner notes
`execute_sql` can mutate data if given DML/DDL; treat as privileged. Connection credentials live in .env (do not commit). Results depend on stats freshness. Owner must confirm target instance, credentials, and that pg_stat_statements is enabled before relying on query stats. Apache-2.0 licensed.

## Category / tags
data · alloydb, postgresql, performance, query-plan, monitoring, google

## Revisions
Single source (gemini). No other tool ships this skill, so no revision comparison.