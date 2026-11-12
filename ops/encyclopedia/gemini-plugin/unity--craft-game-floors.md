# craft-game-floors (Unity)

## Summary
The "craft layer" for agent-built Unity games: 12 opinionated floors (art direction, scene lighting, toon shading, camera rigs, placeholder assets, character motion, game feel, VFX, audio, game shell, live-floor services, visual scorecard) each backed by a reference doc with concrete values, worked examples and a verify step. It enforces an art bible and mixer handshake up front, routes to neighbour skills for pure mechanics, and ends every session with a scored six-axis visual board — "floors, not features": defaults the user can decline but never argued with.

## When to use / when NOT
Use when creating a new game's first playable or when a game looks like programmer art / feels flat / needs polish ("fix the look", "add sound", "score it"). Assessment-only asks get scores, not changes. Do NOT use for pure mechanics on existing setups — those route to neighbours (urp-postprocessing, ui, optimize-audio, 2d-pixel-perfect, etc.). 2D look floor is explicitly not covered yet.

## Inputs, outputs, tools
- Inputs: the game/project, the user's craft ask; mid-flow it restores a commit, detects render pipeline (URP-typed verifies), finds/creates the art bible, probes player identity.
- Outputs: applied floors, a scored visual board (six axes, all ≥3), zero console errors, play-mode check.
- Tools: Read/Write/Edit/Bash; 12 reference docs under `references/`; versioned Unity docs fetched per project version (6000.x stream, package versions from manifest.json).

## 5 most important rules
1. Read the matching reference AND its linked Unity docs before acting — engine knowledge may be stale; name files read in the report.
2. Floors fill engine defaults, never override a developer's existing controller/camera/shader/palette.
3. Order matters: art bible before lighting/materials; loop before content; scorecard always last as the done gate.
4. Scope the done gate to the surface touched; a title-screen session scores shell+look axes only.
5. A declined floor is recorded in the report, never argued; skipped coverage (2D look) is named, not faked.

## Risks / things needing the owner
Writes real project files and may install packages (TMP Essentials etc.) — report every side effect. First playable creation is a large autonomous build; owner should review the scorecard board. URP-specific verifies don't apply on Built-in/HDRP.

## Category / tags
build · unity, game-dev, art-direction, polish, quality-gates

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\unity\skills\craft-game-floors\SKILL.md` with 12 reference docs. Only gemini-plugin holds it.
