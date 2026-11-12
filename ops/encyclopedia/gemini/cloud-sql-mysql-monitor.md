# cloud-sql-mysql-monitor

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\cloud-sql-mysql-monitor\SKILL.md`
- SKILL.md size: 24466 chars

## What it does

Use these skills when you need to troubleshoot slow queries, analyze system-level PromQL metrics, and identify structural performance issues like table fragmentation or missing unique indexes.

## When to use (from skill text)

- which the metrics timeseries data needs to be fetched. To use this skill, you

## Structure (headings inside SKILL.md)

- Usage
- Scripts
- get_query_metrics
- get_query_plan
- get_system_metrics
- list_active_queries
- list_table_fragmentation
- list_table_stats
- list_tables_missing_unique_indexes
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  Interval: Use a default interval of `5m` for `_over_time` aggregation
2. 8.  Percentile with groupby on resource_id, database: `quantile by
3. 1.  `dbinsights.googleapis.com/aggregate/latencies`: Cumulative query latency

## Files inside the skill

- `scripts/get_query_metrics.js`
- `scripts/get_query_plan.js`
- `scripts/get_system_metrics.js`
- `scripts/list_active_queries.js`
- `scripts/list_tables_missing_unique_indexes.js`
- `scripts/list_table_fragmentation.js`
- `scripts/list_table_stats.js`
