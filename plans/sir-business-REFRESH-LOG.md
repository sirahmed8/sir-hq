# SIR Business plan refresh log

## 2026-11-12 - r61 planning-only refresh

Round: `r61-plan-sir-business` (HQ planning only). Scope kept inside `D:/Projects/_SIR`: `plans/`, `ops/competitors/`, `ops/briefs/`, `ops/research/`, plus the required bus/report files. No product code, no Firebase project, no repository and no store work was created. `D:/Projects/SIR Business` was read only.

### What was rescanned

- `D:/Projects/AGENTS.md`, `ops/WORKER_PREAMBLE.md`, `standard/23-premium-code-bar.md`, `.sir/CHECKPOINT.md`, `ops/briefs/r61-plan-sir-business.prompt.txt`, `plans/PRODUCT_DIRECTION_2026-11-12.md`, `plans/sir-business.md`, `plans/sir-business-DEEP.md`, `ops/briefs/sir-business-tasks.md`, `ops/competitors/sir-business.md`, `ops/TICKTICK_MAP.md`, `ops/SKILLS_INDEX.md`, `ops/bus/team.md` and the SIR Business `.sir` deep scan in read-only mode.
- Sector depth outputs from r56: `plans/business-sectors/_INDEX.md`, `_ENGINE.md`, all `_data/*.json`, generated `plans/business-sectors/<slug>.md` and `ops/briefs/business-<slug>-tasks.md`.

### Research added on 2026-11-12

- Egypt-local POS competitors: Circle (free Arabic-first inventory/POS app), inyad (Egyptian POS/invoicing/payments suite with published EGP plans) and Geidea POS (payments-led Egyptian till, no public price). Added to `ops/competitors/sir-business.md` section 6 and to `plans/sir-business.md` section 12.
- Corrections to stale competitor facts: Foodics Egypt now publishes EGP bundles; Daftra prices are visible through dated third-party comparisons and must still be verified on daftra.com before quoting.
- Regulations and rails: ETA e-invoice is B2B under Ministerial Decision 323/2022; ETA e-receipt is B2C and requires e-invoice enrollment plus an ETA mandatory-inclusion decision; ETA published an e-receipt guide and SDK portal; Decision 361/2025 starts a phase-nine sub-phase for listed taxpayers from 2025-11-15. Paymob and Fawry fee snippets were read from search results because direct fetches failed or returned 400; both must be verified before public copy. Firestore Spark free quota and `me-central1`/`me-central2` locations were verified on Google/Firebase docs.

### Plan changes

- `plans/sir-business.md` section 4 now points to the authoritative 41-pack catalogue (`plans/business-sectors/_INDEX.md`, `_ENGINE.md`, per-sector plans and task briefs) and explains how the old grouped tables reconcile with the final list.
- `plans/sir-business.md` section 9 pricing rationale updated with the r61 competitor reads and the inyad/Foodics/Daftra price anchors.
- `plans/sir-business.md` section 11.1 added the API surface table for server/client boundaries, money idempotency, billing webhooks, AI metering, ETA/ZATCA honesty, privacy export/delete and owner analytics.
- `plans/sir-business.md` section 12 competitor matrix expanded from 10 to 13 competitors with dated sources.
- `plans/sir-business.md` section 17 now points to the expanded 48-task queue.
- `plans/sir-business.md` section 23 added launch and marketing gates: sector landing pages, bilingual SEO, pilot-first channels, honest compliance wording, free-tier promise and owner metrics.
- `plans/sir-business.md` section 24 records this refresh.
- `ops/briefs/sir-business-tasks.md` expanded from 10 tasks to 48 smaller tasks. Tasks 1-10 remain ready for M0/M1/M2; tasks 11-48 are gated follow-ons. Every task has Brief, Files, Done when, Check and applicable skills from `ops/SKILLS_INDEX.md`.

### Decisions and open questions

- Sector catalogue: keep the r56 decision of 41 packs; do not reopen it in this round. The grouped tables in `plans/sir-business.md` are a navigation view, not the source of truth.
- Free tier: keep it genuinely useful (offline POS, one business, two seats, receipts, basic reports, export) because Circle and inyad prove a 0 EGP entry is table stakes in Egypt.
- ETA/ZATCA: keep spec-gated and honest. Public copy may say "ETA-ready workflow" only after accountant review and pilot validation; never "ETA compliant" for an unenrolled business.
- Pharmacy/clinic/education packs: keep encryption, no AI on patient/child rows, append-only controlled log and pharmacist/owner review gates.
- Payments: support Paymob and Fawry first, add InstaPay QR and wallet deep links, never depend on one acquirer.
- Pricing: EGP 299-599/mo remains the proposed Egyptian SME band, but final prices still need the pilot interviews listed in `plans/business-sectors/_INDEX.md` section 5.
- Open owner actions remain in `plans/sir-business.md` section 19 and `ops/OWNER_ACTIONS.md` where applicable: Firebase project creation if missing, billing card for Blaze, domain purchase, Paymob/Fawry merchant accounts, accountant/pharmacist/lawyer reviews, Telegram bot handover and pilot consent letters.

### Verification for this round

Planning-only verification, not product verification:

- `python scripts/build_business_sectors.py --check` was run during the repair pass and reported `OK: 41 sectors, 82 generated files are up to date` before this r61 edit set.
- This r61 edit set touches only Markdown planning/brief/competitor files; the sector generator inputs were not changed after that check.
- Local checks for em-dashes, emoji, task count, links and dashboard generation are recorded in the r61 report.
