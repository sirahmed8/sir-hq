# cloud-sql-sqlserver-monitor

## Summary
Google-published observability skill for Cloud SQL SQL Server with a single script, `get_system_metrics`: fetch Cloud Monitoring time-series via a hand-written PromQL query. The documented metric catalog covers CPU/memory/disk/network plus SQL-Server-specific signals — buffer cache hit ratio, pending memory grants, free-list stalls, and swap in/out counts.

## When to use / when NOT
Use for "graph CPU/memory/disk", "is the buffer cache healthy", "are queries waiting on memory grants". There is NO query-level insights, active-query, or lock-inspection script here (unlike the Postgres monitor) — for slow-query diagnosis on SQL Server this skill alone is insufficient. Do NOT use for admin/lifecycle/data tasks.

## Inputs, outputs, tools
- Inputs: `projectId`, `instanceId`, and a PromQL `query` built from the documented `cloudsql.googleapis.com/database/...` metrics; `database_id` label format is `project_id:instance_id`.
- Outputs: time-series metric results.
- Tools: `scripts/get_system_metrics.js` only; Node + JSON; auto-loads .env; default 5m `_over_time` windows.

## 5 most important rules
1. You must construct the PromQL yourself from the metric list — the skill supplies names, descriptions, monitored resource (`cloudsql_database`) and labels.
2. Use `database_id` = `project_id:instance_id` in selectors.
3. Default to 5m aggregation windows for `_over_time` functions unless told otherwise.
4. `project` is pre-configured; never ask unless the user names another.
5. Do not ask about env vars unless a script fails on missing env.

## Risks / things needing the owner
Read-only; PromQL queries consume Cloud Monitoring quota. Memory-grant/lock findings may need DBA action — escalate. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, sqlserver, monitoring, promql

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-sqlserver-monitor\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
