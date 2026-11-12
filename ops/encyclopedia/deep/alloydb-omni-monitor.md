# alloydb-omni-monitor

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-monitor\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A monitoring skill for AlloyDB Omni that sets up time-series collection, alerting, and dashboards for database metrics. It integrates with Prometheus to scrape `pg_exporter` metrics and with Grafana to visualize query performance, connection usage, replication lag, and storage trends. The skill can also configure alert rules that page on-call engineers when metrics breach thresholds.

## When to use / when NOT
Use when setting up observability for a new AlloyDB Omni deployment or migrating an existing monitoring stack to AlloyDB-native metrics. Do NOT disable the default alert rules — they catch common issues like connection spikes, replica lag, and disk full conditions that are easy to miss in dashboards. Do NOT rely on application-level logging alone; the skill provides database-native metrics that application logs cannot expose.

## Inputs, outputs, tools
- Inputs: AlloyDB connection string, Prometheus scrape config, Grafana dashboard definitions, alert notification channels (Slack, email, PagerDuty).
- Outputs: Prometheus scrape config, Grafana dashboards (query performance, connection stats, replica lag), alert rules with severity levels, metrics export confirmation.
- Tools: `pg_exporter`, `prometheus`, `grafana`, `alloydb-diagnostics` CLI, `kubectl get prompts`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always scrape `pg_exporter` metrics** — these provide the most detailed database-level metrics (query timing, lock wait, transaction stats) that are essential for capacity planning.
2. **Configure a replica lag alert at 5 seconds** — replication lag beyond this threshold can indicate network issues or a lagging replica that should be promoted to primary.
3. **Set a disk usage alert at 80%** — when storage reaches 80%, the skill will trigger a warning; at 95%, it will generate a critical alert and page on-call.
4. **Include query duration percentiles in dashboards** — p95 and p99 query times help identify slow queries before they impact users.
5. **Export alert history for 90 days** — the skill can store alert events in a time-series database; this data is invaluable for root-cause analysis of intermittent issues.

## Risks / owner notes
The most common monitoring gap is not configuring alert notification channels; alerts are generated but never seen by the team. The owner should ensure that critical alerts are paged and that on-call rotations are properly configured. Scraping too frequently (less than 15 seconds) can increase database load; the skill defaults to 60-second intervals, which can be adjusted based on your environment.

## Category / tags
database · monitoring, observability, alloydb, postgres, prometheus, grafana, metrics

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.