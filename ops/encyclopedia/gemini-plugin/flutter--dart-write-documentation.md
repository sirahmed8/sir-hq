# dart-write-documentation (Flutter plugin)

## Summary
Effective-Dart documentation rules for `///` doc comments: public APIs only, proper sentences, first paragraph = one-sentence summary (blank `///` line after, never a bare newline), noun phrases for properties, "Whether" for booleans, third-person verbs for methods, NO Javadoc tags (@param/@return woven into prose instead), docs before annotations, inherit via dartdoc (don't duplicate @override), document getter only in get/set pairs, `[identifier]` links (no parens on methods, `.new` for default ctor, `@docImport` for out-of-scope), backticks for keywords/literals, labeled code fences, verify with `dart analyze` + `dart doc`.

## When to use / when NOT
Use when writing or updating Dart API documentation. Do NOT document private `_` members unless asked.

## Inputs, outputs, tools
- Inputs: Dart declarations needing docs.
- Outputs: dartdoc-compliant `///` comments.
- Tools: `dart analyze` (comment_references warnings), `dart doc`.

## 5 most important rules
1. `///` only, proper sentences; first paragraph is the extracted summary — separate it with a `///` blank line (a real newline kills the block).
2. Banned: `@param`, `@return`, `@throws`, `@see` — parameters/exceptions go in prose.
3. `[Square brackets]` link in-scope identifiers; backticks for `null`/`true`/keywords; no parens in method links.
4. Don't re-document @override members or both getter+setter — dartdoc inherits/warns.
5. Label every code fence (```dart, ```sh); verify resolution via dart analyze.

## Risks / things needing the owner
Broken `[...]` references fail analyze — docs aren't free. Public API docs become the package's published face.

## Category / tags
build · dart, documentation, style-guide, dartdoc

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\flutter\skills\dart-write-documentation\SKILL.md`. Only gemini-plugin holds it.
