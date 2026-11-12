# skills (gemini-plugin: android-cli-plugin root skill)

## Summary
This entry is the root SKILL.md of Google's `android-cli-plugin` for Antigravity/Gemini. Despite the slice label "skills", its frontmatter `name` is `android-cli` and it is the specialist manual for Google's `android` CLI: a single command-line tool that manages the Android SDK, scaffolds projects from templates, builds/deploys/runs APKs on emulators and physical devices, captures UI layout trees and annotated screenshots, searches the official Android Knowledge Base, and even manages its own agent skills. The file is mostly a command reference (`android sdk|create|run|layout|screen|docs|emulator|install|studio|skills|update|auth|device|info|init|completion|describe|help`) plus mandatory pointers to two reference docs (`references/interact.md` for UI dump/screenshot interaction rules, `references/journeys.md` for evaluating XML journey tests).

## When to use / when NOT
Use for any Android development task on this machine: installing SDK packages, creating a project, running an app on an emulator/device, inspecting UI layout, taking screenshots, looking up current Android API docs, or running journey tests. Do NOT use for iOS (there is no iOS equivalent here), for general Kotlin questions with no device interaction, or before the `android` binary is installed (the skill gives per-OS install one-liners).

## Inputs, outputs, tools
- Inputs: natural-language Android tasks plus optional flags (`--sdk`, `--device`, `--output`, template names).
- Outputs: project directories, JSON layout trees, PNG screenshots, journey pass/fail evaluation, SDK package changes.
- Tools: the `android` CLI itself (installed from dl.google.com per-OS scripts), adb under the hood for screen/input, the Android SDK, Android Studio integration (`android studio`), and the plugin's own `compose-preview` and `device-hub` companion skills. `android docs` queries Google's Android Knowledge Base online.

## 5 most important rules
1. Before `android layout` or `android screen`, you MUST read `references/interact.md`; before evaluating a journey, you MUST read `references/journeys.md`.
2. `android layout` returns the UI element tree (text, resourceId, bounds, interactions); `layout --diff` returns only changes and keeps context small.
3. `android screen capture --annotate` labels UI elements with numbers; `screen resolve` converts `#N` labels into tap coordinates (chainable into `adb shell input`).
4. Always visually examine the PNG from `screen capture` before acting; layout dumps fail on WebViews and animations.
5. Journey XML is the source of truth: execute each action exactly as written, independently; a crash, exit, freeze or deviation fails the journey.

## Risks / things needing the owner
`android auth login` opens a Google sign-in that only the owner can complete (password/2FA). `android sdk install` and `emulator create` download large files and consume disk. `run`/`install` push code to devices, so confirm the target device with `--device` when several are connected. Nothing else is owner-facing.

## Category / tags
mobile · android, sdk, emulator, ui-testing, cli, google

## Revisions
Only one revision exists: `C:\Users\a7med\.gemini\config\plugins\android-cli-plugin\skills\SKILL.md` (25,026 chars, with references/interact.md and references/journeys.md beside it, plus sibling skills compose-preview and device-hub in the same plugin). No divergent copies.
