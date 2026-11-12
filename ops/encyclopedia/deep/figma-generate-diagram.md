# figma-generate-diagram

## Summary
Router + constraint skill for the `generate_diagram` MCP tool, which turns Mermaid.js syntax into an editable FigJam diagram. It must be loaded before EVERY call. It routes the request to one of five supported types (architecture flowchart, flowchart, sequence, ER, state, Gantt), hard-rejects unsupported types (pie, mindmap, class, timeline, C4, etc.) instead of calling and failing, lists universal Mermaid constraints, demands real context before authoring (source code, docs, existing files, other MCPs, or the user), and offers a hybrid workflow (generate_diagram + use_figma FigJam extensions) for annotations/colors Mermaid cannot express.

## When to use / when NOT
Use for any diagram request that maps to Mermaid-supported types. Do NOT call for unsupported diagram types — tell the user directly. Also push users to manual Figma editing when they ask to change fonts, move individual shapes, or node-by-node edits on an existing diagram (regenerate instead, usually faster).

## Inputs, outputs, tools
- Inputs: diagram intent + real source context; optional `name`, `userIntent`, `useArchitectureLayoutCode` (architecture only), `fileKey` to reuse an existing FigJam file.
- Outputs: a FigJam file/link (tool creates its own file — never call create_new_file first) and optionally use_figma extensions.
- Tools: `generate_diagram`; `use_figma` + `get_figjam`/`get_design_context` for hybrid work; per-type reference docs (architecture, flowchart, sequence, erd, state, gantt, workflow).

## 5 most important rules
1. Load this skill before every generate_diagram call — skipping it causes rendering failures and low-quality output.
2. Unsupported types are refused upfront; after 2 failed iterations on the same diagram, stop regenerating and ask what is wrong or suggest manual editing.
3. Universal Mermaid bans: no emojis (tool rejects), no `\n` escapes or HTML in labels, no reserved IDs (`end`, `subgraph`, `graph`), camelCase node IDs, quote special characters.
4. Sequence `Note over` and Gantt `classDef` styling are silently stripped — use the hybrid workflow or build with use_figma instead; FigJam extensions must never call `figma.createPage()`.
5. Reuse `fileKey` when iterating or adding related diagrams (each keyless call creates a new draft file); ask once whether to regenerate over or keep side-by-side. Garbage in = garbage out: never invent edges/entities — missing info beats hallucinated info.

## Risks / owner needs
Requires authenticated Figma MCP. Quality depends entirely on context gathered; hallucinated topology is the main failure mode the skill guards against.

## Category and tags
Category: design. Tags: figma, figjam, mermaid, diagrams, mcp, documentation.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
