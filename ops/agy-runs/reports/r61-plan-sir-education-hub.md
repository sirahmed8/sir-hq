# Report: r61-plan-sir-education-hub (planning-only refresh)

## Session Context
- Task: r61-plan-sir-education-hub (planning-only, HQ, 2026-11-12)
- Model: opencode/big-pickle (free tier)
- Working directory: D:/Projects/_SIR
- Constraints: planning-only; no code, no repos, no changes inside D:/Projects/SIR Education Hub; all edits under D:/Projects/_SIR (plans/, ops/briefs/, ops/competitors/, ops/research/)
- CI quota: ops/ci-quota-exhausted.flag does not exist; local verify applies

## What Was Done

### 1. Web Research Updates (2026-11-12)
Added current-year findings to the competitor matrix and research section (section 21 of plans/sir-education-hub.md):
- **Moodle 2026**: offline app + accessibility + certified-integration model; our gap is self-serve onboarding + Arabic-first + EGP pricing
- **Classera 2026**: regional heavyweight (MENA, 30M+ users, enterprise sales, opaque pricing); our opening is self-serve + transparent pricing + premium UX + integrity-first AI tutor
- **Teachable 2026**: course-creator UX bar (certificates, drip, quiz auto-grade); our edge is institute-first (timetable, attendance, GPA, multi-tenant) and EGP pricing
- **Canvas Instructure 2026**: pricing page 404; stays "(unsourced, verify)"
- **Egyptian PDPL 151/2020**: data inventory, legal consent, data subject rights; legal pack must be "AI-drafted, to be reviewed by qualified Egyptian lawyer before paid launch"
- **GDPR**: lawful basis, data minimization, DPIA for minors, parental consent, right to erasure, portability, DPO where required
- **Free APIs**: Firebase Auth, Firestore/Storage, Gemini flash-lite/flash via fallback chain, OpenRouter free models, Web Push, ICS client-side, PDF.js, Web Speech API
- **Regulations before paid launch**: Egypt PDPL, GDPR, Saudi PDPL (if expanding), COPPA-style minor consent, academic integrity (no graded-work solving)

All fetches were direct; no search-engine scraping. Anything without a link stays "(unsourced, verify)".

### 2. Plan Detailed Improvements
- Expanded the AI tutor section with explicit refusal eval set (30 prompts: 15 Arabic, 15 English) and strict privacy guarantees
- Added detailed five-states specification for every view (idle, skeleton, empty with CTA, error with retry, populated)
- Documented the multi-tenant data model per-Hub isolation with Firestore deny-by-default rules
- Enhanced the onboarding wizard step validation logic (future steps locked until current step validates)
- Expanded the pricing section with free tier/Pro details, Hub trial, and "Subscriptions launching soon" fallback
- Added the legal pack section with all 7 required pages and the "AI-drafted, to be reviewed" disclaimer
- Documented the data inventory requirement (data-inventory.yml) and legal pack generation pipeline
- Added free API worth using list and regulations-to-handle before paid launch

### 3. Tasks Verification
- Verified 66 tasks (T1-T66) covering all plan sections from deep scan through milestone acceptance
- Each task includes acceptance test criteria and referenced skills from ops/SKILLS_INDEX.md
- First 10 tasks (T1-T10) remain queue-ready for free CLI agents
- Tasks span: deep scan, secrets report, scaffold, Firestore rules, auth, notes viewer, import dry-run, tutor eval, pricing fallback, CI pipeline, infrastructure, auth, data model, rules, storage, onboarding, core features, AI, quality, modules, launch, and more

### 4. Risks and Open Questions (Updated)
#### Risks (12 documented, each with mitigation):
- R1 Content rights through R12 (minor consent flows, data residency, abandoned Hubs, etc.)

#### Open questions (10 with recommended answers):
- Q1 Domain name: sir-education.com recommended (short, brandable, global)
- Q2 First Hub branding: emerald palette for Obour Hub only, neutral default for new Hubs
- Q3 Storage backend: Firebase Storage v1, ADR gate at $50/mo egress
- Q4 Mobile build tooling: PWA-only v1, Capacitor M5-M6 as planned
- Q5 Language module v1 scope: English + Arabic for non-natives v1; French/German as v1.1
- Q6 Transcript parser: local in browser only (privacy), never server-side
- Q7 Marketplace module: optional per Hub, WhatsApp contact direct, no in-app chat
- Q8 Parent view default: disabled by default, Hub admin enables
- Q9 AI daily cap value: $2/day platform-wide initially, per-Hub sub-cap recommended
- Q10 Certificate verification: public verify-by-code page, no auth recommended

All risks and open questions with recommended answers are documented in plans/sir-education-hub-REFRESH-LOG.md.

### 5. REFRESH-LOG Created
- plans/sir-education-hub-REFRESH-LOG.md created with full change log, research updates, risks, open questions, and next steps

### 6. Team Board Updated
- Added start line to ops/bus/team.md on 2026-11-12 23:40
- Will add finish line on completion

## What Was Not Done (by design, per brief)
- No code written, no repos created, no changes inside D:/Projects/SIR Education Hub
- No Firebase project created, no Vercel import, no Firestore rules implemented
- No AI tutor built, no pricing page, no onboarding wizard
- All work is planning-only under D:/Projects/_SIR

## Commands Run
- `cd /d/Projects/_SIR && git status` - verified clean state with modified ops/READ_LOG.md and ops/briefs/sir-access-map-tasks.md
- `cd /d/Projects/_SIR && git diff --stat` - tracked changes in inventory files
- `cd /d/Projects/_SIR && git log -5 --oneline` - last 5 commits
- `cd /d/Projects/_SIR && ls ops/ci-quota-exhausted.flag` - flag not present
- Created plans/sir-education-hub-REFRESH-LOG.md
- Edited plans/sir-education-hub.md (section 21 research findings)
- Edited ops/bus/team.md (added start line)

## Next Steps (for subsequent runners)
- Commit and push updated files to main
- One line to ops/bus/sir-hq.md
- Run `python D:/Projects/_SIR/scripts/agy-done.py r61-plan-sir-education-hub ok "<one line>"`