# graphify-ast-memory

- Tool: `claude`
- Category: research
- Source: `C:\Users\a7med\.claude\skills\graphify-ast-memory\SKILL.md`
- SKILL.md size: 2672 chars

## What it does

Use when a codebase is too large to load into context and you need a deterministic AST knowledge graph to navigate it with far fewer tokens.

## Structure (headings inside SKILL.md)

- Graphify AST Memory & Knowledge Graph Engine
- 1. Core Operating Concept: Graph Over Dump
- 2. Generating Obsidian-Compatible Knowledge Graphs
- 3. Querying & Navigation Commands
- 4. Best Practices for AI Agents
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 4. **Token Reduction**: Achieves up to **71x token savings** by operating on structural signatures instead of raw implementation bodies.
- - Imports: [[TokenManager]], [[PasswordHasher]]
- - First produce a structural dependency tree:

## Key rules (verbatim lines from SKILL.md)

1. 4. **Token Reduction**: Achieves up to **71x token savings** by operating on structural signatures instead of raw implementation bodies.
2. - **Trace Path**: `path(A, B)` — find the exact dependency chain between two modules before making edits.
3. - Never dump an entire directory into context when asked how a feature works.

## Files inside the skill

- (SKILL.md only)
