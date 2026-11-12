# PLAN: SIR Jobs (Wave 2, PERSONAL class, private income engine)

Rebuilt 2026-11-12 (r52-plan-sir-jobs). Replaces the 2026-11-10 audit content; keeps what is still true. PERSONAL product: only Ahmed, never sold, never listed, `noindex`, no public hosting. Commercial sections are marked n/a with the reason; an outline for the hypothetical case is included only so a future GLOBAL spin-off has a starting point, not because it will happen.

## 1. Who it is for and the one-sentence promise

Ahmed (Vibe Coder, second-year CS, Cairo) and nobody else. **Promise: "Open your laptop and every honest, well-fitting remote or freelance opportunity for a Vibe Coder is already found, scored, drafted, applied-to (cap 10 a day) and logged with proof, so your only job is the final tap and the interview."** Sell the end state: income from real work, measured in real numbers, with zero invented claims and zero wasted hours on bad-fit applications. Goal: real, measured income (see `.sir/INCOME_MODEL.md`, 2026-11-11); the old fixed 1,200 EGP figure is cancelled (owner, 2026-11-11).

## 2. Names and IDs

| Item | Value |
|---|---|
| Folder | `D:\Projects\SIR Jobs` |
| GitHub (private) | `sirahmed8/sir-jobs` |
| Runtime | Node ESM, no framework, `src/server.mjs` on `127.0.0.1:3456`; scheduled tasks `SIR_Jobs_Server`, `SIR-Jobs-Weekly-Digest`; SQLite local store |
| Platforms | Windows local dashboard (built, locally verified 2026-11-12) plus phone browser over Tailscale; everything else: see matrix (section 4) |
| Money | None charged; PERSONAL class. Subscription, EGP checkout, legal paid packs: n/a (never sold). If ever offered to others: rebuild on shared-kit billing and legal pack, never inside this folder |
| Domain | None (loopback + tailnet only) |
| Analytics page | Owner-only `/admin` (loopback); no public analytics |

## 3. Current state (honest, dated)

- 2026-11-12 (r46-jobs): competitor matrix + 3 feature gaps implemented and committed; `npm test` all suites pass; `npm run lint` 0 problems; `npm run typecheck` 0 errors; `npm run doctor` HEALTHY; r46 audit 28/28 checks at 320/390/768/1280 EN+AR light+dark. CI quota flag file exists (`ops/ci-quota-exhausted.flag`) but runs today execute and pass (e.g. test run 43254213557, 5 steps, success); local verification is the standing proof while the flag exists.
- Built and locally verified: scraper-to-shortlist-to-draft-to-apply pipeline, fit scoring with evals, undo, Telegram ledger, FX cache, offline CV PDF, tailnet auth, kanban dashboard with six views, auto-apply engine (cap 10/day, dedupe, 15 skip rules, truth audit, Gmail/CDP/owner-queue channels), proof ledger, contacts log.
- Not proven: real interviews, real replies, real income. Zero applications have been verified as submitted with proof (r29-jobs-verify-applies removed a fake fixture; `applications_sent: 0`). Staged opportunities count only after a real reply. Nothing on this page is "live" in the commercial sense.
- Open: scraper terms review per source; Arabic board sources not yet added; redaction test enforced for CV text to outside providers; income model refresh quarterly.

## 4. Platform matrix (what v1 includes)

| Platform | v1 | Notes |
|---|---|---|
| Web (local dashboard) | YES | The product. Browser over loopback or Tailscale; Arabic RTL, English, light/dark/system/contrast |
| Windows app | LATER | Only if the dashboard moves to a tray app; follow `plans/WINDOWS_APP_STANDARD.md` then |
| macOS | n/a | Owner has no Mac |
| Linux | n/a | Not used by owner |
| Android | LATER | Phone uses the tailnet page today; native app only if needed |
| iOS | LATER | Same as Android |
| Wear OS / watchOS | n/a | No use case for a job pipeline on a watch |
| TV | n/a | No use case |
| Car | n/a | No use case |

