Fix every item that failed verification of r81-projects-ai-features.

Verification file: D:/Projects/_SIR/ops/verifications/r81-projects-ai-features.md
Project: D:/Projects (three repos: SIR Jobs, SIR Study, SIR Portfolio)

Failed item (item 2 of the r81 verification): SIR Portfolio's "AI chat" is not AI. `src/components/AIChat.tsx`
is deterministic keyword matching (`matchIntent()` string `includes` over `PORTFOLIO_KNOWLEDGE`), with no model
call, no provider config and no fallback, yet the UI presents it to visitors as "I'm your AI guide". Jobs and
Study already do this correctly with `D:/Projects/_SIR/scripts/ai/ask.ps1` plus a deterministic fallback.

Do this, in SIR Portfolio only (Jobs and Study passed; do not touch them):

1. Give the Portfolio chat a real model path that matches the shared pattern: call the local model through
   `D:/Projects/_SIR/scripts/ai/ask.ps1` (the same wrapper Jobs and Study use) for the natural-language answer,
   grounded ONLY in `src/content/knowledge.ts` (never invent facts about Ahmed, projects, dates or numbers).
2. Keep the current keyword matcher as the deterministic fallback when the model is unavailable or returns
   nothing, exactly like Jobs' `buildDeterministicExplanation()` and Study's `explain_query()` fallback. Add a
   kill-switch env var (e.g. `SIR_PORTFOLIO_DISABLE_AI`) that forces the fallback.
3. If a real model path cannot be built in this round for any reason, the honest alternative is to stop calling
   it AI: change the UI copy from "AI guide"/"AI chat" to plain words that describe what it really is (a guided
   knowledge search over the site), remove the AI claim from any meta/description, and record the decision in
   the checkpoint. Do not leave a fake AI label.
4. Add or update a test that proves the fallback works with no model (deterministic answer returned) and that
   the AI path is only reported as used when a real model answered (mirror Study's `ai_enhanced` flag test).
5. Run the Portfolio gates (`npm test`, `npm run typecheck`, `npm run lint`, `npm run build`) and paste the real
   output. CI is quota-blocked (`ops/ci-quota-exhausted.flag`): local verification is the gate.
6. Commit and push straight to `main` (no pull request), update `SIR Portfolio/.sir/CHECKPOINT.md`, and write a
   short report to `D:/Projects/_SIR/ops/agy-runs/reports/r81-projects-ai-features-fix1.md` with the real
   command output and, for any UI change, a screenshot at 390 px.
