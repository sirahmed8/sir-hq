# agy-customizations

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\agy-customizations\SKILL.md` plus `docs/rules.md`, `docs/skills.md`, `docs/plugins.md`, `docs/hooks.md`, `docs/mcp_servers.md`, and `docs/json_configs.md`.

## Summary
This built-in Antigravity skill is the reference map for extending the agent through rules, skills, plugins, lifecycle hooks, and MCP servers. It explains where customizations are discovered, how workspace and global locations differ, which customization wins when names collide, how progressive disclosure keeps context small, and how JSON manifests register nonstandard paths.

## When to use / when NOT
Use when explaining, auditing, creating, or debugging Antigravity customizations such as `AGENTS.md` rules, `skills/<name>/SKILL.md`, plugin bundles, `hooks.json`, `mcp_config.json`, `skills.json`, or `plugins.json`. Do not use it as a product-code skill, and do not add hooks or MCP servers casually because they can change agent behavior and tool access.

## Inputs, outputs, tools
Inputs are the desired customization type, scope, and target directory or plugin. Outputs are correctly placed files such as `SKILL.md`, `plugin.json`, `hooks.json`, `mcp_config.json`, `skills.json`, or `plugins.json`, plus an understanding of precedence and loading behavior. Tools are the filesystem, Antigravity's customization discovery, shell commands for hook scripts, stdio or Streamable HTTP MCP endpoints, and the bundled docs.

## 5 most important rules
1. Pick the right type: rules for always-on or model-decision guidance, skills for on-demand procedures, plugins for bundles, hooks for lifecycle commands, and MCP for external tools.
2. Respect discovery and precedence: workspace `.agents/` paths are found upward to the repo root, global config lives under `~/.gemini/config/`, declared configs and built-ins have their own priority, and name conflicts resolve by that order.
3. Keep `SKILL.md` frontmatter accurate because only names and descriptions are injected until the skill is activated; put bulky detail in `references/`, `scripts/`, or `examples/`.
4. Use `skills.json` and `plugins.json` for nonstandard locations, with `inherits`, `entries`, `include_only`, and `exclude` controlling one-level scans.
5. Treat hooks and MCP as powerful: hooks are synchronous command handlers with JSON stdin/stdout contracts, while MCP supports stdio and Streamable HTTP but not legacy SSE.

## Risks / owner notes
Rules can over-apply or fail to apply if placed at the wrong directory level; hooks can allow, deny, ask, rewrite tool calls, inject steps, or force continuation; MCP servers expand the tool surface and may need credentials. The owner should review hook commands and MCP endpoints before enabling them, especially in shared or production repositories.

## Category / tags
ops · antigravity, customization, skills, rules, plugins, hooks, mcp, configuration, agent-governance

## Revisions
Single antigravity-builtin source. It is not present as a codex, claude, kilo, cursor, opencode, or windsurf skill copy, so this is the canonical revision.
