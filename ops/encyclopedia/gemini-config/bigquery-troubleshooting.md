# bigquery-troubleshooting

- Tool: `gemini-config`
- Category: design
- Source: `C:\Users\a7med\.gemini\config\skills\bigquery-troubleshooting\SKILL.md`
- SKILL.md size: 8149 chars

## What it does

Provides diagnostic workflows and step-by-step root-cause analysis procedures for actively broken, failing, or slow BigQuery jobs, execution graph and query plan stage bottlenecks, system performance issues, or unexpectedly expensive workloads. Use when interpreting symptoms, isolating bottlenecks, diagnosing cost spikes (on-demand query spend, capacity slot autoscaling, storage growth), execution graph stages or substep variables, identifying root causes, and determining remediation steps. Don't use for writing or optimizing SQL, proactive capacity planning, or storage layout design (use bigquery-optimization), or when the user already knows which telemetry they want and just needs the query (use bigquery-observability).

## When to use (from skill text)

- reductions triggering autoscale surges (`RESERVATION_BASELINE_CHANGED`),

## Structure (headings inside SKILL.md)

- BigQuery Troubleshooting
- Workflow
- Performance Context: The Relativity of "Slow"
- Cost Context: The 4-Step Diagnostic Funnel
- Domain References
- Performance Troubleshooting
- Cost Troubleshooting
- Routing Boundaries

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  **Scope & Symptom Identification:** Identify the primary symptom, target
2. 2.  **Telemetry Tool Selection:** Follow the tool-selection guidance in the
3. 3.  **Open-Ended Triage (Stage 1 Baseline Scan & Conversational Gate):** When

## Files inside the skill

- `OWNERS`
- `references/cost_compute_capacity.md` — "BigQuery Troubleshooting: Capacity (Editions) Cost & Slot Allocation"
- `references/cost_compute_ondemand.md` — "BigQuery Troubleshooting: On-Demand Compute Spend & Query Scans"
- `references/cost_storage.md` — "BigQuery Troubleshooting: Storage Footprint & Billing Models"
- `references/performance_config_changed.md` — "BigQuery Troubleshooting: Performance & Configuration Changes"
- `references/performance_resource_contention.md` — "BigQuery Troubleshooting: Resource Contention & Performance Slowness"
- `references/query_plan_execution_graph.md` — "BigQuery Troubleshooting: Execution Graph & Query Plan"
