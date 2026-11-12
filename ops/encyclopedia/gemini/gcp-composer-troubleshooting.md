# gcp-composer-troubleshooting

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\gcp-composer-troubleshooting\SKILL.md`
- SKILL.md size: 9089 chars

## What it does

Provides expert guidance for troubleshooting Cloud Composer (Apache Airflow) and Orchestration pipelines. Use this skill when the user asks to generate Root Cause Analysis (RCA), troubleshoot or fix a failed pipeline, DAG in Composer environment and generate RCA report. '

## When to use (from skill text)

- triggers:

## Structure (headings inside SKILL.md)

- Composer Troubleshooting Expert Skill
- Role & Persona
- Task Execution Process
- Important Constraints & Instructions
- Workflows & Scenarios
- 1. Code Consistency Check (CRITICAL)
- 2. Troubleshooting Scenarios
- Example Workflow
- Example Gcloud commands
- Declarative Pipeline Templates
- `deployment.yaml` Template
- `orchestration-pipeline.yaml` Template
- IMPORTANT
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **Safety**: Be careful with secrets. If logs contain sensitive info, redact

## Key rules (verbatim lines from SKILL.md)

1. *   **Do not assume** the local code (if any) matches the remote
2. *   **Do not modify code** at this stage. Your goal is to explain *why* it
3. *   **Read-Only First**: Do NOT attempt to fix the code immediately. You must
4. *   **Mismatch**: You must align on which version to analyze.
5. *   Do not modify the code. Just analyze and provide the RCA report. Unless user

## Files inside the skill

- (SKILL.md only)
