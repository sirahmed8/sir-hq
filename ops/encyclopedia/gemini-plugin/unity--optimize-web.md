# optimize-web

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: design
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\optimize-web\SKILL.md`
- SKILL.md size: 38668 chars

## What it does

Optimizes Unity WebGL and WebGPU builds for smaller downloads, faster loading, and smoother browser performance. Use when asked to shrink a web build, speed up its load, or fix stutter, memory or battery problems in the browser.

## When to use (from skill text)

- | Compression | Use when | Notes |
- ### Memory growth slow path triggered

## Structure (headings inside SKILL.md)

- Important
- Performance Notes
- Full topic map
- API reference
- Procedure
- Running C# in the Editor
- Passing C# to `script eval`
- Reading the settings this skill audits
- Applying the settings
- Verify from disk, not from the objects you just wrote
- 0. Pre-Flight
- 1. Assess Current State
- 2. Understand Request
- 3. Web Build Optimization Workflow
- IMPORTANT: One-click optimization script
- Player Settings audit
- Compression and server configuration
- Exception handling
- Remove unused resources
- Quality settings for Web
- Frame rate on Web
- KTX / Basis Universal textures
- Streaming on Web
- Profiling Web builds
- Web memory directives
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - Use `OnDemandRendering.renderFrameInterval` to drop to 5–10 fps on static/idle screens to save battery.
- - WASM heap > 300 MB risks crashes on older iOS; target < 200 MB for broad compatibility.

## Key rules (verbatim lines from SKILL.md)

1. - Before making changes, establish a baseline of the current behavior so you can tell whether a later result is actually caused by your change.
2. - Do only what's asked. Don't change unrelated assets or files.
3. - Avoid long explanations.
4. 4. Grep the yml file locally for a class or method instead of refetching per lookup. The file is large (about 6 MB), so don't read the whole file.
5. - Links inside the pages start with `/engine/`. Add `https://docs.unity.com/en-us` before them.

## Files inside the skill

- `scripts/toktx-examples.sh`
- `scripts/WebOptimizer.cs`
- `SECURITY.md` — "Security notes: optimize-web"
