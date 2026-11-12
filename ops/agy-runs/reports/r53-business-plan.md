REPORT: r53-business-plan - SIR Business merged plan, competitor matrix, queueable tasks

Date: 2026-11-12
Task: Round r53b (HQ) - write ONE merged premium plan for SIR Business ("one site with business types; sign up, choose sector, guided setup, free trial, subscription; owners can run several businesses; the old Restaurant/Market/Library/Pharmacy modes become sector templates"), a 10-competitor matrix, and the first 10 agent-ready tasks. Plan only. Nothing is built in this round.

## What changed

1. `plans/sir-business.md` - rewritten as the ONE merged plan (416 lines, 22 sections). It carries:
   - The promise (owner vision 2026-11-12, PRODUCT_DIRECTION_2026-11-12.md section 3)
   - The flow: sign up -> sector picker -> guided setup wizard (linear stepper, steps disabled until the current one validates) -> 30-day trial (no card) -> subscription; one owner, several businesses
   - Names and IDs (folder, repo sirahmed8/sir-business kept private, stack)
   - A 30-sector catalogue (6 F&B, 8 health/beauty, 7 retail, 5 services, 2 hospitality/real-estate, 2 education) with per-sector modules and regulation risks
   - The common engine (org -> business -> branch -> membership tenancy, RBAC, auth, inventory FEFO, POS, loyalty, finance/Z-report, suppliers, reports, notifications, offline mode, hardware, kiosk, AI copilot)
   - Four sector templates with every legacy feature mapped (Restaurant 6.1, Market 6.2, Library 6.3, Pharmacy 6.4) with port/rebuild/drop/defer verdicts; dropped for good: killSwitch, antiPiracyShield, canned-AI theatre
   - Firestore data model + privacy engineering (per-tenant deny-by-default rules, AES-GCM for pharmacy health data, export/delete, retention)
   - Owner-only analytics page at /owner (company side, behind the `company_owner` claim)
   - Pricing proposal (Free forever, 30-day trial, Starter 299 EGP/$9, Business 599/$19, Pro 1199/$39, +50% per extra business, +60 EGP/$2 per extra seat, annual = 2 months free) - PROPOSED, unsourced until 5 pilot interviews; auto-detect EGP/USD
   - Platform matrix (web + PWA now; Android/iOS PWA; Windows app deferred to M5+; macOS/Linux honestly deferred)
   - Firebase (Spark: Auth, Firestore, Storage, FCM; me-central1 Doha default, fallback europe-west1) + Vercel now architecture; server ops (AI proxy, billing webhooks, ETA/ZATCA, /owner API) as Vercel route handlers until Blaze; POS offline via IndexedDB + Firestore offline persistence; conflict rule in ADR
   - Milestones M0-M6 with acceptance tests stated as commands, M0 recreates the Desktop kit
   - Risks and open questions with defaults (ETA/ZATCA spec-gated, pharmacy data encrypted + pharmacist review, drug DB licensing, DDI phrased "ask your pharmacist")
   - Only-the-owner steps, parity target (honest), verification definition of done, anchor decisions logged
   - Section 17 points at the tasks file; section 12 points at the competitor file

2. `ops/competitors/sir-business.md` - canonical competitor matrix (68 lines), superseding the unsourced 2026-11-09 `plans/competitors/sir-business.md`. Ten competitors, every number tagged to a page opened 2026-11-12 or "(unsourced, verify)": Odoo, Square, Toast, Foodics, Loyverse, Zoho Books, Lightspeed Retail X-Series, Shopify POS, Daftra (دفترة), Qoyod (قيود). Includes a sourced-facts section, a 10-point "we do better" advantage map, cited stealable ideas, and 6 open sourcing tasks (ETA spec read, Foodics/Daftra EGP rates, 10 public SME complaints, Shopify Payments in Egypt, me-central1 availability, ETA mandatory timeline). Claims are the vendors' own pages only; nothing was audited as a user. ETA/ZATCA claims are the vendors'; our own compliance work waits for the official specs and owner onboarding.

3. `ops/briefs/sir-business-tasks.md` - rewritten as 10 ready-to-queue briefs, each under 2 hours with exact files and a done-when check: (1) M0 Desktop kit recreate; (2) M0 dual-hosting import + curl 200 both hosts; (3) M1 Next.js + Firebase monorepo scaffold, `verify` green; (4) M1 money module integer piasters, 30 tests; (5) M1 Firestore rules v0 + emulator cross-tenant denial suite; (6) M1 `sectors.ts` 30-sector catalogue + unit test; (7) M1 auth + claims scaffold, five-state login; (8) M1 tenancy schema + emulator seed; (9) M1 offline-sync ADR refresh against POS reality; (10) M2 legacy parity report regeneration with per-file verification.

