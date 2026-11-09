# 24. Launch package: every project is ready to be switched on (Ahmed, 2026-11-09)

Every project plan (`.sir/MASTER_PLAN.md`) must contain a complete, detailed LAUNCH PACKAGE, so that Ahmed (second-year student, not an expert) only has to do a few tiny owner steps. Nothing is built "later": everything is built and tested now, with safe fallbacks, and switches on when the owner adds keys.

## 1. Fresh identity for every product (rebuilt from zero)
- New repository, new Firebase (or other backend) project, new domain name chosen and written down (real paid domain to be bought by the owner), new brand assets, new keys. Old things are legacy sources only; nothing is reused from old cloud projects.
- Every platform the product makes sense on: web, PWA, Windows, macOS, Linux, Android, iOS, iPadOS, Wear OS, watchOS, TV, car, widgets, browser extension where useful. One architecture, shared Profile and Settings, its own colours, logo and motion personality. For each platform the plan says: built or skipped with the reason, build command, test device or emulator, store listing needs.

## 2. Security and privacy, all layers
- Threat model, auth hardening (HttpOnly cookies, server-side roles, 2FA, rate limits, password checks), input validation, SSRF/XSS/CSRF/injection tests, secrets handling, dependency and licence audit, backups with a tested restore, logging without personal data, abuse protection, rules for the database, privacy pages that match what is really collected, account and data deletion. Written as concrete tasks with tests.

## 3. Fair subscription (not annoying, a real win-win)
- Free tier that is genuinely useful every day. Paid tier unlocks power features the user will want after using the product (sync, unlimited automation, speed, analytics, priority). Prices in EGP first (plus USD, EUR, SAR, AED), monthly and yearly, clear value copy, no dark patterns, one-tap cancellation, honest renewal text.
- Payment code is built and tested against provider TEST modes: Paymob and Fawry (Egypt), Stripe or LemonSqueezy for international, store billing where required. Until live keys exist the product shows "Subscriptions launching soon" with email capture; when keys are added the checkout activates with no code change. Webhooks verified by signature, idempotent, with a reconciliation job.

## 4. Real data only
- No fake data, fake users, fake reviews, fake counters, placeholder text or sample records in any user-visible path. Empty states are honest and useful. Seed data exists only inside tests and is labelled.

## 5. The AI solves its own problems
- Every project has a self-check and self-repair routine: health check command, error log digest, automatic retry and fallback providers, a runbook, and an instruction that the building AI must diagnose and fix any failure itself (read logs, search the web, try another approach, use another tool) before reporting; only sign-ins, 2FA, CAPTCHAs, payments and identity checks go to the owner.

## 6. Owner activation checklist (the only human part)
Each plan ends with a numbered checklist of tiny steps with exact clicks, in plain Arabic and English, for what only the owner can do: buy the domain (where, which name, price estimate), connect it (the exact DNS records are generated), upgrade the cloud plan, create the payment provider account and paste the keys into one `.env` file (exact variable names listed), add store developer accounts, and confirm legal details. After each step the plan says how to verify it worked and what switches on.

## Definition of ready
A product is "ready to launch" only when: all platforms in the plan build; security tasks pass; billing works in test mode and in fallback mode; the legal pages are generated from real data use; the activation checklist exists; a reviewer verified everything end to end on the same day.
