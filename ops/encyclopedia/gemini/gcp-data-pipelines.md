# gcp-data-pipelines

## Summary
gcp-data-pipelines is the primary Google-published entry point skill for building, managing, and orchestrating data pipelines on Google Cloud. It acts as a router: first scans the workspace for existing pipeline indicators (dbt_project.yml, workflow_settings.yaml, deployment.yaml, .py with apache_beam, .ipynb with pyspark, etc.), then if an unambiguous match exists and the request fits, it proceeds directly with that pipeline's specialized skill. If no pipeline or ambiguous, it presents a structured menu of GCP pipeline tools grouped by Data Pipeline Tools (BigQuery DTS, dbt, Dataflow, Dataform, Spark/Dataproc Serverless) and Deployment & Orchestration (Cloud Composer Orchestration, Provisioning), then stops and waits for user selection before activating the corresponding sub-skill.

## When to use / when NOT
Use as the first stop when a user wants to create, update, run, or orchestrate data pipelines on GCP and hasn't specified a tool. Do NOT use if the user already named a specific tool (go directly to that skill), if the workspace has an unambiguous existing pipeline matching the request (route directly to that skill), or for general GCP assistance unrelated to data pipelines.

## Inputs, outputs, tools
- Inputs: User request (may be vague or specific), workspace contents (scanned for pipeline indicators).
- Outputs: Tool recommendation with comparison table, or direct delegation to sub-skill after user confirms.
- Tools: Workspace file scanning (grep/ls), `gcloud` for resource discovery if needed. No scripts/references in skill folder.

## 5 most important rules
1. Always scan workspace first for existing pipeline indicators (table in SKILL.md lists 7 framework indicators).
2. If unambiguous match found and request fits, proceed directly to that skill — do not re-ask.
3. If multiple pipelines present and request ambiguous, ask user which to target.
4. If no pipeline found and no tool hints, present the structured options table (Data Pipeline Tools + Deployment/Orchestration) and MUST stop for user confirmation.
5. For "run" requests, clarify scope (which components) and method (local vs orchestrate/deploy) before acting.

## Risks / things needing the owner
User must confirm tool choice; agent cannot proceed without selection. Workspace scanning may miss obscure indicators; user may need to clarify. No owner-only steps (no secrets, payments, identity).

## Category / tags
cloud · gcp, data-pipelines, router, dbt, dataflow, dataform, spark, composer, orchestration, provisioning

## Revisions
Single revision in `C:\Users\a7med\.gemini\skills\gcp-data-pipelines\SKILL.md` (Google-published, Apache-2.0, v1). Only gemini has this skill; no divergent copies.