# initialize-ai-navigation (unity plugin)

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\initialize-ai-navigation\SKILL.md` (5.3 KB; unity plugin; `references/navigation-system.md` holds component details, API notes, recipes, troubleshooting).

## Summary
Setup guide for Unity AI Navigation (`com.unity.ai.navigation` package): NavMesh surfaces, agents, obstacles, links, modifiers, and movement scripts. It routes user intent via a phrase table ("add navigation" → full setup; "agent won't move" → troubleshooting tree; "patrol"/"click to move"/"animate while navigating" → specific recipes). Workflow: verify/install the package in `manifest.json` (never invent the version — read `packages.unity.com/com.unity.ai.navigation` or copy an adjacent version, since a bad version fails resolution silently), pre-flight inspect existing NavMesh components (live scene query via unity-cli or file search), gather missing info (walkable surfaces, agent size/type, behavior, obstacles, links, areas/costs), execute in order (surface+bake → agent → obstacle → link → modifier → scripts), then validate (blue bake overlay, matching agent types, valid paths, carve behavior, connected links, area masks, no Rigidbody kinematic conflicts) and summarize everything created plus manual steps.

## When to use / when NOT
Use for any Unity navigation/pathfinding task: navmesh setup, patrol routes, obstacle avoidance, area links, agent sizing, animation coupling. Not for non-Unity engines or pure animation work without navigation.

## Inputs, outputs, tools
- Inputs: user description of navigation need, scene/prefab files or live Editor (unity-cli skill) for inspection.
- Outputs: configured NavMeshSurface/Agent/Obstacle/Link/Modifier components plus movement/patrol/click-to-move scripts, and a summary of manual steps (rebake, waypoint tuning).
- Tools: Unity Editor, `com.unity.ai.navigation`, `script eval` for live C# (with the fully-qualified-type caveat), packages.unity.com for versions.

## 5 most important rules
1. Package check FIRST: `com.unity.ai.navigation` must be in manifest.json; never guess the version string (silent resolution failure).
2. `script eval` compiles a statement block, not a file: no `using` directives, all types fully qualified.
3. Pre-flight: inventory ALL existing nav components before proposing changes; summarize before acting.
4. Execution order is fixed: surface+bake → agent → obstacle → link → modifier → scripts.
5. Validate everything (bake visible, agent-type match, paths valid, links connected+activated, masks correct, Rigidbody IsKinematic) and report manual leftovers honestly.

## Risks / owner notes
Baking is Editor-side; scene changes require rebake. Wrong agent-type matching produces agents that silently can't path. Live-Editor automation needs the unity-cli skill and an open Editor.

## Category and tags
Category: mobile. Tags: unity, navigation, navmesh, pathfinding, ai-navigation, package-setup.
