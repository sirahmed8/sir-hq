# build-gtk

Tools: gemini (antigravity plugin). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\build-gtk\SKILL.md (read in full) + references/graph-api.md, state-machine-api.md, runtime-and-visualization.md, pitfalls.md

## Summary
Unity Graph Toolkit (GTK) authoring framework for Editor graph and state-machine tools on Unity 6.6+/6.7+: define Graph/StateMachine assets, Node/State/Condition classes, ports, options, validation, and compile authored graphs into plain runtime assets via a ScriptedImporter. Authoring-only framework; you write the runtime data model and executor. Discovery is by reflection; never use retired GraphModel/Stencil/GraphView APIs.

## When to use / not use
Use for custom graph, node, context/block, subgraph, blackboard-variable, or state-machine editors, or migrating a GraphView tool, on Unity 6.6+ (state machines require 6.7+). NOT for Shader Graph, VFX Graph, Animator Controllers, or runtime execution (GTK has no runtime).

## Inputs, outputs, dependencies
Input: Unity project with Editor version; desired graph/state-machine tool. Output: Editor assembly classes (Graph, Node, State, Condition, importer) plus a runtime asset at import. Needs: Unity 6000.6+ (6.7+ for state machines); no package install (built-in module); runtime asmdef must not reference Unity.GraphToolkit.Editor.

## Key rules
1. Read ProjectVersion.txt first; the State Machine API does not exist before 6000.7 — say so plainly, do not emulate with the Graph API.
2. Every authoring class is [Serializable] in an Editor-only assembly; use public API names exactly (Graph, Node, IPort, State, Condition<T>); IDs are Hash128.
3. End every port builder chain with .Build(); use .Delayed() on count-like options; ports accept multiple wires by default, so declare .WithCapacity(PortCapacity.Single) when one wire is wanted.
4. Validate in OnGraphChanged/OnStateMachineChanged with the logger; never mutate there; put fixes in GraphLogAction, menu items, toolbar buttons, or the importer.
5. Importers use LoadGraphForImporter/LoadStateMachineForImporter then SetMainObject(runtime); runtime assemblies stay free of Unity.GraphToolkit.Editor; guard visualization code with #if UNITY_EDITOR.
6. For a runtime debug view use the GraphVisualization API keyed by the authored Graph.ID and node/port/wire Hash128 IDs; dispose the context when the run ends.

## Risks / owner items
- com.unity.graphtoolkit is a deprecated shim; never add it to the manifest.
- Mutating a graph in OnEnable/OnDisable/OnGraphChanged throws InvalidOperationException.
- GraphChanges (added and modified only) never reports removed nodes; diff a cached HashSet<Hash128> on every version.
- Custom UI (NodeView/StateView/ConditionView): allocate in OnViewBuilt, re-add in OnCullingChanged(false), never in OnViewAttached.
- Importer results are cached per version; bump the ScriptedImporter version to force reimport.

## Category and tags
unity, editor, graph-tool, state-machine, scripted-importer, build.

## Revision note
Single gemini revision covering 6.6 Graph API and 6.7 State Machine API; references read in full.
