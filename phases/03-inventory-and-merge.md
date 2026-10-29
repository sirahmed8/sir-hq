# Phase 3 — Portfolio inventory and strategy (read-only fan-out)

> **Read first:** `START_HERE.md`, then `core/06-portfolio.md` and the benchmark in `standard/21-product-essentials.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with `phases/04-platform.md`.

**3.1 Inventory.** Fan out scouts, one per project and 4–6 in parallel, across every project in `D:\Projects` plus these Desktop folders: Hagoozat Elite, Odysseus, Antigravity Agent Suite, sirahmed8, SIR ModPack, SIR Mods for GTA V, SIR Restaurant, SIR Market, SIR Content Creation Studio, SIR AI, SIR Controller, SIR Optimizer, SIR Library, SIR Pharmacy, Laptop Manager, Negm Furniture, Obour Academic Hub, 11Players, EGFootball5. Also AHome and the folders Ahmed moved into `D:\Projects`: Learning, Obour Institute Second Year 1st term, AI_Models_Hub, Jobs. Each scout writes `_SIR/ops/inventory/<project>.md` covering:

- What it is and who it's for. Current state: does it build, run, deploy? Live URL?
- Stack and versions; repo health (remote, branches, last commit, uncommitted work); structure; which platforms exist; what the Desktop folder holds (installer, start-server launcher, shortcuts, or real code); data layer; auth; AI usage; legal pages; icons; tests and CI; docs.
- A 0–5 score, with evidence, for: architecture, code quality, security, UX/design, performance, completeness, store readiness.
- Red flags: secrets, mock data in production paths, broken builds, license problems, privacy risks.
- An upgrade-size estimate (S/M/L/XL) and the 5 highest-value fixes.
- Whether it covers business operations (videos, social media, jobs, company). One or more existing projects were built for that; find them.

**3.2 TickTick (read first, change later).** Read all projects, lists, tasks and notes. Back them up to `_SIR/ops/ticktick-backup-<date>.json` before any change. Map every item to the portfolio: existing project, new product, merge, or concept.

**3.3 Strategy.**

- Validate the consolidation proposal in A4 against what you found. Improve it where the evidence says so, and give your reasons.
- Assign each project a tier (Flagship / Core / Maintenance / Concept) and a wave.
- Priority score = revenue potential ×3 + closeness to shippable ×2 + strategic value to the platform ×2 + Ahmed's personal priority ×2 − effort. Show the scoring.
- Name the golden-path product for Phase 4.

**3.4 Decide and publish.** Write the Portfolio Report (summary table, consolidation, waves, risks, owner actions) to `_SIR/ops/PORTFOLIO.md` and the Command Center. Make the calls yourself from the scoring and start Phase 4 immediately. Don't wait for Ahmed; he can override anything through the Ideas Inbox.

**3.5 Consolidation: fewer, stronger projects.** Goal: the smallest set of products that covers everything, so effort goes into depth instead of maintenance.

- **Merge** when projects share the same users, the same core job, or the same data model. **Keep separate** when audiences, brands or owners differ (a client's own brand stays separate), or when merging would make a bloated app that does unrelated things.
- **Already merged by Ahmed:** `11Players` + `EGFootball5` → `D:\Projects\Merged sites`.
  - Verify the merge is complete with a feature-parity checklist against both originals, then move the originals to `D:\Projects\old projects\`.
  - "Merged sites" is a working name: give the product a proper name and identity, or keep one of the original names if it's the stronger brand.
- **Candidates to evaluate** (decide by evidence, one ADR each):
  - Hagoozat Elite joining the football platform (bookings + players + matches + Pitch IQ)
  - SIR ModPack + SIR Mods for GTA V → one mods hub
  - The SIR Business verticals (Restaurant, Market, Pharmacy, Library) → one SIR Business product with vertical modes, or separate brands on one shared core (Negm Furniture stays separate if it's a client's brand)
  - SIR AI, SIR Controller, SIR Optimizer, and their overlap with Laptop Manager
  - SIR Media inside SIR Content Creation Studio
  - Each new TickTick product line against the existing projects: a new idea joins an existing product as a module unless it clearly deserves its own product
- **Merge procedure** (`MERGE.md` template in B3):
  1. Name and identity: check domain availability and store-name and trademark conflicts.
  2. The surviving project, or a new project folder with the SIR file set.
  3. A feature-parity checklist for every source project.
  4. Build on the SIR Platform; the whole standard applies.
  5. Data migration: export/import scripts, a dry run, verified record counts.
  6. Redirects: old URLs return 301 to the new ones; deep links keep working.
  7. New Firebase, Vercel, GitHub and EAS setups (rule 17).
  8. Published apps can't be merged (app IDs are permanent): ship a final update of the old app that points users to the new one.
  9. Archive the old GitHub repos (read-only, never deleted) with a README pointing to the new repo.
  10. Move the old folders to `D:\Projects\old projects\<name>\`, each with a pointer README.
  11. Update everything that shows the portfolio: TickTick, the Command Center, PORTFOLIO, the sirahmed8 portfolio and pinned repos, LinkedIn projects (drafts for Ahmed where posting needs him), ByteVibeHQ bios and links, domains, store listings.
- **Stay adaptive:** re-run this analysis every month, and whenever the Ideas Inbox brings a new product idea. Target: fewer projects, each one stronger.

**3.6 Benchmark against the best.** Ahmed wants every product to have what the big apps and sites have, and more. For each product, before its wave starts, its PM runs the benchmark in module 21: the 3–5 leading apps and sites in the category (global and Arabic-market, found through store charts and search, not memory), what they have that we don't, what their users complain about, and which gaps to close first. HQ uses the summaries to adjust the strategy and the waves. Repeat before every major release.
