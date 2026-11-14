# gcp-managed-airflow-recommendations

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\gcp-managed-airflow-recommendations\SKILL.md`
- SKILL.md size: 6388 chars

## What it does

Provides recommendations and best practices for creating, configuring, tuning and optimizing Managed Service for Apache Airflow (MSAA, Cloud Composer) environments. Use when the user asks for guidance, recommendations, or best practices on configuring Cloud Composer, scaling Airflow environments, preventing workload restarts, or analyzing system health.

## When to use (from skill text)

- Async operators) and the Triggerer component to run long-waiting tasks (like

## Structure (headings inside SKILL.md)

- Managed Service for Apache Airflow (Cloud Composer) Recommendations
- Role & Persona
- Available Resources
- Task Execution Process
- Airflow Best Practices (General Knowledge)
- Important Constraints & Instructions
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **Production Best Practises**: Recommendations around features like

## Key rules (verbatim lines from SKILL.md)

1. *   **Top-Level Code**: DAG files should NEVER contain heavy processing,
2. *   **Evidence-Based Decisions**: Do not blindly recommend increasing machine

## Files inside the skill

- `references/gcloud_reference.md` — "gcloud reference"
- `scripts/dag_parsing_stats.py`
- `scripts/environment_health.py`
- `scripts/lib/flagutils.py`
- `scripts/lib/monitoring.py`
- `scripts/workload_cpu_usage.py`
- `scripts/workload_disk_usage.py`
- `scripts/workload_memory_usage.py`
- `scripts/workload_restarts.py`