Why not every platform: PERSONAL class, one owner, one laptop plus a phone. Forcing all-platform parity here would burn the plan for zero user value. The shared kit's all-platform rule applies to GLOBAL products; Jobs adopts tokens, motion, i18n, help-center, security-baseline, operations-standard only (see `plans/SHARED_PLATFORM_KIT.md`, "PERSONAL products adopt").

## 5. Category and competitors

Category: AI career autopilot (job discovery, ATS optimization, auto-apply, tracking). Full matrix with 10 competitors, pricing with sources and dates, complaints, advantage map and ideas to steal: **`ops/competitors/sir-jobs.md`** (researched 2026-11-12). Best-in-class bar to match: Huntr (CRM + tracker), Teal (resume match loop), Simplify (autofill breadth), LoopCV (low-cost auto-apply), Jobscan (ATS depth) - replicated locally, privately, free.

## 6. Features (best-in-category parity plus owner's own ideas)

Parity targets (all local, no paywall):
1. Job discovery: official feeds and manual import only (Remotive, RemoteOK, WeWorkRemotely RSS, Wuzzuf, Mostaql, LinkedIn manual paste); per-source terms review in `docs/SOURCES.md`; disallowed sources switched off.
2. Fit scoring with written rubric + eval set (`scripts/ai_eval.mjs`); accepts a model only if it beats the stored score.
3. ATS-style keyword match + missing keywords per job (gap 9).
4. Drafting in Arabic or English matching the posting; "why it fits / does not fit" in plain words.
5. Application kanban with stages (staged, applied, interviewed, offered, rejected, ghosted), follow-up strip (done, r46), export JSON/CSV (done, r46), contacts CRM tab (done, r46).
6. Auto-apply: vetted matches only, cap 10/day, dedupe by URL, 15 skip rules, second-pass truth audit; channels in priority order Gmail API (post-exposure only), CDP browser with screenshot proof, owner queue (`_local/apply_queue.json`).
7. Proof ledger: no "Applied" without proof file; outcomes (interview/offer/reject/ghost) with dates and amounts (gap 4).
8. Follow-ups: day-3/day-7 post-interview nudges (gap 6); overdue alert strip (done).
9. Weekly outcomes digest (Arabic, simple) + one daily money brief via Telegram, through the shared sender and the job-specific ledger; per-source and per-role-family counters (gap 7).
10. Money/cash hub: cached FX (USD/EGP), money-goal engine kept as an honest tracker against the income model, never a fake fixed target.
11. Analytics (owner-only): response rate, interview rate, offer rate by source and role family; integers only; empty states show 0 (gap 11).
12. Contacts/warm-intro finder: surface logged contacts at the target company (gap 16).
13. Tailored CV export per application (gap 20); per-job attached resume version (gap 5).
14. Offline CV PDF; offline-first dashboard; `data/contacts.json` atomic writes.

Owner's own ideas, ported forward (sources cited):
- From `legacy/Jobs/sir_ahmed_ai_job_automation_master_prompt.md`: 4-year Vibe Coder roadmap context, Arabic/English bilingual evaluator premium, Google Workspace + TickTick career-platforms note (Upwork, Almentor, Roeya, EdClub, iFixit), DataAnnotation/Appen/Telus class evaluator work as a first income wedge.
- From owner decision 2026-11-11 (AGENTS.md, Job applications): auto-apply without waiting for a tap, vetted truthful matches, max 10/day, each logged and reported on Telegram, sign-in via his Google chooser allowed, forms filled from his real profile and portfolio site, never ID uploads, never payments.
- From owner decision 2026-11-11 (Income target): real and measured; SIR Jobs researches what a Vibe Coder can truly earn (`.sir/INCOME_MODEL.md`); no fixed figure anywhere.
- From TickTick-adjacent legacy notes: Upwork Freelance Track and career platforms list (kept as owner checklist `docs/OWNER_STEPS.md`, not as scraping targets).
- From `.sir/plans/FEATURE_GAPS.md` (r46, ranked 1-22): items 1-3 done; 4-22 queued by value (outcome tracker, per-job documents, interview nudges, weekly digest, negotiation tracker, keyword matcher, manual add, analytics, no-applications nudge, 中文/हिन्दी dictionaries, TOTP, calendar sync, warm intro, offer comparison, CSV import, confidence score, tailored CV, vibe tags, offline queue).
- From SIR Jobs's own originated lessons (adopted into OWNER_DEFAULTS.md): per-character bidi detection, native-app feel, five states, real zeros - the codebase is the reference implementation for these rules.

