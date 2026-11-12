# dart-use-primary-constructors (Flutter plugin)

## Summary
Guide for Dart's Primary Constructors feature (class-header parameter lists that declare fields, initializing params, and regular params in one shot, plus `;` empty bodies, in-body `this :` initializer lists, concise constructor syntax, `const` placement before the type name, extension-type requirement). Version-gated: default in Dart 3.13+, experimental flag needed on 3.12, unsupported ≤3.11.

## When to use / when NOT
Use when writing or migrating to the new constructor syntax, or debugging primary-constructor code. First check the project's Dart version — on ≤3.12 enable `--enable-experiment=primary-constructors` or the analysis_options experiment; on ≤3.11 it's unavailable.

## Inputs, outputs, tools
- Inputs: class declarations to write/refactor; project Dart SDK version.
- Outputs: primary-constructor class syntax.
- Tools: none — language feature reference.

## 5 most important rules
1. Check Dart version FIRST — the feature doesn't exist before 3.12 and is opt-in on 3.12.
2. `var`/`final` params are declaring params (create fields); `this.`/`super.` are initializing; bare params are regular (init scope only, via `this :` list).
3. `const` goes before the class name: `class const Point(final int x, final int y);`.
4. Extension types MUST use primary constructors.
5. Empty bodies use `;` — no `{}` needed.

## Risks / things needing the owner
Bleeding-edge syntax — teams on stable SDKs can't adopt it; mixing old/new constructor styles in one codebase hurts readability. Verify SDK version before suggesting.

## Category / tags
build · dart, language-features, constructors, migration

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-primary-constructors\SKILL.md`. Only gemini-plugin holds it.
