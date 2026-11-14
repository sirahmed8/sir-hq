# gcp-spark-observability

- Tool: `gemini-plugin` (plugin: `data-agent-kit-plugin`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\data-agent-kit-plugin\skills.all\gcp-spark-observability\SKILL.md`
- SKILL.md size: 9555 chars

## What it does

Monitors, inventories, and assesses Google Cloud Managed Service for Apache Spark (Dataproc Serverless and Dataproc on Compute Engine) environments, clusters, batches, jobs, sessions, metrics, logs, costs, and configurations across single and multiple regions. Use when listing active or historical Spark workloads, discovering failed batches or jobs, auditing multi-region fleet inventory, calculating Serverless compute (DCU-Hours) and shuffle storage consumption, detecting idle or zombie clusters, inspecting scheduled pipeline cadence health, investigating failed cluster operations or stockouts, checking quotas and alerting coverage, or querying Cloud Monitoring and Cloud Logging telemetry. Don't use for deep root-cause analysis or performance optimization of a specific job or batch (use gcp-spark-troubleshooting), authoring new PySpark code (use gcp-spark), or upgrading Spark versions (use gcp-managed-spark-upgrades).

## When to use (from skill text)

- my last Spark batch fail?"*), use this skill first to find the latest
- *   Handoff: use this skill first to identify top DCU consumers, regressed

## Structure (headings inside SKILL.md)

- Google Cloud Spark & Dataproc Observability
- Skill Routing & Handoff
- Non-Obvious CLI & API Gotchas (Read First)
- Where to Look (Quick Map)

## Tools / MCPs it needs

- MCP mentions: MCP field, MCP list

## Risks / cautions found in text

- *   Never cancel, kill, stop, or delete any workload or cluster without

## Key rules (verbatim lines from SKILL.md)

1. *   `sessions` and `session-templates` require the `beta` track and
2. *   Always pass `--quiet` to `asset`, `metastore`, `composer`, and
3. 3.  **Always specify `--limit` & respect server-side `--filter` restrictions:**
4. *   Always pass an explicit `--limit` (for example `--limit=20` to
5. *   Never cancel, kill, stop, or delete any workload or cluster without

## Files inside the skill

- `references/gcloud_observability_reference.md` — "gcloud Dataproc & Spark Observability Reference"
