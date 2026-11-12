# federate-lakehouse-catalog

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\federate-lakehouse-catalog\SKILL.md`
- SKILL.md size: 10330 chars

## What it does

Sets up Google Cloud Lakehouse federated catalogs to remote Iceberg REST Catalogs. Currently supported catalogs: Databricks Unity, AWS Glue. Supported clouds hosting those catalogs: GCP, AWS. The primary use case is connecting to remote data to query it from GCP engines (BigQuery, Spark). Examples of when to use this: "federate my lakehouse catalog to databricks", "query data in databricks", "query data in s3", "connect to aws glue". Do NOT use for direct remote database SQL execution (e.g., Databricks SQL) or managing remote clusters and infrastructure (e.g., Databricks clusters, AWS Glue jobs).'

## Structure (headings inside SKILL.md)

- Federate Lakehouse Catalog via Cross-cloud Lakehouse
- Prerequisites
- Procedure
- Step 1: Information Gathering and Region Selection
- Step 2: API Verification
- Flow A: Databricks Unity Catalog
- Flow B: AWS Glue
- Querying the Data
- Gotchas and Pitfalls
- Step 3: Validation and Next Steps
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   For AWS Glue: AWS Administrator access to create IAM roles and permissions
- 1.  Create a JSON file named `credentials.json`:
- 1.  Set the Secret Manager API endpoint override for the region:
- 1.  Create the secret:

## Key rules (verbatim lines from SKILL.md)

1. -   For Databricks: Databricks Workspace URL and OAuth Service Principal (Client
2. -   For AWS Glue: AWS Administrator access to create IAM roles and permissions
3. -   Active Google Cloud project with administrative access to create lakehouse

## Files inside the skill

- (SKILL.md only)
