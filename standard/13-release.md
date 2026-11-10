# 13 - Release and versioning

> **Owner rule (Ahmed, 2026-11-09): every project and app stays at version 1.0.0 while under development.** Never bump, tag or release a higher version, and do not use the `-alpha`, `-beta` or `-rc` steps below until the owner says a product is released. The scheme below describes what happens after he does. Until then the version in `package.json`, `.sir/project.yml`, manifests and the UI is exactly `1.0.0`.

- **Semantic Versioning: MAJOR.MINOR.PATCH.**
  - `1.0.0` is the first public release. Before that: `1.0.0-alpha.N` → `1.0.0-beta.N` → `1.0.0-rc.N`.
  - After launch: PATCH for fixes, MINOR for backward-compatible features, MAJOR for breaking changes or major redesigns.
- **One version per product** across all platforms, with a single source of truth (root `package.json`, mirrored in `.sir/project.yml`). Platform build numbers (Android `versionCode`, iOS `buildNumber`) only go up and are auto-incremented by EAS.
- **Changelog:** Conventional Commits feed Changesets or release-please → `CHANGELOG.md` and an in-app "What's new". Git tags `vX.Y.Z`; GitHub Releases carry the desktop installers. The in-app "What's new" reads the generated release notes (JSON bundled at build time, or fetched from the backend); it's never a hand-typed list inside UI code. Release notes are written for users, in every locale.
- **Channels:** development → preview (internal testers) → beta (Play closed testing, TestFlight, Microsoft Store package flights, desktop beta channel) → production with a staged rollout (10% → 50% → 100%), advancing only while the crash-free rate stays ≥ 99.5%.
- **Real builds at every milestone** for every target platform (`D:\Projects\_SIR\phases\10-real-builds.md`): APK and AAB; Wear OS and TV APKs; unsigned IPA plus simulator builds for iPhone, iPad, watchOS and tvOS; Windows installer and Microsoft Store MSIX; macOS DMG; Linux AppImage and `.deb`; the web app. Each one is installed and smoke-tested, then listed in `BUILDS.md` (version, date, SHA-256 checksum, download link, install steps).
- **Store metadata** lives in `docs/store/`: names, subtitles, descriptions and keywords in every project locale (ASO rules in module 16), screenshot plan for every device class, privacy answers, review notes, demo account for reviewers.
- **Rollback:** web through the host's instant rollback (Cloudflare and Firebase Hosting both keep earlier versions); the Microsoft Store by halting a gradual rollout; desktop by moving the update channel back; mobile by halting the rollout and shipping a hotfix (OTA only for JavaScript-safe fixes).
- **After release:** watch Crashlytics/Sentry, analytics and reviews for 72 hours; record lessons in the CHECKPOINT.
