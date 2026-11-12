# shader-graph-create-custom-node

Tools: gemini-plugin (unity). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\shader-graph-create-custom-node\SKILL.md (25 lines, read in full) + resources/all_hints.hlsl

## Summary
Generates custom Unity Shader Graph nodes from HLSL: write a function preceded by `UNITY_EXPORT_REFLECTION`, decorate with sg: hint tags (ProviderKey, SearchCategory, SearchTerms, DisplayName required), then append to an existing ShaderInclude .hlsl asset (asking confirmation first) or create a new one starting with `#include "ShaderApiReflectionSupport.hlsl"`.

## When to use / not use
Use when the user wants a new Shader Graph node or to expose existing HLSL as a reflected function node in a Unity project with com.unity.shadergraph >=17.5.0. NOT for standard surface/shader authoring without custom nodes, or non-Unity render pipelines.

## Inputs, outputs, dependencies
Input: HLSL function code + desired node metadata. Output: a .hlsl ShaderInclude asset containing the reflected function. Needs: Shader Graph package, resources/all_hints.hlsl for valid hint tags, an existing or new .hlsl asset in the project.

## Key rules
1. `UNITY_EXPORT_REFLECTION` preprocessor define MUST precede the function — without it the function won't appear as a node.
2. Four required function hints: sg:ProviderKey, sg:SearchCategory, sg:SearchTerms, sg:DisplayName — check all_hints.hlsl for the full valid set and C#-style doc tag support.
3. Search for an existing ShaderInclude .hlsl asset with custom nodes first; if found, show contents and get user confirmation before APPENDING; only create a new asset when none exists.
4. New assets MUST begin with `#include "ShaderApiReflectionSupport.hlsl"` — the reflection plumbing depends on it.
5. Hint tags live in funchints/paramhints blocks; C#-style doc comments are supported outside those blocks per all_hints.hlsl.

## Risks / owner items
- Minimal skill (25 lines): no guidance on node behavior correctness, performance, or URP/HDRP compatibility — validation is manual in the Shader Graph editor.
- Appending to a shared .hlsl affects every graph using that include — confirmation step exists precisely because the blast radius is project-wide.
- Unity version/package drift: hints format may change across Shader Graph versions.

## Category and tags
build — unity, shader-graph, hlsl, rendering, custom-nodes.

## Revision note
Single plugin revision; terse procedural skill delegating tag vocabulary to resources/all_hints.hlsl.
