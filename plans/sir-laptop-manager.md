# PLAN: SIR Laptop Manager (Wave 2, PERSONAL tool, building)
**Version:** 1.0.0 (strictly enforced)  
**Status:** Active development — replacing `Laptop manager` and `antigravity-agent-suite` (both under `legacy/`, kept until M6)  
**Audience:** Ahmed Alaa only — internal sovereign workstation console, never sold, never listed, `noindex`  
**Last updated:** 2026-11-12 (r52 HQ round) — replaces previous plan dated 2026-11-10  

---

## 1. One-Sentence Promise (sell the end state)
Your Windows laptop runs clean, cool, and quiet — every cache quarantined before deletion, every heavy AI worker pauses automatically when you game, and one canonical agent configuration syncs across all 18 coding tools — so you never debug environment drift again.

---

## 2. Competitors & Best-in-Class (10 products)

*Full matrix with sources: `ops/competitors/sir-laptop-manager.md`*

| # | Product | Category | Strongest 3 | Weakest 3 | Our Edge |
|---|---------|----------|-------------|-----------|----------|
| 1 | **Microsoft PC Manager** | Free Windows suite | One-click health checkup; storage analysis with duplicates/large files; deep uninstall removes leftovers | Shallow advanced control; no undo for cleanup; self-promotes auto-start; no battery health; no developer tooling | Real weighted health score with visible inputs; every destructive action behind dry-run + quarantine; no self-promotion; owner-only data |
| 2 | **CCleaner** | Freemium cleaner | Software updater closes security holes; scheduled cleaning; disk & duplicate analyzers | Paid wall around core health; upsell-heavy; closed source; past telemetry complaints; risky registry cleaning | Free internal tool; local-only; quarantine before delete; no upsell; no account required |
| 3 | **Glary Utilities Pro** | Freemium suite | One-click maintenance bundles cleanup/repair/privacy; broad module set; scheduled auto-maintenance | Aggressive upsell; dated UI; registry repair risk; telemetry complaints; low transparency | Modern interface; dry-run + undo on every module; no registry mutation by default |
| 4 | **Razer Cortex** | Gaming optimizer | Auto game detection with pause/restore of background apps; FPS & system telemetry; game library + deals | Gaming-only scope; account/rewards layer; background service telemetry; no startup/driver/battery care | Full PC care not a launcher; no account; local-only; no rewards manipulation |
| 5 | **MSI Center** | OEM control center | Battery Master with charge thresholds & calibration; hardware monitoring & SSD health; thermal profiles | Locked to MSI hardware; module bloat; opaque automation; no quarantine/undo; poor portability | Works on any Windows 11 PC; transparent thresholds; no vendor lock; no module store |
| 6 | **Dell Optimizer** | OEM AI optimization | Battery charge policy & runtime extension; thermal/power profiles; presence-based security | Locked to Dell hardware; custom charge thresholds removed to BIOS; opaque AI; no cleanup/startup control | Owner-visible thresholds & reasons; cross-vendor; no BIOS trip |
| 7 | **BleachBit** | Open-source cleaner | Deep app/privacy cleaning; portable + CLI; no ads/telemetry/account; CleanerML + winapp2 support | Dated UI; permanent deletion no undo; no startup/power/driver/health modules; manual review needed | Quarantine before delete; restore path; modern UI; integrated health score |
| 8 | **Bulk Crap Uninstaller** | Open-source uninstaller | Thorough app/leftover detection; batch uninstall with safety checks; huge metadata export; startup manager | Uninstall-only scope; technical UI; no real-time care; no health score/battery | Safe uninstall flow with restore point + quarantine first; plain-language impact; one clear primary action |
| 9 | **Windhawk** | Windows mod marketplace | Source-available mods; one-click install; active catalogue; engine stability focus | Technical audience; global injection risk; no cleanup/startup; mod quality varies | Per-mod permissions; no global injection by default; snapshot before every change |
| 10 | **Sysinternals Autoruns** | Microsoft startup inspector | Most complete autorun coverage; signature + VirusTotal checks; CLI & offline scan; hide Microsoft entries | Technical/unsafe for novices; no undo; no cleanup/health; no automation | Plain-language impact; safe disable with backup; owner-only; one-tap restore |

