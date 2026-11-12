# modern-app-engineering

- Tool: `claude`
- Category: design
- Source: `C:\Users\a7med\.claude\skills\modern-app-engineering\SKILL.md`
- SKILL.md size: 2092 chars

## What it does

Use when designing architecture for production desktop (WinUI, Tauri), mobile (Compose, SwiftUI), or cross-platform apps.

## Structure (headings inside SKILL.md)

- Senior Multi-Platform Application Engineering & Architecture Guide
- Universal Senior Engineering Principles
- Detailed Platform Architecture References
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Presentation Layer**: UI Views, Screens, Components, Theme tokens.

## Key rules (verbatim lines from SKILL.md)

1. 1. **Strict Anti-Monolith Rule**: Never write an entire application or complex screen in a single monolithic file (such as a 500+ line single Python, JS, or C# script).
2. 4. **Dependency Inversion**: High-level modules must depend on abstractions (interfaces/protocols), not concrete implementations.
3. 5. **Real Persistence**: Always back applications with real persistence (SQLite, Room, SwiftData, Drift, Realm, or structured local storage).

## Files inside the skill

- `references/android_jetpack_compose_clean_arch.md` — "Android Clean Architecture Blueprint (Kotlin + Jetpack Compose)"
- `references/flutter_feature_first_clean_arch.md` — "Flutter Feature-First Clean Architecture Blueprint"
- `references/ios_swiftui_clean_arch.md` — "iOS Clean Architecture Blueprint (Swift + SwiftUI + SwiftData)"
- `references/windows_desktop_blueprints.md` — "Windows & Desktop Production Architecture Blueprints"
