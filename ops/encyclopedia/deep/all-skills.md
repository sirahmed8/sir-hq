# all-skills

Source read: `C:\Users\a7med\.config\kilo\skills\all-skills\SKILL.md` (kilo revision; identical copies in codex/cursor/windsurf/opencode; not in claude).

## Summary
A meta-skill that provides a searchable index and catalog of all installed AI agent skills, plugins, and MCP connectors across the entire agent ecosystem. It lists each skill's name, description, allowed tools, category, tags, and the deep digest path in `ops/encyclopedia/deep/`. The skill is used by the `skills-discovery-engine` to find relevant skills for a given task, and by the `build-encyclopedia.mjs` script to regenerate the full skill index and SOURCES.md. It supports filtering by category, tool, revision, and keyword, and generates reports on skill coverage gaps and duplicate revisions.

## When to use / when NOT
Use when you need to discover what skills are available for a task, or when you want to audit the skill ecosystem for duplicates, missing categories, or propagation failures. Do NOT use to replace actual skill execution — the index only describes skills, it does not implement them. Do NOT assume the index is up-to-date without running `node gen-index.mjs` first; stale indexes will show skills that have been removed or deep digests that have been deleted.

## Inputs, outputs, tools
- Inputs: optional filters (category, tool, keyword, revision), optional output format (json, markdown, csv).
- Outputs: a formatted table of all skills with name, tools, category, purpose, digest link, and revision notes; or a JSON array for programmatic consumption.
- Tools: filesystem read, node.js script (gen-index.mjs), grep/ripgley for text searching. MCP: none required (pure file-based index).

## 5 most important rules
1. **Always run gen-index.mjs after adding or modifying a skill deep digest** — the index will otherwise be out of sync and report false gaps.
2. **Filter by category when the index is large** — without filtering, the output can exceed 500 lines and be impractical to read.
3. **Check the "Revisions" column for byte-identical copies** — if multiple tools have the same skill but different revision notes, the index will flag them for sync via propagate-deep.mjs.
4. **Never edit SKILLS_INDEX.md manually** — it is regenerated from the deep digests; manual changes will be overwritten and may create inconsistencies between the index and the actual deep files.
5. **Use the search functionality to find skills by keyword** — the index supports substring matching on name, description, and tags to quickly locate relevant skills.

## Risks / owner notes
The most common failure is a worker forgetting to run gen-index.mjs after creating a new deep digest, resulting in the skill being "missing" from the index even though the deep file exists. The owner should add a pre-commit hook that runs gen-index.mjs and fails the commit if the index changes.

## Category / tags
meta-skill · index, catalog, discovery, enumeration, skills-registry, documentation, index-management

## Revisions
The kilo, codex, cursor, and windsurf copies are byte-identical (identical SKILL.md, 112-set shared across these tools). The gemini-plugin version includes additional fields for MCP connector names and plugin-specific flags. The kilo revision is the canonical source; all tool digests should reference it as the base, with gemini-plugin copies updated via propagate-deep.mjs to include the extra MCP fields.