---

## 3. Feature List (Parity with Best-in-Category + Owner Ideas)

### 3.1 Core Hardware Telemetry (MVP — verified in checkpoint)
- **CPU**: per-core frequency, load, temperature (via `psutil` + `nvidia-smi` for GPU)
- **RAM**: pressure, available, virtual memory, compression
- **GPU**: memory, thermals, fan speed, power draw, clock offsets
- **Battery**: design capacity, full charge capacity, wear %, cycle count, charge threshold guidance
- **Disk (C: & D:)**: capacity, free space, category breakdown, largest files, SMART health (NVMe TBW, spare %, temp)
- **Network**: gateway latency, DNS, Tailscale DERP relay RTT, WireGuard peer status

### 3.2 Safe Care & Reversible Actions (MVP — verified)
- **Quarantine Engine**: SHA-256 bucket storage, 30-day retention, atomic rollback manifests
- **Dry-Run Cache Scanner**: category totals, per-file preview, individual exclusion, live total update
- **Desktop Shortcut Doctor**: 53+ shortcuts audited, stale isolated with undo script, icon cache rebuild
- **Startup Doctor**: registry + Task Scheduler + services audit, signature verification, delayed-start toggle (60s), per-item detail sheet
- **Uninstall Manager** (rank 4 gap): leftover folder/registry detection, restore point + quarantine before removal, manifest for full rollback
- **Duplicate File Finder** (rank 5 gap): SHA-256 grouping over user-chosen folder, preview every group, keep-one quarantine rest

### 3.3 Game Mode Orchestration (MVP — verified)
- **Detection**: Steam, Epic, Minecraft, Rockstar executables via window class + process name
- **Graceful Relief**: window close messages → preserve snapshot ledger → re-spawn on session end
- **Custom Profiles** (LP-105): per-game process pause rules, immediate persistence
- **After-Action Report** (rank 22 gap): session duration, apps paused/restored, refused-to-close list

### 3.4 Agent Config Sync (MVP — verified)
- **18 Tools**: Antigravity, Claude Code, OpenCode, Kilo, Codex, Cursor, Windsurf, Devin, GLM, ZCode, VS Code, GitHub Copilot, JetBrains AI, Continue, Aider, Cline, Roo, Supermaven
- **Synced Artifacts**: global prompts, rules, skills, MCP servers, slash commands
- **Validation**: dry-run parity check across all 4+ environments, 0 missing rules

### 3.5 Local RAG Assistant (MVP — partial)
- **Corpus**: `D:\Projects\_SIR` plans, `AI_Models_Hub` docs, project `.sir/` folders, legacy sources
- **Model**: local `qwen` embeddings + `qwen2.5-coder` generation (private text never leaves machine)
- **Interface**: embedded search box in dashboard, returns exact snippet + file path <1s
- **Evals** (rank 23 gap): 20 Arabic + 20 English grounded questions, score recorded

### 3.6 Owner Ideas from TickTick & Legacy (explicitly ported)
| Source | Idea | Status |
|--------|------|--------|
| TickTick Sprint Day 24-28 | Agent suite (97 skills) merged with Laptop Manager | **In progress** — licence audit pending, keepers ported to `src/agent_config/skills/` |
| TickTick Idea 1-5,9-11,13,17,18,22 | Prayer routine, habits, meds, water, diet, gym, expenses, personal dev, skills | → **SIR Life** (Wave 6), not here |
| TickTick Idea 15,16 | Price/game deal finder | **Backlog** — needs lawful data sources |
| TickTick Idea 23,26,28,29 | Cars, accessibility map, handyman, movies | **Concept backlog** |
| Legacy `Laptop manager` | Academic orchestrator, Moodle integration, course inventory | **Dropped** — graded-work rule (Tier 3) |
| Legacy `antigravity-agent-suite` | Telegram bridge, n8n workflows, social outputs | **Ported selectively** — Telegram alerts via shared sender only |

### 3.7 Gaps from Competitor Matrix (ranked, with acceptance tests)
*Full list: `.sir/plans/FEATURE_GAPS.md` (24 items)*

