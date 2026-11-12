# SIR Handyman Planning Refresh Log

## Round r61 - 2026-11-12 (planning-only, free CLI agents)

### Changes made:
1. Expanded tasks from 10 to 42 granular tasks in ops/briefs/sir-handyman-tasks.md
2. Added web research data on Egyptian home services market (FilKhedma, Khidhma features and pricing confirmed via webfetch on 2026-11-12)
3. Added detailed data model API list with 42 exit checks, each with acceptance test criteria
4. Added AI feature specifications with fallback chain (Gemini flash-lite-latest, flash-latest, OpenRouter free models, local model)
5. Added security and privacy specifications (PDPL 151/2020, eKYC, data handling, rate limits, gitleaks)
6. Added monetisation model details (EGP/USD pricing, 12% service fee, Worker Pro EGP 249/month, customer free)
7. Added launch and marketing plan (5 real workers in one Cairo district, lawyer review gate, domain/DNS, first dispute resolution)
8. Added risks and open questions with recommended answers (11 new risks covering RTL design, cold start, PDPL compliance, gateway limitations)
9. Updated competitor study with fresh data sources (FilKhedma and Khidhma pages fetched and documented on 2026-11-12)
10. Enhanced milestones M0-M6 with granular tasks and exit checks

### Research sources used:
- FilKhedma (https://www.filkhedma.com, opened 2026-11-12, webfetch confirmed fixed prices, 1-month guarantee, 19 service categories)
- Khidhma (https://www.khidhma.com, opened 2026-11-12, webfetch confirmed fixed-price list, 25+ categories, EGP 99/149/199 cleaning, EGP 150 plumber, EGP 175 electrician)
- Competitor study: ops/competitors/sir-handyman.md (2026-11-12)
- OWNER_DEFAULTS.md items 14-16 (design system, bidi, motion)
- GEMINI_QUALITY_CHARTER.md (motion, accessibility, five states)
- SHARED_PLATFORM_KIT.md (architecture, packages, accounts)
- AI_FALLBACK_CHAIN.md (Gemini fallback chain)

### Plan improvements:
- Tasks split into: Foundations (M0: tasks 1-4), Request & Quotes (M2: tasks 6-9), Live Visit & Money (M3: tasks 11-15), Ratings & Notifications (M4: tasks 16-20), AI & Desktop (M5: tasks 21-27), Release & Legacy (M6: tasks 28-42)
- Each task has acceptance test criteria and matching skills from SKILLS_INDEX.md
- First 10 tasks ready for agent queue (tasks 1-10 as originally specified)
- 11 new risks added with recommended answers
- RTL design first mandate enforced (item 36 in tasks)
- PWA offline support added (item 41)
- Paymob/Fawry webhook negative test expansion from 10 to 20 recommended

### Date: 2026-11-12