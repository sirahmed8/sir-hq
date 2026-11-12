# pulse-engineering

- Tool: `codex`
- Category: design
- Source: `C:\Users\a7med\.codex\skills\pulse-engineering\SKILL.md`
- SKILL.md size: 2045 chars

## What it does

Expert guidelines for engineering lightweight, production-grade Windows desktop utilities (PowerSync, SysPulse) and modern Next.js 16 Web showcase portals.

## Structure (headings inside SKILL.md)

- PulseTools Engineering & Architecture Standard
- ⚡ Core Rules & Directives
- 1. Strict Versioning Standard
- 2. Native Win32 Performance Principles
- 3. Anti-Flicker & Zero-Glitch Protocol
- 4. Next.js 16 Web Platform Standards
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - All active development tools must remain strictly on **`v1.0.0 (Production Candidate / Developer Preview)`**.
- - Zero fake data: Staged production downloads (`public/downloads/`) and modular Firebase integration (`src/lib/firebase.ts`).

## Key rules (verbatim lines from SKILL.md)

1. - All active development tools must remain strictly on **`v1.0.0 (Production Candidate / Developer Preview)`**.
2. - Do not bump major versions (v2.x, v3.x) until full enterprise release.
3. - Scheme and thermal switches must occur in **<3ms** with zero UI thread blocking.
4. - Synchronize display brightness levels before switching Windows power schemes to eliminate backlight flicker.

## Files inside the skill

- (SKILL.md only)
