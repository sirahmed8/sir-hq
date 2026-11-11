# Running state of HQ (keep this file current; it is printed after every compaction and reset). Updated 2026-11-11 06:45

## OS background tasks (Windows, run without any chat)
SIR_HQ_Autopilot (5 min, MAX_PARALLEL 5, workers), SIR_HQ_Watchdog (10 min: repairs, CI fix tasks, audits, disk, leaked browsers), SIR_HQ_ManagerTick (hourly free-model manager when no HQ note for 50 min), SIR_HQ_Duties (10 min: day rhythm from real prayer times: fajr, health_asr, isha_summary, health_isha, via claude -p), SIR_Portfolio_Refresh (weekly), game pause file: D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json.

## Session crons (die with the Claude session; recreate after a restart)
Hourly watch (a1f9d7a3, :00), WhatsApp digest every 2 h (8b33be71, :30, needs Chrome tools). Day-rhythm one-shots recreated as needed via SendMessage to the duty files when the OS task SIR_HQ_Duties needs a manual nudge. Day-rhythm crons were moved to the OS task SIR_HQ_Duties.

## Sonnet 5.5 subagents (resume with SendMessage by name)
sir-ai-builder (owns SIR AI M1 to M5, hosts https://sir-ai-official.web.app and https://sir-ai-pi.vercel.app), sir-portfolio-builder (owns SIR Portfolio, hosts https://sir-portfolio-site.web.app and https://sir-portfolio-liart.vercel.app), linkedin-improver (LinkedIn profile, post, jobs, max 10 connection requests a day), study-materials-agent (portal manifest, NotebookLM, Drive), owner-method-analyst (finished), keys-agent (per-project Gemini and OpenRouter keys, OAuth apps, bot). Haiku operator agents refuse relayed consent: sign-in taps stay with the owner.

## Free CLI queue (ops/AUTOPILOT_QUEUE.json, models ops/agy-runs/model-pool.json, tool guide plans/AI_TOOLS_CONTROL.md)
One writer per project. Open: r21-ahome, r22-study, r24-jobs-apply (auto-apply, cap 10 a day), r24-games, r26-infra, r27-study-sources.

## Keys and ids (values only in ignored files)
D:/Projects/_SIR/_local/api-keys.env (Gemini key, project SIR Projects, NOT for AHome; also user env GEMINI_API_KEY), _local/ahome-oauth.env (TickTick app, Google Tasks OAuth client for AHome), OpenRouter key pending the owner's emailed code. Local private exports: _local/ahome-events-import.json, _local/job_offers.jsonl, _local/linkedin-plan.md, _local/portal_manifest.json, _local/whatsapp_seen.json.

## Quotas and renewals
Claude weekly resets 2 AM, 5-hour 10 AM (owner). Codex monthly resets about 2026-11-27. Antigravity free accounts weekly about 2026-11-17 (others unknown). ZCode/GLM out; signed out, owner tap only. ChatGPT account shows Free. NotebookLM daily limit resets about 05:49.

## Owner rules in force (full list: standard/OWNER_DEFAULTS.md, plans/OWNER_METHOD.md, ops/OWNER_REQUEST_LEDGER.md, D:/Projects/AGENTS.md)
Never stop for approval on consent taps; passwords, 2FA codes, CAPTCHAs, payments, new accounts stay his; never solve graded college work (practice sets instead); auto-apply to vetted jobs; clean Telegram messages; two hosts per web product; truth only on profiles; AHome data private; TickTick note Accounts never opened.

## New standards (2026-11-11)
plans/AI_FALLBACK_CHAIN.md (per-project keys, Gemini then OpenRouter then other free providers then local), plans/WINDOWS_APP_STANDARD.md (installer, Firebase sign-in, self-update, download page, Product Kit folder, Projects-Hub.html), plans/COMPACTION_PROTOCOL.md.