| Rank | Gap | Acceptance Test |
|------|-----|-----------------|
| 1 ✅ | Weighted health score (CPU 20, RAM 20, Disk 25, GPU 15, Battery 10, Startup 10; critical caps at 69) | `GET /api/health/score` returns 0-100, band, component scores, findings; browser test 16 contexts |
| 2 ✅ | Battery care card (capacity, wear, cycles, plain guidance, no-battery empty state) | `GET /api/power/battery-wear` renders all fields; wear >20% shows warning |
| 3 ✅ | Update checker (winget + NVIDIA driver, check-only, 10-min TTL cache) | `GET /api/updates` returns list; card: "Not checked" → loading → list/empty/error; no install action |
| 4 | Uninstall manager with leftover detection | Read-only list → select → dry-run leftovers → restore point → quarantine + manifest → no delete without `confirm:true` |
| 5 | Duplicate file finder | Scan folder → SHA-256 groups → preview → keep one → quarantine rest; test: 3 identical files = 1 group, 0 deletions dry-run |
| 6 | Largest files browser | Top 100 files by size with path, modified date, "reveal in Explorer"; no inline delete |
| 7 | Startup impact legend, filter, delayed start | Legend explains High/Medium/Low; filter by impact/location; detail sheet with command+path+signature; delayed-start writes scheduled task |
| 8 | Privacy/telemetry report with toggles | Read-only list of Windows/Edge/Chrome/NVIDIA/Office areas; toggles call documented settings after dry-run preview |
| 9 | Scheduled maintenance plan (round times :00/:30) | Plan card shows next run, tasks, last result; runner writes signed report to `.sir/`; dry-run asserts no deletions |
| 10 | Disk SMART/SSD health readout | `GET /api/disk/health` via read-only PowerShell; green/amber/red state + raw counters; empty state if cmdlet missing |
| 11 | Driver update check beyond NVIDIA | `pnputil /enum-drivers` + NVIDIA version; UI states never auto-installs |
| 12 | Windows Update status card | Last checked, pending count, "check now" opens documented page; never installs |
| 13 | Process detail sheet | PID, CPU, memory, disk, start time, command line, "safe to end" verdict; confirmation + logging |
| 14 | Temperature & fan monitoring | CPU/GPU/fan readings with graph when exposed; "not exposed" state otherwise; no invented numbers |
| 15 | Exportable health/storage report (Markdown + JSON) | Button exports to `_local/`; no secrets/private paths; valid JSON/Markdown headings |
| 16 | First-run setup & consent | Sheet explains local-only, quarantine promise, three never-dos; one primary action; flag stored; reopenable from Settings |
| 17 | Simplified Chinese & Hindi | Every static label + finding message renders in zh-Hans/hi; no AR/EN leakage; no layout break at 320px |
| 18 | Notification center for recommendations | Slide-over: last 50 recs with time, severity, status (open/done/dismissed), link to tab; nothing auto-done |
| 19 | Item-level clean preview | Dry-run lists every file with size, age, category; exclude individual files; total updates live |
| 20 | Quarantine bulk restore & compare | Select 2+ buckets → compare paths/sizes/hashes → bulk restore preview with single confirmation |
| 21 | Startup signature & publisher column | `Get-AuthenticodeSignature` per row; unsigned system-adjacent flagged |
| 22 | Game mode result report | Post-session card: start time, duration, paused, restored, refused; stored locally, dismissible |
| 23 | Backup schedule & last verified time | Timeline: every backup with time, size, hash status, restore drill; weekly schedule at :00/:30 |
| 24 | In-app "what changed" log | Last 30 actions (clean/restore/disable/enable/scan) with time, result, link to tab; appended by services |

---

## 4. Platform Matrix (v1 Scope)

| Platform | v1 Status | Notes |
|----------|-----------|-------|
| **Windows (Host)** | ✅ Built, unverified | Python 3.14 OpsServer on 127.0.0.1:8765; `pythonw.exe` silent logon task `SIR_Laptop_Manager`; system tray companion (`pystray`) |
| **iPhone Companion** | ✅ Built, unverified | Tailscale Tailnet access to 8765; `Tailscale-User-Login` header + CSRF HMAC; no separate app |
| **Web / PWA** | ⏭️ Skipped | Windows-only tool; no public web surface |
| **Android** | ⏭️ Skipped | iPhone companion covers mobile |
| **macOS / Linux** | ⏭️ Skipped | Hardware telemetry Windows-specific (NVML, WMI, winget) |
| **Wear OS / watchOS** | ⏭️ Skipped | No wearable value for PC care |
| **TV / Car** | ⏭️ Skipped | Not applicable |

