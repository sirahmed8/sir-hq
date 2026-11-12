# dart-use-doc-examples (Flutter plugin)

## Summary
Guide for Dartdoc `{@example}` directive: extract multi-line code examples into real `.dart` files (so they're analyzed/linted/executed) and inject them into doc comments — `{@example /path/file.dart[#region] [lang=..] [indent=strip|keep]}` — with `#region`/`#endregion` to show only a snippet and trailing `#hide` to drop compiler-needed-but-doc-noise lines.

## When to use / when NOT
Use when writing API docs that need multi-line code samples. Do NOT use for one-line snippets (inline backticks are fine) or non-Dart files unless lang override fits.

## Inputs, outputs, tools
- Inputs: doc comments + example `.dart` files under the package.
- Outputs: generated dartdoc with fenced, analyzable code blocks.
- Tools: `dart doc` to verify; examples/ dir in the skill.

## 5 most important rules
1. External file + `{@example}` over inline markdown for anything multi-line.
2. Leading `/` in path = package root; otherwise relative to the current file.
3. Wrap showable snippets in `#region name`/`#endregion name`; reference with `#name`.
4. `#hide` trailing comment drops a line from docs while keeping it in compiled code (e.g. mock server startup).
5. `indent=strip` (default) removes shared indentation; set `lang` explicitly for non-Dart blocks.

## Risks / things needing the owner
Example files are real code — they must compile; broken examples fail analyze/doc. Keep license headers consistent.

## Category / tags
build · dart, documentation, dartdoc

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-use-doc-examples\SKILL.md`. Only gemini-plugin holds it.
