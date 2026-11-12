# modern-app-engineering

Source read: `C:\Users\a7med\.claude\skills\modern-app-engineering\SKILL.md` (2.1 KB; claude revision; codex/cursor/kilo/opencode/windsurf listed; `references/` has 4 platform blueprints).

## Summary
Senior multi-platform architecture guide enforcing universal principles — strict anti-monolith (no 500+ line single files), four-layer separation (Presentation / Domain-State / Data / Core-DI), reactive state management (UI derived from state streams), dependency inversion on abstractions, and real local persistence (SQLite/Room/SwiftData/Drift/Realm) — then routing to platform-specific blueprint references: Windows desktop (Tauri v2, PySide6 MVVM, .NET 9 WinUI 3), Android (Kotlin + Compose + Room + Hilt clean architecture), iOS (Swift 6 + SwiftUI + SwiftData + @Observable), Flutter (feature-first clean architecture, Riverpod 2.x + Drift + GoRouter).

## When to use / when NOT
Use when starting or restructuring a native/cross-platform app project (desktop, mobile, Flutter). Not for web-only Next.js work (use nextjs/modern-web-guidance) or for small scripts where layering is overkill.

## Inputs, outputs, tools
- Inputs: target platform(s), app scope.
- Outputs: layered project structure, boilerplate, dependency choices per platform.
- Tools: Tauri v2, PySide6, WinUI 3/.NET 9, Kotlin/Compose/Room/Hilt, SwiftUI/SwiftData, Flutter/Riverpod/Drift/GoRouter — per references.

## 5 most important rules
1. Anti-monolith: decompose into Presentation / Domain-State / Data / Core layers; never one giant file.
2. UI is strictly derived from reactive state streams.
3. Depend on abstractions (interfaces/protocols), not concrete implementations.
4. Always real persistence — no in-memory-only state for production apps.
5. Read the platform blueprint reference before scaffolding; each has copy-paste-ready structure and deps.

## Risks / owner notes
Blueprints are starting points — adapting them blindly can produce over-layered code for simple apps (YAGNI tension with karpathy-skills). Version drift in referenced frameworks is possible.

## Category and tags
Category: build. Tags: architecture, clean-architecture, desktop, mobile, flutter, tauri, compose, swiftui.