> **Rule:** PERSONAL products adopt design-tokens, motion, i18n, legal-pack, help-center, ui/styles/hooks, security-baseline, operations-standard, launch-package, visibility-standard from `SHARED_PLATFORM_KIT.md`. No auth/billing/ai-proxy needed (single owner, loopback).

---

## 5. Architecture (on SHARED_PLATFORM_KIT)

### 5.1 Runtime & Daemon
- **OpsServer**: Python 3.14 native (`src/sir_laptop_manager/ops_ui/server.py`) on port 8765, RFC 9110 status codes, graceful `WinError 10054/10053` handling
- **Binding**: 127.0.0.1 only; phone via Tailscale with `Tailscale-User-Login: a7medorabe7@gmail.com` + CSRF HMAC
- **Autostart**: Silent Windows logon task (`scripts/dev-start.vbs` → `SIR_Laptop_Manager`), zero console flash

### 5.2 Layered Structure (per 23-premium-code-bar.md)
```
src/sir_laptop_manager/
├── core/              # Config, logging, constants, threat model
├── telemetry/         # CPU, RAM, GPU, Battery, Disk, Network collectors
├── care/              # Cleaner, shortcuts, startup, quarantine, game_mode, model_pruner, windows_update, task_scheduler, affinity_manager
├── agent_sync/        # 18-tool sync engine, skill manifest, licence audit
├── rag/               # Local embeddings index, workspace search, eval runner
├── look/              # Windhawk manager, display manager, Dynamic Island UI components
├── ops_ui/            # FastAPI routes, static SPA (index.html, app.js, app.css)
├── tray/              # pystray companion (health icon, Game Mode toggle, browser launcher)
└── reports/           # Health report PDF, weekly Telegram builder
```

### 5.3 Shared Kit Adoption (from `SHARED_PLATFORM_KIT.md`)
| Kit Piece | Status | Notes |
|-----------|--------|-------|
| Design Tokens (light/dark/system/high-contrast) | ✅ Adopted | CSS custom properties in `:root`, logical properties only |
| Motion (spring, transform/opacity, Dynamic Island) | ✅ Adopted | `cubic-bezier(0.16,1,0.3,1)`; matching open/close |
| i18n (Arabic RTL first, English, per-char bidi) | ✅ Adopted | `tr()`/`trf()` + `bucketWord()`/`fileWord()`; `<bdi>` isolation |
| Legal Pack (Privacy, Terms, Cookies, DPA) | 📋 Planned | Generated from `data-inventory.yml`; marked "AI-drafted, lawyer review before paid launch" |
| UI Styles/Hooks (InputBox, TabBar, BottomSheet, Card, Chip, Button, DynamicIsland) | 📋 Partial | Extract to Platform when 2+ products consume |
| Security Baseline (Firestore rules deny-by-default, CSP, gitleaks, secrets in env) | ✅ Adopted | Adapted for local-only: no Firestore, secrets in Credential Manager |
| Operations Standard 26 (health check, error digest, nightly backup, weekly deps, status page, Telegram report) | 📋 Partial | Local equivalents: `doctor` cmd, daemon log rotation, weekly snapshot to `D:\Projects\Backups` |
| Launch Package Standard 24 (domain, Cloudflare, Firebase, payment test mode, code-signing) | ⏭️ N/A | Private tool — no public hosting, no billing |
| Visibility Standard 27 (llms.txt, JSON-LD, Search Console, Arabic queries first) | ⏭️ N/A | `robots.txt: Disallow: /`; `<meta name="robots" content="noindex,nofollow">` |

### 5.4 AI Fallback Chain (per `OWNER_DEFAULTS.md` item 11)
1. Gemini `flash-lite-latest` (free tier)
2. Gemini `flash` (free tier)
3. Any Gemini model
4. OpenRouter free models
5. Other free providers (Groq, etc.)
6. **Local models** (Ollama in `D:\Projects\AI_Models_Hub`) — **forced for private text** (`private=true` flag)

