# figma-use-motion

## Summary
Motion addendum to figma-use: the time dimension of the Figma Plugin API via `use_figma` — manual keyframe tracks (`manualKeyframeTracks`, `applyManualKeyframeTrack`, `removeManualKeyframeTrack`), animated fill/stroke, animation styles (`applyAnimationStyle`, `figma.motion.figmaAnimationStyles()`), local custom animation styles, native `TextStagger` for within-text animation, timeline duration read/write, and easing. Verification is the hard part: `get_screenshot` shows only the resting state, so motion must be checked via `export_video` frame sampling.

## When to use / when NOT
Load (with figma-use, passing `skillNames: "figma-use-motion"`) whenever a use_figma task touches keyframes, animated colors, animation styles, text reveals/typewriter effects, or timeline duration. Static design work does NOT need it. Custom `"figma:motion"` preset module authoring is out of scope.

## Inputs, outputs, tools
- Inputs: target nodes (never top-level frames — animate descendants), desired motion (keyframes, styles, text stagger, duration in seconds).
- Outputs: mutated nodes with returned IDs, applied/removed animation styles, timeline durations.
- Tools: `use_figma` motion APIs; `export_video` (top-level frame only, returns jobId, slow/expensive ~10s-minutes) + local `ffmpeg -ss <t> -i anim.mp4 -frames:v 1` for frame extraction; reference docs motion-patterns, motion-custom-styles, text-animation, motion-easing.

## 5 most important rules
1. Motion APIs are runtime-gated: on `"<name>" is not a supported API` bail out immediately — no retries; custom animation styles may be gated even when other motion works.
2. Easing uses public shapes only: `{ type: 'EASE_OUT', easingFunctionCubicBezier/Spring }`, exact enum `EASE_IN_AND_OUT` (never `EASE_IN_OUT`); transform fields use public names (TRANSLATION_X, ROTATION, SCALE_XY), never internal MOTION_* names; keyframe fields come from the documented allowlist.
3. Animate descendants, never a top-level frame; extend timelines via `setTimelineDuration`, never shorten unless asked; return all mutated node IDs.
4. Text motion = discovered `TextStagger` on the existing text node (discover via `figma.motion.figmaAnimationStyles()` first; absent = explain unavailability, never substitute whole-layer motion); `duration` is total stagger span, not per-character.
5. Verify motion by export_video, not screenshots: plan 4-6 frames at the needed phases, render small (WIDTH 320-768, quality low, fps 5-10), extract frames with ffmpeg, batch all fixes into one pass before re-rendering; skip export for trivial changes.

## Risks / owner needs
Motion features may be disabled per-account — the skill treats that as a hard stop. export_video is slow and costly; misuse burns time. Requires authenticated Figma MCP.

## Category and tags
Category: design. Tags: figma, motion, animation, keyframes, mcp, plugin-api.

## Revisions
Single gemini-plugin figma copy; no competing revisions.
