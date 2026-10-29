# Phase 7 — Launchpad, Command Center, TickTick

> **Read first:** `START_HERE.md`, then `standard/15-launchpad.md` and `standard/18-automations.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with `phases/08-business.md`.

**7.1 Desktop launchpad.** Each product gets `C:\Users\a7med\Desktop\<Product>\` containing **shortcuts only**, never builds or copies: Start PM session (Claude Code in the project, on Sonnet at high effort, with the project-manager start prompt from A2), Start dev, Open in VS Code, Open in Antigravity, Open Claude Code here, Run tests, Build installers, Open live site / preview, Open Firebase console, Open GitHub repo, Open CHECKPOINT. All of them point into `D:\Projects\<Product>\tools\launcher\`, so every agent knows the source and build location is `D:\Projects`. Apply icons. If a Desktop folder currently holds real source code, back it up, move the code into `D:\Projects`, verify it builds, and leave shortcuts behind.

**7.2 SIR Command Center.** Use `/data:build-dashboard` if available; otherwise build it. It's a local web app in `_SIR/dashboard/`, refreshed by a `collect-status` script that reads every `.sir/status.json` plus git, GitHub, the hosting providers, Firebase, EAS and TickTick. Sections:

- Portfolio grid: product, tier, wave, version, health score, last commit, CI state, web URL.
- Platform matrix: web, Windows (with its Microsoft Store listing), macOS, Linux, Android, iOS, iPad, Wear OS, watchOS, TV and car, each as not started / building / beta / store-ready / live.
- Store-readiness checklist per product.
- Owner actions and blockers.
- Free-tier usage: each provider against its limit, with the next reset time and alerts at 70% and 90% (module 22); AI provider usage and fallbacks (module 10); Claude usage this week.
- Business funnel: content posted, followers, leads, job applications, revenue.

Optionally publish a private, read-only version Ahmed can open on his phone.

**7.3 TickTick.** Restructure into the approved portfolio:

- one TickTick project (or folder) per product line, each with a detailed note (vision, links, status, platform matrix) and checklists per phase;
- merged ideas linked to the product that absorbed them;
- done items checked; nothing deleted (archive instead).

Sync it at the end of every work session.

**7.4 AI automations portfolio (n8n; module 18).**

- **Per project,** in `automations/n8n/` with exported workflows and a README. Examples: a release triggers multilingual changelog posts for approval; a weekly Search Console pull gets an AI analysis that becomes BOARD tasks; new store reviews get AI triage and reply drafts; the support inbox gets classified with drafted answers; a failed health check gets an AI diagnosis summary and a push.
- **Personal and PC automations** live in `D:\Projects\Laptop Manager\automations\`:
  - Downloads organizer (AI classifies and moves files; never deletes)
  - Disk-space watcher; backup reminders; a daily digest of everything
  - Obour Drive watcher (new lecture → summary, flashcards, TickTick deadlines)
  - Job-feed scorer (new postings scored against the CV → shortlist)
  - Lead tracker for freelance and local clients
- Every automation uses AI where judgment is needed and plain nodes for plumbing, logs to the usage ledger, alerts on failure, and has a dry-run mode.
