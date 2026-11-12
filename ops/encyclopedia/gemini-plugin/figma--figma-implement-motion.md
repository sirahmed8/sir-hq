# figma-implement-motion

- Tool: `gemini-plugin` (plugin: `figma`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\figma\skills\figma-implement-motion\SKILL.md`
- SKILL.md size: 23477 chars

## What it does

Translate Figma motion.

## When to use (from skill text)

- - Use this skill when the deliverable is motion code in the user's repository.

## Structure (headings inside SKILL.md)

- Implement Motion
- Overview
- Skill Boundaries
- Prerequisites
- Tool Choice
- Required Workflow
- Step 1: Confirm static design context is available
- Step 2: Fetch authoritative motion data
- Step 3: Merge static and motion context
- Step 4: Apply the motion in code
- Step 5: Validate
- Critical Rules
- Framework Recommendations
- Examples
- References
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP server

## Risks / cautions found in text

- - This skill currently covers **animations** as emitted by `get_motion_context` (snippets plus fallback keyframe tracks, including preset-authored motion resolved into those forms). Broader interactive variant flows may still need product-specific state handling in code.
- - [references/examples-and-anti-examples.md](references/examples-and-anti-examples.md) — worked examples and failure patterns. Load when applying the merge workflow, handling interleaved transforms, or checking whether a generated implementation has rebuilt the DOM, swapped node positions, or droppe
- - [references/motion-lint-rules.md](references/motion-lint-rules.md) — Linting rules: known export limitations (errors and warnings) that must be surfaced to the user. Load when generating motion code to check whether any active limitations apply.

## Key rules (verbatim lines from SKILL.md)

1. - Node ID parsed from the Figma URL the user provides. URL format: `https://figma.com/design/:fileKey/:fileName?node-id=1-2` — extract `fileKey` (the segment after `/design/`) and `nodeId` (the value of the `node-id` query parameter, e.g. `42-15`).
2. - `codeSnippets` — pre-generated CSS `@keyframes` and motion.dev strings. **Use these directly.** Do not regenerate them from fallback track data.
3. - `textAnimations` — Always implement these text-group animations. If `codeSnippets` are also present, apply both; the snippet does not replace `textAnimations`.
4. - Use `derivedTimingInfo`: each group starts at `startMs + orderPosition * staggerStepMs` and plays for `groupDurationMs`. `startMs` already includes `delayMs`; do not add it again. `presetDurationMs` covers the full staggered sequence, not each group.
5. - Compute `orderPosition` from `grouping` and `order`, not always the character index (`CENTER_OUT` starts symmetric pairs together). Convert milliseconds to seconds for Motion.dev, and fit the supplied easing into `groupDurationMs`, including springs.

## Files inside the skill

- `references/examples-and-anti-examples.md` — "Examples and Anti-Examples"
- `references/framework-recommendations.md` — "Framework Recommendations"
- `references/gotchas.md` — "Figma Motion Gotchas"
- `references/motion-lint-rules.md` — "Motion lint rules"
- `references/svg-and-path-motion.md` — "SVG and Path-Level Motion"
- `references/unsupported-and-fallbacks.md` — "Unsupported Features and Fallbacks"
