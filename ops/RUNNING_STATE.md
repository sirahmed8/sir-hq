# Running state of HQ (keep this file current; it is printed after every compaction and reset). Updated 2026-11-12 02:45

## OS background tasks (Windows, run without any chat)
SIR_HQ_Autopilot (5 min, MAX_PARALLEL 5, workers), SIR_HQ_Watchdog (10 min: repairs, CI fix tasks, audits, disk, leaked browsers), SIR_HQ_ManagerTick (hourly free-model manager when no HQ note for 50 min), SIR_HQ_Duties (10 min: day rhythm from real prayer times: fajr, health_asr, isha_summary, health_isha, via claude -p), SIR_Portfolio_Refresh (weekly), game pause file: D:/Projects/SIR Laptop Manager/.sir/game_mode_snapshot.json.

## Session crons (die with the Claude session; recreate after a restart)
Hourly watch (a1f9d7a3, :00), WhatsApp digest every 2 h (8b33be71, :30, needs Chrome tools). Day-rhythm one-shots recreated as needed via SendMessage to the duty files when the OS task SIR_HQ_Duties needs a manual nudge. Day-rhythm crons were moved to the OS task SIR_HQ_Duties.

## Sonnet 5.5 subagents (resume with SendMessage by name)
sir-ai-builder (owns SIR AI M1 to M5, hosts https://sir-ai-official.web.app and https://sir-ai-pi.vercel.app), sir-portfolio-builder (owns SIR Portfolio, hosts https://sir-portfolio-site.web.app and https://sir-portfolio-liart.vercel.app), linkedin-improver (LinkedIn profile, post, jobs, max 10 connection requests a day), study-materials-agent (portal manifest, NotebookLM, Drive), owner-method-analyst (finished), keys-agent (finished: per-project Gemini/OpenRouter keys, SIR AI OAuth apps + Telegram bot + Notion integration; idle now). Haiku operator agents refuse relayed consent: sign-in taps stay with the owner.

## Free CLI queue (ops/AUTOPILOT_QUEUE.json, models ops/agy-runs/model-pool.json, tool guide plans/AI_TOOLS_CONTROL.md)
One writer per project. Open: r21-ahome, r22-study, r24-jobs-apply (auto-apply, cap 10 a day), r24-games, r26-infra, r27-study-sources.

## Keys and ids (values only in ignored files)
D:/Projects/_SIR/_local/api-keys.env (Gemini key, project SIR Projects, NOT for AHome; also user env GEMINI_API_KEY), _local/ahome-oauth.env (TickTick app, Google Tasks OAuth client for AHome), OpenRouter key pending the owner's emailed code. Local private exports: _local/ahome-events-import.json, _local/job_offers.jsonl, _local/linkedin-plan.md, _local/portal_manifest.json, _local/whatsapp_seen.json.

## Quotas and renewals
Claude weekly resets 2 AM, 5-hour 10 AM (owner). Codex monthly resets about 2026-11-27. Antigravity free accounts weekly about 2026-11-17 (others unknown). ZCode/GLM out; signed out, owner tap only. ChatGPT account shows Free. NotebookLM daily limit resets about 05:49.

## Owner rules in force (full list: standard/OWNER_DEFAULTS.md, plans/OWNER_METHOD.md, ops/OWNER_REQUEST_LEDGER.md, D:/Projects/AGENTS.md)
Never stop for approval on consent taps; passwords, 2FA codes, CAPTCHAs, payments, new accounts stay his; never solve graded college work (practice sets instead); auto-apply to vetted jobs; clean Telegram messages; two hosts per web product; truth only on profiles; AHome data private; TickTick note Accounts never opened.

## Desktop & Product Kits (r31, 2026-11-11)
- Projects Hub: D:\\Projects\\Projects-Hub.html (Desktop shortcut: Projects Hub.url). Product Kit folders created for SIR AI, SIR Portfolio, SIR Jobs, SIR Laptop Manager, _SIR. AHome and SIR Study skipped this round because their locks/workers were active (no repo writes).

## New standards (2026-11-11)
plans/AI_FALLBACK_CHAIN.md (per-project keys, Gemini then OpenRouter then other free providers then local), plans/WINDOWS_APP_STANDARD.md (installer, Firebase sign-in, self-update, download page, Product Kit folder, Projects-Hub.html), plans/COMPACTION_PROTOCOL.md.

## Disk cleanup r41 (2026-11-12)
Freed 14.81 GB regenerable space: D: 2.03→14.82 GB (+12.79), C: 7.61→9.63 GB (+2.02). Deleted legacy node_modules (9.3 GB), legacy build outputs (2.4 GB), caches (pnpm 0.49, Playwright 1.58, Gradle 0.51, Temp 0.22), _quarantine folders, browser profiles, old agy-runs logs. Protected: legacy/, old projects/, games/, AI_Models_Hub, Backups/, AHome data, git history, secrets.

## Daily pool health
- pool health 2026-11-12: available=24 cooling=2

## Usage windows & scheduling (r42)
- 5-hour window resets: 10 AM daily (owner). Current window: 2:45 AM - 7:45 AM (next reset ~10:00 AM).
- Weekly quota resets: Antigravity free accounts ~2026-11-17, Claude weekly ~2026-11-16 2 AM.
- Scheduling rule: Heavy rounds (verification, full audits, UI overhauls) scheduled into accounts with >50% weekly remaining and >50% 5h remaining.
- Current account availability for heavy work:
  - a7medorabe7: weekly exhausted (0%), 5h exhausted
  - a01083835229: weekly exhausted (0%), 5h 100% (but paid reserve has Gemini 4 Argon)
  - ahmedalaa2006.7.6: weekly 24%, 5h 23%
  - 1sir1ahmed1: weekly 5%, 5h 100%
  - a01083835229 (paid): Gemini 4 Argon 100%, Claude/GPT 50% weekly
- Next heavy round (r43+) should use a01083835229 paid reserve (Gemini 4 Argon) or ahmedalaa2006.7.6 if available.
- Free CLI pool (kilo/opencode/devin/local Ollama): 31 entries, 2 new OpenCode free models proven (nemotron-3.5-lightning-free, beam-free); AHome runs local models only; OpenRouter free cap shared, resets 00:00 UTC. Limits: ops/USAGE_LIMITS.md. Owner one-tap sign-ups: ops/research/free-tools-2026-11-12.md.

<!-- r42-usage:start -->
## Usage windows & heavy-round plan (r42)

How the numbers are read: from the tool's own usage banner, never by sending a test message.
- Five-hour window resets at 10:00 (owner).
- Claude weekly resets 02:00 (owner).
- Antigravity free accounts reset weekly around 2026-11-17.
- Codex monthly limit resets around 2026-11-27.
- NotebookLM daily limit resets around 05:49.

Heavy rounds go to (at least 50% left in both windows):
- a7medorabe7@gmail.com / Claude Sonnet 4.6 (Thinking), Claude Opus 4.6 (Thinking), GPT-OSS 120B (Medium): 5h 100%, weekly 100% (read 2026-11-09 operator14)
- a01083835229@gmail.com / Claude and GPT models (Claude Opus 5.5, Claude Sonnet 5.5, GPT-OSS 120B): 5h 50%, weekly 100% (read 2026-11-09 operator23)

Light work only (one window is low):
- a7medorabe7 / Gemini: 5h 12%, weekly 10% (read 2026-11-09 evening)
- a01083835229 / Gemini: 5h 100%, weekly 18% (read 2026-11-09 evening)
- 1sir1ahmed1 / Gemini: 5h 49%, weekly 16% (read 2026-11-09 evening)
- a7medorabe7@gmail.com / Gemini 3.8 Flash High: 5h 100%, weekly 10% (read 2026-11-09 operator14)

Unknown, read the banner before using:
- --- / --- (read ---)
- OpenCode (Copilot, Google, OpenRouter) / opencode free models (read 2026-11-09 operator15)
- Kilo Gateway (a7medorabe7@gmail.com) / kilo free router and stealth models (read 2026-11-09 operator15)
- Codex (ChatGPT login in ~/.codex/auth.json) / gpt-6-luna (read 2026-11-09 operator15)

Free CLI pool (kilo, opencode, devin, codex): separate from these accounts and used first for verification and scout rounds.
Plan written 2026-11-12 03:08 by scripts/hq_usage_plan.py.
<!-- r42-usage:end -->
- SIR_HQ_Dashboard (:00 and :30, regenerates ops/artifact/control-room.html), SIR_HQ_ArtifactPublish (hourly :05 from 17:05, hidden Haiku run republishes the Claude artifact only when the file changed; log ops/artifact/publish.log; tested once by hand: published). Owner no longer has to ask for status: Control Room is the answer.
