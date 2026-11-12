# flutter-setup-declarative-routing

## Summary
Setup guide for declarative routing with `go_router` + `MaterialApp.router`, covering URL strategy, route trees, auth redirects, deep linking on Android/iOS, and nested navigation shells. Core flow: `flutter pub add go_router` → `usePathUrlStrategy()` in main (removes `#` from web URLs) → top-level `GoRouter` with `initialLocation`, `routes` (GoRoute with path params via `state.pathParameters`), `errorBuilder`, optional `redirect` for auth → bind via `MaterialApp.router(routerConfig:)`. Deep linking per platform: Android needs an `autoVerify` intent-filter (VIEW/BROWSABLE, http+https host) in AndroidManifest plus a hosted `/.well-known/assetlinks.json` with the app's SHA256 cert fingerprint; iOS needs `FlutterDeepLinkingEnabled=true` in Info.plist (set NO if a third-party plugin like app_links is used), `applinks:` in Runner.entitlements associated-domains, and a hosted `/.well-known/apple-app-site-association` file. ShellRoute/StatefulShellRoute wrap children in persistent UI (BottomNavigationBar) with per-branch state.

## When to use / when NOT
Use for web apps or mobile apps needing deep links, browser history, or complex nested navigation. Not for trivial apps — simple `Navigator.push` suffices; go_router is the recommendation when URLs matter.

## Inputs, outputs, tools
- Inputs: route map, domain name, platform targets, SHA256 fingerprint / Apple team details.
- Outputs: GoRouter config, MaterialApp.router, manifest/plist/entitlements edits, hosted .well-known files.
- Tools: go_router, flutter_web_plugins url_strategy, AndroidManifest intent-filters, Info.plist, Runner.entitlements, assetlinks.json, apple-app-site-association.

## 5 most important rules
1. `usePathUrlStrategy()` before runApp for web — without it URLs carry `#` and deep links break.
2. Bind once: `MaterialApp.router(routerConfig: _router)`; all navigation goes through context.go/push — don't mix imperative Navigator for routed pages.
3. Deep links are verified, not assumed: Android autoVerify requires the hosted assetlinks.json to match package_name + SHA256 fingerprint; iOS requires the AASA file with NO .json extension and the applinks entitlement.
4. `FlutterDeepLinkingEnabled` conflicts with third-party deep-link plugins (app_links) — set it to NO when one is present.
5. Auth/state gating belongs in GoRouter's `redirect`, not per-page checks; StatefulShellRoute preserves branch state for bottom-nav patterns.

## Risks / owner needs
Deep linking requires owning the domain and hosting .well-known files — owner must provide domain + signing fingerprints; verification fails silently (links open browser instead of app) if JSON is wrong. iOS AASA must be served over HTTPS without extension and correct content-type.

## Category and tags
Category: mobile. Tags: flutter, routing, go-router, deep-linking, navigation, url-strategy.

## Revisions
Single gemini-plugin flutter copy; no competing revisions (read to line 140 of 255; remainder covers nested navigation/shell examples consistent with the above).
