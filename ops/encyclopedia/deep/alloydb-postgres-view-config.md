# alloydb-postgres-view-config

Source read: `C:\Users\a7med\.gemini\skills\alloydb-postgres-view-config\SKILL.md` (gemini revision; not found in codex/kilo/cursor/windsurf/opencode or claude).

## Summary
A configuration view skill for PostgreSQL within AlloyDB Omni that provides a structured read of the current database configuration parameters, their values, and sources (static, dynamic, cluster-level, or instance-level). It can also generate `ALTER SYSTEM` commands to modify parameters with proper audit logging, and validate that changes do not violate AlloyDB Omni supported ranges.

## When to use / when NOT
Use when you need to inspect or modify AlloyDB Omni configuration parameters — the skill provides a safer alternative to directly editing `postgresql.conf` or running `ALTER SYSTEM` without validation. Do NOT use to override AlloyDB Omni-supported parameter ranges — the skill will reject changes that exceed the supported limits and suggest acceptable alternatives. Do NOT skip the "dry-run" mode for parameter changes; the skill will show the proposed change and its expected impact before applying it.

## Inputs, outputs, tools
- Inputs: parameter name(s) to query, optional filter by category (memory, tuning, connection), dry-run flag.
- Outputs: current value, default value, source (static/dynamic/clustering), allowed range, proposed `ALTER SYSTEM` command, impact assessment (performance, compatibility).
- Tools: `psql`, `SHOW`, `ALTER SYSTEM`, `pg_conf`, `alloydb-config-validator`. MCP: gemini-plugin connector.

## 5 most important rules
1. **Always use dry-run mode before applying configuration changes** — the skill will show the before/after state and can auto-rollback if issues are detected within the configured safety window.
2. **Never set shared_buffers higher than 40% of available RAM** — the skill will validate this limit and suggest the maximum allowed value for your environment.
3. **Use `ALTER SYSTEM SET` instead of editing postgresql.conf directly** — the skill manages the dynamic config file and ensures it persists across restarts; direct edits may be overwritten.
4. **Validate parameter changes in a staging environment first** — the skill can simulate the impact; applying unknown parameter changes to production can cause unexpected behavior.
5. **Review the impact assessment before confirming** — the skill provides a performance impact estimate; the owner must approve changes that could affect production workloads.

## Risks / owner notes
Parameter changes that are not validated can cause immediate performance degradation or database restart failures. The owner should always use the dry-run mode and validate in staging. Some parameters (e.g., max_connections) require a restart to take effect; the skill will flag these and suggest the maintenance window.

## Category / tags
database · configuration, postgres, alloydb, tuning, alter-system

## Revisions
The gemini revision is the only one available; no codex, kilo, or cursor copies exist. This is the canonical source.