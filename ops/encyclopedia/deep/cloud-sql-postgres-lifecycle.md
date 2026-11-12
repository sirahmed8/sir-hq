# cloud-sql-postgres-lifecycle

## Summary
Google-published skill for Cloud SQL PostgreSQL lifecycle operations: on-demand backups, restores (including cross-project via source_project/source_instance), instance listing/get, a database_overview snapshot (version, replica status, uptime, connection counts), wait_for_operation polling, and — distinctively — `postgres_upgrade_precheck`, which analyzes a major-version upgrade and returns ERROR/WARNING/INFO findings with remediation steps.

## When to use / when NOT
Use for "backup now", "restore this backup", "can we upgrade to POSTGRES_18", "how many connections are in use". Do NOT use for day-to-day queries (data), provisioning (admin — note clone lives in admin for Postgres), or PromQL monitoring.

## Inputs, outputs, tools
- Inputs: `instance`, `location`, `backup_description` for backups; `target_project`/`target_instance`/`backup_id` (+ optional `source_project`/`source_instance`) for restores; `project`+`instance`+`targetDatabaseVersion` (default POSTGRES_18) for the upgrade precheck; `projectId`/`instanceId` for get_instance.
- Outputs: operation IDs, backup/restore results, precheck report graded ERROR (blocking) / WARNING / INFO.
- Tools: `scripts/{create_backup,restore_backup,get_instance,list_instances,database_overview,postgres_upgrade_precheck,wait_for_operation}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. Follow every mutating call with wait_for_operation until DONE.
2. Treat precheck ERROR findings as hard blockers — resolve the provided actions_required steps before attempting the upgrade; WARNINGs should be reviewed, INFO needs nothing.
3. `backup_id` is used verbatim (BackupRun ID, backup name, or BackupDR name) — never parse it.
4. `source_project`/`source_instance` are required only for BackupRun-ID restores from another project.
5. `project` is pre-configured; never ask unless the user names another.

## Risks / things needing the owner
restore_backup overwrites target data — confirm target first. Backups/clones cost storage. Major-version upgrades are irreversible in place; the precheck reduces but doesn't eliminate risk. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, postgres, backup, restore, upgrade

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-lifecycle\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
