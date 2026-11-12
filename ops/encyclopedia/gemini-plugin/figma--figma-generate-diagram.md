# figma-generate-diagram

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-generate-diagram\SKILL.md`
- SKILL.md size: 9563 chars

## What it does

Generate diagrams.

## When to use (from skill text)

- - **The user themselves** — when the description is thin or ambiguous (unclear direction of flow, unclear scope, unclear which entities matter), ask one or two focused questions before generating. Examples: "What are the 3–5 main steps?", "Who owns each step?", "What triggers the next step?". One go

## Structure (headings inside SKILL.md)

- generate-diagram
- Step 1: Is `generate_diagram` the right tool?
- Supported diagram types
- Unsupported — don't call the tool
- When to push the user to edit in Figma
- Step 2: Pick the diagram type
- Step 3: Universal constraints (apply to every diagram type)
- Step 4: Garbage in, garbage out
- Step 5: Will the diagram need more than Mermaid can express?
- Step 6: Calling the tool
- Step 7: After generation
- Reuse the same file when iterating or adding related diagrams
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP servers

## Risks / cautions found in text

- 2. If you want to replace the previous diagram rather than adding next to it, use the `use_figma` tool (see the `figma-use-figjam` skill) to delete the old diagram's nodes first, then call `generate_diagram` with the same `fileKey`. Or leave the old diagram and place the new one beside it — readers 

## Key rules (verbatim lines from SKILL.md)

1. - Edit a diagram node-by-node after generation
2. 2. **No `\n`** in labels. Use newlines only when absolutely required and only via actual line breaks (not the escape sequence).
3. 4. **Reserved words** — don't use `end`, `subgraph`, `graph` as node IDs.
4. 6. **Special characters in labels** must be wrapped in quotes: `A["Process (main)"]`, `-->|"O(1) lookup"|`.
5. 7. **Sequence diagrams** — Mermaid `Note over X` / `Note left of X` / `Note right of X` are silently stripped by the renderer; don't put them in the source. If the user wants annotations on a sequence diagram, generate the base diagram first and add stickies/text via the hybrid workflow ([references

## Files inside the skill

- `references/architecture.md` — "Architecture Diagrams"
- `references/erd.md` — "Entity-Relationship Diagrams"
- `references/flowchart.md` — "Flowcharts (non-architecture)"
- `references/gantt.md` — "Gantt Charts"
- `references/sequence.md` — "Sequence Diagrams"
- `references/state.md` — "State Diagrams"
- `references/workflow.md` — "Hybrid Diagram Workflow"
