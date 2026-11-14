# bigquery-optimization

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\bigquery-optimization\SKILL.md`
- SKILL.md size: 7041 chars

## What it does

>- Provides workflows to optimize BigQuery environments (capacity planning, editions), storage assets (partitioning, clustering, storage lifecycles, billing models), and SQL queries. Use when optimizing cost, modeling Edition migrations, rightsizing reservations, evaluating logical vs. physical storage, designing table partitioning/clustering, generating table DDL, migrating unpartitioned tables, managing partition expiration, optimizing individual SQL queries, or evaluating acceleration structures (search indexes, materialized views, BI Engine). Do not use for raw usage reporting (use bigquery-observability), query execution plan analysis, error troubleshooting, or diagnosing why a specific job was slow (use bigquery-troubleshooting).

## Structure (headings inside SKILL.md)

- BigQuery Optimization Workflow
- Workflows
- Execution Guardrails
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **Table & Storage Optimization:** Optimize storage costs from a billing
- *   *Billing Architecture:* Read `references/storage_billing_models.md` for

## Key rules (verbatim lines from SKILL.md)

1. -   **Terminology & Cost Framing:** Never promise or guarantee "cost-reduction"
2. -   **Explicit Scope Framing & Region Resolution:** Always state the target
3. -   **No Autonomous Purchasing or Financial Mutations:** Never provide the user

## Files inside the skill

- `references/bi_engine.md` — "BI Engine Acceleration Strategy"
- `references/capacity_planning_editions.md` — "Compute Capacity Planning (Editions Migration & Rightsizing)"
- `references/materialized_views.md` — "Materialized Views"
- `references/search_indexes.md` — "Search Indexes"
- `references/sql_optimization.md` — "BigQuery SQL Optimization"
- `references/storage_billing_models.md` — "Storage Billing Models: Logical vs. Physical Optimization"
- `references/storage_lifecycle_management.md` — "Storage Lifecycle Management (Retention & TTL Optimization)"
- `references/table_partitioning_clustering.md` — "Table Partitioning & Clustering Strategy"
