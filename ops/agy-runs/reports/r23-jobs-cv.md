# r23-jobs-cv Report

Date: 2026-11-11
Repo: D:/Projects/SIR Jobs (main)
Commit: 207bc30 "r23: evidence-backed Vibe Coder truth for CV, profile and fit evaluator"
Brief: D:/Projects/_SIR/ops/briefs/r23-jobs-cv.prompt.txt
Checklist: .sir/r23-jobs-cv_CHECKLIST.md (items 1-7 ticked with evidence; item 8 this report + CI)

## What changed

1. Evidence registry (checklist 1)
   - New tracked registry `config/skill-evidence.json` (the brief said `data/skill-evidence.json`; `data/` is gitignored by the secrets shield, so the registry lives in `config/` and `src/fit-evaluator/skill-evidence.mjs` accepts `data/` only as a runtime fallback).
   - 23 skills: 16 proven, each with repo + exact proof types (package deps, file existence, glob counts, file contents, git remote); 7 explicit gaps with reasons (python-backend-apis, enterprise-cloud-devops, ml-model-training, systems-languages, senior-engineering-tenure, completed-university-degree, mobile-native-development).
   - New `scripts/audit_skill_evidence.mjs` re-scans `D:/Projects`, evaluates every citation, exits non-zero on stale proofs.
   - Doctor gate 7 "Skill Evidence & Claim Registry" added to `scripts/doctor.mjs`.
   - Output: `[skill-evidence] Audited 23 skills against D:/Projects` / `Proven: 16/16 | Gaps confirmed: 7/7` / `OK: every citation holds` (.sir/evidence/r23/skill-evidence-audit.txt).

2. CV rewritten as Vibe Coder (checklist 2)
   - `src/cv/cv-data.mjs` + `src/cv/cv-html.mjs`: title is now Vibe Coder / AI product builder. Claims limited to AI-directed product building, Firebase Hosting and Vercel deploys, prompt and agent management, Arabic/English UI, CS study at Higher Obour Institute. Removed: Full-Stack Software Engineer, Python backend, Starlette/FastAPI, Docker, SQLite WAL, RAG, RLHF, seniority claims.
   - Regenerated `docs/Ahmed_Oraby_Verified_CV.html` and `docs/Ahmed_Oraby_Verified_CV.pdf` (77,870 bytes) via `node scripts/generate_cv_pdf.mjs`.

3. Profile alignment (checklist 3)
   - `src/parsers/profile.mjs`: 6 verified projects (SIR Jobs, SIR Portfolio, SIR AI, SIR Study, SIR Obour Hub, SIR Laptop Manager), repo-verified tech only.
   - `src/drafter/profile.mjs`, `src/drafter/keywords.mjs`, `src/drafter/draft.mjs`, `src/parsers/proposals.mjs`: new project ids, truthful pitch copy, no fabricated stack claims.
   - `src/public/js/views/profile.js`: "Verified Products & Repositories" replaces "Audited Shipped Applications (100% live HTTP 200)".
   - `.sir/PROFILE.md`, `src/public/i18n/en.json`, `src/public/i18n/ar.json` aligned; `src/money-engine/catalog.mjs` proposal template de-hyped.
   - Grep sweep over candidate-facing files: no Full-Stack SWE, no 100% HTTP 200, no Starlette/FastAPI/SQLite WAL/RAG/RLHF claims remain (remaining hits are job-requirement matching in scorer.mjs, benchmark job descriptions in fit-evaluator/dataset.mjs, historical fixture records, and gap documentation).

4. Evidence-backed fit evaluator (checklist 4)
   - `src/fit-evaluator/skill-evidence.mjs`: `loadSkillRegistry`, `isSkillProven`, `provenReposFor`, `criterionEvidence`, `CRITERIA_SKILL_MAP` covering all 11 scorer criteria.
   - `scripts/digest/scorer.mjs`: `proven` flags now come from the registry; each proven item exposes `provenEvidence` with citing repos; `Python Backend / APIs` maps to `python-backend-apis` which is a confirmed gap. Output contract preserved (provenCount, totalCount, ratioText, ratio, provenList, unprovenList, scorePercentage, explanation).

