# plugin

Tools: antigravity-builtin. Source: C:\Users\a7med\.gemini\antigravity\builtin\skills\plugin\SKILL.md (309 lines, read in full)

## Summary
Antigravity's internal skill for managing plugins — namespaced bundles of skills, agents, rules, MCP servers, and hooks that install/enable/disable as one unit. It defines a preflight RPC channel to the language server (`GetAllPlugins` via curl + CSRF token), routes lifecycle ops (enable/disable/uninstall/install-from-marketplace) to UI links and plugin cards, and authors new plugins under `~/.gemini/config/plugins/<name>/`.

## When to use / not use
Use when enabling/disabling/installing/uninstalling a plugin, creating a new plugin, or consolidating loose skills/rules/MCP entries into a bundle. Not for the underlying customization system itself (discovery roots, loading priority, standalone authoring) — that belongs to the customizations guide skill.

## Inputs, outputs, dependencies
Input: user intent (lifecycle verb or new capability) plus live language-server state. Output: plugin state changes via UI links/cards, or a new `plugin.json` + subdirectories bundle. Needs: `ANTIGRAVITY_LS_ADDRESS`/`ANTIGRAVITY_CSRF_TOKEN` env, curl, jq, `search_marketplace` tool for catalog IDs.

## Key rules
1. Step 0 always: healthz check, write `/tmp/lsrpc.sh`, inventory via `GetAllPlugins` piped through jq — NEVER unfiltered (it inlines full SKILL.md text, floods context).
2. `dir` (install directory name) keys every `customization://<dir>` link — NOT `plugin.json`'s `name`; names share a global namespace and collisions silently drop one plugin.
3. Never call mutation RPCs (`JetboxWriteState`, `DeletePlugin`, `InstallCustomization`) from run_command or hand-edit config.json — give the user a customization:// link or `<plugin-card catalog-id>` instead; built-ins can't be uninstalled, only disabled.
4. Bundle shape: plugin.json (JSONC, name/description/logo/suggestedPrompts/author/etc. — unknown top-level fields silently discarded) + only the subdirs actually used (skills/, agents/, rules/AGENTS.md, mcp_config.json, hooks.json, assets/).
5. MCP server names are global — prefix plugin servers with the plugin name; moving an MCP entry into a plugin ties its lifecycle to the plugin's enabled state.

## Risks / owner items
- Plugin name collisions drop plugins silently — check inventory before naming.
- Consolidating MCP servers changes lifecycle and control surface; warn the user first.
- config.json holds sibling state (userSettings, permission grants) — manual edits can clobber concurrent grants.
- Logo rules: local relative path only, URLs/absolute rejected silently.

## Category and tags
ops, ai — antigravity, plugins, customization, mcp, governance, internal.

## Revision note
Single antigravity-builtin revision; harness-internal machinery, not portable knowledge.
