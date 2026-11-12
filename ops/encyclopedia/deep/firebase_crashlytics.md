# firebase-crashlytics

## Summary
A thin onboarding pointer for Firebase Crashlytics: real-time crash reporting for Android/iOS apps. It covers prerequisites (Firebase project + app; MCP server in Firebase CLI to READ collected crash data), SDK setup via per-platform references (android_setup.md, ios_setup.md), and SDK usage features — custom keys, custom logs, user identifiers, non-fatal exception reports — pointing to official docs for customization details.

## When to use / when NOT
Use when adding crash reporting/diagnostics to an Android or iOS app, or when reading crash data via the Firebase CLI MCP server. Do NOT use for web apps (Crashlytics is mobile-only) or for general logging/analytics (use Analytics/other products).

## Inputs, outputs, tools
- Inputs: Firebase project + Android/iOS app (see firebase-basics), target platform.
- Outputs: Crashlytics SDK integrated; crash reports readable through Firebase CLI MCP tools.
- Tools: per-platform setup references, Firebase CLI MCP server for data access; official customize-crash-reports docs.

## 5 most important rules
1. Requires BOTH a Firebase project and a platform app first — run firebase-basics setup before anything.
2. Android and iOS only — check platform before starting; no web support.
3. SDK setup differs per platform — load android_setup.md or ios_setup.md, don't improvise Gradle/Podfile steps.
4. Reading crash data goes through the Firebase CLI MCP server, not manual API calls or console scraping.
5. Enrich reports with custom keys, custom logs, user identifiers and non-fatal exception reporting — raw crashes alone are hard to act on.

## Risks / owner needs
Crash data contains user/device info — check privacy policy coverage (legal-compliance). SDK adds build size; symbolication needs correct upload of debug symbols/mapping files on release builds.

## Category and tags
Category: cloud. Tags: firebase, crashlytics, crash-reporting, mobile, observability, android, ios.

## Revisions
Identical across the 7 tools; claude copy used.
