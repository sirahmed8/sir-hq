# alloydb-postgres-access-management

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-access-management\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A PostgreSQL access management skill for AlloyDB Omni that extends standard PostgreSQL user/role management with AlloyDB-specific IAM integration. It handles creating and managing PostgreSQL roles, assigning IAM-based authentication, managing password policies, and auditing role membership changes. The skill also integrates with Google Cloud IAM to synchronize database roles with cloud identity platforms.

## When to use / when NOT
Use when managing PostgreSQL-compatible access control in AlloyDB Omni and you need centralized IAM integration. Do NOT manage database roles solely through SQL CREATE ROLE/DROP ROLE for production environments — the skill provides the IAM synchronization layer that ensures consistency between cloud identity and database roles. Do NOT reuse the same role across multiple applications without role segregation; the skill will flag role overlap and recommend namespace-based role naming.

## Inputs, outputs, tools
- Inputs: role name, login credentials, IAM principal emails, password policy settings, role membership list.
- Outputs: created/modified PostgreSQL role, IAM mapping confirmation, password policy report, role membership audit log, access review summary.
- Tools: `psql`, `gcloud iam`, AlloyDB IAM integration, `pg_role`, `pg_authid`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always use IAM-authenticated users for application connections** — Google Cloud IAM authentication is more secure and easier to manage than passwords.
2. **Never grant LOGIN privilege to more roles than necessary** — the skill will generate a role audit report highlighting overly permissive roles.
3. **Synchronize role changes via the skill, not direct SQL** — if you CREATE ROLE in psql, the IAM sync will be out of date; use the skill's API for all role modifications.
4. **Enforce password policies for non-IAM users** — the skill can validate password strength and expire old passwords after 90 days.
5. **Review role membership quarterly** — the skill generates an access review report; the owner must approve or revoke unused role memberships.

## Risks / owner notes
Role explosion is a common issue — when roles are created for each new feature without cleanup, the access matrix becomes unmanageable. The owner should use the quarterly review to consolidate redundant roles. IAM sync failures (usually due to permission changes in Google Cloud) will cause the skill to report mismatched roles; these should be resolved by re-running the sync, not by editing database roles directly.

## Category / tags
database · access-control, iam, postgres, alloydb, security, user-management

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.