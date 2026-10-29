# Phase 5 — Upgrade existing projects, in waves

> **Read first:** `START_HERE.md`, then `standard/README.md`, `standard/agent-files.md` and `standard/project-templates.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with the next wave (Phase 10 builds run at every milestone).

Per project:

1. Take the lock and create branch `sir/upgrade-v1`.
2. Install the SIR file set (AGENTS, CLAUDE, GEMINI, `.sir/`, docs).
3. Security first: fix every finding, then harden the project to module 04 (threat model, rules, App Check, rate limits, headers, the CI security job).
4. Restructure to the standard layout. Rule: **rebuild instead of patching** any area that scores ≤ 2/5 in the inventory (for example broken themes, messy UI, no real architecture).
   - First write a feature-parity checklist of everything the old version does.
   - Rebuild on the SIR Platform, verify parity, then switch over. The `pre-sir-snapshot` branch keeps the old version.
   - Areas scoring 3 or more are refactored incrementally, building at every step.
   - Record an ADR either way; no need to ask.
5. Adopt the shared packages.
6. Add missing platforms per the platform matrix (A4).
7. Themes rebuilt from tokens: light, dark, system and high contrast. The old themes are broken, so don't patch them. Keyboard shortcuts (both in module 05).
8. AI at the core: the flagship AI feature, the assistant and the free provider chain (module 10); legal and consent; all project locales (module 05); TV and car apps, widgets and the other platforms in module 20; notifications, the owner dashboard, help and support, and subscriptions (module 21; AHome has none); the benchmark gaps (module 21); search and store discovery (module 16); project automations (module 18); icons and launchers; tests and CI; then the completeness sweep (module 19).
9. Version `1.0.0-beta.N`.
10. Fresh-agent review; merge once CI is green and the reviewer approves (Tier 1).
11. Real builds for every target platform (Phase 10).
12. Update CHECKPOINT, PORTFOLIO and TickTick; release the lock.

Special cases:

- **Laptop Manager, sirahmed8, Antigravity Agent Suite** are not multi-platform products. Give them the SIR file set and the engineering and quality standard, tailored to their type. Laptop Manager is a local Windows utility. sirahmed8 is Ahmed's GitHub profile and portfolio; make it a strong hiring magnet. Antigravity Agent Suite is agent tooling; align it with this standard so it reinforces the same rules inside Antigravity.
- **SIR ModPack and SIR Mods for GTA V** (proposed): a website plus a Windows installer or mod manager. No mobile or watch apps unless Ahmed overrides. Follow the game publisher's current mod policy (for GTA V, Rockstar's PC single-player mod policy: no online use, no paid access, no ripped assets; verify), and list them only in stores whose policies allow mod tools.
- **Client and organization projects** (the inventory confirms ownership; possibly Negm Furniture, Hagoozat Elite or Obour Academic Hub): their brand and production belong to the owner. Build and upgrade on previews; production releases go out after the owner approves (the agent prepares the summary and a link for Ahmed to forward). That's an outside dependency, not a wait: other work continues.
- **AHome** is private, for Ahmed and Habiba only. It gets the full platform set and everything in this standard, but stays auth-gated, in a private repo, with no public store listing unless Ahmed decides otherwise, and with no subscriptions, ads or paywalls: every feature is free for its two users. Its AI runs **locally** (on the laptop's RTX 4050, for example through Ollama, sized for 6 GB VRAM), with a secure private path for the phones (for example a private VPN/tunnel). Design it and write an ADR. Keep its special features, and propose new ones built just for the two of them.
