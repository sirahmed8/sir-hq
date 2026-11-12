# cloud-sql-postgres-admin

## Summary
Google-published skill for administering Cloud SQL for PostgreSQL instances: provisioning instances (default POSTGRES_17), creating databases and users (password or IAM), cloning (full or PITR), listing instances/databases, and polling operations. Same Node-script JSON-param wrapper as the other cloud-sql-* skills.

## When to use / when NOT
Use for Postgres instance/database/user provisioning and clones. Do NOT use for SQL/schema exploration (cloud-sql-postgres-data), monitoring (cloud-sql-postgres-monitor/-health), backups/restores (cloud-sql-postgres-lifecycle), or MySQL work.

## Inputs, outputs, tools
- Inputs: `name`, `rootPassword`, `databaseVersion` (default POSTGRES_17), `editionPreset` (Development/Production) for create_instance; `instance`, `name`, `iamUser` for create_user; `sourceInstanceName`/`destinationInstanceName`/`pointInTime` for clone; `project` pre-configured.
- Outputs: GCP instance/user/database objects and operation IDs.
- Tools: `scripts/clone_instance.js`, `create_database.js`, `create_instance.js`, `create_user.js`, `get_instance.js`, `list_databases.js`, `list_instances.js`, `wait_for_operation.js`; Node + JSON; auto-loads .env.

## 5 most important rules
1. Never ask for the GCP project ID — pre-configured; override only on explicit user request.
2. Poll `wait_for_operation` (multiplier 4) until DONE after every mutating call.
3. `editionPreset` controls machine type/availability defaults — confirm Production vs Development.
4. `rootPassword` required for instance creation; IAM users get no password.
5. Do not ask about env vars unless execution fails on missing env.

## Risks / things needing the owner
Creates billable GCP resources and handles root credentials — owner confirms sizing/edition. Cloning duplicates storage cost. Requires GCP credentials in env.

## Category / tags
cloud · gcp, cloud-sql, postgres, provisioning, admin

## Revisions
Single revision: `C:\Users\a7med\.gemini\skills\cloud-sql-postgres-admin\SKILL.md` (Apache-2.0, publisher google). Only the gemini tool holds it.
