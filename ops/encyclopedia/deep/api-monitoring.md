# api-monitoring

Source read: `C:\Users\a7med\.gemini\config\plugins\postman\skills\api-monitoring\SKILL.md` (gemini-plugin revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An API monitoring skill that continuously watches REST API health, latency, and error rates. It integrates with Prometheus and Grafana to provide dashboards, and can alert on SLA violations, latency spikes, or error rate increases. The skill supports synthetic heartbeat pings, endpoint availability checks, and can correlate metrics with deployment events to identify if a recent release caused performance degradation.

## When to use / when NOT
Use when you need to monitor production API health and SLA compliance. Do NOT rely on a single health check endpoint — the skill monitors multiple endpoints and requires at least 2 of 3 to be healthy to report the API as "up". Do NOT disable alert rules during deployments without a rollback plan; the skill will flag if error rates spike after a deployment and can automatically suggest a rollback.

## Inputs, outputs, tools
- Inputs: API base URL, health check endpoints, alert thresholds (latency, error rate), notification channels (Slack, email, PagerDuty), monitoring interval.
- Outputs: dashboard URLs (Prometheus/Grafana), alert rule configuration, health status (up/down/degraded), correlation events (deployment timestamps).
- Tools: Prometheus, Grafana, Healthchecks.io, PagerDuty integration, curl. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always monitor at least 3 key endpoints** — the skill reports the API as "up" only if at least 2 of 3 health checks pass; never rely on a single endpoint.
2. **Set latency alerts at the 95th percentile** — the skill tracks response time percentiles; alert if p95 exceeds your SLA threshold.
3. **Configure error rate alerts at 1%** — if more than 1% of requests return 4xx or 5xx, the skill will generate a warning and trend the data.
4. **Correlate alerts with deployment events** — the skill can integrate with your CI/CD system; when a deployment occurs, it marks the event on the timeline for root-cause analysis.
5. **Review alert trends weekly** — the skill accumulates historical data; the owner should review weekly to distinguish transient spikes from sustained issues.

## Risks / owner notes
Alert fatigue is a common problem; if too many thresholds are triggered, the team begins ignoring all alerts. The owner should start with conservative thresholds and tighten them over time as the team learns the normal operating range. Correlating alerts with deployments requires proper integration; if the CI/CD system is not configured to send deployment events, this feature will not work.

## Category / tags
api · monitoring, observability, health-checks, alerting, prometheus, grafana, sla

## Revisions
The gemini-plugin copy is the only revision available; no codex, claude, or kilo versions exist. This is the canonical source for this skill.