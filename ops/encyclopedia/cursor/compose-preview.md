# compose-preview

## Summary
Instructions for the Android Compose Preview sidecar (android-cli plugin): a local loopback web server that renders Compose `@Preview` functions via `android preview render` and displays them in the IDE's Android Compose Preview pane. The agent configures sessions over HTTP (`POST /api/session` with `wait: true`), discovers FQNs via `android preview list`, re-renders after edits, and can inspect the JSON component tree (semantics, modifiers, parameters, source locations) without parsing pixels.

## When to use / when NOT
Use when the user wants to see Compose previews or review UI changes in Android projects — always re-render after code edits so the pane shows current results. Do NOT run `android preview render` directly in the shell; the sidecar owns it. Not for non-Compose UI or non-Android platforms.

## Inputs, outputs, tools
- Inputs: `project_dir`, `reference` (`[system://]path?target`, e.g. `gradle://.?:app@debug`, variants flavors-first like `demoDebug`), `fqns` list, optional `build_args`.
- Outputs: rendered PNGs under `<output_dir>/<fqn>/`, job status/output, `GET /api/state` per-preview config (night mode, font scale, device), component-tree JSON.
- Tools: sidecar HTTP API (`/api/session`, `/api/render`, `/api/state`, `/api/settings`, status endpoint), `android preview list`, `android preview render` (sidecar-run only). Port changes on every sidecar restart; loopback only; `X-Sidecar-Conversation` header required.

## 5 most important rules
1. Agree with the user on which previews to render — never guess silently when several modules/previews match.
2. Never batch a render in the same parallel call batch as an edit — it may build old code; render only after edits are saved.
3. Do not run `android preview render` yourself or probe `--help`; wrong references fail fast via job `output` — fix args and re-POST /api/session.
4. Image filenames don't reveal configuration — read `configuration` in /api/state; numbered images have no guaranteed order.
5. Render only requested previews (each render costs build time); report failures with the relevant output lines instead of silently retrying.

## Risks / things needing the owner
Renders run real Gradle/Bazel builds — first render can be slow. `--daemon` keeps a renderer alive 10 min idle; `--component-tree` is on by default and writes JSON next to images. Settings changes should only happen when the user asks.

## Category / tags
mobile · android, compose, preview, sidecar, tooling

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude copy); codex copy chosen (newest/first listed), all 12968 bytes — identical across tools.
