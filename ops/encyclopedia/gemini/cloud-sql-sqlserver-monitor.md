# cloud-sql-sqlserver-monitor

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\cloud-sql-sqlserver-monitor\SKILL.md`
- SKILL.md size: 10171 chars

## What it does

Use these skills when you need to troubleshoot slow queries and analyze system-level PromQL metrics.

## When to use (from skill text)

- which the metrics timeseries data needs to be fetched. To use this tool, you

## Structure (headings inside SKILL.md)

- Usage
- Scripts
- get_system_metrics
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  Interval: Use a default interval of `5m` for `_over_time` aggregation
2. 8.  Percentile with groupby on database_id: `quantile by
3. 1.  `cloudsql.googleapis.com/database/cpu/utilization`: Current CPU utilization

## Files inside the skill

- `scripts/get_system_metrics.js`