### 5.5 Hosting & Identity
- **GitHub (private)**: `sirahmed8/sir-laptop-manager`
- **Firebase Project**: `sir-laptop-manager` (for shared sender token only; no Auth/Firestore used)
- **Cloudflare**: `sir-laptop-manager` (for Tunnel if needed; currently Tailscale only)
- **Dual Hosting**: ⏭️ N/A — no public web product
- **Code Signing**: Required for Windows installer (Standard 24) — owner buys cert

---

## 6. Premium Quality Bar (Apple-Level)

### 6.1 Visual & Motion
- **Design Identity**: Obsidian Cybernetic Console — Emerald `#10B981` primary, Cyan `#06B6D4` secondary, Deep Obsidian `#080C14` canvas, Smoked Glass cards `rgba(17,24,39,0.75)` + `backdrop-filter: blur(16px)`
- **Typography**: `Inter` (UI), `Cairo` (Arabic), `JetBrains Mono` (metrics, hex, paths)
- **Zero Emojis / Zero Yellow Buttons** — purged across Python CLI, web UI, tests
- **Spring Motion**: `cubic-bezier(0.16,1,0.3,1)`; transform/opacity only (120Hz safe); matching open/close for every sheet/panel/modal/drawer
- **Dynamic Island Tab Bar**: active label centered in pill, inactive collapse to monochrome SVG icons, swipe between tabs, zero white outline glitches

### 6.2 Responsive & Accessible
- **Breakpoints**: 320, 390, 768, 1280, 1920 px — no horizontal overflow (`scrollWidth <= innerWidth`)
- **RTL-First**: logical CSS properties (`margin-inline-start`, `padding-inline-end`); per-character bidi detection in inputs (Arabic types right, Latin left); mixed content `<bdi>` isolated
- **Touch Targets**: minimum 44px; click-target audit in CI (no covered/zero-size hit areas)
- **Five States on Every Screen**: idle, loading skeleton (matches final layout), empty (one clear action), error (human message + Retry), populated (paginated/virtualized, fine with 1000+ items)
- **Themes**: light, dark, system, high contrast (WCAG 2.2 AA) — all tokens defined once in `:root`
- **Browser Tests**: Playwright + system Chrome/Edge; headless, `--mute-audio`, `speechSynthesis.speak` stubbed; browser closed in `finally` block

### 6.3 Content Integrity
- **No Mock Data**: every value from real command/file/sensor or UI says "unavailable"
- **No Invented Numbers**: health score computed from real telemetry; battery wear from WMI; disk from `Get-Volume`
- **Arabic First**: Egyptian dialect; English second; zh-Hans/hi planned (rank 17)
- **Escaping Discipline**: `escHtml()` for all interpolated text/attributes; `escapeJs()` only inline handlers; `safeHref()` http(s) only for external links

---

## 7. Free Tier & Fair Pricing (EGP / USD)

| Tier | Audience | Price | Includes |
|------|----------|-------|----------|
| **Internal (Owner)** | Ahmed only | Free (private repo) | Full feature set; local models only; no quota; all platforms Windows+iPhone |
| **Future Commercial** | If ever sold | EGP 0 / USD 0 (free tier) | Core telemetry + cleanup dry-run; no Game Mode, no agent sync, no RAG |
| | | EGP 149/mo / USD 3/mo (Pro) | All features; cloud sync opt-in; priority support |
| | | EGP 449/mo / USD 9/mo (Team) | Pro + 5 seats; admin dashboard; shared quarantine policies |

> **Note:** Currently PERSONAL — no billing, no Auth, no public distribution. If commercialized, generic billing moves to the shared standards kit first (Wave 7).

---

## 8. Milestones M0–M6 (with Acceptance Tests)

