# cloud-sql-postgres-health

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-health\SKILL.md`
- SKILL.md size: 27694 chars

## What it does

Use these skills when you need to audit database health, identify storage bloat, find invalid indexes, analyze table statistics, and manage maintenance configurations like autovacuum.

## When to use (from skill text)

- which the metrics timeseries data needs to be fetched. To use this tool, you

## Structure (headings inside SKILL.md)

- Usage
- Scripts
- get_query_metrics
- get_query_plan
- get_system_metrics
- list_active_queries
- list_database_stats
- list_locks
- list_query_stats
- long_running_transactions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  Interval: Use a default interval of `5m` for `_over_time` aggregation
2. 8.  Percentile with groupby on resource_id, database: `quantile by
3. 1.  `cloudsql.googleapis.com/database/postgresql/insights/aggregate/latencies`:

## Files inside the skill

- `scripts/get_query_metrics.js`
- `scripts/get_query_plan.js`
- `scripts/get_system_metrics.js`
- `scripts/list_active_queries.js`
- `scripts/list_database_stats.js`
- `scripts/list_locks.js`
- `scripts/list_query_stats.js`
- `scripts/long_running_transactions.js`
