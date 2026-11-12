# flutter-implement-json-serialization

## Summary
Manual JSON serialization guide using only `dart:convert` — the lightweight path when codegen (freezed/json_serializable) is overkill. Model classes are plain Dart classes with `final` properties, a `factory Model.fromJson(Map<String,dynamic>)` (pattern-matching switch that throws FormatException on shape mismatch), and `toJson()`. Fetching workflow: http request → validate statusCode (200/201 proceed, else throw Exception, never return null) → choose parsing strategy → decode via `jsonDecode` cast to `Map<String,dynamic>`/`List<dynamic>` → map through fromJson. Large payloads (>16ms parse) must offload to a background isolate via `compute()` with a top-level parse function to avoid UI jank.

## When to use / when NOT
Use for simple data structures where manual mapping is acceptable and you want zero codegen. Do NOT use for complex/nested models at scale — the skill set's architecture skill points to freezed/built_value or json_serializable codegen for those; manual casting is error-prone on deep schemas.

## Inputs, outputs, tools
- Inputs: JSON schema/API response shape, http.Client.
- Outputs: model classes with fromJson/toJson, fetch functions, unit tests.
- Tools: `dart:convert` (jsonEncode/jsonDecode), http package, `compute()` from flutter/foundation.

## 5 most important rules
1. Always cast `jsonDecode`'s dynamic result explicitly (`as Map<String,dynamic>`, `.cast<Map<String,dynamic>>()` for lists) — dynamic silently propagates type errors.
2. fromJson should validate shape via pattern matching and throw FormatException on mismatch; toJson returns the inverse map.
3. HTTP: throw on non-2xx, never return null; distinguish 200 vs 201 only where relevant.
4. Payloads taking >16ms to parse go through `compute(parseFn, body)` — parseFn MUST be a top-level/static function (isolates can't capture closures).
5. Write unit tests for both directions and run the validator to catch casting/type mismatches early.

## Risks / owner needs
Manual serialization drifts silently when the API changes — no schema enforcement; consider codegen if the API surface is large or evolves. compute() isolates can't use closures or non-sendable objects.

## Category and tags
Category: mobile. Tags: flutter, json, serialization, dart-convert, http, isolates, dart.

## Revisions
Single gemini-plugin flutter copy; no competing revisions.
