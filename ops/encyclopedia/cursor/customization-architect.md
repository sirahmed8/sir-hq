# customization-architect

## Summary
Meta-skill for engineering and auditing AI-assistant customizations (skills, rules, instruction files) across Antigravity/Gemini, Cursor, Codex/Copilot and Claude Code. It defines a token-efficiency philosophy (density over verbosity, selective plugin activation), a 5-vector audit rubric (token efficiency, real persistence, UI aesthetics, security, defensive execution), the canonical SKILL.md anatomy, per-platform rules file mapping, a rules synchronizer, and a token-budget recovery protocol.

## When to use / when NOT
Use when writing, auditing, or syncing skills/rules/AGENTS.md/CLAUDE.md/.cursorrules across tools, or when customization budget runs low. Do NOT use for product code itself — it governs the agent-config layer. Related: skill-creator (builds skills), skill-repair (fixes installs).

## Inputs, outputs, tools
- Inputs: skill/rule files, `~/.gemini/config/config.json`, `mcp_config.json`, project rule files.
- Outputs: audited/enhanced SKILL.md files, synced per-platform rule files, plugin/MCP pruning recommendations.
- Tools: filesystem edits across `~/.gemini/config/skills/`, `.cursor/rules/*.mdc`, `AGENTS.md`, `CLAUDE.md`; no external APIs.

## 5 most important rules
1. Every customization must earn its tokens — strip fluff, use imperative bullets and code contracts.
2. Never load domain-specific plugins globally; reserve global skills for cross-cutting standards.
3. SKILL.md needs kebab-case name, trigger-explicit description, non-negotiable guardrails, and real code examples (no TODO stubs).
4. Audit against the 5 vectors: persistence must be real (Postgres/SQLite/Drift), security server-side, UI off AI clichés.
5. Under <15% customization budget: disable irrelevant plugins in config.json, consolidate overlapping skills, prune unused MCP schemas.

## Risks / things needing the owner
Editing global configs affects every project — changes to `~/.gemini/config` and manifest files should be confirmed. Wrong platform mapping (e.g. putting Claude-only syntax in AGENTS.md) silently degrades other tools.

## Category / tags
ai · skills, rules, config, token-optimization, cross-platform

## Revisions
Six tools hold it; bodies byte-identical, only `description` differs. Claude copy preferred for trigger-style description.
