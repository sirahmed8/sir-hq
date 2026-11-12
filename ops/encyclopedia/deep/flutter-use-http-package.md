# flutter-use-http-package

## Summary
Guide for REST calls with the `http` package: `flutter pub add http`, import as `http`, platform permissions (Android `INTERNET` uses-permission in main AndroidManifest; macOS `com.apple.security.network.client` in BOTH DebugProfile and Release entitlements). Request rules: `Uri.parse` all URLs, headers map with `HttpHeaders.authorizationHeader`/content-type, `jsonEncode` bodies for POST/PUT, GET appends query params, DELETE returns empty model on 200. Response handling: validate statusCode (200 GET/PUT/DELETE, 201 POST), throw explicit Exception on failure — never return null because FutureBuilder then never reaches its error state and the UI spins forever. Deserialize via `jsonDecode` → fromJson factory. Large payloads parse in a background isolate via `compute()` (top-level/static function only). UI integration via FutureBuilder handling hasData/hasError/loading.

## When to use / when NOT
Use for straightforward REST fetch/mutate in Flutter without a heavier client (Dio/interceptors, retrofit). Not for streaming, websockets, or GraphQL — those need different packages.

## Inputs, outputs, tools
- Inputs: API endpoints, auth tokens, JSON schemas.
- Outputs: Future<Model> fetch functions, permission/entitlement edits, FutureBuilder UI wiring.
- Tools: http package, dart:convert, flutter/foundation compute, AndroidManifest, macOS entitlements, FutureBuilder.

## 5 most important rules
1. Never return null on HTTP failure — throw; null breaks FutureBuilder's error path and leaves infinite loading.
2. Status-code contract: 200 for GET/PUT/DELETE, 201 for POST; anything else throws with the status in the message.
3. Platform permissions are separate per platform: Android manifest INTERNET + macOS sandbox entitlements in both debug AND release files — missing release entitlement is a classic "works in debug" bug.
4. `compute()` parse functions must be top-level or static — closures can't cross isolates.
5. Content-Type `application/json; charset=UTF-8` + jsonEncode body on mutations; auth via HttpHeaders constants, not stringly-typed keys.

## Risks / owner needs
Auth tokens in headers must come from secure storage, never hardcoded (the example's 'Bearer your_token_here' is a placeholder pattern, not a real credential). http has no retry/timeout by default — production apps may need .timeout() wrappers; this skill doesn't cover them.

## Category and tags
Category: mobile. Tags: flutter, http, rest-api, networking, json, futurebuilder, dart.

## Revisions
Single gemini-plugin flutter copy; no competing revisions (read to line 120 of 174; remainder is model/UI example consistent with this).
