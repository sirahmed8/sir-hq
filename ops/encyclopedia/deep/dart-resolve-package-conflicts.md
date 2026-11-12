# dart-resolve-package-conflicts (Flutter plugin)

## Summary
Dependency-management workflow for Dart's strict single-version resolution: read `dart pub outdated` columns correctly (Current/Upgradable/Resolvable/Latest), prefer caret constraints, tighten dev_dependencies lower bounds, enforce lockfiles in CI with `--enforce-lockfile`, upgrade via `dart pub upgrade` (+`--tighten`) for compatible bumps or manual pubspec edits for major ones, and resolve conflicts by surgically deleting only the offending package's entry from pubspec.lock — NEVER the whole lockfile.

## When to use / when NOT
Use when `pub get` fails on version conflicts, a package is retracted, or doing periodic dependency audits/upgrades. Do NOT use for adding a brand-new dependency (dart pub add) or for Flutter-specific plugin issues.

## Inputs, outputs, tools
- Inputs: pubspec.yaml constraints, pubspec.lock state, `dart pub outdated` output.
- Outputs: resolved dependency graph, updated constraints/lockfile.
- Tools: `dart pub outdated|get|upgrade|deps`, `dart analyze`, `dart test` for the feedback loop.

## 5 most important rules
1. NEVER delete all of pubspec.lock and re-get — that causes uncontrolled upgrades across the graph; delete only the conflicting package's block.
2. Caret syntax (`^1.2.3`) for dependencies; pin dev_dependencies lower bounds to the version in use.
3. `--enforce-lockfile` in CI so tested versions ship.
4. Upgradable → `pub upgrade` (+`--tighten`); Resolvable (major) → edit pubspec.yaml constraint first, then upgrade.
5. After any resolution change: `dart pub deps` to verify the graph, then analyze + test.

## Risks / things needing the owner
Major upgrades can break APIs — the analyze/test loop must pass before commit. Retracted versions need the surgical lockfile edit; pinning a yanked version breaks everyone.

## Category / tags
build · dart, flutter, dependencies, pub, versioning

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-resolve-package-conflicts\SKILL.md`. Only gemini-plugin holds it.
