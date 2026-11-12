# cloud-sql-mysql-admin

## Summary
Google-published skill for administering Cloud SQL for MySQL instances: provisioning new instances, creating databases and users (password or IAM), listing instances/databases, and polling long-running operations. It is a thin wrapper that runs the Node.js scripts in `scripts/` with a JSON parameter object.

## When to use / when NOT
Use for infrastructure lifecycle tasks on Cloud SQL MySQL: "create an instance", "add a database/user", "what instances exist". Do NOT use for running queries or inspecting schema (cloud-sql-mysql-data) or backups/restores/clones (cloud-sql-mysql-lifecycle).

## Inputs, outputs, tools
- Inputs: JSON params per script — `instance`, `name`, `rootPassword`, `databaseVersion` (default MYSQL_8_4), `editionPreset` (Development/Production), `iamUser`, etc. `project` is pre-configured; do not ask unless the user names a different one.
- Outputs: GCP API results (instance/database/user objects, operation IDs).
- Tools: `scripts/*.js` run with Node (`node <skill_dir>/scripts/<name>.js '{...}'`), same syntax on Bash and PowerShell. Scripts auto-load .env files — only ask about env vars if execution fails.

## 5 most important rules
1. Never ask for the GCP project ID — it is pre-configured; only use a different one if the user explicitly provides it.
2. Call `wait_for_operation` after any mutating call and poll until the operation is DONE before reporting success.
3. `editionPreset` decides machine type and availability defaults — confirm Production vs Development intent.
4. `rootPassword` is required for instance creation; IAM users (`iamUser: true`) must not get a password.
5. Do not prompt for env vars preemptively; scripts load .env themselves.

## Risks / things needing the owner
Creates billable GCP resources and sets root passwords — owner should confirm instance size/edition and credential handling. Deleting or resizing is not covered here. Requires GCP credentials in env.

## Category / tags
cloud · gcp, cloud-sql, mysql, provisioning, admin

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-mysql-admin\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
