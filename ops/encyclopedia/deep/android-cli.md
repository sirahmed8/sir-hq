# android-cli

Source read: `C:\Users\a7med\.claude\skills\android-cli\SKILL.md` (24.6 KB; claude revision; content identical to the codex and kilo copies).

## Summary
Google-published skill that drives the `android` command line tool for Android development: installs the CLI, manages SDK packages, creates projects, runs apps on devices or emulators, inspects UI layouts, captures screenshots, searches the Android documentation knowledge base, and manages AVDs and updates.

## When to use / when NOT
Use when the task is Android-side: scaffolding, build and deploy, device UI inspection, emulator management, doc lookup, APK runs. Do NOT use for writing or reviewing native Android source code or Gradle configuration.

## Inputs, outputs, tools
- Inputs: command intent and parameters, for example `android create empty-activity --name=MyApp --output=./my-app` or `android sdk install platforms/android-34`.
- Outputs: command output, layout JSON, screenshots, doc articles.
- Tools: `android <command>`; before `android layout` or `android screen` read the interact reference; before journey evaluation read the journeys reference.

## 5 most important rules
1. Before using `android layout` or `android screen`, read the interact reference first; read the journeys reference before evaluating a journey.
2. Install with the official curl installer for the platform; on Windows use the provided .cmd installer.
3. Confirm a device or emulator is connected before layout, screen or run operations; check state with `android info`.
4. Use `android docs` for authoritative, up-to-date API and concept answers, including migration guides and examples.
5. Update the CLI with `android update`; manage SDK packages with `android sdk install`, `update`, `remove` and `list`.

## Risks / things needing the owner
A physical device or emulator must be available; SDK license acceptance is required; release signing is outside this skill.

## Category / tags
Category: mobile. Tags: android, cli, sdk, emulator, device, layout, docs, apk.

## Revisions
Claude copy is the preferred source (24.6 KB); content is identical to the codex and kilo copies. Not present in the antigravity builtin set.
