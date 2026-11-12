# optimize-web

Tools: gemini-plugin (unity plugin). Source: C:\Users\a7med\.gemini\config\plugins\unity\skills\optimize-web\SKILL.md (530 lines) + scripts/WebOptimizer.cs, scripts/toktx-examples.sh

## Summary
A rigorous audit-and-apply workflow for shrinking and speeding up Unity WebGL/WebGPU builds: Player Settings (Brotli compression, managed stripping High, Wasm 2023, exceptions, memory), server header requirements, shader/package stripping, KTX2/Basis textures, Addressables streaming, browser profiling, and iOS Safari memory limits. Nearly everything runs through a live Editor via `unity command script eval`, with a critical verify-from-disk discipline.

## When to use / not use
Use for "build too large", "download too slow", browser stutter, battery, memory, or Web-specific issues in a Unity project. Requires a reachable Editor with `script eval`; without one it falls back to docs-based recommendations and marks build/runtime checks unperformed.

## Inputs, outputs, dependencies
Input: a Unity project (version read from ProjectVersion.txt) plus a stated optimization goal. Output: applied Player Settings, optional WebOptimizer.cs menu script, validated build with before/after sizes. Needs: unity-cli skill, `com.unity.pipeline`, docs lookup discipline (local Documentation folder or versioned docs.unity.com pages — never training knowledge).

## Key rules
1. Baseline first (Pre-Flight snippet reads all settings), create a restore point, do only what's asked.
2. THE trap: applying a setting and reading it back in the same session proves nothing — Player Settings are in-memory until `AssetDatabase.SaveAssets()`. Verify `ProjectSettings.asset` on disk; `codeOptimization` lives in gitignored `Library/` and must be applied in CI.
3. Release matrix: Brotli (HTTPS) / Gzip (HTTP), Decompression Fallback off if server sends Content-Encoding, Strip Engine Code on, Managed Stripping High, Disk Size+LTO, exceptions None, API .NET Standard 2.1, IL2CPP Optimize Size, targetFrameRate=-1, vSync=0.
4. Don't hand-edit ProjectSettings.asset (serialized names differ, per-target values); `script eval` takes statement blocks — no usings, fully-qualified types; three API spellings are traps (GetManagedStrippingLevel etc.).
5. KTX2/Basis only for runtime-loaded textures on unknown GPUs (ETC1S size / UASTC quality, encode offline with toktx, `--lower_left_maps_to_s0t0`); AudioEffects don't work on WebGL; iOS <18 caps WASM heap ~2GB, prefer high Initial Memory over growth.

## Risks / owner items
- Server misconfiguration silently negates compression — Decompression Fallback is a ~150KB fallback only.
- Stripping shaders/packages can break referenced content; test after stripping, keep link.xml for reflection users.
- Safari caps 60fps and has different GC/JIT — always verify in both Chrome and Safari; batch-mode `-quit` runs cannot reproduce the unsaved-settings bug.

## Category and tags
build, web, mobile — unity, webgl, wasm, optimization, performance, game-dev.

## Revision note
Single plugin revision; the deepest and most operationally honest skill in the slice (documents its own observed failure modes).
