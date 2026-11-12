# ui-plugin-navigation (gemini antigravity builtin)

## Summary
A small Antigravity/Gemini-CLI builtin skill for surfacing clickable "pills" in chat that open UI plugin panels in the side pane. UI plugins and UI extensions are the same thing: sidecar-backed web panels rendering in the auxiliary pane. The skill has two trigger situations: (1) contextual relevance — read enabled UI plugins' description/display_name and offer a pill when a panel would genuinely help the current task; (2) right after the user enables a new UI plugin pane, include a pill so they can open it immediately. Mechanics: find sidecars under `~/.gemini/config/sidecars/<id>/`, `~/.gemini/<app>/builtin/sidecars/`, or plugin `sidecars/` dirs (plugin sidecars are namespaced `<plugin>/<folder>`); check `sidecar.json` for `has_web_ui: true` and a `ui_config.views` entry with `entrypoint: SIDECAR_UI_ENTRYPOINT_AUX_PANE`; take `path` as view-path and title/display_name for the label; emit `[Label](sidecar://<sidecar-id>/<view-path>)` markdown. The pill toggles the pane — only for enabled AND running plugins.

## When to use / when NOT
This is ambient behavior, not a user-invoked tool: surface a pill when a running UI plugin's panel matches the task, or after a new pane is enabled. Do NOT force pills when nothing matches, repeat dismissed pills, emit multiple links to the same view, or link plugins that aren't enabled/running.

## Inputs, outputs, tools
- Inputs: filesystem scan of sidecar.json files under the Gemini config/plugin dirs.
- Outputs: one markdown link per relevant panel in the chat reply.
- Tools: read-only file inspection; no scripts or MCPs.

## 5 most important rules
1. Relevance is judged from the plugin's own description/display_name — never guesswork.
2. Only AUX_PANE views of enabled, running plugins get pills; the pill toggles the pane.
3. Plugin sidecar ids are namespaced `<plugin>/<folder>`; plain sidecars use the folder name.
4. One pill per pane; don't repeat what the user already opened or dismissed.
5. `has_web_ui` must be true AND a view must use the AUX_PANE entrypoint — a sidecar without both has no panel to link.

## Risks / things needing the owner
Minimal risk: worst case is a useless or dead link if the sidecar stopped between scan and click. No owner actions.

## Category / tags
ops · antigravity, gemini, ui-plugins, sidecar, navigation

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\antigravity\builtin\skills\ui-plugin-navigation\SKILL.md`. No divergent copies.
