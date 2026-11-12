# alloydb-postgres-monitor

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-monitor\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A PostgreSQL monitoring skill for AlloyDB Omni that sets up query performance tracking, connection monitoring, and replication status checks. It integrates with `pg_exporter` to expose metrics for CPU, memory, query latency, and lock contention. The skill can also configure alert rules for slow query detection, connection spikes, and replication lag, feeding these into the broader AlloyDB Omni monitoring stack.

## When to use / when NOT
Use when setting up PostgreSQL-specific monitoring for an AlloyDB Omni deployment. Do NOT disable the default slow-query alert rules — they catch queries running longer than 2 seconds, which are easy to miss in dashboards. Do NOT rely on application-level logging for query performance — the skill provides database-native metrics that application logs cannot expose.

## Inputs, outputs, tools
- Inputs: AlloyDB connection string, Prometheus scrape config, alert notification channels, slow-query threshold (default 2s).
- Outputs: Prometheus scrape config for pg_exporter, Grafana dashboards (query performance, connection stats, replication lag), alert rules with severity levels, metrics export confirmation.
- Tools: `pg_exporter`, `prometheus`, `grafana`, `psql`, `pg_stat_activity`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always enable pg_exporter metrics** — these provide the most detailed PostgreSQL-level metrics (query timing, lock wait, transaction stats) essential for capacity planning.
2. **Configure a slow-query alert at 2 seconds** — any query exceeding this threshold is logged and tracked; the skill can generate a top-N list of slowest queries.
3. **Set a connection count alert at 80% of max_connections** — a steady increase may indicate a connection leak; the skill will flag this and recommend investigation.
4. **Monitor replication lag if using read replicas** — the skill tracks replica lag and will alert if it exceeds 5 seconds, indicating a potential performance or network issue.
5. **Export alert history for 90 days** — the skill can store alert events in a time-series database; this data is invaluable for root-cause analysis of intermittent issues.

## Risks / owner notes
The most common monitoring gap is not configuring alert notification channels; alerts are generated but never seen by the team. The owner should ensure that critical alerts are paged and that on-call rotations are properly configured. Scraping too frequently (less than 15 seconds) can increase database load; the skill defaults to 60-second intervals, which can be adjusted based on your environment.

## Category / tags
database · monitoring, observability, postgres, alloydb, prometheus, grafana, metrics

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.