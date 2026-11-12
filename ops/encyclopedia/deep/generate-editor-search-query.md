# generate-editor-search-query (Unity plugin)

## Summary
Unity plugin skill that translates natural-language "find/search/locate/list/filter" requests into Unity Search query syntax and opens the Editor's Search window with it. Scope is strictly read-only asset/scene-object search (materials, textures, prefabs, scenes, scripts, shaders, Lights, Rigidbodies, Canvas/UI, named GameObjects, path/label/type/filename/keyword/ref searches). Default behavior: build ONE concise query, show it to the user, and open Search via an Editor-side C# snippet unless the user asked for query text only; if opening fails, hand over the query to paste manually. Query rules: simplest possible query, `t:` type filters, `dir:` folders, `l:` labels, `ref=`/`{t:...}` expressions for reference searches, never invent unsupported filters — open the closest safe query and state the limitation. Has a SECURITY.md documenting the accepted risk of running C# in the user's Editor via `unity command script eval`.

## When to use / when NOT
Use for "find assets/objects in the Unity project" requests. NOT for general explanations, architecture walkthroughs, repo text search, build logs, package installs, or any modification — results are never acted on without separate confirmation.

## Inputs, outputs, tools
- Inputs: natural-language search request, optional asset/scene names or paths from context.
- Outputs: a Unity Search query string shown to user + Search window opened in Editor.
- Tools: Unity Search query syntax, `unity command script eval` (requires unity-cli skill prerequisites: CLI installed, Editor connected, com.unity.pipeline package), references/query-patterns.md and open-search-window.md.

## 5 most important rules
1. Read-only forever: the C# snippet ONLY opens the Search window — never select/rename/delete/move/import/edit/save anything; modifying results needs a separate confirmed workflow.
2. `script eval` compiles a statement block, not a file: NO `using` directives (CS0210), all types fully qualified (bare SearchService → CS0246, bare Object → CS0104).
3. Base64-encode the query (UTF-8) before embedding in C# — base64 alphabet contains no quotes, so query text can never break out of the string or shell quoting; decode inside the snippet.
4. Ambiguity handling: "this/selected/current" without a name/path → ask; don't invent targets. Search-opening opt-outs ("query only", "do not open") must be honored; never claim Search opened if the command failed.
5. Dependencies: needs the unity-cli skill's prerequisites (CLI + connected Editor + com.unity.pipeline); if `script eval` is absent, output query text only and say the window can't be opened.

## Risks / owner needs
Runs C# inside the user's open Editor — accepted risk documented in SECURITY.md (local machine, user's own session, capability-gated, no remote code). Requires Unity Editor running with Pipeline package; on headless/CI there's no Editor to drive.

## Category and tags
Category: build. Tags: unity, editor, search, csharp, game-dev, read-only, query-generation.

## Revisions
Single gemini-plugin unity copy; no competing revisions.
