# bigquery-observability

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\bigquery-observability\SKILL.md`
- SKILL.md size: 12656 chars

## What it does

Provides data-retrieval best practices, tool selection guidance, and performant SQL query syntax for BigQuery telemetry across INFORMATION_SCHEMA, Cloud Monitoring, and the REST API. Use when the telemetry to fetch is already known, selecting telemetry tools, writing performant INFORMATION_SCHEMA queries, retrieving telemetry for diagnosing single-job performance bottlenecks, investigating slot contention, job concurrency and queue latency, analyzing reservation capacity, utilization and autoscaling saturation, or auditing capacity-based and on-demand compute and storage resource billable usage. Don't use for root-cause diagnosis or symptom troubleshooting when the cause is unknown (use bigquery-troubleshooting first), or for writing or optimizing business logic SQL (use bigquery-optimization).

## Structure (headings inside SKILL.md)

- BigQuery Observability
- Tool Selection
- Workflow
- Best Practices for Writing `INFORMATION_SCHEMA` Queries
- Qualification Syntax & Scope Matching
- Principle of Least Privilege & Scope Selection
- Execution Guardrails & Query Invariants
- Domain References & SQL Queries
- Telemetry Query Guides
- Performance & Troubleshooting Guides
- Schema Dictionaries (Column Definitions & Units)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 3.  **Project-Level over Org/Folder-Level (`_BY_PROJECT`):** Always start with
2. *   **Mandatory Partition & Time Filtering:** Always filter on `creation_time`
3. *   **Column Pruning:** Never use `SELECT *` against `INFORMATION_SCHEMA`; only

## Files inside the skill

- `references/capacity_and_configuration_queries.md` — "Capacity & Configuration Queries"
- `references/compute_capacity_billable.md` — "Billable Capacity Compute (Slots & Commitments)"
- `references/compute_ondemand_billable.md` — "Billable On-Demand Compute (Bytes Billed)"
- `references/job_performance_queries.md` — "Query Performance Queries"
- `references/resource_contention_queries.md` — "Resource Contention Queries"
- `references/schema_compute.md` — "BigQuery Compute & Capacity INFORMATION_SCHEMA Reference"
- `references/schema_others.md` — "BigQuery Platform, Governance & Ingestion INFORMATION_SCHEMA Reference"
- `references/schema_storage.md` — "BigQuery Storage & Catalog INFORMATION_SCHEMA Reference"
- `references/storage_footprints.md` — "Storage: Logical & Physical Pricing (Bytes Stored)"
