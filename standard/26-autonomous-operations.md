# 26. Autonomous operations: the products run themselves, the owner is the chairman (Ahmed, 2026-11-09)

Goal: after launch, every product is operated by AI. A manager AI (Claude today, Gemini or any later model tomorrow) runs everything from written runbooks. Ahmed is the chairman: he receives short Telegram reports and is contacted only for real emergencies or things only a human can do. Every plan must contain this section, fully detailed.

## 1. Inside every product
- A support assistant connected to the product: floating widget or docked drawer, grounded only in the product's real docs, FAQ, changelog and the user's own state (never invented policies), answers in the user's language, walks users through tasks, collects feedback and bug reports, opens a ticket with logs attached when it cannot solve something, and hands over to human-style email support only when needed. Free users have a fair daily limit, owners are unmetered.
- Modern AI features that fit the product (the flagship feature plus assistant, search, summaries, suggestions, automation, voice, vision where useful), on several providers with automatic fallback, privacy routing, cost caps, an evaluation set, and a kill switch. The newest suitable models are chosen from `ops/MODELS.json`-style registry, reviewed monthly.
- Self-diagnosis for the user: "why is this slow or failing" explained in plain words, with a one-tap fix when safe.

## 2. Operations runbook per product (written as tasks with owners and schedules)
- Monitoring and health checks, error digests, automatic restarts and rollbacks, backup and restore drills, dependency and security updates (weekly, with tests), cost and quota watch, incident handling steps, a status page, release trains with staged rollout.
- Support desk: inbox triage by AI, answer templates, escalation rules, response-time targets, weekly insight report from tickets and aggregated usage.
- Growth and marketing, fully planned: positioning, audience, SEO and content calendar, landing pages, store listings and screenshots, launch plan (pre-launch list, launch day, week 1 to 12), social channels run through OFFICIAL APIs and schedulers (brand voice, not impersonating Ahmed), community replies in the brand's name, partnerships and outreach lists, email lifecycle (welcome, activation, win-back), referral program, paid-ad tests only under a spend cap the owner sets, analytics review each week, A/B tests, press kit.
- Business: pricing reviews, subscription health (churn, conversion, refunds), invoices and taxes checklist, legal document refresh when laws change.

## 3. The management ladder
- Owner (chairman) > manager AI (one per portfolio, reads `plans/INSTRUCTIONS_FOR_MANAGER.md`) > project AIs (builder and operator per product) > review AIs (cross-review, different model or lens). Every AI has a written job, daily and weekly loops, and a handover file so the next model continues without loss. The manager can be replaced at any time by any model by reading the handover files.

## 4. When the owner is contacted
- Only: real emergencies (data breach, outage that cannot be fixed, legal notice, money or account at risk, a platform ban), and the few acts only a human can do (sign-in, passkey, 2FA, CAPTCHA, payment, identity or legal signature, buying a domain or plan). Everything else is decided, logged and done by AI.
- Reports reach him on Telegram in short simple Arabic: one weekly summary per product plus emergency alerts. Each alert says what happened, what the AI already did, and the one tap he must do, if any.

## 5. Guard rails that never change
- Tier 3 stays: no leaking secrets, no bypassing CAPTCHAs or 2FA, no fake reviews, followers or engagement, no engagement bots, no scripting X's website, no payments made by the AI, no posing as Ahmed in live conversations, no graded work, AHome and Habiba data never leave their private systems.
- Autonomy has limits written in money and scope (daily AI cost cap, ad spend cap, posting frequency, what may be deleted); anything beyond a limit becomes an owner decision.

## Definition of done for the plan
Each product has: the in-product support assistant and AI feature specified with evals, the full operations runbook, the marketing and launch plan with a dated calendar, the management ladder with handover files, the Telegram report format, the emergency list, and the guard-rail limits.

> AHome exception (owner, 2026-11-09): AHome is private, so it does NOT get the commercial parts of this standard (no subscription, store launch, marketing, SEO, market law packs, public analytics, public legal pages). It still gets everything about quality: best-in-class design, features, animation, security, privacy, reliability, local AI, backups, self-repair. Competitor study for AHome is only feature and design inspiration from the best couple/home/organizer apps.
