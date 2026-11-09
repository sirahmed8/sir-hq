# 25. Market grade: built like the big companies, per country (Ahmed, 2026-11-09)

Every plan (all projects, built, current and future) must also contain a MARKET-GRADE section. It is written by the AI after real research (web search, store pages, reviews, forums, pricing pages, documentation), with sources and the date of research. Nothing here is a guess.

## 1. Competitor study (per product)
- Find the 5 to 10 strongest competitors and the biggest company in the category (for example Google, Microsoft, Apple, Notion, Todoist, LinkedIn, Upwork). For each: what it does, how it is built (stack hints, platforms, pricing, plans), best features, weaknesses, what users complain about (store reviews, Reddit, forums, support threads), and what is missing for Arabic and Egyptian users.
- Output `plans/competitors/<slug>.md` with a feature matrix, a pain-point list with links, and a "we do better" list that becomes tasks in the product's backlog. Repeat every quarter.

## 2. Country and region fit
- Per target market (Egypt first, then Saudi Arabia, UAE, Gulf, Levant, North Africa, then EU, UK, US): language and dialect, RTL/LTR, calendar and numerals, currency and price points, payment methods people really use, tax (VAT, e-invoicing, Egyptian tax rules), data-protection law (Egypt PDPL 151/2020, Saudi PDPL, UAE PDPL, GDPR, UK GDPR, CCPA/CPRA, COPPA, Apple/Google store policies), content rules, consumer-protection and auto-renewal rules, accessibility law (WCAG 2.2 AA, European Accessibility Act), cookie and tracker consent, data residency, age limits, export controls. Each rule becomes a concrete task with a test or a page.
- Per-region switches in the product: language, currency, legal pages, payment methods, feature flags, consent banners and store listings.

## 3. Personalization and learning from use, without exposing people
- Opt-in, privacy-first analytics: collect only what improves the product (feature usage counts, funnel steps, error rates, speed, device class), pseudonymous IDs, no message text or private content, short retention, aggregation, a clear consent screen with an off switch, and a data-export and delete flow. No third-party trackers before consent.
- Personalization on the device or with aggregated signals: suggestions, defaults, onboarding paths and diagnostics ("what is slowing you down") based on the user's own usage, always explainable and switchable.
- A weekly product-insight report generated from the aggregated numbers, feeding the backlog.
- NOT for private projects: AHome and everything about Habiba collect nothing and send nothing; Study, Jobs and Laptop Manager are personal tools: local-only insight unless the owner decides otherwise.

## 4. Legal protection (best effort, honest)
- Terms, privacy policy, cookie policy, refund and auto-renewal terms, acceptable use, DMCA/IP complaint process, sub-processor list, DPA for business users, AI-use disclosure, limitation of liability and arbitration clause drafted per market from the real data flows; third-party licence audit (no unlicensed fonts, images, packages, models); trademark and name check for each product name and domain; no claims we cannot prove (no fake certifications, no uptime promises we cannot meet, no fake reviews or logos).
- Honest limit: AI drafting reduces risk but nobody can promise that nobody will ever sue. Every legal document is marked "AI-drafted, to be reviewed by a qualified lawyer in each market before paid launch", and the owner checklist includes that step.

## 5. Things the big companies do that we must also cover (the AI adds more when it finds them)
Accessibility and keyboard support, localization quality review by a native reader, SEO and structured data, store-listing quality (screenshots, text, ratings prompts done fairly), onboarding and empty states, in-app help and search, support inbox and ticket flow, status page and incident process, backups and disaster recovery drills, observability (logs, metrics, alerts, crash reports), performance budgets, release channels and staged rollouts, feature flags, A/B testing with consent, abuse and fraud protection, rate limits, a security.txt and responsible-disclosure page, bug bounty-style reporting inbox, cost and quota monitoring for AI providers, changelog and roadmap pages, referral and sharing flows, email deliverability (SPF, DKIM, DMARC), unsubscribe and notification preferences, data export, team and family plans, offline mode and sync conflict handling, update flow and version compatibility, deprecation policy, documentation for developers if an API exists.

## Definition of done for the plan
A plan is market-grade only when every product has: a dated competitor study with sources, a per-country rules table with tasks, a privacy-first insight design, drafted legal pack with the lawyer-review step, and the extra-coverage list marked done, skipped with reason, or scheduled.

> AHome exception (owner, 2026-11-09): AHome is private, so it does NOT get the commercial parts of this standard (no subscription, store launch, marketing, SEO, market law packs, public analytics, public legal pages). It still gets everything about quality: best-in-class design, features, animation, security, privacy, reliability, local AI, backups, self-repair. Competitor study for AHome is only feature and design inspiration from the best couple/home/organizer apps.