## 7. Architecture (on the shared kit; PERSONAL tier)

- **Accounts**: single owner, loopback bind + `Tailscale-User-Login` check; no Firebase Auth needed (SHARED_PLATFORM_KIT section "PERSONAL products"). If ever spun out: owner-auth pack from the kit.
- **Owner-only analytics page**: `/admin` (loopback) shows real counters only (applications, replies, interviews, offers, income vs model); fail closed; never public.
- **AI with fallback chain** (`plans/AI_FALLBACK_CHAIN.md` order): Gemini `flash-lite-latest` → `flash` → any Gemini → OpenRouter free → local Ollama (`D:\Projects\AI_Models_Hub`). Personal documents (CV, phone, address, notes) never go to an outside provider: local model or redacted public job text only (redaction unit test on the prompt builder). Kill switch `JOBS_AI=off`. `private=true` forces local; fail closed if local unavailable.
- **Hosting**: none. PERSONAL class: no Firebase Hosting, no Vercel, no domain (n/a by class, owner decision 2026-11-12 portfolio map). If ever offered: dual hosting per kit section 15, own Firebase project, own repo, legal pack, lawyer review.
- **Data**: SQLite (local), atomic writes; backups weekly via `scripts/snapshot.py` to `D:\Projects\Backups\SIR-Jobs-data` with monthly restore check; gitleaks in CI; secrets in Credential Manager/untracked `.env`.
- **Notifications**: shared sender `_SIR/scripts/deliver/send-telegram.mjs`; one brief per day via the ledger; weekly Monday digest at :00 Cairo.
- **Kit adoption**: design-tokens, motion, i18n, help-center, ui/styles/hooks, changelog, security-baseline, operations-standard, launch-package (prepared, unused), visibility-standard (n/a, noindex). NOT adopted: billing, owner-auth (single owner), bot-link, signed-webhook.

## 8. Premium quality bar

Design: one design system (shared tokens until kit extraction); spring motion (transform/opacity only, 120 Hz safe); Arabic RTL-first and English; per-character bidi detection in every input; `<bdi>`/`unicode-bidi:isolate` for mixed runs; five states on every screen (idle, loading skeleton, empty with one action, error with retry, populated); 44 px touch targets; light/dark/system/high-contrast; WCAG 2.2 AA; 320-1920 px no clipping; real zeros, never invented numbers; version stays 1.0.0; no emoji in UI; no em-dashes in copy; escaping discipline (escHtml/escapeJs/safeHref); headless muted browser tests that always close. Verification: `npm test`, `npm run lint`, `npm run typecheck`, `npm run doctor` green before any push; screenshots at the widths above; browser audits (r34/r46-style CDP harnesses) with zero defects before claiming done.

## 9. Free tier and fair pricing (EGP and USD)

**n/a for this product (PERSONAL, never sold).** Outline only, if a GLOBAL spin-off ever happens: Free (1 owner, local, 5 applications/day, manual import), Pro USD 9/mo or 450 EGP/mo (auto-apply 10/day, AI scoring, digests), Pro Plus USD 19/mo or 950 EGP/mo (tailored CV export, interview prep, priority evals); EGP first with USD toggle auto-detected from locale (never manual-only); Paymob/Fawry for Egypt; lawyer-reviewed legal pack before any paid launch; never inside this folder.

