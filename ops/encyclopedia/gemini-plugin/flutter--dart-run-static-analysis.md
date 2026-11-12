# dart-run-static-analysis

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: automation
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-run-static-analysis\SKILL.md`
- SKILL.md size: 5033 chars

## What it does

Execute `dart analyze` to identify warnings and errors, and use `dart fix --apply` to automatically resolve mechanical lint issues. Use during development to ensure code quality and before committing changes.

## When to use (from skill text)

- Use this workflow to identify type-related bugs, style violations, and potential runtime errors.
- Use this workflow to resolve outdated API usages, apply quick fixes, and migrate code (e.g., Dart 3 migrations).

## Structure (headings inside SKILL.md)

- Analyzing and Fixing Dart Code
- Contents
- Analysis Configuration
- Diagnostic Suppression
- Workflow: Executing Static Analysis
- Workflow: Applying Automated Fixes
- Examples
- Comprehensive `analysis_options.yaml`
- Inline Diagnostic Suppression
- (none)

## Tools / MCPs it needs

- MCP mentions: MCP tool

## Risks / cautions found in text

- none flagged by keyword scan

## Key rules (verbatim lines from SKILL.md)

1. - **Base Configuration:** Always include a standard rule set (e.g., `package:lints/recommended.yaml` or `package:flutter_lints/flutter.yaml`) using the `include:` directive.
2. - **Linter Rules:** Explicitly enable or disable specific rules under the `linter: rules:` node. Use a key-value map (`rule_name: true/false`) when overriding included rules, or a list (`- rule_name`) when defining a fresh set. Do not mix list and map syntax in the same `rules` block.
3. - [ ] 4. If info-level issues must be treated as failures, append the `--fatal-infos` flag.
4. - [ ] 3. If additional fixes are required, verify that the corresponding linter rules are enabled in `analysis_options.yaml`.

## Files inside the skill

- (SKILL.md only)
