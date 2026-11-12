# cloud-sql-postgres-monitor

## Summary
Google-published performance-troubleshooting skill for Cloud SQL PostgreSQL. Identical script set to cloud-sql-postgres-health (verified byte-for-byte): PromQL query-level and system-level Cloud Monitoring metrics, EXPLAIN plans, active queries, database stats, lock inspection, pg_stat_statements query stats, and long-running transaction detection.

## When to use / when NOT
Framed for "performance bottlenecks, query plans, resource-heavy processes, PromQL metrics" — use it for "why is Postgres slow" investigations. Because the scripts are the same as the health skill, either works; pick by name semantics. Do NOT use for provisioning, backups, or schema exploration.

## Inputs, outputs, tools
- Inputs: PromQL `query` + projectId/instanceId; `min_duration`, `exclude_application_names`, `limit`, `database_name` filters for inspectors.
- Outputs: time-series metrics, active query details with wait events, lock aggregates, per-query timing/I/O stats, long-transaction report, JSON EXPLAIN.
- Tools: `scripts/{get_query_metrics,get_system_metrics,get_query_plan,list_active_queries,list_database_stats,list_locks,list_query_stats,long_running_transactions}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. get_query_plan is estimate-only (no ANALYZE, no execution) — safe on production, but say "estimated" when reporting.
2. list_query_stats requires pg_stat_statements; if missing, say so instead of reporting zeros.
3. PromQL: aggregate per-query metrics by query_hash, skip querystring unless asked, never use latency metrics, default 5m windows.
4. `resource_id` = `project_id:instance_id`; labels include user, client_addr, io_type/lock_type where relevant.
5. `project` is pre-configured; do not ask for it.

## Risks / things needing the owner
Read-only diagnostics; PromQL consumes monitoring quota. Terminating queries or changing config is out of scope — escalate. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, postgres, monitoring, performance, promql

## Revisions
Body and all 8 scripts are byte-identical to cloud-sql-postgres-health — only the name/description differ (monitor = performance framing). If the two ever diverge, prefer whichever carries the fix; today they are interchangeable. Single copy on gemini.
