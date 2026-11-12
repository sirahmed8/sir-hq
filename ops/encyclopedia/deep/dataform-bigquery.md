# dataform-bigquery (Gemini skill, Google)

## Summary
Expert workflow for Dataform-on-BigQuery ELT pipelines: verify CLI env (dataform/bq/node/npm, `dataform init` if no workflow_settings.yaml, `.df-credentials.json` via init-creds or manual), compile to map the DAG as source of truth, gather schemas/samples via bq for sources AND targets, ALWAYS apply data-autocleaning + bigquery optimization protocols (with mandatory summary sections), plan non-trivial work, write SQLX, validate with `dataform compile` + `dataform run --dry-run` (never a real run without explicit confirmation), plus coding standards — declaration files per source, incremental type for appends, GCS CSV external tables with jagged/quoted-newline options, metadata overview blocks, and a BigLake Iceberg 4-part-naming workaround.

## When to use / when NOT
Use for creating/modifying Dataform pipelines, actions, source declarations, GCS→BigQuery ingestion, or project setup. For dbt projects use dbt-bigquery instead; for standalone SQL use bigquery skill.

## Inputs, outputs, tools
- Inputs: user request, existing SQLX repo, source/destination table specs.
- Outputs: SQLX files (config blocks, declarations, incremental/operations), compiled DAG, implementation_plan.md with Profiling Evidence + Verification Plan.
- Tools: `dataform` CLI (init/compile/run --dry-run), `bq` CLI, gcloud config; sibling skills data-autocleaning, bigquery, discovering-gcp-data-assets.

## 5 most important rules
1. `dataform compile` output is the source of truth for existing assets — never assume.
2. Data cleaning and SQL optimization are mandatory even unrequested; response must include "Automatic Cleaning Summary" and "Optimization Summary" sections.
3. NEVER run real `dataform run` without explicit user confirmation — dry-run only.
4. `type: "incremental"` for ALL appends/copies to existing tables (never "operations"); body = SELECT only, `${ref()}` for sources, SELECT schema must match target.
5. `implementation_plan.md` must contain Profiling Evidence and reference Step 3 quality review; `walkthrough.md` needs Quality Review Profiling Evidence — don't finish without them.

## Risks / things needing the owner
Real pipeline runs materialize/modify BigQuery tables — cost and data impact; credentials file contains project/location (not secrets but config). Dry-run "table not found" for unmaterialized project nodes may be ignored per the documented exception.

## Category / tags
data · dataform, bigquery, elt, sqlx, gcp

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\dataform-bigquery\SKILL.md` (v3, Apache-2.0, google). Only gemini tool holds it.
