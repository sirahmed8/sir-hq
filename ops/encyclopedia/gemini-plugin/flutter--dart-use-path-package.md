# dart-use-path-package

- Tool: `gemini-plugin` (plugin: `flutter`)
- Category: data
- Source: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-path-package\SKILL.md`
- SKILL.md size: 11275 chars

## What it does

>- Cross-platform file and directory path manipulation, segment splitting, extension extraction, and context conversion using `package:path` and `package:file`. Use when writing, inspecting, joining, splitting, or refactoring file paths, directory names, or extensions, or replacing raw string path operations (`.split('/')`, `'$dir/$file'`, `.endsWith('.ext')`, `.replaceAll('\\', '/')`). Don't use for HTTP network URI routing, database query strings, or non-path string processing.

## Structure (headings inside SKILL.md)

- Safe Cross-Platform Path Manipulation in Dart
- Contents
- 1. Core Principles & Cross-Platform Rules
- Avoid Treating File Paths as Raw Strings
- Pragmatic Boundary Joining vs. Multi-Segment Decomposition (`p.join`)
- Normalization vs. Canonicalization (`p.normalize` vs. `p.canonicalize`)
- Strip Location Specifiers & Convert URIs Safely
- 2. Recommended package:path Idioms vs. String Anti-Patterns
- Path Joining
- Segment Matching
- Root and Directory Prefixes
- File Extensions
- Extension Slicing and Compound Extensions
- POSIX and URL Path Conversion
- URI Conversion
- Directory Basename Helper
- 3. Bridging Native Paths to POSIX, Git, & URL Contexts
- Git Paths and Repository Metadata
- 4. Mockable File Systems (`package:file` vs. Global `p.*`)
- 5. Extensions, Compound Extensions & Stem Extraction
- 6. Workflows & Audit Checklist
- Path Refactoring Checklist
- References & Examples
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- * String interpolation like `'$dir/$file'` injects forward slashes on Windows and produces duplicate slashes (`//`) when `$dir` ends with a trailing slash.
- * **Why**: String matching fails on Windows backslashes (`foo\bar`) and produces

## Key rules (verbatim lines from SKILL.md)

1. * Extract the trailing `:line-col` suffix via regular expression (`RegExp(r'^(.*?):(\d+(?:-\d+)?)$')`) *before* passing the file path to `package:path`.
2. * **URI Boundary Conversions**: When converting between file paths and `Uri` objects, always use `p.toUri(path)` and `p.fromUri(uri)` rather than `Uri.parse(path)` or manual string concatenation.
3. * **Avoid**: `'$dir/$file'` or `'a/$b'`
4. * **Avoid**: `path.contains('foo/')`
5. * **Avoid**: `path.startsWith('foo/')` or `p.split(path).first == 'foo'`

## Files inside the skill

- `examples/cross_platform_paths.dart`
- `examples/file_system_context.dart`
