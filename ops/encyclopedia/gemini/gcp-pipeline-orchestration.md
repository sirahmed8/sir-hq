# gcp-pipeline-orchestration

- Tool: `gemini`
- Category: data
- Source: `C:\Users\a7med\.gemini\skills\gcp-pipeline-orchestration\SKILL.md`
- SKILL.md size: 17130 chars

## What it does

This skill helps the agent generate or update orchestration pipeline definitions for Google Cloud Composer to initialize orchestration pipeline or update the orchestration definition for orchestration of various data pipelines, like dbt pipelines, notebooks, Spark jobs, Dataform, Python scripts or inline BigQuery SQL queries. This skill also helps deploy and trigger orchestration pipelines.

## When to use (from skill text)

- ## How to use this skill
- ## How to use this skill
- > auto-run. Use Step 7 to trigger it.

## Structure (headings inside SKILL.md)

- Mandatory Reference Routing
- How to use this skill
- How to use this skill
- Step 1: Assess Orchestration Pipeline Status and Initialize if Necessary
- Replace <ORCHESTRATION_PIPELINE_NAME> with the actual name
- Replace <ENV_NAME> with the actual environment name
- Step 2: Review the orchestration pipeline code structure and syntax instruction
- Step 3: Generate the pipeline files
- Step 4: Validate the content (REQUIRED)
- Replace <ENV_NAME> with the identified environment name
- Step 5: Handle Validation Errors
- Declarative Pipeline Templates
- `deployment.yaml` Template - IMPORTANT FORMAT MUST MATCH-
- Step 6: Deploy the Orchestration Pipeline (Optional)
- Step 7: Trigger the Orchestration Pipeline Run (Optional)
- Definition of done
- Other actions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. -   All files should always be maintained together. And all files should be
2. 2.  **Determine if initialization is required**: Initialization is required if
3. 4.  **Environment Name**: If initialization is needed, you MUST ask the user for
4. -   Before generating, check if an orchestration pipeline definition file and
5. -   First, before creating the orchestration pipeline definition file, you

## Files inside the skill

- `references/orchestration-pipelines-schema.md` — "Pipeline YAML Schema"
- `scripts/trigger/airflow_trigger.py`
