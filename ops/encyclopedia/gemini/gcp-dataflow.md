# gcp-dataflow

- Tool: `gemini`
- Category: design
- Source: `C:\Users\a7med\.gemini\skills\gcp-dataflow\SKILL.md`
- SKILL.md size: 21343 chars

## What it does

| Guides writing, packaging, executing, and troubleshooting Apache Beam pipelines on Dataflow. Use when creating new pipelines, configuring Flex Templates, or analyzing performance of Dataflow jobs. Capabilities include Java/Python/Go setup, Cloud Build integration, and deep diagnostic analysis of job health and autoscaling. Use when: - Creating an Apache Beam Dataflow pipeline. - Creating a Google Dataflow Flex Template. - Using an existing Google Dataflow Template. - Debugging Dataflow pipeline - Troubleshooting Dataflow pipeline - Analyzing Performance of Dataflow pipeline. Key capabilities: Java/Python/Go project setup, Flex Templates (with Cloud Build), and diagnostics for streaming job health, bottlenecks, and autoscaling. Do NOT use for: - General GCP resource management unrelated to Dataflow. - Issues with other GCP services (e.g., GCE, GCS, BigQuery) unless directly impacting Dataflow pipeline execution. - Pipeline technologies other than Apache Beam on Dataflow.

## When to use (from skill text)

- Use this section when implementing Dataflow pipeline logic using Apache Beam.
- Use this section when creating a new project for a Dataflow pipeline from
- Use this section when configuring a Dataflow Java pipeline project using gradle.

## Structure (headings inside SKILL.md)

- Apache Beam Pipelines on Cloud Dataflow
- Pipeline authoring
- Check if existing Google Dataflow Template exists
- Create a new pipeline from scratch
- Java projects using Gradle
- Packaging a pipeline as a Flex Template
- Configuring Google-provided templates
- Destination-specific prerequisites
- Configuring Custom Pipelines (Dataflow Runner)
- Lookup environment resources instead of using placeholder values
- Job Execution
- Universal Execution Workflow
- Job Monitoring
- Diagnostics & Troubleshooting
- Task Execution Workflow
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- -   **Providing SSL certificates and Secrets to Workers**:
- -   If certificates or keys are stored in Secret Manager, **NEVER** bake
- *   **Parameter-Based SSL / Secret Staging**: If the Google-provided
- *   If it does not exist, ask for permission to create it. If permitted,

## Key rules (verbatim lines from SKILL.md)

1. -   YOU MUST use same version of Apache Beam consistently throughout the project
2. -   **Shadow Jars (Fat Jars)**: Do NOT propose to use the Shadow plugin
3. -   You MUST configure the application logging backend (`slf4j-simple`,
4. -   Do NOT assume local Docker availability on the workspace machine.
5. -   When building images with Cloud Build in the background you MUST provide

## Files inside the skill

- `references/bottlenecks_and_parallelism_context.md` — "Bottlenecks and Parallelism Context"
- `references/dataflow_diagnostics_reference.md` — "Dataflow Diagnostics Reference"
- `references/dataflow_metrics_bigquery.md` — ""
- `references/dataflow_metrics_core_job.md` — "Core Job Metrics"
- `references/dataflow_metrics_pubsub.md` — ""
- `references/dataflow_metrics_streaming_engine.md` — ""
- `references/python_flex_template_reference.md` — "Dataflow Flex Template - Single Docker Image Configuration"
- `references/streaming_horizontal_autoscaling_analysis.md` — "Dataflow Streaming Horizontal Autoscaling Analysis"
- `references/streaming_job_health.md` — "Streaming Job Health Analysis"
- `resources/dataflow_diagnostics_reference.md` — "Dataflow Diagnostics Reference"
- `resources/dataflow_metrics_bigquery.md` — ""
- `resources/dataflow_metrics_core_job.md` — "Core Job Metrics"
- `resources/dataflow_metrics_pubsub.md` — ""
- `resources/dataflow_metrics_streaming_engine.md` — ""
- `resources/python_flex_template_reference.md` — "Dataflow Flex Template - Single Docker Image Configuration"
