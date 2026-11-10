# The SIR Standard (install in every project)

Standard version: **1.0.0** (SemVer; Phase 9 explains how it evolves). This folder is the master copy. Projects receive the modules as `docs/sir/standard/` through `sync-standard` and never edit their copy.

## B0. The file set, and how each tool loads it

Every project gets this file set. "Read AGENTS.md" is the one phrase Ahmed can use in any tool, any project.

| File | Purpose | Loaded by |
|---|---|---|
| `AGENTS.md` | The front door: project facts, core laws, workflow, DoD summary, module index. **Keep it under 18 KB.** | Antigravity natively; Claude Code through `CLAUDE.md`; Codex, Cursor and others natively |
| `CLAUDE.md` | First line `@AGENTS.md`, then Claude-only notes. Short. | Claude Code |
| `GEMINI.md` | Antigravity/Gemini guardrails. Short. Antigravity combines it with `AGENTS.md`. | Antigravity |
| `.agents/rules/sir-standard.md` | `trigger: model_decision` index so Antigravity loads modules on demand. Frontmatter is mandatory; a rule without it is silently dropped. | Antigravity |
| `docs/sir/standard/NN-*.md` | Synced copy of the 27 modules (01 to 27). Never edit locally; change the master in `_SIR/standard` and run `sync-standard`. | Read on demand |
| `.sir/` | `project.yml`, `CHECKPOINT.md`, `BOARD.md`, `inbox/`, `reports/`, `decisions/`, `status.json` | Every agent at session start |
| `README.md`, `docs/PRODUCT.md`, `docs/ARCHITECTURE.md`, `docs/CODEMAP.md`, `CHANGELOG.md`, `SECURITY.md` | Human and AI documentation | Humans and agents |

Why the size discipline: Antigravity truncates any rule file over 24,000 bytes and gives all always-on rules a shared budget of about 20,000 tokens. Claude Code loads `CLAUDE.md` imports in full into every session. So the always-loaded part stays lean, and depth lives in modules that agents read when the task needs them.

Personal information stays out of repos. The owner line is the only personal data in this standard; anything else about Ahmed lives in the global user files, never in project files (some repos may be public).


## B2. Standard modules

Each module below becomes one file in `docs/sir/standard/`, named exactly as the AGENTS.md index expects: `01-engineering.md`, `02-architecture.md`, `03-data-backend.md`, `04-security-privacy.md`, `05-design-system.md`, `06-web.md`, `07-mobile.md`, `08-watch.md`, `09-desktop.md`, `10-ai.md`, `11-legal-stores.md`, `12-quality-gates.md`, `13-release.md`, `14-continuity.md`, `15-launchpad.md`, `16-search-discovery.md`, `17-engineering-playbook.md`, `18-automations.md`, `19-completeness.md`, `20-platforms-tv-car.md`, `21-product-essentials.md`, `22-free-stack.md`, `23-premium-code-bar.md`, `24-launch-package.md`, `25-market-grade.md`, `26-autonomous-operations.md`, `27-visibility.md`. Versions and policies marked "verify" must be checked against official docs at the time of use.
