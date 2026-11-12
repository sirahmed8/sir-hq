# build-gtk

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\build-gtk\SKILL.md`
- SKILL.md size: 18083 chars

## What it does

>- Builds node-based Editor tools with Unity Graph Toolkit (GTK) on Unity 6.6+: graphs, nodes, ports and validation, State Machine API tools on 6.7+, and runtime assets via a scripted importer. Use for custom graph, node or state machine editors, or migrating a GraphView tool. Not for Shader Graph, VFX Graph or Animator Controllers.

## When to use (from skill text)

- Derive from `Condition` directly for a valueless trigger. Group (And/Or) and variable conditions are

## Structure (headings inside SKILL.md)

- Unity Graph Toolkit (GTK)
- Important
- References
- Step 1: Check the Editor version and pick the API
- Mental model
- Workflow A: build a graph tool
- Workflow B: build a state machine tool (Unity 6.7 and newer)
- Editing a graph from code
- Decisions
- Constraints
- Verify
- Final report
- Topic map
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 3. With an importer, select the asset and confirm the produced runtime object is the main asset in

## Key rules (verbatim lines from SKILL.md)

1. - Do only what's asked. Don't change unrelated assets or files. Avoid long explanations.
2. - Before you go forward with a workflow or diagnosis, open and read the reference file(s) named in
3. - `references/pitfalls.md` — the mistakes that survive compilation. Read before handing off, and
4. - Graph Toolkit is an authoring framework only. It draws and persists graphs; it never executes them.
5. - Link to the Script Reference or manual instead of restating them, so the answer stays correct when

## Files inside the skill

- `references/graph-api.md` — "Graph API reference (Unity 6.6 and newer)"
- `references/pitfalls.md` — "Pitfalls that survive compilation, and the ones that do not"
- `references/runtime-and-visualization.md` — "From authored graph to runtime, and back"
- `references/state-machine-api.md` — "State Machine API reference (Unity 6.7 and newer)"
