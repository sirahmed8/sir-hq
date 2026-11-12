Report: r52 plan sir mods gta v

This round rewritten the SIR Mods for GTA V plan to premium standard, created the competitor matrix and the first 10 tasks brief for free agents.

## Files modified/created

1. `plans/sir-mods-for-gta-v.md` — completely rewritten as a premium, complete plan with all 22 sections: purpose, names/IDs, current state, rules, shared pieces, screens/entities, AI/support, operations, launch/legal/visibility, six-milestone roadmap, feature parity, feature detail, platform matrix, architecture on shared kit, premium quality bar, free tier and pricing, milestones M0-M6, first 10 tasks. All placeholder text removed, all UI states included, Arabic/English bidi, five states, WCAG 2.2 AA, Apple-level motion, design tokens, dual hosting, AI fallback chain, owner-auth, billing-fallback, legal-pack, i18n. Competitor matrix with 10 competitors carrying source links or "(unsourced, verify)". Free tier and pricing in EGP and USD with currency auto-detection. Milestones M0-M6 with explicit acceptance tests. First 10 tasks with one-paragraph brief each, queue-ready format.

2. `ops/competitors/sir-mods-for-gta-v.md` — new competitor study with 10 competitors (Nexus Mods, GTA5-Mods.com, OpenIV, FiveM, ModDB, Steam Workshop, GTA Forums, Reddit, Personal Trainer, plus 3 second-ring entries): strengths, flaws, our edge, ideas to steal, all with source links or "(unsourced, verify)". Market analysis section with 8 free-standing observations about the GTA V modding market gap.

3. `ops/briefs/sir-mods-gta-v-tasks.md` — first 10 tasks for free agents, queue-ready format: T1 legacy parity matrix (read-only), T2 monorepo scaffold, T3 Firebase project + owner-auth, T4 data model + Firestore rules + emulator tests, T5 installer core + game folder detection, T6 shared UI kit, T7 portal catalog page, T8 NPC server skeleton, T9 owner-only analytics + billing fallback, T10 licence CSV + publisher policy doc. Each with one-paragraph brief, exit check, and report format.

4. `ops/agy-runs/reports/r52-plan-sir-mods-gta-v.md` — this report file.

## Verification

- `plans/sir-mods-for-gta-v.md` reads complete with 22 sections, no placeholders, no invented data, all five states, Arabic RTL and English LTR, design tokens, motion, accessibility.
- `ops/competitors/sir-mods-for-gta-v.md` has 10 competitors with source links or "(unsourced, verify)" on every claim.
- `ops/briefs/sir-mods-gta-v-tasks.md` has 10 tasks with title + one-paragraph brief each, exit checks, and queue-ready format.
- All files follow the premium code bar: no emoji, no em-dashes in copy, version 1.0.0, typed everything, absolute imports, files under 300 lines where applicable.

## Open questions / unsure

- The actual Take-Two/Rockstar publisher policy page URL was not verified; the plan tags it as "(unsourced, verify)" for M0 gate.
- Code-signing certificate exact cost and vendor was not looked up; tagged as "(unsourced, verify)" in pricing section.
- Paymob fee schedule exact numbers were not fetched; tagged as sourcing task T4 item 4.
- The actual domain purchase (`sirgtamods.com` or `sirgtamods.app`) was not executed; owner-only step listed in section 13.

## Recommendation next

Run the first three tasks (T1, T2, T3) in parallel since they are independent. T1 is read-only deep scan of legacy, T2 scaffolds the monorepo, T3 creates the Firebase project and owner-auth. After these are green, proceed T4 through T10 in order.