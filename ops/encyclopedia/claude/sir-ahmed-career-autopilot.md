# sir-ahmed-career-autopilot

Tools: claude (also codex/cursor/opencode/windsurf; claude chosen). Source: C:\Users\a7med\.claude\skills\sir-ahmed-career-autopilot\SKILL.md (44 lines, read in full)

## Summary
Owner-specific career automation for Ahmed Alaa: encodes his real identity (Vibe Coder/AI Operator positioning, Syrian national in Cairo, Egyptian-document KYC rule for US platforms), target role categories, the D:\Jobs master workspace with ATS CVs and application tracker, a weekly Saturday 9AM Cairo cron cadence via career_engine.py, and bilingual reporting rules (Egyptian colloquial Arabic reports, zero-fluff English outreach).

## When to use / not use
Use for job discovery, ATS CV tailoring, auto-apply workflows, and recruiter outreach FOR SIR AHMED specifically. Not a general job-search skill — it contains his personal data and positioning; useless or wrong for anyone else, and should never be generalized into templates containing his PII.

## Inputs, outputs, dependencies
Input: job boards/targets per the 5 role categories. Output: ATS-ready CVs (HTML+MD), applications_tracker.json, DAILY_JOB_REPORT.md weekly Arabic report, outreach messages. Needs: D:\Jobs workspace, career_engine.py, Playwright-class scraping, cron scheduling.

## Key rules
1. Identity ground truth is fixed: name, contacts, profiles, "Vibe Coder & AI Operator" positioning — never inflate into "writes systems code manually" claims; the working approach is directing AI tools.
2. KYC rule: for US verification flows (Outlier, Alignerr) NEVER submit Syrian passport — select Egypt (EG) with Egyptian residence permit/driver's license, because OFAC filters trigger id_disallowed_country_detection.
3. Cadence is fixed: weekly Saturday 9:00 AM Africa/Cairo via CRON_TZ; single consolidated workspace D:\Jobs with named tracker/report files.
4. Reports in authentic Egyptian colloquial Arabic with strict orthography (إلّي، ڤ، masculine pronouns); outreach in high-signal English citing shipped products (obourinstitutes.web.app, egfootball5.vercel.app, github).
5. Five target categories only: AI data annotation/eval, vibe coding/AI operator, no-code delivery, entry-level support/QA, freelance (Upwork/Mostaql).

## Risks / owner items
- Contains real PII (full name, emails, phone, national ID-adjacent KYC guidance) — the file itself is sensitive; it lives in a private skills dir, must never leak into public repos or prompts to external services.
- Auto-apply carries platform-ToS and misrepresentation risk; the skill doesn't include anti-ban safeguards.
- Identity claims (2nd-year CS student, "vibe coder") must stay truthful in outreach — fabrication would burn the profiles it cites.
- Depends on D:\Jobs existing with the engine script — machine-specific paths.

## Category and tags
jobs, automation, business — career, job-search, ats, owner-specific, autopilot.

## Revision note
Single claude revision; owner-personal skill — treat contents as private data.