## 10. Milestones M0 to M6 with acceptance tests

| M | Goal | Acceptance test |
|---|---|---|
| M0 | Desktop folder kit recreated (owner default 19): `D:\Projects\Desktop\SIR Projects\SIR Jobs\` with folder.ico (project root), Start/Stop dev, web link (tailnet), Open project folder, Versions.txt (1.0.0, plain status); GitHub repo exists and is private | Folder exists; folder.ico is the project's icon; shortcuts resolve; Versions.txt says 1.0.0; `gh repo view sirahmed8/sir-jobs` shows private |
| M1 | Clean tracker with proof discipline | `npm run proof-report` prints rows with and without proof; zero "Applied" without proof; old rows without proof show "unverified" |
| M2 | Pipeline offline reproduces | `npm run pipeline:offline` produces shortlist + drafts from fixtures; `npm test` green |
| M3 | Security | `node test/test-security.mjs` passes; redaction test passes; gitleaks clean |
| M4 | AI quality | `npm run evals` prints a score, saves to `.sir/evidence/`; model swap requires beating stored score |
| M5 | Quality | Screenshots 320/390/768/1440 light/dark/RTL; a11y audit passes; r46-audit 28/28; zero horizontal overflow |
| M6 | Real outcomes | At least one real application submitted with proof file; first reply logged with date; income ledger in `.sir/evidence/` shows real USD/EGP amounts or honest zeros |

Exit rule: a milestone is done only when its acceptance test was run and its output recorded; nothing is "working" because the code exists.

## 11. Risks and open questions (defaults)

- Job-board terms may forbid scraping: default is official feeds and manual import; switch the source off otherwise (`docs/SOURCES.md`).
- Auto-apply can spam: cap 10/day, truth audit, proof ledger, per-source terms check; if a source forbids automation, it is manual-only.
- "Staged" looking like progress: counts only after a real reply.
- Python 3 and Node both used (`scripts/snapshot.py`): keep, they are small.
- Outside AI sees public job text only; personal data local-only.
- Market claims (rates, fees) not in this plan unless sourced or "(unsourced, verify)".
- CI quota: while `ops/ci-quota-exhausted.flag` exists, local verification is the green proof; still commit and push to main. (Flag is stale as of 2026-11-12: runs pass; the flag stays until the owner deletes it.)
- AHome/Habiba data never enters this product; no exceptions.

## 12. Only the owner can do

Sign in to job/freelance platforms, solve CAPTCHAs, click Submit (when not auto-submitted under the 2026-11-11 mandate), set payout details, accept contracts, identity checks, buy anything.

## 13. Skills picked for this product (from `ops/SKILLS_INDEX.md`)

Design: modern-ui-ux-design-system, anti-vibecoded-design-system, emil-motion-impeccable, a11y-debugging, mobile-ergonomics-polish, modern-app-engineering, react-best-practices, high-conversion-copywriting
Security: owasp-vulnerability-shield, zero-trust-security-hardening, vibe-auth-hardening
AI/automation: ai-sdk, ai-gateway, gemini-api-dev, workflow, karpathy-skills
Data/integrations: gdrive, gsheets, gcalendar (interview sync, owner tap), agent-reach (read-only research), video-digest (analyze job-hunt content)
Applied from SIR Jobs already: per-character bidi, native-app feel, five states, real zeros (see OWNER_DEFAULTS.md "Adopted from SIR Jobs")

## 14. Next steps into tasks

The first 10 tasks for the free agents are in **`ops/briefs/sir-jobs-tasks.md`** (title + one-paragraph brief each, ready to queue). Competitor matrix: `ops/competitors/sir-jobs.md`. Gap backlog: `D:\Projects\SIR Jobs\.sir\plans\FEATURE_GAPS.md` (items 4-22).
