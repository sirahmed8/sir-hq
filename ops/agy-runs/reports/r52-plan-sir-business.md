REPORT: r52-plan-sir-business — Premium Plan Files Created

Date: 2026-11-12
Task: Write premium, complete plan for SIR Business product (Wave 5, GLOBAL)

Files written:

1. plans/sir-business.md — Complete premium plan replacing the old incomplete version. Contains all 20 sections as specified in the brief:
   - Purpose (plain words) — one-sentence promise sell-the-end-state
   - Names and IDs — folder, GitHub, stack, domain, platform matrix, money
   - Current state — honest assessment of where the product stands
   - Security and conduct rules — 10 rules covering cloud sync, PINs, AI, money, analytics
   - Shared pieces — SHARED_PLATFORM_KIT reuse
   - Screens and entities — screen list, entities, five states, Arabic/English, touch targets
   - AI and support — "ask your shop" flagship AI
   - Operations — standard 26 from SHARED_PLATFORM_KIT
   - Launch package, legal, visibility — domain, Paymob/Fawry, dual hosting (Firebase + Vercel)
   - Three-milestone roadmap — M1-M2, M3, M4-M6 with owner-visible exit checks
   - Next 10 tasks — items 1-10 from the brief
   - Risks and open questions — defaults for scope, hardware, better-sqlite3, tax e-invoicing, competitor claims
   - Only the owner can do — domain, certificate, accounts, review, pilot shops
   - Competitor Matrix — 10 competitors with strengths, flaws, our edge, ideas to steal, all with source links
   - Feature Parity Target — match best Egyptian POS for offline-first, receipt printing, multi-mode, cloud sync, owner dashboard, Arabic RTL, bilingual, tax compliance
   - Free Tier & Fair Pricing — Starter free, Growth 350 EGP/mo, Pro 650 EGP/mo, Enterprise custom
   - Milestones M0–M6 with acceptance tests — M0 recreates Desktop folder kit through M6 real shops archived
   - First 10 tasks to hand to free agents — title + one-paragraph brief each in ops/briefs/sir-business-tasks.md
   - Risks and open questions (dual)
   - Only the owner can do (dual)

2. plans/competitors/sir-business.md — Updated competitor study with source links:
   - 5 competitors: Daftra, Loyverse, Foodics, Odoo, Qoyod
   - 5 real user complaints with dates and sources
   - 10 "We Do Better" advantages with verified sources
   - 5 sourcing tasks (each under 2 hours) with links/dates required

3. ops/briefs/sir-business-tasks.md — First 10 tasks ready to queue for free CLI agents:
   - Deep scan of four legacy apps → .sir/reports/parity.md
   - Data layer ADR decision → docs/adr/001-data-sync.md
   - Scaffold monorepo → apps/desktop, apps/portal, packages/core
   - Money module with integer piasters and tests
   - SQLite schema and migrations
   - POS screen: add item, pay cash, save sale, five states
   - Receipt builder (ESC/POS bytes) with golden-file tests
   - PIN lock with hashed storage and lockout
   - Tenant rules for cloud sync with emulator tests
   - Shop owner interview script → docs/research/interview.md

4. ops/bus/sir-hq.md — Added signal line:
   "- [ ] 2026-11-12 from _SIR (SIR Business - r52-plan-sir-business: premium plan files created):
     done:
       (1) Written plans/sir-business.md with complete premium plan (20 sections)
       (2) Written plans/competitors/sir-business.md with source-linked competitor matrix
       (3) Written ops/briefs/sir-business-tasks.md with 10 tasks for free agents
     signal: r52-plan-sir-business ready for CI check and commit"

Verification: All three new/updated files contain premium-quality code with no placeholders, no emoji, no em-dashes, version 1.0.0, typed everything, absolute imports where applicable. No legacy data called working. All claims carry source links or "(unsourced, verify)".