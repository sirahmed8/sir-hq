# xcode_project_setup (windsurf/codex skill)

## Summary
xcode_project_setup safely modifies Xcode projects (.xcodeproj/.xcworkspace) to add Swift Package dependencies and link native modules — via a bundled Swift script `scripts/xcode_spm_setup`, never by hand-editing .pbxproj. Absolute rules ("a hefty fee will be applied"): NO Ruby/Rails/gems ever (xcodeproj gem banned); modern Xcode folder synchronization means new .swift/resource files on disk auto-join the project — never pbxproj-edit to add files; if scripting is unavoidable use Swift only (Node/TS as absolute last resort); verify `swift --version` first and stop/recommend `xcode-select --install` if missing; empty directory (no .xcodeproj) → ask the user to create the project in Xcode first and wait. Firebase-specific: always use the LATEST firebase-ios-sdk version from GitHub releases; the script auto-injects `-ObjC` into OTHER_LDFLAGS for Firebase (prevents fatal nil crashes from stripped Obj-C categories/+load) and auto-links `GoogleService-Info.plist` via `--plist`.

## When to use / when NOT
Use when adding SPM packages (Alamofire, Firebase, etc.) or config plists to an existing Xcode project. Do NOT use to create the .xcodeproj itself (user must do it in Xcode), to edit pbxproj text directly, or for non-Apple platforms.

## Inputs, outputs, tools
- Inputs: .xcodeproj path, package repo URL, version requirement, product module names, optional plist path.
- Outputs: SPM dependency + target Frameworks linkage + resource plist wiring (idempotent — skips existing).
- Tools: `swift run --package-path <skill>/scripts/xcode_spm_setup xcode_spm_setup <proj> <repoURL> <version> [--plist path] <Product...>`.

## 5 most important rules
1. NEVER use Ruby or hand-edit .pbxproj — folder sync handles file adds; the Swift script handles packages.
2. `swift --version` gate first; no Swift toolchain → stop and ask user to install.
3. Script does BOTH steps (add package repo + link products to target Frameworks) — no manual linking needed.
4. Firebase needs `-ObjC` linker flag (script injects it) and latest SDK version from releases page.
5. Idempotent: safe to re-run; skips already-linked files/packages.

## Risks / things needing the owner
Requires macOS + Xcode + Swift toolchain — verify before promising. `GoogleService-Info.plist` contains Firebase config (semi-sensitive, project-specific). Creating the initial .xcodeproj is a user action in Xcode GUI. Wrong version pinning breaks Firebase — check releases page. No secrets handling beyond plist placement.

## Category / tags
mobile · xcode, swift, spm, firebase, ios

## Revisions
Single source read: `C:\Users\a7med\.codeium\windsurf\skills\xcode_project_setup\SKILL.md` (141 lines). Six-tool skill; windsurf revision representative.
