# alloydb-postgres-monitor

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\alloydb-postgres-monitor\SKILL.md`
- SKILL.md size: 22831 chars

## What it does

Use these skills when you need to troubleshoot slow performance, analyze query execution plans, identify resource-heavy processes, and monitor system-level PromQL metrics.

## When to use (from skill text)

- To use this tool, you must provide the Google Cloud `projectId` and a PromQL `query`.
- To use this tool, you must provide the Google Cloud `projectId` and a PromQL `query`.

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

- 13. `alloydb.googleapis.com/database/postgresql/deleted_tuples_count_for_top_databases`: The total  number of rows deleted per db for top 500 dbs as a result of the queries in the instance. `alloydb.googleapis.com/Database`. `cluster_id`, `instance_id`, `database`.
- 24. `alloydb.googleapis.com/instance/postgresql/deleted_tuples_count`: Number of rows deleted while processing the queries in the instance since the last sample. `alloydb.googleapis.com/Instance`. `cluster_id`, `instance_id`.

## Key rules (verbatim lines from SKILL.md)

1. 1. Interval: Use a default interval of `5m` for `_over_time` aggregation functions unless a different window is specified by the user.
2. 1. Basic Time Series: `avg_over_time({"__name__"="alloydb.googleapis.com/instance/cpu/average_utilization","monitored_resource"="alloydb.googleapis.com/Instance","instance_id"="alloydb-instance"}[5m])`
3. 2. Top K: `topk(30, avg_over_time({"__name__"="alloydb.googleapis.com/instance/cpu/average_utilization","monitored_resource"="alloydb.googleapis.com/Instance","instance_id"="alloydb-instance"}[5m]))`

## Files inside the skill

- `scripts/get_query_metrics.js`
- `scripts/get_query_plan.js`
- `scripts/get_system_metrics.js`
- `scripts/list_active_queries.js`
- `scripts/list_database_stats.js`
- `scripts/list_locks.js`
- `scripts/list_query_stats.js`
- `scripts/long_running_transactions.js`
