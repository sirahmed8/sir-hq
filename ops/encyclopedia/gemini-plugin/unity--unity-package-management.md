# unity-package-management (gemini-plugin: unity)

## Summary
unity-package-management adds, removes, upgrades and discovers Unity UPM packages from outside the Editor — Pipeline `package` commands first (`unity command package add/remove/list/resolve/search/status` after `unity pipeline install` + open + `--until-ready`), falling back to a C# `UnityEditor.PackageManager.Client` script run in batch mode only when no Editor can answer. Hard rule: never hand-edit `Packages/manifest.json` — manual edits break dependency resolution. The fallback has a critical trap: `Client.AddAndRemove` is async and needs EditorApplication.update ticks, so `unity run` cannot be used (its injected `-quit` quits before UPM resolves); instead launch the Editor binary directly in `-batchmode` WITHOUT `-quit` and let the script call `EditorApplication.Exit(code)`. Also covers package selection guidance (references/select-packages.md maps genre/platform/monetization to package ids), verifying via manifest.json, and a synchronous `ProjectSaver` for headless .meta generation (unity run IS safe here since it's synchronous).

## When to use / when NOT
Use to add/remove/upgrade/discover UPM packages non-interactively or in CI. Do NOT hand-edit manifest.json, do NOT use `unity run` for installs, and prefer the Pipeline commands whenever an Editor can run them.

## Inputs, outputs, tools
- Inputs: package ids (optionally `@version` pins), project path.
- Outputs: updated Packages/manifest.json, resolved package list; Editor logs via `-logFile -`.
- Tools: `unity` CLI, Editor binary direct invocation, C# scripts written to Assets/Editor/ProjectBootstrap/. references/select-packages.md.

## 5 most important rules
1. Never edit Packages/manifest.json by hand — resolution breaks.
2. Read the command schema before calling (`unity command --query package`); parameter names come from the Editor.
3. Fallback requires the project CLOSED in every Editor (`unity editors running --format json` + UnityLockfile check); never kill the user's Editor — ask them to save and close.
4. `-quit` deadlocks async UPM: direct Editor binary + `-batchmode` + no `-quit`; script polls on EditorApplication.update with a 600s timeout and exits 0/1/2.
5. Add all packages in ONE `Client.AddAndRemove` pass; pin with `@version`; verify by reading manifest.json afterwards.

## Risks / things needing the owner
The batch fallback can fail on project locks — the skill insists on asking the user to close the Editor rather than force-killing (unsaved scenes risk). Large package downloads are slow (600s timeout). Editor scripts under Editor/ never ship in builds. Nothing needs the owner beyond closing an open Editor when asked.

## Category / tags
build · unity, upm, packages, ci, csharp

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\unity\skills\unity-package-management\` with references/select-packages.md. No divergent copies.
