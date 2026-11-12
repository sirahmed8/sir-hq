# validate-urp-render-graph-renderer-feature (gemini-plugin: unity)

## Summary
A code-review skill, not a generator: it validates a Unity 6+ URP Render Graph `ScriptableRendererFeature` and its pass for correctness before integration — especially AI-generated code. Inputs required: Unity version, URP version, the feature/pass code, intended behavior, optional constraints. Output is a fixed 6-section review: Validation Summary, Confirmed Issues, Likely Issues/Risky Assumptions, Recommended Fixes, Corrected Snippets, Missing Information — deliberately separating confirmed from likely issues to avoid false certainty. The 8-part checklist covers: material binding (all required textures bound before execution, primary input texture explicitly bound, property names match shader), texture resource wiring (UseTexture for reads vs SetRenderAttachment for writes, no confused roles), execution structure (render function MUST be static, every PassData field explicitly assigned each recording — pooled stale handles are a named hazard), Render Graph descriptors (prefer `GetDescriptor(renderGraph)` from an existing graph resource over hand-built TextureDesc; only override fields that differ), simplification (don't write custom raster passes for plain copies — use AddBlitPass/AddCopyPass helpers), global resource exposure (no SetGlobalTextureAfterPass or cmd.SetGlobalTexture unless a real downstream consumer exists — it extends lifetime and kills aliasing), and ConfigureInput declarations (declare needed pipeline inputs, don't request unused ones that force extra copies).

## When to use / when NOT
Use when reviewing or validating URP Render Graph renderer feature code — typically AI-generated or unfamiliar code — before integrating. Do NOT use to write a renderer feature from scratch, to validate unrelated gameplay/shader internals, or to guarantee runtime correctness (it reviews code, it doesn't execute it).

## Inputs, outputs, tools
- Inputs: Unity/URP versions, feature + pass source, intended behavior, constraints.
- Outputs: the structured 6-section review with minimal targeted fixes, not rewrites.
- Tools: none — pure analysis skill; no scripts or MCPs.

## 5 most important rules
1. Render function must be `static`; instance-state access where static is expected is a confirmed issue.
2. EVERY PassData field used must be assigned during each RecordRenderGraph — partial init of pooled pass data leaves dangling handles.
3. Source TextureDesc from `resourceData.activeColorTexture.GetDescriptor(renderGraph)` and modify only needed fields; fresh TextureDesc is a flag unless justified.
4. No global exposure by default: `SetGlobalTextureAfterPass`/`cmd.SetGlobalTexture` only with a proven consumer — hidden coupling and memory pressure otherwise.
5. Declare inputs with ConfigureInput exactly matching use; unnecessary declarations cost copies/perf and are higher severity.

## Risks / things needing the owner
Review quality depends on provided context — the skill must state when code is insufficient for certainty rather than invent APIs. Misclassified severity (confirmed vs likely) is the main failure mode. No owner actions.

## Category / tags
build · unity, urp, render-graph, code-review, validation

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\validate-urp-render-graph-renderer-feature\SKILL.md`. No divergent copies.
