# bigquery-data-transfer-service

**Source:** `C:\Users\a7med\.gemini\skills\bigquery-data-transfer-service\SKILL.md` (+ `scripts/bigquery_dts.py`)
**Category:** data
**Tags:** bigquery, data-transfer-service, dts, ingestion, gcp, deployment-yaml, rest-api

## Summary
A Google skill (metadata version v1, Apache-2.0) for discovering and inspecting BigQuery Data Transfer Service (DTS) configurations. It finds existing ingestion pipelines, extracts datasource and transfer config metadata, and guides the creation of new transfers through the gcp pipeline resource provisioning framework (generating a `deployment.yaml`) rather than imperative CLI commands. It ships a Python discovery script that calls the DTS REST API.

## When to use / when not to
Use it to identify existing ingestion pipelines, extract datasource or transfer config metadata, or when the user asks to "ingest" or "add" data that may already be managed by a DTS transfer. Do not use it to create transfers with `bq mk` or `gcloud` (forbidden) or for non-DTS ingestion.

## Inputs, outputs, tools
Inputs: a GCP project and region, a datasource ID, and a transfer config name. Outputs: discovered transfers, validated parameters, a `deployment.yaml`, and a triggered and monitored transfer run. Tools: `gcloud`, `bq`, `python3 scripts/bigquery_dts.py`, and the gcp pipeline resource provisioning framework. No MCP.

## Five most important rules
1. Provision all new DTS configurations declaratively through the gcp pipeline framework with a `deployment.yaml`; use the CLI only for discovery and manual runs.
2. Check for existing transfers first: reuse a transfer with a successful run, confirm before triggering, and ask before enabling a disabled transfer.
3. Run the discovery script every time a new transfer is planned, identify every required parameter explicitly, and present them all to the user before generating config.
4. For Google data sources using end-user credentials, generate an OAuth URI, use the returned versionInfo code as `definition.versionInfo`, and ask for Secret Manager resource IDs for authentication parameters.
5. Trigger a manual run and poll every 30-60 seconds for up to five minutes; on timeout, stop and ask the user for "proceed guidance".

## Risks and owner actions
Ingestion can be long-running and requires GCP authentication and sometimes OAuth; the user must confirm parameters and ingestion completion. No secrets belong in the generated files.

## Revisions
Only one copy exists (`.gemini/skills/bigquery-data-transfer-service`, 7139 bytes, dated 2026-06-26).
