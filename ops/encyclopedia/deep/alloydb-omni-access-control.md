# alloydb-omni-access-control

Source read: `C:\Users\a7med\.gemini\skills\alloydb-omni-access-control\SKILL.md` plus `scripts/database_overview.js`, `scripts/list_pg_settings.js`, and `scripts/list_roles.js`.

## Summary
This Google skill provides read-only AlloyDB Omni/PostgreSQL inspection helpers for database overview, `pg_settings`, and roles. Each Node script is a thin wrapper that invokes `@toolbox-sdk/server@1.1.0` with the `alloydb-omni` prebuilt configuration, loads environment variables from the usual `.env` locations, and returns database state without implementing user or grant management itself.

## When to use / when NOT
Use when an agent needs a quick server overview, filtered PostgreSQL settings, or a list of roles and role attributes for an AlloyDB Omni instance. Do not use it to create users, change grants, rotate credentials, or enforce IAM; those are separate administrative actions and may require different tooling and authorization.

## Inputs, outputs, tools
Inputs are JSON arguments passed to the script, such as `setting_name`, `role_name`, and `limit`, plus connection environment variables like `ALLOYDB_OMNI_HOST`, `ALLOYDB_OMNI_PORT`, `ALLOYDB_OMNI_PASSWORD`, and `ALLOYDB_OMNI_QUERY_PARAMS`. Outputs are the toolbox result for server version/replica status/uptime/connections, matching settings, or role details including privileges and memberships. Tools are Node.js, `npx`, `@toolbox-sdk/server`, and the AlloyDB Omni database endpoint.

## 5 most important rules
1. Run scripts as `node <skill_dir>/scripts/<script_name>.js '<json>'`, with PowerShell quoting adjusted for the shell.
2. Do not ask for environment variables until execution fails because they are missing; the scripts attempt to load `.env` files automatically.
3. Omit empty optional environment variables rather than passing blank connection fields.
4. Use `setting_name` and `limit` to narrow `pg_settings`, and `role_name` plus `limit` to narrow role listings.
5. Treat the scripts as inspection helpers; verify any security conclusion against the actual database before changing roles or settings.

## Risks / owner notes
The scripts need Node, network access for `npx`, and valid AlloyDB Omni credentials. Environment files may contain secrets and should not be printed or committed. Role and settings output can expose security-sensitive configuration, so the owner should control where results are stored and who can see them.

## Category / tags
data · alloydb, postgres, access-control, pg-settings, roles, google-cloud, node, inspection

## Revisions
Single gemini skill revision with three Node scripts. No codex, claude, kilo, cursor, opencode, or windsurf copy was present.
