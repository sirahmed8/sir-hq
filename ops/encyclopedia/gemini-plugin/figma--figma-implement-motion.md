# figma-implement-motion

## Summary
Skill for translating Figma animations into runnable code (motion.dev, CSS keyframes, or framework libraries like SwiftUI). It orchestrates two MCP tools by node id: `get_motion_context` is the authoritative source for the animated-node inventory, precomputed `codeSnippets` (CSS @keyframes + motion.dev), fallback `keyframeBindings`, `textAnimations` timing, and `timelineCohorts` for coordinated timelines; `get_design_context` supplies the structure (hierarchy, sizing, assets, Code Connect hints, motion placement markers). The job is merging motion values onto the right structural elements — exact `data-node-id` match wins, `fallbackNodeId` only for componentized children.

## When to use / when NOT
Use when the deliverable is motion CODE in the user's repo. Do NOT use for editing animations inside Figma (that is figma-use). Only covers what `get_motion_context` emits — interactive variant flows may still need hand-written state handling.

## Inputs, outputs, tools
- Inputs: Figma URL (fileKey + nodeId), target codebase/stack, existing motion conventions.
- Outputs: implemented animation code merged into the component's structure.
- Tools: `get_motion_context` (recursive:true, ≤500 nodes), `get_design_context`; reference docs: examples-and-anti-examples, gotchas (+motion-lint-rules), svg-and-path-motion, framework-recommendations, unsupported-and-fallbacks, motion-lint-rules; asset downloads via curl; ffmpeg-style local tooling not required.

## 5 most important rules
1. Use `codeSnippets` verbatim — never regenerate values from keyframeBindings (loses custom bezier/spring/overshoot fidelity); a missing field never means "no animation"; every returned node IS animated.
2. Match by exact nodeId/`data-node-id` first, `fallbackNodeId` only when exact lookup fails — exact wins because per-instance root motion differs and fallback points at the shared component body; componentized children usually need the fallback.
3. Preserve interleaved-transform nesting (`data-motion-wrapper-for` OUTER wrapper > static-transform div > INNER `data-node-id`): place transform tracks by `data-motion-keys`, re-apply `data-motion-transform-template`, and subtract the static base rotation to avoid double-rotation; keep layout translates off Motion-animated elements (split wrapper or encode in x/y).
4. Respect the user's existing motion stack (Framer Motion/GSAP/etc. — adapt, don't force motion.dev); honor `prefers-reduced-motion`; validate ONE animation end-to-end before batching; never fabricate motion for nodes without data (leave a TODO comment instead).
5. Download expiring asset URLs into the project and reference local files (never the temp URLs); for path-level SVG motion inline the SVG and animate the real `<path>`; factor repeated motion into one parameterized component/variants/constants — never paste the snippet per element.

## Risks / owner needs
Requires Figma MCP. Unsupported Figma motion (text/path/mask/variant transitions) has documented fallbacks incl. video/lottie — load unsupported-and-fallbacks before concluding data is missing. SwiftUI path is evolving — confirm with user when unsure.

## Category and tags
Category: design. Tags: figma, motion, animation, code-generation, mcp, motion-dev, css-keyframes.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
