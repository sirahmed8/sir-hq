# Defaults every project and agent applies from day one (Ahmed, 2026-11-09 to 2026-11-11). Read with ops/WORKER_PREAMBLE.md; update when he gives a new standing rule, so no project needs the chat repeated.
1. Quality: premium UI, spring animations, one shared component per pattern (tab bars and segmented controls draggable by finger), five states on every view, nothing clipped at 320 to 1920 px, Arabic RTL and English, light and dark; browser tests for layout invariants; the agent finds defects before the owner does (self-audit loops until two clean cycles).
2. Names and hosting: own Firebase project and own repo named after the product; every public site on Firebase Hosting AND Vercel, same build, same environment variables set on both (AI keys and any .env values must exist in the Vercel project settings too); both addresses curl-checked.
3. Truth: nothing marked working until seen working; CI green is required; no invented numbers; profiles and CV say Vibe Coder only; no fixed income figure.
4. Privacy: AHome and Habiba data never leave AHome; never read or write the TickTick note Accounts; secrets only in ignored files and env vars; _local/ is the place for private exports.
5. Messages to the owner: title, at most 5 one-fact lines, one action or nothing needed; buttons for questions; Egyptian Arabic.
6. Automation: Windows background tasks, pause during games, low priority while he works, independent of any chat; test browsers headless, muted and always closed.
7. Initiative: agents suggest and advise, capture new ideas into the right plan in the same turn, adapt improvements from one project to the others (new component, new rule, new fix) and record them here.
8. College work: help him learn (summaries, practice sets, worked examples, flashcards, mock quizzes); never solve graded work for submission.
9. Jobs: apply automatically to vetted truthful matches (cap 10 a day), report every application and every first answer.
10. Integrations: link every useful account (Google Workspace, TickTick, Telegram, WhatsApp read-only) through the app's own OAuth, with five states and a retry.
11. AI calls in every project follow plans/AI_FALLBACK_CHAIN.md: Gemini flash-lite-latest, then flash, then any Gemini, then OpenRouter free models, then other free providers, then local; one key per project created on that project's own Firebase/GCP project and its own OpenRouter key.
12. Times: scheduled jobs use round times (:00 and :30), never odd minutes, except prayer-based duties.