5. Vibe-coder ranking (checklist 5)
   - `src/fit-evaluator/role-families.mjs`: 7 families (prompt writing, data labeling/evaluation, AI operations, tech support, bilingual content, proven web front end, AI-assisted building) with bounded weights.
   - `scripts/digest/scorer.mjs` emits `roleFamily` + `priorityScore` (ratio + bounded family bonus, capped at 1).
   - `scripts/digest/filter.mjs` admits family roles (title-scoped classification) while hard exclusions remain.
   - `src/parsers/digest.mjs` + `src/pipeline-engine/runner.mjs` sort by `priorityScore ?? ratio`.
   - `src/public/js/views/openings.js` renders a role-family badge and citing repos per proven item.

6. PDF (checklist 6)
   - `docs/Ahmed_Oraby_Verified_CV.pdf` regenerated (77,870 bytes); `/api/profile/cv.pdf` hash-based background regen + HTML fallback preserved; fx/profile test suite green.

7. Tests and gates (checklist 7)
   - `test/test-r23-vibe-cv.mjs`: 10 tests covering registry shape, lookups, audit correctness (incl. negative proof), full-workspace audit (skipped in CI without D:/Projects), evaluator citations, filter admission/rejection, role families, CV truth + docs regeneration, profile API claims, criterion map coverage.
   - Wired into `npm test`. Updated stale fixtures: test-pipeline.mjs (sir-study proof), test-cycle12-power-features.mjs (sir-study URL, evidence-registry wording), test-dashboard.mjs unchanged (6th project added to profile data instead).
   - Local gates: `npm test` all suites pass (exit 0), `npm run lint` 0 problems, `npm run typecheck` 0 errors, `npm run doctor` 7/7 gates green. Evidence: .sir/evidence/r23/{npm-test,lint,typecheck,doctor,test-r23-vibe-cv,skill-evidence-audit}.txt

## CI

- Pushes: `git push origin main` e541f2b..207bc30, then fixes 07ac3ff and b2d296c.
- Run 42937513952 (207bc30): FAILED - ubuntu+windows on test-r23 audit check `git-min-commits` (CI checkout is shallow, depth 1) plus a pre-existing auth-ui e2e timing flake on windows.
- Fix 1 (07ac3ff): `git-min-commits` returns satisfied on shallow clones (`git rev-parse --is-shallow-repository`), still enforced on full clones.
- Run 42938081314 (07ac3ff): ubuntu tests GREEN; windows failed again on the same auth-ui race.
- Fix 2 (b2d296c): test-auth-ui-flow.mjs polls up to 15s for `#pipeline-populated` (the SPA unhides it only after /api/pipeline resolves) instead of asserting on first paint.
- FINAL RUN 42938319928 (b2d296c): `gh run view` -> `{"conclusion":"success","jobs":[windows:success, tests:success, secrets:success]}`. `gh run watch 42938319928 --exit-status` exit 0. CI on main is GREEN.

## Commands run (real output)

- `node scripts/audit_skill_evidence.mjs` -> `[skill-evidence] Audited 23 skills against D:/Projects` / `Proven: 16/16 | Gaps confirmed: 7/7` / `OK: every citation holds`
- `node scripts/generate_cv_pdf.mjs` -> `Wrote printable CV HTML ...` / `Generated physical PDF ... (77870 bytes)`
- `node test/test-r23-vibe-cv.mjs` -> `tests 10 / pass 10 / fail 0`
- `npm test` -> all suites pass, exit 0
- `npm run lint` -> eslint clean, 0 problems
- `npm run typecheck` -> tsc --noEmit, 0 errors
- `npm run doctor` -> `OVERALL SYSTEM VERDICT: HEALTHY & PRODUCTION-READY (ALL GATES GREEN)` incl. gate 7
- `gh run list --limit 3` / `gh run watch 42937513952` -> see CI section

## Notes / deviations

- Registry path is `config/skill-evidence.json`, not `data/skill-evidence.json`, because `data/` is gitignored; documented in checklist item 1 and code header.
- Historical records (`src/pipeline-engine/baseline-applications.json`, `test/fixtures/legacy_applications_fixture.json`) still contain old pitch text with legacy project names; these are records of what was actually sent, not current claims, and were intentionally left unchanged.
- Benchmark job descriptions in `src/fit-evaluator/dataset.mjs` legitimately mention Python/Starlette as employer requirements; the evaluator now reports them as gaps for the candidate.
