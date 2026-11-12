# federate-lakehouse-catalog

## Summary
A Google-authored runbook for federating a BigQuery Lakehouse catalog to a remote Apache Iceberg REST catalog — currently Databricks Unity Catalog or AWS Glue Data Catalog — so GCP engines (BigQuery, Spark) can query data that lives in AWS or Databricks over the public internet. It is a strict sequential procedure: gather region/credentials, verify the biglake API, then follow Flow A (Databricks: regional Secret Manager secret + federated catalog + service-account IAM binding) or Flow B (AWS Glue: placeholder-trust IAM role, permissions policy, catalog creation, trust-policy update, then enable refresh).

## When to use / when NOT
Use for "federate my lakehouse catalog to databricks", "query data in s3/glue", "connect to aws glue". Do NOT use for direct remote SQL execution (e.g. Databricks SQL warehouses) or for managing the remote clusters/jobs themselves — this skill only wires metadata federation and querying from GCP.

## Inputs, outputs, tools
- Inputs (must be collected first, Step 1): target catalog type, AWS region of data, chosen GCP region per the latency pairing table, and credentials (Databricks workspace URL + OAuth service principal client id/secret, or AWS account ID + admin access).
- Outputs: a `federated` BigLake Iceberg catalog queryable as `<project>.<catalog>.<namespace>.<table>` in BigQuery; validation via `bq ls --location=<region>`.
- Tools: `gcloud alpha biglake iceberg catalogs create/describe/update`, `gcloud secrets` (Secret Manager with regional endpoint override), `aws iam` CLI, `bq` CLI, BigQuery SQL. No MCP.

## 5 most important rules
1. Collect all info and confirm region choice BEFORE any command; enable `biglake.googleapis.com` only after explicit user permission.
2. Secret and catalog MUST be in the same GCP region; pick paired regions (us-east-1↔us-east4, eu-central-1↔europe-west3, etc.) and run BigQuery queries with matching `--location`.
3. Databricks: store `{client_id, client_secret}` JSON as a regional secret, grant the catalog's `biglake-service-account-id` `roles/secretmanager.secretAccessor`.
4. AWS Glue: `--glue-warehouse` takes the 12-digit AWS account ID (not an S3 URI); create the catalog WITHOUT refresh interval, then update the IAM trust policy `aud`/`sub` with the real service-account ID, and only then set `--refresh-interval`.
5. Never apply wildcard IAM resources blindly — scope Glue/S3 ARNs to the user's specific catalog, databases and buckets.

## Risks / owner needs
Real cloud mutations: enabling APIs, creating secrets, IAM roles/policies, catalogs — all need an active GCP project with admin rights and AWS admin credentials; costs apply. Credential JSON files must be handled carefully (never committed). Validation and a proposed analytical question are mandatory closing steps.

## Category and tags
Category: cloud. Tags: gcp, bigquery, biglake, iceberg, databricks, aws-glue, federation, data-engineering.

## Revisions
Single gemini-tool copy only; no competing revisions in this slice.
