# r24-jobs-apply — Final Report

Date: 2026-11-11
Repo: D:/Projects/SIR Jobs (main)
Shared ops: D:/Projects/_SIR (sir-hq main)
Brief: D:/Projects/_SIR/ops/briefs/r24-jobs-apply.prompt.txt
Checklist: .sir/r24-jobs-apply_CHECKLIST.md — all 10 items ticked with evidence under .sir/evidence/r24/

## Owner decision honored

- Old fixed "1,200 EGP" income goal cancelled; replaced by .sir/INCOME_MODEL.md — sourced weekly ranges and scenarios for the real Vibe Coder profile. No fixed income promise anywhere.
- TRUE profile only: the fit checker now hard-gates on the digest's canonical matchesProfileKeywords (title+tags role-family evidence) plus a licensed-profession blocklist. Description keyword overlap alone never admits a job. Verified live: a "Registered Nurse" AI-trainer post and a "Junior Market Analyst" post are rejected with licensed_profession / outside_profile flags.
- Never claims skills Ahmed does not have: drafts say "I do not claim experience I do not have" and cite only repo-proven products.
- One Telegram message per suitable job; every reply path requires the owner's tap.
- SUBMITTED is recorded only with real proof; otherwise the stage stays APPROVED awaiting the owner's final manual submit.
- AHome/Habiba material untouched; legacy/ untouched (read-only respected).

## What was built

1. src/job-sources/index.mjs — aggregates RemoteOK, WeWorkRemotely, Jobicy, Arbeitnow, Remotive (offline fixtures: 51 jobs) + _local/job_offers.jsonl WhatsApp offers (10) = 61 normalized jobs. Upwork-like signed-in source is an explicit path that returns nothing until a real browser session exists — no fabricated data.
2. src/apply-pipeline/fit-checker.mjs — scoreFit/evaluateRisk/getRiskDetails + role families + truth gate; emits ratio, family, priorityScore, machine risk flags, 2-line Arabic-ready fit summary. 40/61 fixture jobs pass the gate.
3. src/apply-pipeline/drafter.mjs — truthful AR/EN cover notes, CV + Verified_CV.pdf + 4 live proof repos; Gmail draft structure; recipient email only when the post itself exposes one (guessed hiring@domain fallback removed from both drafter and apply-gmail).
4. src/apply-pipeline/notify.mjs — one message per match via send-buttons.mjs: title, company, pay with EGP conversion + FX rate/date, 2-line fit, risk flags; Arabic قدّم/تخطي buttons; compact a_/s_ callback_data (64-byte safe, sha256 for long ids) auto-registered in ops/telegram-actions.json.
5. scripts/apply/handler.mjs + apply-browser.mjs + apply-gmail.mjs + send-reply.mjs + reply-handler.mjs + send-confirmation.mjs + weekly-report.mjs — apply/skip handler resolving jobs across sources + pipeline DB (incl. hashed callback ids); submission channels in order: Gmail send (real OAuth + post-exposed email only), dependency-free CDP headless Chrome apply with screenshot proofs (--mute-audio, always closes, verified no leaked process), owner's signed-in browser; honest SUBMITTED-vs-APPROVED staging; weekly Arabic metrics report.
6. src/apply-pipeline/gmail-watcher.mjs — real Gmail API polling (lazy googleapis, data/gmail-credentials.json + gmail-token.json), applied-domain filter, answer/interview/info_request/rejection classification, persisted replies, Telegram suggested-reply + ابعت الرد (reply_<threadId>); skips cleanly without credentials; never sends without tap.
7. src/apply-pipeline/metrics.mjs + runner.mjs — real counters applications_sent/answers_received/interviews/offers by source, role family, ISO week; delivered-vs-submitted distinction (markDelivered does not inflate metrics).
8. .sir/INCOME_MODEL.md — 171 lines: rate ranges per work type, conservative/moderate/optimistic weekly scenarios, application funnel estimates, risk factors, measurement plan, named sources.

## Shared _SIR changes (sir-hq commit 8fd9ab6, pushed)

- scripts/deliver/telegram-inbox.mjs — routes a_<jobId> (apply), s_<jobId> (skip) to SIR Jobs scripts/apply/handler.mjs and reply_<threadId> to reply-handler.mjs.
- ops/telegram-actions.json — added view_pipeline action (opens dashboard pipeline view).

## Repairs made this session (prior round was broken mid-work)

- Fixed ESM require() leftovers, async test helper that never awaited, path-module shadowing, stale fixture path, missing exports across all new modules.
- Rewrote handler staging to eliminate false SUBMITTED claims; added hashed-callback-id resolution; added SIR_APPLY_DRY_RUN + env path overrides (SIR_JOBS_DB_PATH, SIR_APPLY_STATE_PATH, SIR_GMAIL_STATE_PATH, SIR_APPLY_METRICS_PATH, SIR_ROOT) for isolated evidence runs.
- Replaced apply-browser Playwright dependency with dependency-free CDP (no new npm deps).
- Added the missing truth gate after discovering 60/61 jobs (incl. a physician role) passed the naive scorer.
- Removed speculative hiring@<board-domain> email fallback.
- Zero TODOs, zero em-dashes, lint 0 problems, typecheck 0 errors.

## Verification (all real command output in .sir/evidence/r24/)

- node test/test-r24-apply-pipeline.mjs: 31 passed, 0 failed
- node test/test-r24-apply-browser.mjs: 2 passed, 0 failed (real headless Chrome vs local page, screenshots verified, no leaked process)
- npm test: exit 0, every suite green (output: npm-test.txt)
- npm run lint: 0 problems; npm run typecheck: 0 errors
- node scripts/doctor.mjs: ALL GATES GREEN (7/7)
- CI: gh run watch 42946934207 on 42ae8fa — SUCCESS (tests, windows, secrets)

## Commits

SIR Jobs main: 7f628d2 (sources+fit+drafter), 22e30e1 (notify+handler+gmail+metrics), cfa1b86 (tests+income model+evidence+checklist), 42ae8fa (barrel), plus docs(r24) checkpoint/checklist commit.
_SIR sir-hq main: 8fd9ab6.

## Known honest limitations

- Live (non-fixture) fetch and real Telegram/Gmail sends were not exercised end-to-end in this session (no live send performed; dry-run and isolated-state evidence used instead). First real run happens on the owner's machine via the runner/notify path.
- Gmail watcher needs data/gmail-credentials.json + gmail-token.json (OAuth) to poll; until then it logs a clean skip.
- Upwork-like platforms contribute nothing until a signed-in browser session path is built (explicit, no fake data).
- Role-family terms are English; Arabic-titled WhatsApp offers may be under-matched by the profile gate (consistent with the digest's own filter).
