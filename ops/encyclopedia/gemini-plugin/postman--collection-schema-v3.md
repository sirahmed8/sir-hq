# collection-schema-v3 (Postman v3 Git-native collections)

## Summary
Reference skill for authoring and debugging Postman v3 collections stored as Git-native directories: one folder per collection, `*.request.yaml` per request, `.resources/` for scope metadata and saved examples, plus environment/globals/other-protocol file shapes. Its core doctrine: keep entities small and independently editable so a PR can carry one request change beside the code it checks.

## When to use / when NOT
Use when writing or fixing local `postman/collections/` YAML — lint failures, malformed requests, wrong body shapes, misplaced examples. Do NOT use for executing collections (api-testing), authoring mocks (api-mocking), or writing datasets (datasets skill). Reference docs exist for http.md, environment.md, globals.md, other_protocols.md.

## Inputs, outputs, tools
- Inputs: the collection directory or single entity file being edited; the relevant reference doc.
- Outputs: correctly shaped YAML entities preserving inherited auth/variables/scripts.
- Tools: `postman collection lint <path>`, `postman environment lint <path>`, `postman workspace lint`; reference files under `reference/`.

## 5 most important rules
1. Edit only the entity that owns the change; never regenerate a monolithic collection export.
2. Preserve inherited auth, variables, and scripts — do not copy inherited fields into each request (creates competing values).
3. Respect per-protocol shapes: an HTTP field is not valid on another request kind; consult the matching reference file.
4. Preserve YAML types at the boundary: quote `{{variables}}` and boolean/number-looking strings; JSON bodies use block scalars.
5. Keep `order` values spaced for insertion, filenames portable and unique case-insensitively, and check examples paths when renaming a request.

## Risks / things needing the owner
Ignored YAML fields can silently change request behavior even when parsing succeeds — warnings in lint output must be reviewed, not just errors. Behavior claims require an actual run against a target.

## Category / tags
data · postman, api, yaml, git-native, schema

## Revisions
Single revision: `C:\Users\a7med\.gemini\config\plugins\postman\skills\collection-schema-v3\SKILL.md` with a `reference/` folder (environment.md, globals.md, http.md, other_protocols.md). Only gemini-plugin holds it.
