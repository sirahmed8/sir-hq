# audio-setup-mixers

**Source:** `C:\Users\a7med\.gemini\config\plugins\unity\skills\audio-setup-mixers\SKILL.md` (+ `references/api.md`)
**Category:** media
**Tags:** unity, audio, mixer, editor-automation, routing, csharp

## Summary
A Unity Editor skill that inventories every Audio Mixer in a project and the groups inside it, classifies each Audio Source in the open scene by the sound it plays (Foley, SFX, Music, Dialogue, and so on), agrees a routing plan with the user, and then assigns each source's output group through the public Unity API. It deliberately cannot create mixers or groups because those authoring calls exist only on non-public controller types; the user adds missing groups in the Audio Mixer window. Routing lives on the Audio Source, so it is a scene edit and persists only when the scene is saved.

## When to use / when not to
Use it when the user wants to clean up mixer assignments, route audio through a mixer, decide which group a sound belongs in, or audit what is currently routed where. Do not use it to create mixers or groups, change group volume or effects, or re-parent groups (all non-public API), and do not use it when no live Editor with `script eval` is available: the skill stops rather than hand-editing `.mixer` files.

## Inputs, outputs, tools
Inputs: a live Unity Editor connected through the `unity-cli` skill, `script eval` present in the Editor command catalog, the project's Audio Mixer assets and scene Audio Sources. Outputs: a mixer/group inventory, a proposed source-to-group routing, the routing applied in a single undo step, and a report of `NO SUCH GROUP` and `NOT IN THE MAPPING` entries. Tools: the `unity-cli` skill and `unity command script eval` (requires the Pipeline package). No MCP.

## Five most important rules
1. Confirm `script eval` appears in the Editor command catalog before anything else; if it is missing, say so and stop.
2. Never create mixers or groups programmatically and never hand-edit `.mixer` files; ask the user in the Audio Mixer window, then re-run the inventory to confirm the groups exist and are spelled as expected.
3. Classify from the clip asset name first and fall back to the GameObject name; key the routing mapping on whichever identifier you actually classified by, or sources are silently dropped.
4. Wait for the user to approve the proposed routing before writing, and do not collapse categories a mixing engineer would keep apart (Foley is a subset of SFX, not a synonym).
5. Report unmatched sources and missing groups explicitly, and tell the user the scene was modified and must be saved.

## Risks and owner actions
Routing modifies the open scene and needs the user to save it; an unreachable Editor is a stop, not a cue to improvise. No secrets or owner credentials are involved.

## Revisions
Two copies exist (the installed plugin and the marketplace cache for unity 0.1.9-beta), both 7553 bytes and byte-identical. There is no meaningful revision difference.
