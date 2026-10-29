# Requirements ledger

Everything Ahmed has asked for, in one place, so nothing is forgotten. Each row says where the mission handles it. HQ updates only the **Status** and **Evidence** columns (⬜ not started · 🔄 in progress · 🔄 agy, opencode (free model), kilo and local Ollama all answer through `_SIR/scripts/ai/ask.ps1`; fallback and secret guard tested; agy credit overage setting turned off. Data terms of OpenCode free and Kilo still to read

"Phase N.x" means a step in `phases/`; "module NN" means `standard/NN-….md`; A0–A6 are the `core/` files (map in `START_HERE.md`).

## Working style and autonomy

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-001 | Agents never ask Ahmed anything and never wait for his approval; they run until everything is finished, and review the team's work until it's right | Rules 7, 18; tiers (A1); quality loop (A2) | 🔄 | Rule written into `D:\Projects\CLAUDE.md` (Phase 0.1); Tier 2 items go to `ops/OWNER_ACTIONS.md` |
| R-002 | Full permission: install whatever is missing, control the browser and the computer | Rule 8; tiers; Phase 1.4 | ⬜ | |
| R-003 | No money is available: nothing is purchased; free tiers and free channels only | Rule 18; Phase 8.0 ladder | 🔄 | Nothing purchased so far; gitleaks installed from the free winget source. Rule is in the workspace `CLAUDE.md` |
| R-004 | Subagents coordinate through shared checkpoint files and messages, report to the main agent, and many focused subagents keep usage low | A2 | ⬜ | |
| R-005 | Team: Sonnet (high) HQ tailors every project's files; a Sonnet (high) manager per project; Haiku (max) builders working from detailed specs | A0, A2 | ⬜ | |
| R-006 | Use the four Google AI Pro accounts through the Antigravity CLI, OpenCode and Kilo as extra workers, and handle their limits | A2 external workforce; Phase 1.10 | 🔄 | agy, OpenCode (free model), Kilo and local Ollama all answer through `scripts/ai/ask.ps1`; fallback and secret guard tested; agy credit overage setting turned off. Data terms of OpenCode free and Kilo still to read |
| R-007 | Handle errors and usage limits without stopping; continue automatically after limits; main agents watch usage | A2 usage and recovery playbooks | ⬜ | |
| R-008 | Claude acts as Ahmed's personal AI this month: proactive, on schedules, maximum results for minimum usage | A0; Phase 1.12 | ⬜ | |
| R-009 | Agents ask themselves: did we forget anything, what's missing, what's next, what would Ahmed think, what might he need | A2 quality loop; AGENTS.md section 9; module 19 | ⬜ | |
| R-010 | Agents remember everything and lose nothing when the context is compacted | `core/04-memory.md`; this ledger | 🔄 | Hooks installed in `~/.claude/settings.json` and script-tested 2026-10-29 (session-start prints reload block, pre-compact wrote snapshot + bridge). Not yet confirmed through a real compaction: check `ops/memory.log` afterwards |
| R-011 | The mission is split into small files to save tokens, with no version labels | This folder | ✅ | Folder structure |
| R-012 | Advice on how many projects to run at once and how to start | A2 "How many projects at once"; `HOW_TO_START.md` | ✅ | |

## Workstation, tools and continuity

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-013 | Fix the Remote Control error ("CCR v2 worker registration failed … 404") | Phase 1.2 | ✅ | 2026-10-29: 27 stale bridge pointers backed up to `D:\Backups\SIR-2026-10-29\bridge-pointers\` and moved; `scripts/rc-hq.ps1` run twice, worker registered on attempt 1 both times, no HTTP 404. Logon task left to Ahmed (OWNER_ACTIONS) |
| R-014 | See and continue every laptop session from the iPhone, in any project, any time | Phase 1.3 | 🔄 | `remoteControlAtStartup: true` set; HQ server connects (Capacity 0/8). Not yet confirmed from the iPhone (needs Ahmed to open the Code tab); power plan is in OWNER_ACTIONS |
| R-015 | Clean connectors; re-enable all skills, MCP servers and connectors that are useful | Phase 1.7 | ⬜ | |
| R-016 | Android SDK and CLI tools, and everything needed to build and test apps, installed and configured | Phase 1.8 | ⬜ | |
| R-017 | After this month, Antigravity with Gemini continues at the same quality without breaking anything, and every change it makes improves things | Phase 9; module 14 | ⬜ | |
| R-018 | Antigravity, Codex/ChatGPT and every CLI (OpenCode, Kilo) get the same rules, skills, agents, MCP servers, plugins and automations, so the end of the month feels like no change | Phase 1.13 | ⬜ | |
| R-019 | Improve and train the local AI models | Phase 1.14 | ⬜ | |
| R-020 | Many n8n AI automations connected to local AIs and the CLIs | Phase 1.11, 7.4; module 18 | ⬜ | |
| R-021 | Non-project instructions, automations and PC tasks live in Laptop Manager (his "Personal OS") | Phase 1.9, 2.4 | ⬜ | |
| R-022 | Disk space is tight; clean drive C:, the Antigravity folder on C:, Laptop Manager, and empty files and folders | Rule 10; Phase 2.4 | ✅ | Dry run (ops/PC_CLEANUP_DRYRUN.md) and cleanup ran 2026-10-29: about 5.9 GB freed (C: 14.47 to 16.27 GB, D: 14.60 to 18.70 GB). Antigravity caches cleared, history kept. Remaining space is games, duplicates in runtime paths and models: personal, left alone |
| R-023 | Everything lives in `D:\Projects`; fix links to the folders he moved there (Learning, Obour Institute Second Year 1st term, AI_Models_Hub, Jobs) | Rule 11; Phase 8.7 | 🔄 | All four folders exist in `D:\Projects`. No Desktop/Start Menu shortcut or Laptop manager/SIR Controller script points to the old paths (scan 2026-10-29). Still open: Ollama does not serve the models in `AI_Models_Hub` (needs `OLLAMA_MODELS`), Phase 1.14 |
| R-024 | A dashboard for Ahmed with everything he needs | Phase 7.2 (Command Center) | ⬜ | |
| R-025 | Update TickTick: detailed, organized notes and tasks for every project, current state checked off | Phase 3.2, 7.3 | ⬜ | |

## AHome

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-026 | Recover the `.remember` folder deleted by mistake in AHome | Phase 2.1 | ✅ | Unrecoverable (not in git, Recycle Bin or any copy); made by the remember plugin, which rebuilds it; `.remember/` now gitignored in AHome (commit a6c254b) |
| R-027 | Remove `D:\Projects\AhmedAndHabiba`; AHome replaces it | Phase 2.2 | ✅ | Backup tested, references mapped, ran and verified 2026-10-29: AHome is the real folder, old name gone, daemons restarted (backup D:\Backups\AHome-2026-10-29) |
| R-028 | AHome's folder shows its project icon | Phase 2.3 | 🔄 | folder.ico (6 sizes) + desktop.ini (Hidden+System, relative path) + read-only folder already set; Explorer visual check pending |
| R-029 | AHome gets everything in the standard, plus special features built just for Ahmed and Habiba | Phase 5 (special cases) | ⬜ | |
| R-030 | AHome uses local AI, stays private, and has no subscriptions | Phase 5; module 21; A4 | ⬜ | |

## Portfolio, merges and new products

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-031 | Make every project premium; they were written by an older model and nothing is trusted until tested | A0; Phase 5 | ⬜ | |
| R-032 | Scan and analyze every project folder, including the Desktop folders he listed | Phase 3.1 | 🔄 | Mapped only (Phase 0.3): `ops/PORTFOLIO.md` lists 20 repos + 5 non-git folders + 25 Desktop launcher folders (all shortcuts, no source). Deep scan and scoring still to do in Phase 3 |
| R-033 | Rebuild broken areas instead of patching them | Phase 5 step 4 | ⬜ | |
| R-034 | 11Players and EGFootball5 are already merged into "Merged sites"; finish it and move the originals to `old projects` | Phase 3.5 | ⬜ | |
| R-035 | Find more merges among existing and new projects; merged products get a new name and identity, or keep a strong existing one; fewer, stronger projects | Phase 3.5 | ⬜ | |
| R-036 | Reflect every merge everywhere: GitHub repos, LinkedIn, profiles, TickTick | Phase 3.5 step 11 | ⬜ | |
| R-037 | New and merged projects get their own Firebase, hosting and GitHub setup, without coming back to Ahmed | Rule 17 | ⬜ | |
| R-038 | The 30 TickTick ideas become products, merged where they fit, each with folders in `D:\Projects` and on the Desktop and an exhaustive plan | Phase 6; A4 | ⬜ | |
| R-039 | Laptop Manager, sirahmed8 and Antigravity Agent Suite get tailored instruction files | Phase 5 (special cases) | ⬜ | |
| R-040 | Benchmark against the big apps and sites in each category and add what they have that we lack | Phase 3.6; module 21 | ⬜ | |

## Every product: platforms and design

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-041 | Web, Windows, macOS, Android, iPhone, iPad, Wear OS and Apple Watch apps for every project | A4 platform matrix | ⬜ | |
| R-042 | TV and car apps are core, not extras | A4; module 20 | ⬜ | |
| R-043 | Support Android 17 and iOS 27 plus older OS versions; Windows and macOS versions as far back as modern toolchains allow | Modules 07, 09; verify-first | ⬜ | |
| R-044 | Layouts for every screen and device, including foldables and Apple's newest form factors | Module 07 | ⬜ | |
| R-045 | Material 3 Expressive on Android and Liquid Glass on Apple platforms | Modules 05, 07 | ⬜ | |
| R-046 | One architecture and structure for all projects; clean, organized, extensible, easy for any developer or AI to understand | Modules 01, 02, 17 | ⬜ | |
| R-047 | A shared design family: different colors and layouts per product, the same Profile and Settings, smooth animations | Module 05 | ⬜ | |
| R-048 | Dark and light modes everywhere; the broken themes rebuilt | Module 05; Phase 5 step 7 | ⬜ | |
| R-049 | Keyboard shortcuts everywhere | Module 05 | ⬜ | |
| R-050 | High performance: 120 Hz and above; every screen size and zoom level | Modules 05–07 | ⬜ | |
| R-051 | Premium backend, frontend, UI/UX, logic and calculations | Modules 01–07 | ⬜ | |
| R-052 | Unique app icon per product; project folders show the project icon | Module 15 | ⬜ | |
| R-053 | Easy test launchers (installer, start local server) in each Desktop folder, opening from the main project folder | Module 15; Phase 7.1 | ⬜ | |
| R-054 | Arabic, English and the two most-spoken other languages (Chinese, Hindi) | A4; module 05 | ⬜ | |

## Every product: features, trust and quality

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-055 | EULA, privacy policy, terms; acceptance required, like any professional app | Module 11 | ⬜ | |
| R-056 | AI features in every project (cloud AI), except AHome's local AI | Module 10 | ⬜ | |
| R-057 | A real changelog generated from releases, never hard-coded | Modules 13, 21 | ⬜ | |
| R-058 | Notifications in every product | Module 21 | ⬜ | |
| R-059 | An owner dashboard for Ahmed: users, analytics and everything else | Module 21 | ⬜ | |
| R-060 | Subscriptions that feel win-win | Module 21 | ⬜ | |
| R-061 | Support, FAQ, help, suggestions and more in every product | Module 21 | ⬜ | |
| R-062 | Secure against hackers and every kind of attack | Module 04; rule 19 | ⬜ | |
| R-063 | No fake or mock data, no inflated or hype wording; everything built professionally | Rule 16; AGENTS.md laws 7 and 14 | ⬜ | |
| R-064 | Versioning starts at 1.0.0: patch for small fixes, minor for features, major for big changes (once live) | Module 13 | ⬜ | |
| R-065 | Same Firebase, hosting, GitHub and Cloudinary setup for every project; ready for real domains and paid cloud later | Rule 17; module 03 | ⬜ | |
| R-066 | Each project's AI instruction file has the same name everywhere ("read AGENTS.md"), is tailored per project, and starts with a deep scan | `standard/agent-files.md` | ⬜ | |
| R-067 | Think of everything Ahmed didn't mention, including technical details | Rule 20; module 19 | ⬜ | |
| R-068 | Every project aims for the top of search engines and AI-assistant recommendations, except AHome | Module 16 | ⬜ | |
| R-069 | Apply how the top tech companies engineer software | Module 17 | ⬜ | |

## Builds and distribution

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-070 | Real, compiled builds of everything at the end: Android, iOS, watches, TV, car, desktop, web | Phase 10 | ⬜ | |
| R-071 | Test APKs on his Android phone; iOS on his iPhone 14 through SideStore | Phase 10 | ⬜ | |
| R-072 | Apps ready for the stores, needing only the developer accounts | Phase 10; A6 owner actions | ⬜ | |

## Income, media, jobs and studies

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-073 | Earn back the 1,200 EGP subscription first, then build a real, growing income | Phase 8.0 | ⬜ | |
| R-074 | Run the ByteVibeHQ accounts (signed in in Chrome): Instagram, TikTok, Reddit, Snapchat, Facebook and X | Phase 8.2 | ⬜ | |
| R-075 | Make videos and posts, with an organized exports project | Phase 8.2 | ⬜ | |
| R-076 | The jobs agent finds work and does it as Ahmed would, or finds and builds projects that bring money | Phase 8.3 | ⬜ | |
| R-077 | The Jobs folder holds the CV and job material; a polished CV and portfolio | Phase 8.3 | ⬜ | |
| R-078 | Build the company: documents, plan, sales kit | Phase 8.4 | ⬜ | |
| R-079 | Obour Institute help: assignments, quizzes, the institute site, the Drive folder, study kits, with academic honesty | Phase 8.6; rule 14 | ⬜ | |
| R-080 | Organize `Learning` and `AI_Models_Hub` | Phase 8.7 | ⬜ | |

## From the original constitution (still in force)

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-081 | All five UI states everywhere (first use, loading skeleton, empty, error with retry, populated with large data) | Module 05; AGENTS.md DoD | ⬜ | |
| R-082 | No queries inside loops; indexes; pagination; transactions and idempotency for money, bookings and inventory | Modules 01, 03 | ⬜ | |
| R-083 | Legal routes with no dead links, a computed copyright year, a cookie banner with "Reject all" | Modules 06, 11 | ⬜ | |
| R-084 | Design craft: no generic AI look, the 60-30-10 color split, WCAG contrast, tabular numbers, 44-pixel targets, instant feedback, no horizontal overflow | Module 05 | ⬜ | |
| R-085 | Self-healing verification loops and evidence-based reports | A2 recovery playbook; A5 | ⬜ | |

## Added on 2026-10-29

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
| R-086 | Where a platform has no posting API, post through the browser: the AI opens the site and uploads the post | Phase 8.2 (order and safeguards); tiers (A1) | ⬜ | |
| R-087 | Every Windows app in the Microsoft Store | Modules 09, 11, 13; Phase 10 | ⬜ | |
| R-088 | Use the best free services available, preferring quotas that reset daily, weekly or monthly; Firebase, Vercel, Cloudinary and Cloudflare are not required if something is better | Module 22 (researched October 2026) | ⬜ | |
| R-089 | AI in every app as the top feature, with AI from several providers and automatic fallback | Module 10; A4 "AI at the core" | ⬜ | |
| R-090 | Find what's missing anywhere in the mission and add it | This review added: rule 21 (content is data); Android without Google services; POS hardware and Egypt e-receipts for SIR Business; tenant isolation; iPhone push needs the Apple account; payments for Egypt; provider adapters; free build minutes; the `ai-engineer` agent. Ongoing through rule 20 and module 19 | 🔄 | October 2026 review |

## New requests

Add new rows here from the Ideas Inbox (R-091 onward), each linked to its inbox entry.

| ID | Requirement | Where | Status | Evidence |
|---|---|---|---|---|
