# SIR Education Hub Plan Refresh Log (r61, 2026-11-12)

## Overview
Planning-only refresh round r61. No code built, no repos created, no changes inside D:/Projects/SIR Education Hub. All changes under D:/Projects/_SIR (plans/, ops/briefs/, ops/competitors/, ops/research/).

## Changes Made

### 1. Web Research Updates (2026-11-12)
Added current-year findings to the competitor matrix and research section:
- **Moodle 2026**: open-source LMS with WCAG 2.2 AA, certified integrations, B-Corp certified, MoodleCloud hosted option. Takeaway: our self-serve onboarding + Arabic-first + EGP pricing opens a gap below the heavy-admin LMS bar.
- **Classera 2026**: MENA-focused LMS with 30M+ users across 45+ countries, AI + gamification + personalization, ministries and K-12/higher-ed/corporate solutions, enterprise sales motion, opaque pricing. Takeaway: self-serve + transparent pricing + premium UX + integrity-first AI tutor is our opening.
- **Teachable 2026**: course-selling platform with USD pricing, 7.5% transaction fee on Starter only, 7-day free trial + 30-day money-back, iOS/Android student apps, auto-graded quizzes, certificates, drip content, memberships, affiliate program. Takeaway: course-creator UX bar (certificates, drip, quiz auto-grade); our edge is institute-first (timetable, attendance, GPA, multi-tenant) and EGP pricing.
- **Canvas Instructure**: pricing page returned 404 on fetch 2026-11-12; stays "(unsourced, verify)" for exact tiers.
- **Egyptian PDPL 151/2020**: data inventory, legal consent, data subject rights (access, correction, deletion, portability), cross-border transfer restrictions, breach notification. Legal pack must be marked "AI-drafted, to be reviewed by a qualified Egyptian lawyer before paid launch".
- **GDPR**: lawful basis, data minimization, DPIA for minors, parental consent for under-16 (varies by member state), right to erasure, portability, DPO where required.
- **Free APIs worth using**: Firebase Auth (Google sign-in), Firebase Firestore/Storage, Gemini flash-lite/flash via fallback chain, OpenRouter free models, Web Push, ICS (RFC 5545) generation client-side, PDF.js for transcript parsing, Web Speech API for pronunciation practice (local where possible).
- **Regulations to handle before paid launch**: Egypt PDPL 151/2020, GDPR, Saudi PDPL (if expanding to KSA), COPPA-style minor consent, academic integrity (no graded-work solving).

### 2. Plan Detailed Improvements
- Expanded the AI tutor section with explicit refusal eval set (30 prompts: 15 Arabic, 15 English) and strict privacy guarantees
- Added detailed five-states specification for every view (idle, skeleton, empty with CTA, error with retry, populated)
- Documented the multi-tenant data model per-Hub isolation with Firestore deny-by-default rules
- Added the onboarding wizard step validation logic (future steps locked until current step validates)
- Enhanced the pricing section with free tier/Pro details, Hub trial, and "Subscriptions launching soon" fallback
- Expanded the platform matrix with specific version milestones (M0-M6 acceptance tests)
- Added the legal pack section with all 7 required pages and the "AI-drafted, to be reviewed" disclaimer
- Documented the data inventory requirement (data-inventory.yml) and legal pack generation pipeline

### 3. Tasks Expansion
- Verified 66 tasks (T1-T66) covering all plan sections from deep scan through milestone acceptance
- Each task includes acceptance test criteria and referenced skills from ops/SKILLS_INDEX.md
- First 10 tasks (T1-T10) remain queue-ready for free CLI agents
- Additional tasks (T11-T66) cover infrastructure, auth, data model, onboarding, core features, AI, quality, and launch

### 4. Risks and Open Questions (Updated)
#### Risks (each with mitigation):
- R1 Content rights: only notes classmates own and agree to publish; takedown form + upload agreement; default conservative.
- R2 Paying capacity unknown: test price with interviews; keep Pro cheap; no dark patterns.
- R3 Large legacy (62k lines, 24+ files >530 lines): port by feature, never copy wholesale; deep scan first.
- R4 Unverified market claims: every competitor number without a link stays "(unsourced, verify)".
- R5 Result-day traffic spikes: static/edge-cached public pages (timetable, hall directory).
- R6 Multi-tenant isolation must be proven by emulator tests before any real Hub data.
- R7 Parent/guardian view privacy-sensitive: opt-in only, read-only, no cross-student access, audit-logged.
- R8 AI cost can grow with many Hubs: per-Hub cost tracking and daily cap; alert owner if over.
- R9 Graded-work solving by AI (integrity): eval 100% refusal before launch.
- R10 Minor consent flows add friction; needed for compliance.
- R11 Data residency/cross-border transfer under PDPL; keep Firestore region documented.
- R12 Abandoned Hubs (trial expired): grace period, export, archive, not delete.

#### Open questions with recommended answers:
- Q1 Domain name: obourhub.com or sir-education.com or sir-edu.com? Recommended: buy sir-education.com (short, brandable, global) and keep obourhub.com as a redirect for Obour Hub; owner buys per standard 24.
- Q2 First Hub branding: ship Obour Institute as a seeded Hub with emerald palette from the deep plan, or neutral default? Recommended: emerald palette for Obour Hub only, neutral default for new Hubs.
- Q3 Storage backend: Firebase Storage now, R2 as scale alternative behind ADR if egress costs bite. Recommended: Firebase Storage v1, ADR gate at $50/mo egress.
- Q4 Mobile build tooling: Capacitor (per platform matrix) vs PWA-only for v1? Recommended: PWA-only v1, Capacitor M5-M6 as planned.
- Q5 Language module v1 scope: English + Arabic for non-natives only, or more? Recommended: English + Arabic for non-natives v1; French/German as v1.1.
- Q6 Transcript parser: local in browser only (privacy) - keep as planned, never server-side.
- Q7 Marketplace module: optional per Hub, WhatsApp contact direct (no in-app chat for marketplace) - keep as planned.
- Q8 Parent view default: disabled by default, Hub admin enables - keep as planned.
- Q9 AI daily cap value: $2/day platform-wide initially, per-Hub sub-cap - recommended.
- Q10 Certificate verification: public verify-by-code page, no auth - recommended.

### 5. Research Sources (2026-11-12)
All fetches direct, no search-engine scraping. Anything without a link stays "(unsourced, verify)".

### 6. Plan Version
Remains 1.0.0. No version bump during development.

### 7. Next Steps
- Create report at ops/agy-runs/reports/r61-plan-sir-education-hub.md
- Commit and push explicit paths to main
- One line to ops/bus/sir-hq.md