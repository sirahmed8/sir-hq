# migrate-workflows (antigravity-builtin)

Source read: `C:\Users\a7med\.gemini\antigravity\builtin\skills\migrate-workflows\SKILL.md` (6 KB; antigravity-builtin; `migrate-agent-settings` is a sibling).

## Summary
Autonomous migration of legacy "workflow" markdown files to modern skills. Workflows (`.agents/workflows/*.md`, `_agents/workflows/*.md`, `.agent/`, `_agent/` variants, plus global `~/.gemini/config/global_workflows/*.md` and `~/.gemini/config/workflows/*.md`, and `workflows.json` manifests) are deprecated; skills add slash commands, semantic discovery, and multi-file support. The agent must execute automatically: (1) scan global and workspace dirs for workflows, check each against existing `<skills>/<name>/SKILL.md`, and present a scope/name/source/target/status table; (2) for each unmigrated workflow, read it, ensure YAML frontmatter (`name`, one-sentence `description`), write `<target>/<name>/SKILL.md` preserving all instructions, then safely archive the source by renaming to `.md.bak` (never delete) and removing entries from `workflows.json`; (3) verify and summarize migrated/skipped/archived. Overwrite protection: existing SKILL.md files are never overwritten.

## When to use / when NOT
Use when the user asks to migrate, convert, or clean up legacy workflow files into skills. Not for authoring new skills from scratch (skill-creator) or for settings migration (migrate-agent-settings).

## Inputs, outputs, tools
- Inputs: legacy workflow `.md` files and `workflows.json` manifests in global (`~/.gemini/config/`) and workspace (`.agents/`, `_agents/`, `.agent/`, `_agent/`) locations.
- Outputs: new `SKILL.md` files with frontmatter; `.md.bak` archives; cleaned manifests.
- Tools: filesystem search/read/write; OS-aware path display (Windows `\` vs POSIX `/`).

## 5 most important rules
1. Scan BOTH global and workspace locations, including all four dir spellings and manifests.
2. Present the discovery table with Pending/Already-Migrated status before converting.
3. Never overwrite an existing SKILL.md — skip and archive only.
4. Archive by rename to `.md.bak`, never delete; remove manifest entries.
5. Preserve ALL prompt instructions/arguments from the original workflow inside the new SKILL.md.

## Risks / owner notes
Runs autonomously over config dirs — a wrong target path pollutes the skills namespace. `.bak` archives are safe but accumulate; manifest edits can corrupt JSON if not careful. Workspace paths adapt to host OS.

## Category and tags
Category: ops. Tags: migration, workflows-to-skills, antigravity, config-cleanup, idempotent.
