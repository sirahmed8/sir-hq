# cloud-sql-mysql-monitor

## Summary
Google-published observability skill for Cloud SQL for MySQL. Two families of scripts: live database inspection (active queries from processlist/innodb_trx, table stats, fragmentation, missing unique indexes, query plans) and Cloud Monitoring time-series queries via PromQL for per-query insights (dbinsights aggregate metrics like execution_time keyed by query_hash) and system metrics (CPU, memory, etc.).

## When to use / when NOT
Use for "why is the database slow", "show long-running queries", "which tables are fragmented/unused-indexed", "graph CPU over the last hour". Do NOT use for provisioning (admin) or backups (lifecycle); for raw ad-hoc SQL use cloud-sql-mysql-data.

## Inputs, outputs, tools
- Inputs: PromQL `query` + projectId/instanceId for metrics scripts; `table_schema`, `table_name`, `min_duration_secs`, `limit`, `data_free_threshold_bytes`, `sort_by` for inspection scripts.
- Outputs: JSON query details, schema stats, fragmentation percentages, PromQL time-series results.
- Tools: `scripts/get_query_metrics.js`, `get_system_metrics.js`, `list_active_queries.js`, `list_table_stats.js`, `list_table_fragmentation.js`, `list_tables_missing_unique_indexes.js`, `get_query_plan.js`; Node + JSON params; auto-loads .env.

## 5 most important rules
1. get_query_metrics/get_system_metrics require a hand-built PromQL query — construct it from the documented metric names, labels (`instance_id`, `query_hash`, `database_id` = `project_id:instance_id`) and default 5m `_over_time` windows.
2. list_active_queries merges processlist and innodb_trx to surface transaction wait time, state, rows locked/modified — start triage here.
3. Fragmentation output identifies reclaimable space via OPTER TABLE suggestions — report percentage, don't run OPTIMIZE without asking.
4. `project` is pre-configured; only override if the user names another project.
5. Do not ask about env vars unless a script fails on missing env.

## Risks / things needing the owner
Read-only by design, but PromQL queries hit Cloud Monitoring billing/quotas; OPTIMIZE TABLE on large tables locks/rebuilds — needs owner sign-off. Requires GCP + Cloud SQL credentials.

## Category / tags
cloud · gcp, cloud-sql, mysql, monitoring, performance, promql

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-mysql-monitor\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