4. `ops/bus/sir-hq.md` - one bus line appended (this plan round).

## Commands run and real output

- `wc -l plans/sir-business.md ops/competitors/sir-business.md ops/briefs/sir-business-tasks.md` ->
  `416 plans/sir-business.md` / `68 ops/competitors/sir-business.md` / `54 ops/briefs/sir-business-tasks.md`
- `grep -n "^## " plans/sir-business.md` -> 22 sections, from `## 1. The promise` to `## 22. Anchor decisions` (full list pasted below)
- webfetch on 2026-11-12 (all pages opened the same day, no other source): odoo.com/pricing, squareup.com/us/en/point-of-sale/pricing, pos.toasttab.com/pricing, foodics.com, loyverse.com/pricing/, zoho.com/books/pricing.html, lightspeedhq.com/pricing/, shopify.com/pos/pricing, daftra.com, qoyod.com. Toast and Foodics publish no prices on the pages opened; all their prices are "(unsourced, verify)".
- `ls ops/ci-quota-exhausted.flag` -> exists; CI cannot be watched (2026-11-12, GitHub Actions minutes 100%). Local file checks only; pushed to main per worker rule 18.
- Section list (real output): 1 The promise; 2 The flow; 3 Names and IDs; 4 Sector catalogue; 5 The common engine; 6 Sector templates and the legacy feature map; 7 Data model and privacy; 8 Owner-only analytics page; 9 Pricing; 10 Platform matrix; 11 Architecture on Firebase plus Vercel now; 12 Competitor matrix; 13 Quality bar; 14 AI and support; 15 Security, legal and compliance; 16 Milestones M0-M6; 17 First 10 tasks; 18 Risks and open questions; 19 Only the owner can do; 20 Feature parity target; 21 Verification and definition of done; 22 Anchor decisions.

## What is unsure / open (honest)

- Nothing in M0-M6 is built. No code exists for this product in this round; `.sir/CHECKPOINT.md` in `D:\Projects\SIR Business` still says M0 not started and points at an outdated T-003; the r53 M0/M1 briefs supersede it and the checkpoint must be refreshed when the first M0 task runs.
- Pricing is PROPOSED and unsourced. It must not appear in public copy or store listings until 5 pilot interviews re-price it; all figures tagged as such in the plan.
- ETA (Egypt e-receipt/e-invoice) and ZATCA (Saudi) compliance is spec-gated: no public "compliant" claim until an Egyptian accountant reads the official specs and a lawyer drafts the wording. Daftra and Qoyod claims are theirs, not ours.
- Vercel Hobby vs Pro terms for commercial use, and Firebase Blaze (Cloud Functions) needing an owner card: both are owner decisions, defaulted in the plan (Firebase App Hosting for production, Vercel for preview), not resolved.
- Dual hosting (Firebase + Vercel) is not yet wired: repo `sirahmed8/sir-business` exists (private) but no Vercel project is imported and no Firebase project `sir-business` is confirmed created; both are M0 tasks, neither is done.
- The Desktop kit is NOT recreated yet; `D:\Projects\SIR Business\folder.ico` and the Desktop shortcuts are an M0 acceptance item, unverified.
- Legacy parity: the feature maps in plan section 6 are based on the 2026-10-29 scout inventories (`ops/inventory/`), not on a fresh per-file audit; task 10 regenerates `.sir/reports/parity.md` with per-file verification before any "ported" claim is made.
- Pharmacy: controlled-drug log, encrypted patient records and DDI warnings are designed but unbuilt and untested; no real pharmacy pilot before pharmacist review.
- Localization copy deck (Egyptian Arabic MSA + dialect) is named, not written.
- Windows app deferred to M5+ and only if a Windows kiosk customer appears; macOS/Linux/iOS shipping remains deferred until the Windows/PWA path proves out; the plan says so plainly.
- CI is quota-blocked (flag file present), so no GitHub Actions run was or could be watched; verification here is file-level only (line counts, section list, links present on disk), not a green build.
- The old `plans/competitors/sir-business.md` remains on disk (never deleted) and is declared superseded by `ops/competitors/sir-business.md` in that file's header.

## Verification status vs definition of done

This is a plan round. Plan, matrix and tasks are written and pushed; the report above is the evidence. No end-to-end verification is possible or claimed. Done for this round = files written, pushed to main, bus line appended, agy-done signal sent. M0-M6 remain open work.

CI note: `ops/ci-quota-exhausted.flag` is present, so rule "CI must be seen green" is replaced by local checks per worker rule 18; the flag content was read (2026-11-12, minutes 100%, expected reset ~2026-12-01).
