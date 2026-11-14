# alloydb-omni-health

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-health\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A health monitoring skill for AlloyDB Omni clusters that checks database connectivity, query performance, replica lag, storage utilization, and alert metrics. It integrates with Prometheus and Grafana to provide dashboards for CPU, memory, connection count, and long-running query detection. The skill can also auto-terminate stuck transactions and generate health reports on demand.

## When to use / when NOT
Use for ongoing production monitoring of AlloyDB Omni clusters — schedule it to run every 5 minutes via a cron job or Kubernetes cronjob. Do NOT ignore health alert recommendations; the skill prioritizes alerts by severity (critical, warning, info) and each should be addressed. Do NOT run health checks during planned maintenance windows without first disabling alerts, otherwise the skill will generate false-positive alerts that require manual suppression.

## Inputs, outputs, tools
- Inputs: cluster connection string, Prometheus/Grafana endpoint URLs, alert threshold values (connection count, query time, replica lag), check interval.
- Outputs: health status (healthy/degraded/critical), metrics data (CPU, memory, connections, replica lag), alert list with severity, recommended actions.
- Tools: `psql` for connectivity check, `pg_stat_activity` for query monitoring, `kubectl get pods` for pod status, Prometheus API, Grafana dashboard URLs. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always set replica lag alerts** — if replication lag exceeds 5 seconds, it indicates a performance or network issue that should be investigated.
2. **Monitor long-running queries** — any query running longer than 30 seconds should be logged and reviewed; the skill can automatically kill queries that exceed 5 minutes.
3. **Track connection count trends** — a steady increase in connections may indicate a connection leak in the application; set alerts at 80% of max_connections.
4. **Enable storage autoscaling warnings** — if disk utilization exceeds 80%, the skill will flag it as a warning and recommend increasing the PVC size.
5. **Run a full health check after any schema change** — adding indexes, altering tables, or changing column types can temporarily degrade performance.

## Risks / owner notes
Ignoring health alerts can lead to cluster outages or performance degradation that is difficult to diagnose later. The owner should ensure that alert recipients are paged for critical alerts and email-ed for warnings. Storage full conditions are a common cause of AlloyDB outages; automate PVC resizing or set up notifications before hitting 80% utilization.

## Category / tags
database · monitoring, health-check, alloydb, postgres, observability, prometheus, grafana

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.