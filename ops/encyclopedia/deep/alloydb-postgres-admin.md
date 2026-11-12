# alloydb-postgres-admin

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-admin\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
An administration skill for AlloyDB Omni that provides backup management, user administration, performance tuning, and cluster maintenance operations. It handles routine admin tasks such as user creation/deletion, password resets, index maintenance, vacuum planning, and configuration changes with proper safeguards and audit logging.

## When to use / when NOT
Use for routine AlloyDB Omni administration tasks — the skill provides a safer alternative to direct psql commands by wrapping them in audit logs and validation checks. Do NOT skip the pre-flight validation; the admin skill verifies the cluster is healthy before performing any operation, and will abort if the cluster shows signs of degradation. Do NOT use for emergency crash recovery — the skill is for planned maintenance; use the lifecycle skill or contact Google Cloud support for crash scenarios.

## Inputs, outputs, tools
- Inputs: admin operation type (create_user, reset_password, vacuum, reindex, configure), target database/object names, operation-specific parameters.
- Outputs: operation confirmation, updated user/config, audit log entry, performance metrics before/after (for tune operations).
- Tools: `psql`, `gcloud alloydb`, `pg_basebackup`, `pg_dump`, `vacuumdb`, `reindexdb`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always run a pre-flight health check before any admin operation** — the skill will abort if the cluster is in a degraded state, preventing partial or failed operations.
2. **Schedule vacuum and reindex during low-traffic windows** — the skill will warn if it detects active connections and recommend off-peak timing.
3. **Use the skill's password reset flow instead of direct pg_hba.conf edits** — the reset generates an audit log entry and rotates the password securely.
4. **Never apply configuration changes (shared_buffers, work_mem) without a post-change health check** — the skill compares metrics before and after and can automatically roll back if performance degrades.
5. **Maintain audit logs for all admin operations** — the skill writes to a persistent log; do not delete these logs as they are needed for compliance and troubleshooting.

## Risks / owner notes
Applying configuration changes without testing in staging can cause outages; the owner should always validate shared_buffers and work_mem changes on a copy of the production data first. Password reset via the skill is secure but will invalidate all active connections — the owner should notify users before running a mass password reset.

## Category / tags
database · administration, postgres, alloydb, admin, vacuum, reindex, security

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.