| Milestone | Goal | Owner-Visible Exit Check |
|-----------|------|--------------------------|
| **M0: Foundations & Desktop Kit** | Create folder from naming rules; `git init`; private GitHub repo `sirahmed8/sir-laptop-manager`; `.sir/` file set (project.yml, CHECKPOINT, BOARD); AGENTS/CLAUDE/GEMINI from templates; data dir + `.env` outside git; backup to `D:\Projects\Backups`; snapshot/restore drill in `.sir/evidence/`; threat model + privacy map in `docs/`; auth design (2 named accounts, passkey/password+TOTP, sessions, lockout, device allow-list, Tailscale/Cloudflare Access) as ADR; local verify (lint, typecheck, tests, gitleaks) green | 1. `git status` clean; 2. GitHub repo exists private; 3. `.sir/` complete; 4. `scripts/verify.ps1` green → `.sir/evidence/verify-latest.md` with real counts; 5. `git check-ignore` confirms no secrets; 6. Threat model ADR in `docs/`; 7. CI green badge URL in checkpoint |
| **M1: Core Slice** | Dry-run cleanup + quarantine with manifest/restore tests; agent config sync tested on temp workspace; skills imported post-licence-audit; routines registered in Task Scheduler | 1. Quarantine temp file → restore → hashes equal (evidence); 2. Sync dry-run on temp workspace → no deletions; 3. `schtasks /query` shows `SIR_Laptop_Manager` routine; 4. Licence audit CSV: every row has licence or "unknown"; unknown not imported |
| **M2: Parity with Old Project** | All legacy features ported: telemetry, care, game_mode, agent_sync, RAG, look, tray; 207+ tests pass; browser tests at 4 widths × 2 langs × 2 themes = 16 contexts | 1. `uv run pytest -q` → 0 failed; 2. Browser test screenshots in `.sir/evidence/m2/` at 320/390/768/1280 × en/ar × light/dark; 3. `scrollWidth <= innerWidth` in all captures |
| **M3: Security & Reliability** | Security checklist green: no public bind, no route answers without valid session, brute-force lockout, bad input/path traversal/secret scan tests; backup/restore/rollback runbook tested; `doctor` command prints health in one screen; dry-run + undo for every destructive action tested | 1. `scripts/verify.ps1` green; 2. Security tests in `tests/test_security_*.py` pass; 3. Restore drill evidence; 4. `doctor` output screenshot; 5. Path traversal test for every POST route |
| **M4: AI & RAG** | RAG over notes with Arabic + English evals (20+20); local model fallback chain working; `private=true` forces local; eval runner exits non-zero below threshold | 1. `.sir/evidence/rag-eval.md` with 20 AR + 20 EN scores; 2. Fallback chain test: quota → local → fail closed; 3. Search returns exact snippet + path <1s |
| **M5: Quality Sweep** | Every screen/command has 5 states; Arabic/English correct; keyboard use complete; accessibility checked; performance budget recorded; self-audit loop: 2 clean cycles at 4 widths × 2 langs × 2 themes, 10+ defects found & fixed per cycle, before/after in `.sir/evidence/` | 1. Screenshots of every tab at 320/390/768/1280 × RTL/LTR × light/dark; 2. Lighthouse mobile ≥90; 3. Axe a11y 0 violations; 4. 2 clean audit cycles with 10+ fixes each |
| **M6: Release & Retirement** | Retire both v1 folders; archive `antigravity-agent-suite` repo; move `legacy/*` → `D:\Projects\old projects\`; record in checkpoint; keys rotated (names only in `docs/OWNER_STEPS.md`); Desktop folder kit recreated per OWNER_DEFAULTS.md item 19 | 1. `legacy/` moved to `old projects\`; 2. Old GitHub repos archived; 3. Keys rotated (list in `OWNER_STEPS.md`); 4. Desktop folder exists with `folder.ico`, shortcuts (web links×2, Start/Stop dev, Windows app, Android APK, iOS guide, Open project folder), `Versions.txt` (1.0.0, status) |

---

## 9. First 10 Tasks for Free Agents (ready to queue)

*Full briefs: `ops/briefs/sir-laptop-manager-tasks.md`*

| # | Title | One-Paragraph Brief |
|---|-------|---------------------|
| 1 | **Fix 19 Failing Tests** | Restore or rename `execute_cleanup` in `src/sir_laptop_manager/ops_ui/server.py` or update tests in `tests/test_ops_ui_server.py` and `tests/test_tailnet_allowlist.py`; run `uv run --offline pytest -q` until 0 failed; update checkpoint with real pass count. |
| 2 | **Hardening `verify.ps1`** | Make `scripts/verify.ps1` fail on any failing test, write date + result to `.sir/evidence/verify-latest.md` with real counts; run it, confirm file shows actual numbers; commit. |
| 3 | **Push to GitHub & Record CI** | Push to `sirahmed8/sir-laptop-manager`; if Actions red, fix; record green run URL in checkpoint; ensure `.github/workflows/` runs lint+typecheck+tests+gitleaks. |
| 4 | **Security Tests for Every POST Route** | Add `tests/test_ops_ui_security.py` with path traversal + bad-origin tests for every POST route; a route without guard must fail; pytest passes. |
| 5 | **Restore Drill Evidence** | Quarantine a temp file via API, restore via API, compare SHA-256 hashes; write `.sir/evidence/restore-drill.md` with before/after hashes; confirm equal. |
| 6 | **Licence Audit Script for 97 Skills** | Write `scripts/license_audit.py` scanning `legacy/antigravity-agent-suite/skills/`; output CSV (name, licence, source URL); every row has licence or "unknown"; unknown skills excluded from import; save CSV to `.sir/evidence/skills-licences.csv`. |
| 7 | **Port Keeper Skills with Manifest** | Port licence-clear skills from legacy into `src/agent_config/skills/` with `manifest.json` (name, version, licence, source); sync dry-run lists them with 0 deletions; test passes. |
| 8 | **RAG Eval Set + Runner** | Create 20 Arabic + 20 English grounded questions in `tests/rag_eval/`; write `scripts/rag_eval.py` runner using local `qwen` embeddings; print + save scores to `.sir/evidence/rag-eval.md`. |
| 9 | **Telegram Weekly Report Builder + Privacy Filter** | Implement `src/sir_laptop_manager/core/report.py` building weekly Arabic report (disk free C:/D:, bytes freed, quarantine size, last backup, failed tests); privacy filter redacts paths outside project names; test proves private path redacted; real send returns API ok. |
| 10 | **Five-State Screenshots + Overflow Fix** | Capture Cleanup and Game Mode tabs at 320/390 px (en/ar, light/dark) via `scripts/capture_*.mjs`; assert `scrollWidth <= innerWidth`; fix any overflow; save evidence to `.sir/evidence/m5/`. |

---

## 10. Relevant Skills (from `ops/SKILLS_INDEX.md`)

| Skill | Category | Why It Applies |
|-------|----------|----------------|
| `laptop-admin` | security | Official executive laptop management for Sir Ahmed; desktop launchers, multi-app workflows, security hygiene |
| `modern-app-engineering` | design | Production desktop (Tauri/WinUI), mobile (Compose/SwiftUI), cross-platform architecture |
| `production-engineering-standards` | ops | Zero-mock persistence, atomic transactions, schema validation, testing |
| `database-reliability-transactions` | data | Atomic transactions with rollback, idempotency keys, query indexing, keyset pagination |
| `zero-trust-security-hardening` | security | RLS tenant isolation, parameterized queries, secure cookies, rate limiting |
| `emil-motion-impeccable` | design | Spring physics, fluid micro-interactions, layout morphing, spatial rhythm |
| `mobile-ergonomics-polish` | build | Eliminates horizontal scroll, fluid drawers, responsive touch targets, feedback |
| `anti-vibecoded-design-system` | design | Bespoke high-contrast tactile UI, eliminates purple gradients/pill buttons |
| `taste-design-engine` | design | Premium visual polish, self-auditing, image-to-code replication |
| `modern-ui-ux-design-system` | design | Tokens, micro-interactions, visual hierarchies |
| `verification` | build | Full-story E2E across browser, API, data flow, runtime |
| `pulse-engineering` | design | Lightweight Windows desktop utilities + Next.js 16 showcase portals |
| `pc-storage-guardian` | automation | Storage telemetry, safe temp/cache pruning, SSD wear preservation |
| `omniroute-resilience-gateway` | automation | AI model routing with multi-provider failover on quota exhaustion |
| `gemini-api-dev` / `gemini-live-api-dev` | design | Local RAG inference, structured output, streaming |
| `firebase_basics` / `firebase_auth_basics` / `firebase_firestore` | data | Shared sender token, future cloud sync if commercialized |
| `vercel-cli` / `vercel-functions` / `vercel-storage` | design | Dual hosting preparation, serverless functions, Blob/Edge Config |
| `shadcn` | design | Radix UI + Tailwind components for web dashboard if extended |
| `a11y-debugging` | design | Chrome DevTools MCP for WCAG 2.2 AA auditing |
| `debug-optimize-lcp` | build | LCP optimization for web dashboard |
| `owasp-vulnerability-shield` | security | OWASP Top 10 audit for API endpoints |
| `vibe-auth-hardening` | security | Cookie security, server-side RBAC, 2FA/OTP, rate-limited endpoints |
| `legal-compliance-shield` | security | Privacy policy matching collection, liability caps, cookie reject, DPAs |
| `commercial-app-blueprint` | design | llms.txt, service silos, case studies, sticky CTAs, trust signals |
| `open-seo-auditor` | design | SEO/GEO, JSON-LD schemas, AI search visibility |
| `system-design-architect` | design | Distributed caching, rate limiters, message brokers, high-scale backends |
| `agent-supercharged-os` | automation | 4-phase discipline (Plan, Test, Implement, Review) + cross-session learning |
| `direct-action-shield` | media | Terse, numbered, immediately actionable steps |
| `high-conversion-copywriting` | design | Direct-response copy, eliminates AI buzzwords, sells end state |
| `internet-skill-finder` | research | Discovering, vetting, benchmarking, importing cutting-edge skills |
| `skill-creator` | automation | Creating new agent skills from workflows |
| `sir-ecosystem-orchestrator` | automation | Coordinating 23 workspaces, health check validation |
| `sir-ahmed-career-autopilot` | design | Job applications, multi-board scraping, ATS CV, recruiter outreach |
| `github-gem-seeker` | research | High-potential open-source repos, emerging tooling |

---

## 11. Risks & Open Decisions (with Defaults)

| Risk | Default Decision |
|------|------------------|
| Safety classifier blocks global agent config edits | Project-scope sync only; global writes → `OWNER_ACTIONS.md` as one command |
| "All green" claim was false (19 failing tests) | No milestone called done until Task 1 & 2 complete |
| Python 3.14 wheel availability | Keep 3.14, pin in `pyproject.toml`; fallback to 3.13 if wheel missing |
| Game Mode pauses other local services (Jobs, Study, Control Room, Ollama) | Visible banner + one-tap restore, tested |
| Licence audit of 97 skills incomplete | Keep MIT/Apache/BSD; drop unknown; unknown skills never imported |
| Tailscale terms change / Cloudflare Access limits | ADR documents current terms; fallback to Tailscale-only with header check |
| NVML / WMI access on non-ASUS hardware | Graceful "not exposed" states; no invented numbers |
| Owner UAC prompt for scheduled task install | Documented in `OWNER_STEPS.md`; agent prepares script, owner runs once |

---

## 12. Verification & Definition of Done

**Nothing is "working" until verified today** (Truth Rule). Every checkpoint claim must have:
- Command output pasted in checkpoint
- Screenshot paths in `.sir/evidence/`
- Test results (pytest, ruff, mypy, Playwright)
- Browser audit: 0 findings at 320/390/768/1280/1920 × RTL/LTR × light/dark/high-contrast
- Self-audit loop: 2 clean cycles, 10+ defects found & fixed per cycle with before/after evidence

---

## 13. Files to Commit (this round)

- `plans/sir-laptop-manager.md` (this file — replaces 2026-11-10 version)
- `ops/competitors/sir-laptop-manager.md` (competitor matrix with sources)
- `ops/briefs/sir-laptop-manager-tasks.md` (10 task briefs for free agents)

---

## 14. Bus Note (one line to `ops/bus/sir-hq.md`)

`r52: SIR Laptop Manager premium plan written — competitor matrix (10), 24 ranked gaps, 10 tasks queued, M0–M6 with acceptance tests, skills listed, SHARED_PLATFORM_KIT adoption mapped`