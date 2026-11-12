# SIR Company blueprint: one human, an AI team, many products, launched legally
Owner and CEO: Ahmed Alaa. Manager (acts almost as CEO): Claude in the Claude desktop app until about 2026-11-23, then Gemini in Antigravity (AgentsRoom was retired on 2026-11-08). This file is the improved version of the idea. It is not legal advice: every legal step ends with "a licensed lawyer or accountant confirms it before it is relied on". Agents prepare; a human professional signs.

## 1. The model
- One human sets direction and signs what only a human can sign (identity, payments, contracts, filings). Everything else is run by the AI company: manager, reviewer, QA, specialists (roles in `_SIR/standard/roles`), workers on Antigravity, OpenCode and Kilo, and local models for private work.
- Products: the shared kit (shared auth, billing fallback, AI gateway, design system), SIR AI, Content Creation Studio, Business, Hagoozat, Education Hub, Study, Jobs, Laptop Manager, Negm Furniture, Portfolio, ModPack, Life, Controller. AHome stays private forever: never listed, never exposed, no subscriptions.
- Waves decide the order (`WAVE_STUDY.md`). The CEO can reorder at any time; no project is "finished" until he says so.

## 2. Company structure (human decisions, agents prepare the paperwork)
1. Entity: decide with an Egyptian accountant or lawyer between an individual, a sole proprietorship or a limited liability company (separates personal assets from product risk). Agents prepare: business description, activity codes, ownership note, cost and tax summary, document checklist. The human files, signs and pays.
2. IP ownership: the company (or Ahmed) owns all code, brand and assets. Keep an IP register (section 4). Contributors, freelancers and AI outputs: written assignment or work-for-hire terms; AI-generated assets are checked against each tool's terms.
3. Brand: choose the umbrella name; check trademark availability (Egyptian trademark office, WIPO and EUIPO databases, domain, app stores, social handles) before launch; file the mark for each flagship product through a lawyer; keep logos with source files and the licence of every font and icon.
4. Money: a business bank account, Paymob and Fawry merchant accounts, invoices and receipts, VAT or tax registration where required, a monthly bookkeeping export prepared by the CFO role.
5. Insurance: ask about professional liability and cyber cover once there is revenue.

## 3. "Anti-sued": risk management every product passes before launch
No product can be made lawsuit-proof. The goal is to remove avoidable claims and limit the rest.
- Legal pages generated from what the product really does: privacy policy (data map: what, why, where, how long, who processes it, sub-processors), terms (limited liability, "as is", governing law and forum chosen with the lawyer, acceptable use, account termination), cookie policy with real consent (reject as prominent as accept, no trackers before consent), refund and cancellation (one-click cancel), AI disclosure and an AI-training prohibition clause, takedown and abuse contact, accessibility statement, security contact (`security.txt`).
- Privacy law checklist per product: Egypt Personal Data Protection Law (Law 151 of 2020) and its regulation (registration or licensing duties, data subject rights, breach notice), GDPR when EU users exist, children (age gate, no data from minors without consent), store privacy labels true to the code. Data minimisation, encryption, deletion and export on request, retention schedule, breach runbook.
- Licences: dependency licence scan (SPDX) on every release, no GPL or AGPL in proprietary code, attribution file, font, image, model and music licences recorded; no scraped or ripped content; no third-party logos without written permission; open-source upstream code in `legacy/` is read for ideas only.
- Truth in claims: no fake reviews, counts, testimonials or "certified" claims; no SOC 2 or uptime promises without proof; ads and copy checked against consumer-protection rules.
- Payments: no card data stored (hosted checkout only); prices shown with tax; auto-renew disclosure before checkout.
- Security as defence: threat model, secret scanning, dependency audit, rate limits, backups and an incident log; a documented response beats a surprise.
- Third parties: each API or provider's terms read once and recorded (rate limits, allowed use, data rules). Spotify, Google, Telegram, Meta and X rules respected; official APIs first; never script X's website.
- Client contracts (Negm and others): written scope, ownership, support period, liability cap, confidentiality; agents draft, a lawyer reviews the template once.
- Evidence per product: `.sir/legal/` holds the generated pages, data map, licence report, consent screenshots and the last review date. A release is blocked if it is missing or older than 90 days.

## 4. Registry (one source of truth, kept by the Compliance agent)
`D:\Projects\_SIR\ops\COMPANY_REGISTRY.md` lists, per product and for the company (facts only, no secrets, nothing private about people): legal entity, trademark status and numbers, domains and DNS owner, app-store accounts and listings, cloud projects (Firebase, Cloudflare, Vercel) and billing owner, OAuth clients and consent-screen status, where each API key lives (vault name, never the value), licence report date, privacy-law registrations, legal page URLs and review date, insurance, renewal and expiry dates (domains, certificates, store fees), and the owner-only actions still open. Renewal dates feed reminders to Ahmed.

## 5. AI company org chart (all under the manager)
Manager and deputy CEO; Reviewer; QA; Architect; Security auditor (weekly); Compliance and legal-prep officer (legal pages, licences, privacy, registry); CFO and bookkeeper (costs, quotas, revenue, invoices, tax export); Release manager; SRE and ops (health, backups, disk, uptime); Support and community (inbox, FAQ, bug triage, suggestions); Growth and content (ByteVibeHQ posting through official APIs, SEO, store listings); Localiser (Arabic and English); Design systems lead (the global system); Data and AI engineer (eval sets, model routing, cost caps); Private worker (local models only, for AHome). Hire or retire roles as needed; every role has a brief template, a model level and a read-first list.

## 6. Controls so one human can trust the machine
- Approval gates (owner actions only): signing, payments, public announcements that speak as him, filings, account creation, anything irreversible outside the repo. Everything else the team does and logs.
- Spend caps: zero paid services by default; a quota and cost ledger (`usage-ledger.jsonl`); paid overages never turned on.
- Audit trail: every deploy, rule change, key rotation and data export is logged with time, actor (agent id) and evidence.
- Separation: a different agent reviews each change; production credentials only in the vault; private data never leaves its zone (AHome stays local).
- Recovery: backups, restore drills, rollback for every deploy, and a one-page "if the human is away" runbook (who rotates keys, how to take a product offline) kept in the registry.
- Continuity: the same rules for every AI app (`START_ANY_AI.md`), so the company survives any single tool, account or quota limit.

## 7. Launch path per product (gates)
Discovery and benchmark, plan and legal data map, build on the global design system, security review, licence and privacy review, legal pages and consent, accessibility and performance gate, store and listing assets, beta with consenting real users, launch, support and monitoring, weekly improvement loop. A product counts as launched only when its registry row is complete.

## 8. First week after a reset (manager)
1. Create `COMPANY_REGISTRY.md` from section 4 and fill what the repos already show (domains, Firebase, Cloudflare and Vercel projects, OAuth clients, licences).
2. Add the Compliance, CFO, SRE and Support roles to `_SIR/standard/roles` if missing.
3. Add the legal gate (section 3 evidence) to each project's QUALITY.md and to the release checks.
4. Prepare the entity and trademark briefing for Ahmed's lawyer and accountant: one page per decision with options and costs, no action taken.
5. Re-plan each wave with the launch path and refresh the Control Room.
