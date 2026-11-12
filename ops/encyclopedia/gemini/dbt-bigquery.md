# dbt-bigquery (Gemini skill, Google)

## Summary
Expert workflow for dbt-on-BigQuery ELT: verify env (dbt/bq CLIs, Python env via managing-python-dependencies for dbt-bigquery install, gcloud project), locate `dbt_project.yml` (compile to map the DAG as truth), gather schema+samples via bq for sources AND destinations (use discovering-gcp-data-assets for missing IDs, confirm with user), ALWAYS apply data-autocleaning protocol + bigquery optimization protocol with mandatory "Automatic Cleaning Summary"/"Optimization Summary" sections (or strong evidence why not), ensure profiles.yml exists, implement, validate via `dbt compile`/`dbt run` (dry-run/build), iterate.

## When to use / when NOT
Use for creating, modifying, or troubleshooting dbt models/pipelines, optimizing SQL in a dbt project, or project setup. For Dataform use dataform-bigquery; for ad-hoc SQL use bigquery.

## Inputs, outputs, tools
- Inputs: dbt project, source/target table specs, user request.
- Outputs: model/config changes, compiled DAG, cleaning+optimization summaries.
- Tools: `dbt` CLI (compile/run/test), `bq` CLI, gcloud config; sibling skills data-autocleaning, bigquery, discovering-gcp-data-assets, managing-python-dependencies.

## 5 most important rules
1. `dbt compile` output is the source of truth for existing assets.
2. Data cleaning + SQL optimization are mandatory even unrequested — document with the two summary sections or strong counter-evidence.
3. Verify `profiles.yml` exists in the project working directory before running.
4. Fetch schema AND sample data from both sources and destinations before writing models.
5. Ambiguous/missing asset IDs → discovering-gcp-data-assets, and ASK the user when multiple candidates exist.

## Risks / things needing the owner
`dbt run`/`dbt build` materialize real BigQuery tables (cost + data mutation) — confirm before executing against prod datasets. Python env setup for dbt-bigquery installs packages.

## Category / tags
data · dbt, bigquery, elt, sql, gcp

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\dbt-bigquery\SKILL.md` (v3, Apache-2.0, google). Only gemini tool holds it.
