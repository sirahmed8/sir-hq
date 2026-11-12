# plugin

- Tool: `antigravity-builtin`
- Category: security
- Source: `C:\Users\a7med\.gemini\antigravity\builtin\skills\plugin\SKILL.md`
- SKILL.md size: 17122 chars

## What it does

How to manage and create plugins — namespaced bundles of skills, agents, rules, MCP servers and hooks that install, enable and disable as a single unit. Use this skill when the user wants to enable, disable, install or uninstall a plugin, when they want to create a new plugin, or when a new customization should be packaged into a plugin rather than left loose. Also triggered by the /plugin slash command. Don't use for the underlying customization system itself — discovery roots, loading priority, or authoring a standalone skill, agent, rule, hook or MCP server outside a plugin; see the customizations guide skill for those.

## Structure (headings inside SKILL.md)

- Plugins
- Quick Start
- Step 0: Preflight and inventory
- Step 1: Decide the kind
- Step 2A: Lifecycle operations
- Step 2B: Decide where the functionality belongs
- Consolidating loose customizations
- Step 3: Author the bundle
- Step 4: Verify and hand back
- Constraints & Tips
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP servers, MCP server, MCP config

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. 1.  If you do not already have the catalog ID, look it up with the
2. -   **Never hand-edit `config.json` or call mutation RPCs from `run_command`.**
3. -   **Keep `description` honest and current.** It is what the user reads before

## Files inside the skill

- (SKILL.md only)
