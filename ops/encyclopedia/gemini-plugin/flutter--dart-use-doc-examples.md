# dart-use-doc-examples

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: study
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-doc-examples\SKILL.md`
- SKILL.md size: 5344 chars

## What it does

How to inject external code examples into Dartdoc using the {@example} directive, and how to filter those files using #hide, #region, and #endregion tags.

## When to use (from skill text)

- *   **Package-Root Paths (`/`)**: Paths starting with a leading slash automatically resolve directly to the root of the Dart package. Use this when the destination file is deep.

## Structure (headings inside SKILL.md)

- Using Examples in Dartdoc
- Contents
- 1. The `{@example}` Directive
- 2. Using Regions
- 3. Hiding Setup Code
- 4. Marker Filtering Rules
- 5. Placement and Path Resolution
- 6. Verification
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- 2.  (Optional) Run `dart doc` to verify that dartdoc successfully parsed the directive without throwing a "Failed to read file" or "missing region" warning.

## Key rules (verbatim lines from SKILL.md)

1. *   **Region Required:** The markers are only processed and stripped when you target a specific region suffix (e.g., `{@example file.dart#region_name}`). If you inject an entire file without a region suffix, the file is embedded exactly as it appears in the source, including any marker text like `//
2. *   **Boundary Enforcement:** Using `..` segments to traverse upward is perfectly acceptable, but dartdoc natively stops directory traversal at the package root (it will never escape the package).
3. *   **No Network URLs:** Absolute URIs (e.g., starting with `https://`) are strictly not supported. The example file *must* sit natively somewhere in the local filesystem.
4. *   **Separators & Encoding:** Because dartdoc resolves the path as a URI, you must always use forward slashes (`/`) as folder separators (even on Windows). You can natively include URI-encoded characters (like `%20` for spaces) as permitted by URI reference rules.

## Files inside the skill

- (SKILL.md only)
