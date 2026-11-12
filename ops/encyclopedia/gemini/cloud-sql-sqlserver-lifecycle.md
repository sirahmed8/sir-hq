# cloud-sql-sqlserver-lifecycle

## Summary
Google-published skill for Cloud SQL SQL Server durability: on-demand backups, restores (incl. cross-project via source_project/source_instance), instance cloning (copy or PITR via pointInTime RFC 3339), instance list/get, and operation polling.

## When to use / when NOT
Use for "backup", "restore", "clone for staging", "is the operation done" on SQL Server instances. Do NOT use for queries (data), provisioning (admin), or metrics (monitor).

## Inputs, outputs, tools
- Inputs: `sourceInstanceName`/`destinationInstanceName`/`pointInTime`/zones for clones; `instance`/`location`/`backup_description` for backups; `target_project`/`target_instance`/`backup_id` (+ optional `source_project`/`source_instance`) for restores.
- Outputs: Cloud SQL Operation objects; poll wait_for_operation to DONE.
- Tools: `scripts/{clone_instance,create_backup,restore_backup,get_instance,list_instances,wait_for_operation}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. Follow every mutating call with wait_for_operation until DONE.
2. PITR clones need exact RFC 3339 pointInTime; omit it for a direct copy.
3. `backup_id` verbatim — BackupRun ID, backup name, or BackupDR name; never parse it.
4. source_project/source_instance required only for BackupRun-ID restores across projects.
5. `project` is pre-configured; never ask unless the user names another.

## Risks / things needing the owner
restore_backup overwrites target data — confirm target. Clones/backups incur storage cost. SQL Server backups follow the instance's backup window config. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, sqlserver, backup, restore, clone

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-sqlserver-lifecycle\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
