# gcp-spark

## Summary
Spark-on-GCP development skill (v2): writes and executes Spark code on Dataproc clusters and Serverless, reading/writing BigLake Iceberg catalogs, BigQuery and Spanner, and debugging failures. Mandatory Task Execution Workflow: (1) ALWAYS discover schemas first via the `discovering-gcp-data-assets` skill or references/schema_direct_inspection.md — include schema in reasoning BEFORE writing code, never guess column names; (2) generate code as Python NOTEBOOKS (.ipynb) by default (.py only if explicitly requested), consulting read_write_data.md, ml-best-practices/ml_tasks.md for ML, and spark_optimizations.md for optimizations; (3) verify DataFrame schema matches destination (df.printSchema() + destination schema check) before writes; (4) compile before executing — `jupyter nbconvert --to script` then `python3 -m py_compile`; (5) execute .py scripts via gcloud dataproc commands in references/gcloud_dataproc.md (notebooks excluded). Ships a Common Mistakes checklist and the Dataproc service-account IAM requirements.

## When to use / when NOT
Use for Spark ETL pipelines, ML training/inference with Spark, and Dataproc cluster/job/batch/session management on GCP. NOT for generic Python, or simple SQL answerable directly in BigQuery.

## Inputs, outputs, tools
- Inputs: data asset references (BigQuery/Spanner/Iceberg/GCS), schemas discovered via discovering-gcp-data-assets.
- Outputs: .ipynb notebooks (default) or .py scripts, compiled+executed on Dataproc.
- Tools: pyspark, Dataproc (clusters/jobs/batches/sessions), BigLake Iceberg, BigQuery, Spanner, jupyter nbconvert, gcloud, references (read_write_data, spark_optimizations, ml_tasks, gcloud_dataproc, schema_direct_inspection).

## 5 most important rules
1. Schema discovery is step zero and non-negotiable — never guess column names; schemas go into reasoning before codegen.
2. Output format is .ipynb notebooks unless the user explicitly asks for .py — compile path differs (nbconvert→py_compile→dataproc submit only for .py).
3. Always verify df.printSchema() against the destination Iceberg table schema before writing.
4. Common-mistakes gate: all pyspark.sql.functions imports present; `vector_to_array` comes from `pyspark.ml.functions` NOT pyspark.sql.functions; CSV reads need header+inferSchema; avoid toPandas() (OOM risk, only for viz in Spark 3.5).
5. IAM: Dataproc SA needs roles/dataproc.worker, biglake.admin, bigquery.jobUser, storage.objectUser, spanner.databaseUser as applicable.

## Risks / owner needs
Cluster/job execution incurs real GCP cost — resource sizing and cluster lifecycle are owner-visible. IAM roles listed are broad; scope to least privilege where possible.

## Category and tags
Category: data. Tags: spark, dataproc, gcp, etl, iceberg, bigquery, pyspark, notebooks.

## Revisions
Single gemini skill copy (v2); no competing revisions.
