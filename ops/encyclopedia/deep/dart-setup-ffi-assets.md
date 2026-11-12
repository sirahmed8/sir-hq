# dart-setup-ffi-assets (Flutter plugin)

## Summary
Guide for packaging C/C++ code as Dart Code Assets via the Native Assets hook system: `hook/build.dart` compiles local sources with `package:native_toolchain_c` (CBuilder/CLibrary — never raw gcc/clang shell-outs) or downloads prebuilt binaries; `hook/link.dart` applies linker tree-shaking via `record_use` mappings; deps are `code_assets`, `hooks`, `native_toolchain_c`, `record_use`, dev `ffigen`; hooks run automatically during `dart test`/`run`/`build`.

## When to use / when NOT
Use when a package needs to compile/bundle native C/C++ for Dart/Flutter, implement build.dart/link.dart hooks, or integrate prebuilt native libs. Pairs with dart-use-ffigen for the Dart-side bindings. Do NOT use for pure-Dart packages or manual FFI without native assets.

## Inputs, outputs, tools
- Inputs: C sources or prebuilt libs, `lib/src/c_library.dart` spec shared by both hooks.
- Outputs: compiled code assets + tree-shaken runtime binary.
- Tools: `package:hooks` (build/link callbacks), `package:native_toolchain_c` (toolchain detection: MSVC/Xcode/GCC), `package:code_assets` (CodeAsset/DynamicLoadingBundled), `package:record_use`; deps fetched from pub.dev.

## 5 most important rules
1. Hooks live strictly in `hook/` (`build.dart`, optional `link.dart`); all path resolution platform-independent via `Platform.script.resolve()`/Uri — no hardcoded paths or shell scripts.
2. Never invoke gcc/clang/msvc directly — use native_toolchain_c's programmatic API.
3. Every source file needs the package license/copyright header.
4. Tree-shaking requires a `record_use_mapping` `.g.dart` under `lib/src/third_party/` mapping Dart methods to C symbols (generate via ffigen).
5. Prebuilt downloads MUST be hash-verified (MD5/SHA-256 lookup tables) with an offline fallback (local_build flag).

## Risks / things needing the owner
Two integration methods trade off: local compile+tree-shake (needs host toolchain, smallest binary, fully offline) vs prebuilt downloads (zero toolchain, bigger, needs network+integrity checks). Wrong hashes or missing fallbacks break users.

## Category / tags
build · dart, ffi, native-assets, compilation, packaging

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-setup-ffi-assets\SKILL.md`. Only gemini-plugin holds it.
