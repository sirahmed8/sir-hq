# PLAN: SIR Jobs (Wave 2, private income tool)
Audited 2026-11-10. Replaces the old `D:\Projects\Jobs` data folder (data imported, folder kept for now). Private tool for one owner: not sold, not listed, `noindex`. Commercial items are marked "n/a" with the reason.

## 1. Purpose (plain words)
It finds remote and local jobs and freelance gigs that fit Ahmed, ranks them, writes a draft application for each good one, and tracks what really happened. Nothing is sent without his approval, and a row never says "Applied" unless there is proof. Goal behind it: the first income of 1,200 EGP.

## 2. Names and IDs
| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Jobs` |
| GitHub (private) | `sirahmed8/sir-jobs` |
| Runtime | Node (ESM, no framework), `src/server.mjs` on `127.0.0.1:3456`, scheduled tasks `SIR_Jobs_Server` and `SIR-Jobs-Weekly-Digest` |
| Platforms | Windows local dashboard plus phone browser over Tailscale: built, unverified. Web hosting, Android, iOS, macOS, TV, watch: skipped (private tool; phone uses the tailnet page) |
| Money | none charged. Subscription, EGP checkout, legal packs: n/a. Default: if ever offered to others, rebuild on the shared kit billing and legal pack, never inside this folder |

## 3. Current state
Claimed in `.sir/CHECKPOINT.md` (2026-11-10): M0 to M6 and 24 audit cycles done, 18 tasks T-001 to T-018 green. PORTFOLIO.md (2026-11-08): 21 of 21 tasks, 44 commits, 86 tests.
Verified by this audit on 2026-11-10: `npm test` (chain of 24 suites joined by `&&`) ran to its final suite with 4 of 4 passing in that suite and no failure printed. Per-suite counts were not captured; the "86 tests" number is unverified. `npm run doctor` and `verify.ps1` were not re-run.
Built, unverified: scraper to shortlist to draft to approval pipeline (`src/pipeline.mjs`, `src/drafter.mjs`), fit scoring with evals (`src/fit-evaluator.mjs`, `scripts/ai_eval.mjs`), undo (`src/undo.mjs`), Telegram send ledger that stops duplicate sends (`src/telegram-ledger.mjs`), money-goal engine (`src/money-engine.mjs`), cached exchange rates (`src/fx.mjs`), offline CV PDF, tailnet auth check (`src/auth.mjs`), kanban dashboard with six views, daemon scripts.
Not started or not proven: real outcomes (interviews, replies, income) recorded with evidence; the 5 "staged" opportunities have no proof of any reply; scraper terms-of-use review per source; Arabic job boards; local-model draft path for CV text (see risk 2); freelance platform profile checklist for the owner.

## 4. Security and conduct rules
1. Loopback bind plus `Tailscale-User-Login` check; no public ingress. Test: `test/test-security.mjs` (exists, re-run and keep).
2. A row may be "Applied" only with a proof file (screenshot, email id or confirmation URL) in `data/store/proof/`. Test: a pipeline test rejects "Applied" without proof.
3. No auto-submit to any site whose terms forbid automation. No CAPTCHA bypass, no fake claims in a CV, no engagement bots, no impersonation in live chats. Every submission is a human click.
4. Personal documents (CV, phone, address) never go to an outside AI provider. Drafts that include them use the local model; outside providers may only see the public job text. Test: a redaction unit test on the prompt builder.
5. Secrets in Credential Manager or untracked `.env`; gitleaks in CI.
6. Telegram sends go through the ledger (one brief per day).

## 5. Shared pieces
- Telegram delivery: use `scripts/deliver/send-telegram.mjs` (the shared sender), not a second bot. The ledger stays here because it is job-specific.
- AI calls: for anything not personal, go through `_SIR/scripts/ai/ask.ps1` (fallback chain, usage ledger). When the shared kit's ai-proxy exists, switch to it.
- Design tokens and settings/profile: reuse the Laptop Manager and Study look until Platform extracts the kit (last wave).
- Gig income feeds SIR Portfolio only as real, proven results (case studies), never as numbers from this tracker unless proof exists.

## 6. Screens and entities
Screens: Pipeline board, Job detail, Drafts, Outcomes, Cash hub (money goal), Security and diagnostics, Settings and Profile. Entities: Job, Application, Contact, Draft, Outcome, Proof, MoneyGoal.
Five states on each, Arabic RTL and English, light/dark/system/contrast, 320 px to 4K, WCAG 2.2 AA, own logo.

## 7. AI and assistant
Fit score with a written rubric; drafts in Arabic or English matching the posting; "why this job fits / does not fit" in plain words. Fallback: local model, then an outside provider on public text only, then a rule-based score. Eval set of past real outcomes in `scripts/ai_eval.mjs`; a new model is accepted only if it beats the stored score. Kill switch: `JOBS_AI=off` env. Support assistant: n/a (single owner); the doctor page explains failures.

## 8. Operations
Weekly digest (Monday brief) and one daily money brief, both via Telegram in simple Arabic: new fits, drafts waiting for approval, proofs missing, next deadline. Health line in `.sir/health.txt`. Backups: `scripts/snapshot.py all` weekly to `D:\Projects\Backups\SIR-Jobs-data` with a monthly restore check. Dependency update weekly (few dependencies).

## 9. Milestones with exit checks
| M | Goal | Exit check |
|---|---|---|
| M0 | Foundations | `npm run verify` green; `docs/THREAT_MODEL.md`; ADR-001 auth exist |
| M1 | Clean tracker | a script prints counts: rows with proof vs without; zero "Applied" without proof |
| M2 | Pipeline | `npm run pipeline:offline` produces a shortlist and drafts from fixtures |
| M3 | Security | `node test/test-security.mjs` passes; redaction test passes |
| M4 | AI | `npm run evals` prints a score and saves it to `.sir/evidence/` |
| M5 | Quality | screenshots at 320, 390, 768, 1440 in light/dark/RTL; a11y test passes |
| M6 | Real outcomes | at least one real application submitted by the owner with proof; first reply logged |

## 10. Next 10 tasks (each under 2 hours)
1. Run `npm test` with output saved per suite and record counts. Files: `scripts/verify.ps1`, `.sir/evidence/tests-2026-11-10.md`. Check: file lists suite names and pass counts.
2. Proof rule: reject "Applied" without a proof file. Files: `src/pipeline-db.mjs`, `test/test-pipeline.mjs`. Check: new test passes; old rows without proof show "unverified".
3. Report command `npm run proof-report` printing rows with and without proof. Files: `scripts/proof-report.mjs`. Check: output matches the data.
4. Prompt redaction for outside providers (strip name, phone, address, email). Files: `src/drafter.mjs`, `test/test-redaction.mjs`. Check: test feeds a CV and finds none of the fields in the prompt.
5. Source terms review: for each scraper source in `scripts/digest/`, write the terms URL and "allowed / manual only" in `docs/SOURCES.md`. Check: every source has a row; disallowed ones are switched off in config.
6. Add two Arabic-region sources (Wuzzuf and a remote board) as official feeds or manual-import only. Files: `scripts/digest/sources/`. Check: offline fixture test passes. (Whether their terms allow it: "(unsourced, verify)".)
7. Draft quality eval: 10 past real postings with accepted/rejected drafts, score in `.sir/evidence/`. Check: score printed by `npm run evals`.
8. Owner checklist file `docs/OWNER_STEPS.md`: freelance profile (Upwork, Freelancer, Mostaql), payout method, one tap each, plain Arabic. Check: file exists with exact clicks; nothing requires the agent to sign in.
9. Gitleaks and CI run proof: push and record the Actions URL. Check: green run URL in checkpoint.
10. Weekly report builder dry run to Telegram with the ledger test for duplicates. Check: second send same day is blocked (test), real send returns ok.

## 11. Risks and open questions (defaults)
- Job-board terms may forbid scraping: default is official feeds and manual import; switch off the source otherwise.
- "Staged" opportunities can look like progress: default is they count only after a real reply.
- Python 3 and Node both used (`scripts/snapshot.py`): default is keep, they are small.
- Market claims (pay rates, platform fees) are not in this plan; any added later need a source or "(unsourced, verify)".

## 12. Only the owner can do
Sign in to job and freelance platforms, solve CAPTCHAs, click Submit on applications, set payout details, accept contracts, any identity check.

## 13. Market-grade note
`plans/competitors/sir-jobs.md` holds the competitor study (check it for dates and links; unsourced lines stay tagged). Country rules (Egypt PDPL 151/2020 for stored contact data) apply only if third-party contacts are stored: default is store names and emails of recruiters minimally, delete after 12 months.
