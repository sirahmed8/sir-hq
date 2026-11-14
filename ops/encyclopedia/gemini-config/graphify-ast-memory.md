# graphify-ast-memory

Source read: `C:\Users\a7med\.claude\skills\graphify-ast-memory\SKILL.md` (claude revision; codex/cursor/kilo/opencode/windsurf listed).

## Summary
A context-engineering method (inspired by Graphify-Labs/graphify and Karpathy's context principles) for navigating large codebases via a deterministic AST knowledge graph instead of dumping files. Nodes are files/classes/functions/routes/types; edges are imports, calls, implements, inherits. The agent traces relationship paths (`path(A,B)`), inspects only export signatures and 1-hop neighbors, and claims up to 71x token savings. It also describes emitting Obsidian-compatible Markdown nodes with wiki-links so the architecture renders as an interactive graph view.

## When to use / when NOT
Use when a codebase is too large to load into context and the task is architectural navigation or planning a cross-module change. Do NOT use for small repos where reading the relevant files directly is cheaper, and note the skill is a method/playbook — it does not ship a runnable indexer; building the graph is implied work.

## Inputs, outputs, tools
- Inputs: a codebase plus a question or planned change (e.g., "how does login flow work", "what breaks if I change UserRepository").
- Outputs: a structural dependency tree, traced paths, surgical edit targets, optionally an Obsidian vault of wiki-linked nodes.
- Tools: AST parsing (language-appropriate), Obsidian graph view for visualization; file edits stay surgical.

## 5 most important rules
1. Never dump an entire directory into context to answer "how does X work" — build the dependency tree first.
2. Always produce the structural chain before editing: `UI -> Hook -> Service/API DTO -> Entity`.
3. Query by relationship (`path(A,B)`, imports, consumers) and load only the node being edited plus direct dependency type declarations.
4. Make surgical edits that do not disturb unaffected graph edges.
5. For visualization, emit one Markdown node per module with `## Relationships` wiki-links and open the folder as an Obsidian vault.

## Risks / owner notes
Low risk; it is guidance, not code that runs. The 71x figure is the upstream project's claim, not a measured guarantee — real savings depend on graph quality. Keeping the graph in sync as code changes is unaddressed.

## Category and tags
Category: ai. Tags: context-engineering, ast, knowledge-graph, token-optimization, codebase-navigation, obsidian.
