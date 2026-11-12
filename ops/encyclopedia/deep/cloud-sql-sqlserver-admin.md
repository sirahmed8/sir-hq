# cloud-sql-sqlserver-admin

## Summary
Google-published skill for administering Cloud SQL for SQL Server: create instances (default SQLSERVER_2022_STANDARD), databases, and users (password or IAM), list instances/databases, get instance state, and poll operations. Same Node-script JSON-param wrapper as the other cloud-sql-* skills.

## When to use / when NOT
Use for SQL Server instance/database/user provisioning on Cloud SQL. Do NOT use for queries/schema (cloud-sql-sqlserver-data), backups/clones (cloud-sql-sqlserver-lifecycle), or metrics (cloud-sql-sqlserver-monitor), or any MySQL/Postgres work.

## Inputs, outputs, tools
- Inputs: `name`, `rootPassword`, `databaseVersion` (default SQLSERVER_2022_STANDARD), `editionPreset` (Development/Production) for create_instance; `instance`, `name`, `password`, `iamUser` for create_user.
- Outputs: GCP objects and operation IDs.
- Tools: `scripts/{create_database,create_instance,create_user,get_instance,list_databases,list_instances,wait_for_operation}.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. Never ask for the GCP project ID — pre-configured; override only on explicit user request.
2. Poll wait_for_operation until DONE after every mutating call.
3. editionPreset decides machine type/availability — confirm Development vs Production.
4. rootPassword required for instance creation; IAM users get no password.
5. Do not ask about env vars unless execution fails on missing env.

## Risks / things needing the owner
Creates billable GCP resources and handles sa credentials; SQL Server licensing is baked into the edition/version choice — confirm before creating. Requires GCP credentials.

## Category / tags
cloud · gcp, cloud-sql, sqlserver, provisioning, admin

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-sqlserver-admin\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
