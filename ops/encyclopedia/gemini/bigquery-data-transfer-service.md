# bigquery-data-transfer-service

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\bigquery-data-transfer-service\SKILL.md`
- SKILL.md size: 7139 chars

## What it does

Discovers and inspects BigQuery Data Transfer Service (DTS) configurations. Use this to identify existing ingestion pipelines and extract datasource or transfer config metadata for data pipelines. Use when a user asks for ingestion scenarios while building or managing data pipelines or when a user asks to "ingest" or "add" data that may already be managed by a DTS transfer.

## When to use (from skill text)

- >     triggering manual runs.
- -   If not found: Confirm with user if it's ok to trigger the transfer
- ### Step 4: Trigger and Verify Transfer

## Structure (headings inside SKILL.md)

- BigQuery Data Transfer Service (DTS)
- Mandatory Guidelines
- Workflow
- Step 0: Discover Environment Parameters
- Step 1: Check for Existing Transfers
- Step 2: Discover & Validate Parameters (New Transfers)
- Step 3: Extract Transfer Config Data
- Step 4: Trigger and Verify Transfer
- Definition of Done
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   Present every required parameter to the user BEFORE generating config
2. 3.  **Wait for User Response**: You **MUST NOT** proceed until parameters are
3. -   **Timeout (5 mins)**: If the run is still in progress after 5 minutes,
4. 3.  **Wait for User Guidance**: Do NOT proceed until the user confirms ingestion

## Files inside the skill

- `scripts/bigquery_dts.py`
