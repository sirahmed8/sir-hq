# migrate-agent-settings (antigravity-builtin)

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\migrate-agent-settings\SKILL.md` (10.5 KB; antigravity-builtin; sibling `migrate-workflows` handles workflow files only).

## Summary
Imports a user's MCP servers, skills, slash commands, subagents, and instruction files from other agents (Claude Code, Codex, Cursor, Gemini CLI) into ONE reversible Antigravity plugin at `~/.gemini/config/plugins/<name>/`. Four steps: discover (scan `~/.claude.json` mcpServers, `~/.claude/skills|commands|agents`, `~/.claude/CLAUDE.md`; `~/.codex/config.toml` `[mcp_servers.*]`, skills, prompts, AGENTS.md; `~/.cursor/mcp.json`, `.cursor/rules/*.mdc`; `~/.gemini/settings.json`, commands/*.toml, GEMINI.md), confirm (counts+names per source, skip-list with reasons, plugin name suggestion, ONE approval question — never write before confirmation, never print secret values), write (plugin.json + converted mcp_config.json + skills/ + rules/ + subagents/), hand back (JSON-parse check, migration report, `customization://<plugin>` link, variable-fill instructions).

## When to use / when NOT
Use when the user wants to bring their setup from Claude Code/Codex/Cursor/Gemini CLI into Antigravity. Not for Marketplace plugin installs or authoring a plugin from scratch; not for migrating legacy workflow files (that's migrate-workflows).

## Inputs, outputs, tools
- Inputs: source configs in the four agents' home dirs + optional workspace `.mcp.json`/`.cursor/` files.
- Outputs: a plugin folder with `plugin.json`, `mcp_config.json`, `skills/<name>/SKILL.md`, `rules/*.md`, subagent files; a `.bak`-free, reversible bundle.
- Tools: filesystem reads/writes; Antigravity plugin schema.

## 5 most important rules
1. NEVER write anything before the user confirms the plan; never modify/delete source files.
2. Everything lands in ONE plugin so the import is reversible (delete the folder to undo).
3. MCP conversion is schema-strict: only `command,args,env,cwd,url,headers,disabled,variables` survive; `${X}` placeholders need `variables` declarations or literal passthrough; plugin configs do NOT expand OS env vars.
4. Make every `cwd` absolute NOW (`${workspaceFolder}`, `$HOME`, `~` resolved) — relative cwd resolves against the plugin dir.
5. Record non-convertible items (hooks, permissions, SSE-transport servers, Cursor DB rules) for the report; skills need frontmatter name+description; rules capped at 24KB.

## Risks / owner notes
Handles the owner's real credentials — secrets must never be echoed in chat (key names only) though literal values are preserved inside the local plugin file. Plugins with unfilled `variables` start DISABLED by design. Workspace-sourced configs become global once imported — flag that in the plan.

## Category and tags
Category: ops. Tags: migration, antigravity, mcp, plugin, claude-code, codex, cursor, reversible.
