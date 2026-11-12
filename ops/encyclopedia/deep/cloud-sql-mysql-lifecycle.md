# cloud-sql-mysql-lifecycle

## Summary
Google-published skill for durability and recovery of Cloud SQL for MySQL: creating on-demand backups, restoring a backup into an instance, cloning an instance (full copy or point-in-time recovery to an RFC 3339 timestamp), listing/getting instances, and waiting on long-running operations.

## When to use / when NOT
Use for "take a backup", "restore to yesterday", "clone this instance for staging/testing", "is the operation done". Do NOT use for schema/query work (cloud-sql-mysql-data) or instance/user creation (cloud-sql-mysql-admin — though clone_instance lives here).

## Inputs, outputs, tools
- Inputs: `sourceInstanceName`/`destinationInstanceName`, optional `pointInTime` (RFC 3339) for PITR clones, `preferredZone`/`preferredSecondaryZone`, `backup_id` + optional `source_project`/`source_instance` for cross-project restores, `location`, `backup_description`.
- Outputs: Cloud SQL Operation objects; call wait_for_operation after each mutating call.
- Tools: `scripts/clone_instance.js`, `create_backup.js`, `restore_backup.js`, `get_instance.js`, `list_instances.js`, `wait_for_operation.js`; JSON params; auto-loads .env; project pre-configured.

## 5 most important rules
1. Every mutating call returns an Operation — always follow with `wait_for_operation` (the skill notes multiplier 4 polling) until DONE before claiming success.
2. PITR clones need an exact RFC 3339 `pointInTime`; omitting it makes a direct full copy.
3. `backup_id` is used verbatim — BackupRun ID, backup name, or BackupDR name; do not parse it.
4. `source_project`/`source_instance` are required only when restoring via a BackupRun ID from another project.
5. Never ask for the GCP project ID; it is pre-configured.

## Risks / things needing the owner
Restores and clones create billable resources and restore_backup overwrites the target instance's data — confirm the target before running. PITR is only as good as the instance's backup/PITR window. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, mysql, backup, restore, clone, disaster-recovery

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-mysql-lifecycle\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
