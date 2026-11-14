# SIR Jobs / SIR Study / SIR Portfolio: AI features pass

Owner request (2026-11-14): make sure these projects have real AI features and smarter logic, not just static sites.
For each project (D:/Projects/SIR Jobs, SIR Study, SIR Portfolio):
1. Audit what AI/LLM features exist today (grep for openai/gemini/ollama/ai calls).
2. Add or fix at least one genuinely useful AI feature per project that fits its purpose (e.g. Jobs: match scoring/explanation of why a job fits; Study: quiz/explanation generation; Portfolio: AI-assisted project descriptions or chat about projects). Use existing provider config patterns in the repo; free tiers only; no secrets in git.
3. Keep it real - no fake/mock AI output, graceful fallback when no key configured.
4. Run verify/tests, commit to main, update .sir/CHECKPOINT.md.
