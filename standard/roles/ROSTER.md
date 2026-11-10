# Specialist roster (Antigravity workers)

> Status 2026-11-10: AgentsRoom was retired on 2026-11-08 (`ops/AGENTSROOM_RETIRED.md`). The role names `sir-<name>` below are now role descriptions: paste a role file from this folder into the brief when you hand a specialist task to an Antigravity or CLI worker (`plans/CHAT_PROMPT_TEMPLATES.md`). Ignore `agents_spawn`.

The Claude subagent definitions in C:/Users/a7med/.claude/agents and D:/Projects/.claude/agents exist as AgentsRoom roles `sir-<name>`. The Manager (Claude, Sonnet high) sends a specialist task to the matching role on Antigravity (max thinking) with agents_spawn; Claude's own subagents stay for quick read-only chores. The Reviewer approves.

| Specialist | AgentsRoom role | Use for |
|---|---|---|
| ai-engineer | sir-ai-engineer | Module 10 in every product: AI features, the AI gateway and provider adapters, prompts and eval sets, privacy  |
| architect | sir-architect | Designs, ADRs, migration plans, platform decisions and task specs for large features. Writes docs only, never  |
| architect-refactor | sir-architect-refactor | Use when a project needs structural refactoring or a framework upgrade (Next.js 16, React 19, TypeScript stric |
| automation-engineer | sir-automation-engineer | Module 18: n8n workflows with AI steps, exported to the repo and tested. |
| builder | sir-builder | Implements features and refactors from a written task spec (web, backend, shared packages). |
| desktop-engineer | sir-desktop-engineer | Electron, installers, signing, auto-update and Windows/macOS integration. |
| desktop-release-qa | sir-desktop-release-qa | Use for desktop and Electron app QA, binary size and startup checks, GitHub Release workflows, and verifying t |
| docs-keeper | sir-docs-keeper | Keeps CHECKPOINT, BOARD, README, CODEMAP and the session-end ritual current. Edits docs and .sir/ only. |
| explorer | sir-explorer | Use for read-only codebase scanning, dependency checks, log reading, and "where is X / what uses Y" questions. |
| growth-operator | sir-growth-operator | Content strategy and calendars, scripts, posts, community replies, job and freelance search, proposals and bus |
| legal-compliance-counsel | sir-legal-compliance-counsel | Use to draft or sync project-specific legal pages and repo docs (privacy, terms, cookies, refunds, disclaimer, |
| localizer | sir-localizer | Translation pipeline for Arabic, English, Chinese (Simplified) and Hindi: drafts, glossary, consistency and ps |
| mobile-engineer | sir-mobile-engineer | Expo/React Native, config plugins, Android and iOS builds, tablets and foldables, watch targets, EAS. |
| pc-janitor | sir-pc-janitor | Disk audits and cleanup with dry runs first (Phase 2.4). |
| qa-breaker | sir-qa-breaker | Unit, integration and e2e tests, adversarial testing and bug reproduction. |
| release-manager | sir-release-manager | Versioning, changelogs, CI/CD, store metadata and build pipelines. |
| reviewer | sir-reviewer | Fresh-eyes review of every diff against its spec, the SIR Standard and the Definition of Done. Approves or ret |
| scout | sir-scout | Read-only inventory, mapping, incremental scans, log digestion, dependency and licence audits, docs lookup. Ne |
| security-auditor | sir-security-auditor | Threat models, auth and rules review, secrets, dependencies and privacy. Reports, does not fix. |
| security-shield-auditor | sir-security-shield-auditor | Use for security audits and hardening: CSP and security headers, Firestore/RTDB rules, Supabase RLS, secret ex |
| seo-specialist | sir-seo-specialist | Module 16 on every site and store listing: technical SEO, structured data, hreflang, content briefs and ASO. |
| study-coach | sir-study-coach | Obour Institute materials, study kits, practice quizzes and deadline tracking. |
| ui-craftsman | sir-ui-craftsman | Design system, motion, accessibility, RTL and visual verification with screenshots. |
| ui-motion-director | sir-ui-motion-director | Use for visual identity, design tokens, Tailwind v4 @theme systems, Framer Motion spring animations, RTL Arabi |
