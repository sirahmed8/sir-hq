# cloud-sql-postgres-health

## Summary
Google-published "database health audit" skill for Cloud SQL PostgreSQL. In practice its script set is identical to cloud-sql-postgres-monitor: PromQL query/system metrics via Cloud Monitoring, pg_stat_activity active queries, pg_locks, pg_stat_statements query stats, long-running transactions, database stats, and a non-executing EXPLAIN plan.

## When to use / when NOT
Use for a broad health check: slow queries, lock contention, bloated stats, connection pressure. The description advertises storage-bloat/invalid-index/autovacuum audits, but the shipped scripts cover activity, locks, query stats and PromQL metrics — verify coverage before promising those specific audits. Do NOT use for provisioning (admin), backups/upgrades (lifecycle), or schema listing (data).

## Inputs, outputs, tools
- Inputs: PromQL `query` + projectId/instanceId; `min_duration`, `exclude_application_names`, `limit`, `database_name`, `include_templates`, `order_by` for the inspectors.
- Outputs: time-series metrics, active query details (pid, waits, duration, SQL), lock lists, per-query timing/buffer stats (requires pg_stat_statements), long-transaction report, JSON EXPLAIN plan.
- Tools: `scripts/{get_query_metrics,get_system_metrics,get_query_plan,list_active_queries,list_database_stats,list_locks,list_query_stats,long_running_transactions}.js`; Node + JSON params; auto-loads .env.

## 5 most important rules
1. get_query_plan returns the optimizer's estimated plan WITHOUT executing — safe for production, but estimates not actuals.
2. list_query_stats needs the pg_stat_statements extension; report its absence rather than empty results.
3. For per-query PromQL metrics aggregate by query_hash and do not fetch querystring unless the user asks; latency metrics are explicitly not to be used.
4. `resource_id` label format is `project_id:instance_id` (effectively the instance id).
5. `project` is pre-configured; never ask unless the user names another.

## Risks / things needing the owner
Read-only, but PromQL queries consume Cloud Monitoring quota. Destructive actions (killing queries, VACUUM/REINDEX) are not in scope — escalate to owner. Requires GCP + DB credentials.

## Category / tags
cloud · gcp, cloud-sql, postgres, monitoring, health, performance

## Revisions
SKILL.md body is byte-identical to cloud-sql-postgres-monitor except name/description frontmatter, and all 8 scripts are byte-identical — only the advertised intent differs. Single revision on gemini: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-health\SKILL.md` (Apache-2.0, publisher google).
