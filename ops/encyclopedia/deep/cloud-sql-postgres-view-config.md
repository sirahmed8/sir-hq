# cloud-sql-postgres-view-config

## Summary
Google-published read-only inspection skill for Cloud SQL PostgreSQL configuration: server overview (version, replica status, uptime, connection usage), instance details, available vs installed extensions with versions/schemas, memory-related pg_settings, and general pg_settings lookup.

## When to use / when NOT
Use for "which extensions can I install", "is pg_stat_statements/vector installed", "what are the memory settings", "how many connections are in use". Despite "manage ... engine-level settings" in the description, every shipped script is a read-only lister — it cannot change configuration. Do NOT use for applying config changes (use gcloud/console), backups, or query analysis.

## Inputs, outputs, tools
- Inputs: `projectId`/`instanceId` for get_instance; `setting_name` + `limit` for list_pg_settings.
- Outputs: JSON inventories — extensions (name, default_version, description / installed version, schema, owner), memory settings, connection stats.
- Tools: `scripts/{database_overview,get_instance,list_available_extensions,list_installed_extensions,list_memory_configurations,list_pg_settings}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. All scripts are read-only — report findings; configuration changes go through gcloud/Cloud Console and need owner approval.
2. Distinguish available (installable) from installed extensions before recommending `CREATE EXTENSION`.
3. list_memory_configurations surfaces the memory knobs most relevant to tuning conversations.
4. `project` is pre-configured; never ask unless the user names another.
5. Do not ask about env vars unless a script fails on missing env.

## Risks / things needing the owner
None destructive — but acting on its output (enabling extensions, changing memory params) has real cost/lock implications; escalate to owner. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, postgres, configuration, extensions, audit

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-view-config\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
