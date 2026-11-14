# audio-setup-mixers

Source read: `C:\Users\a7med\.gemini\config\plugins\unity\skills\audio-setup-mixers\SKILL.md` (gemini-plugin unity revision, the only copy) plus references/api.md and SECURITY.md presence noted.

## Summary
A Unity Editor skill that routes Audio Source components into existing Audio Mixer Groups. It is deliberately narrow: inspecting mixers and assigning output groups is public Unity API (the tedious part it automates), but creating mixers or groups has no public API, so the skill inventories what exists, proposes a routing, asks the user to create any missing group in the Audio Mixer window, then performs all routing itself through C# executed inside a live Editor via the Unity CLI `script eval` command. Classification is by clip asset name first (e.g. "FootStep4_Sound" -> Foley, "GunShot" -> SFX, "Menu_Theme_Variation" -> Music), falling back to GameObject/MonoBehaviour names, with an "Uncategorized" escape hatch.

## When to use / when NOT
Use when the user asks to clean up mixer assignments, route audio through a mixer, or decide which group a sound belongs in — typically on a project that already has an Audio Mixer with groups. Do NOT use it to create mixers or groups (no public API — the skill will stop and ask the user), to set volumes/effects/re-parenting (non-public API, out of scope), or when no live Editor with `script eval` is available.

## Inputs, outputs, tools
- Inputs: a Unity project with a running Editor reachable through the Unity CLI (`com.unity.pipeline` package), an existing .mixer asset with named groups, Audio Sources in open scenes.
- Outputs: scene edits assigning each Audio Source's output AudioMixerGroup, wrapped in a single undo step; a report of routed, `NO SUCH GROUP`, and `NOT IN THE MAPPING` sources.
- Tools: Unity CLI `unity command script eval --caller plugin --skill audio-setup-mixers --code '<snippet>'` (parameter shape discovered via `unity command --format json`; `script eval_file` often absent), the `unity-cli` skill for Editor connectivity, references/api.md for the inventory and routing snippets. MCP: none.

## 5 most important rules
1. **Step 0 gate: confirm `script eval` exists in the Editor command catalog first** — a reachable Editor can still lack it depending on Pipeline package version; if missing, stop. Never fall back to hand-editing `.mixer` files.
2. **`script eval` takes a statement block, not a file** — no `using` directives (CS0210) and all types fully qualified (CS0246/CS0103/CS0104); qualify types from the api.md snippets before passing.
3. **WAIT for user approval of the proposed routing before assigning** — and re-run the inventory after the user creates missing groups to confirm names/spelling.
4. **Never collapse categories a mixing engineer keeps apart** — Foley is a subset of SFX, not a synonym; prefer existing groups only when they genuinely cover the category.
5. **Report honestly**: `NO SUCH GROUP` (spelling mismatch — resolve with user), `NOT IN THE MAPPING` (missed sources — never claim success while sources are unrouted), and remind that routing lives on the scene's Audio Source, persisting only when the scene is saved (with user agreement).

## Risks / owner notes
Requires a live Unity Editor on the machine — cannot run headless or in CI. Scene edits are real modifications; save only with user consent. Do not reach for reflection or private APIs to create groups — the skill explicitly forbids it.

## Category / tags
build · unity, audio, mixer, csharp, game-dev, editor-automation

## Revisions
Single revision (gemini-plugin unity). Not present in claude/codex/cursor/kilo/windsurf/opencode — canonical and only source.
