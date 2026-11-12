# dart-resolve-package-conflicts

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-resolve-package-conflicts\SKILL.md`
- SKILL.md size: 5267 chars

## What it does

Workflow for fixing package version conflicts. Use this when `pub get` fails due to incompatible package versions.

## Structure (headings inside SKILL.md)

- Managing Dart Dependencies
- Contents
- Core Concepts
- Version Constraints
- Workflow: Auditing Dependencies
- Workflow: Upgrading Dependencies
- Workflow: Resolving Version Conflicts
- Examples
- Tightening Constraints
- Surgical Lockfile Removal
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- *   **Enforce Lockfiles in CI:** Use `dart pub get --enforce-lockfile` in CI/CD pipelines to ensure the exact versions tested locally are used in production.
- - [ ] Delete ONLY that package's entry from the lockfile.

## Key rules (verbatim lines from SKILL.md)

1. *   **Use Caret Syntax:** Always use caret syntax (e.g., `^1.2.3`) for dependencies in `pubspec.yaml`. This allows `pub` to select newer, non-breaking versions (up to, but not including, the next major version) during resolution.
2. - [ ] Review the **Resolvable** column to identify packages that require constraint modifications in `pubspec.yaml` to update.

## Files inside the skill

- (SKILL.md only)
