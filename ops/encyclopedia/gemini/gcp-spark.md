# gcp-spark

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\gcp-spark\SKILL.md`
- SKILL.md size: 3892 chars

## What it does

| Develops and executes Spark code on Dataproc Clusters and Serverless. Reads and writes data using BigLake Iceberg catalogs, BigQuery and Spanner. Debugs execution failures. Use when: - Writing Spark ETL pipelines on GCP. - Training or running inference with ML models with spark on GCP. - Managing Spark clusters, jobs, batches, and interactive sessions. Don't use when: - Writing generic Python scripts that don't use Spark. - Performing simple SQL queries that can be done directly in BigQuery.

## Structure (headings inside SKILL.md)

- Spark on Dataproc
- Task Execution Workflow
- Common Mistakes Checklist
- IAM Requirements
- Spark resource management
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  **Understand schemas**: **ALWAYS** use `@skill:discovering-gcp-data-assets`
2. *   **Output Format**: **ALWAYS** generate code in **Python Notebooks
3. *   **Read and Write data**: **ALWAYS** Refer to
4. *   **Spark Optimizations**: **ALWAYS** refer to
5. 3.  **Verify schema before write**: **ALWAYS** verify that the dataframe and

## Files inside the skill

- `references/gcloud_dataproc.md` — "Dataproc and Spark Integration"
- `references/ml_tasks.md` — "ML on Dataproc"
- `references/read_write_data.md` — "Definitive Guide to reading and writing tables using spark code"
- `references/schema_direct_inspection.md` — "Direct Inspection of table schema"
- `references/spark_optimizations.md` — "Spark Optimizations"
- `resources/gcloud_dataproc.md` — "Dataproc and Spark Integration"
- `resources/ml_tasks.md` — "ML on Dataproc"
- `resources/read_write_data.md` — "Definitive Guide to reading and writing tables using spark code"
- `resources/schema_direct_inspection.md` — "Direct Inspection of table schema"
- `resources/spark_optimizations.md` — "Spark Optimizations"
