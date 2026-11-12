# Phase 8 — Business engine: income, media, jobs, company, studies

> **Read first:** `START_HERE.md`, then `core/07-reporting.md` and the tiers in `core/02-rules.md`. **When this phase is done:** add an entry to `ops/MISSION_LOG.md`, update `ops/HQ_CHECKPOINT.md` and `REQUIREMENTS.md`, send the short report (`core/07-reporting.md`), and continue with the other phases; this one runs in parallel from week 1.

**8.0 Revenue: the first milestone is 1,200 EGP; the goal is a real, growing income.** Start in week 1, in parallel with the engineering.

- **Zero budget.** Every play must start with no money: free platforms, free tiers, free tools. Fees are never paid up front; a play that needs money waits for the ladder below.
- **Reinvestment ladder.** Spend only real earnings, in this order, logging each step and its reason:
  0. Free first: the GitHub Student Developer Pack (Ahmed verifies his student status once; it brings GitHub Pro and other student offers, so check the current list), the free Microsoft Store account, free alternative Android stores.
  1. Google Play's one-time developer fee (Android is the biggest market in Egypt; start the 12-tester, 14-day closed test early).
  2. Domains for the strongest products, unless a free student offer covers them.
  3. Firebase Blaze with a hard budget alert, only where a product truly needs Cloud Functions or Storage.
  4. Apple's yearly developer fee, once iOS revenue can cover it.
  5. Code signing and paid hosting tiers.
  6. Small, measured paid promotion of posts that already perform well organically.
- Plays ranked by speed (research current rates on each platform before pricing anything):
  1. **Local businesses** in Al Obour and Cairo: a fast, professional package (website or landing page, Google Business Profile setup, QR menu or booking page) built from SIR templates. One-off fee plus optional monthly maintenance. These double as SIR Business pilots.
  2. **Freelance platforms:** Khamsat (small fixed-price services) and Mostaql (projects) in Arabic; Fiverr and Upwork globally. Offer services Claude can deliver fast and well: landing pages, React/Next.js fixes, n8n automations, AI chatbots for businesses, spreadsheet automation, bug fixing.
  3. **Jobs:** part-time, remote and internship roles (8.3).
  4. **Products that earn on their own:** templates, n8n workflow packs, browser extensions, small paid tools and micro-SaaS on the the shared standards kit (8.3 finds and builds them).
- **The agent prepares:** profiles and gig listings (Arabic and English), portfolio pieces with live demos, proposal templates, a price list, demo videos, and outreach scripts for local businesses.
- **Who does what:** the agent does everything a platform's terms allow: it writes the profiles and gigs, sends proposals and messages in Ahmed's name through the platform's normal tools, builds and delivers the work, and follows up (Tier 1: honest, personal, never bulk). Ahmed only does what needs him in person (Tier 2, never blocking): identity and payout verification, 2FA codes, calls and meetings, and the platforms whose terms require a human to send messages (the agent leaves those ready to send).
- Track the pipeline (lead → proposal → won → delivered → paid) in the Command Center and report progress toward 1,200 EGP every week. Income isn't guaranteed: if a play doesn't convert within a week, switch to the next.
- **After the first milestone, build recurring revenue:**
  - subscriptions in every product (module 21)
  - SIR Business monthly plans for shops
  - maintenance retainers for freelance and local clients
  - then content monetization and affiliate income (SIR Deals)
  Track monthly recurring revenue in the Command Center, and set each new month's target from the real numbers.

**8.1 Positioning.** A one-page strategy for Ahmed as builder-founder. The likely fastest real revenue is **SIR Business**: B2B software for Egyptian SMEs (restaurants, markets, pharmacies, libraries, furniture shops) sold as monthly subscriptions plus setup fees. Consumer apps build the portfolio and long-term scale. Evaluate this claim with evidence; don't just accept it.

**8.2 Media engine: run ByteVibeHQ.** Ahmed has created the accounts and wants the agent to run them: **Instagram, TikTok, Reddit, Snapchat, Facebook and X**, all with the username **ByteVibeHQ** and signed in inside his Chrome browser. Find each one through Claude in Chrome, and check for others (YouTube, Threads, a LinkedIn page) the same way. ByteVibeHQ is the public studio and creator identity; link it clearly to the SIR products and to Ahmed (sirahmed8), with one consistent name, bio, avatar and set of links. SIR Content Creation Studio (or whichever project the inventory shows was built for this) becomes the engine.

- **Strategy:** use the installed social-media and marketing skills for brand voice, content pillars, hooks, scripts and a 30-day calendar. Topics: building the SIR products, dev tips, AI automation, behind the scenes, launches and real results. Arabic first, English second. Each platform gets its own plan:
  - **TikTok, Instagram Reels, Facebook Reels and Snapchat Spotlight:** short vertical videos (one master edit, re-cut and re-captioned for each platform).
  - **Instagram and Facebook posts:** carousels, product screenshots, release notes.
  - **X:** short threads, build-in-public updates, useful replies in developer conversations.
  - **Reddit:** genuinely useful posts and answers in relevant communities. Read each community's rules first, respect its self-promotion limits, and never post the same thing across many communities.
- **Organic growth first.** There's no budget for paid "boosts"; they come later from real earnings (8.0 ladder), and only on posts that already perform well organically.
- **Production:** short videos, carousels, thumbnails and captions, made with free and local tools where possible: Remotion and ffmpeg for video, local speech-to-text (Whisper) for captions, local text-to-speech for voice-overs, screen recordings of the real products, free design tools. Licensed or royalty-free music only. Never use a real person's face or voice without their permission.
- **Profile setup** (bio, photo, links, highlights) through Claude in Chrome while Ahmed is signed in.
- **Publishing, in this order:**
  1. The platform's official API, for example through a self-hosted open-source scheduler such as Postiz (free, uses the official APIs; check which platforms it supports). Some APIs need app review before public posting, and X's API may charge for posting.
  2. The platform's own scheduling tools (Meta Business Suite for Instagram and Facebook, TikTok's web scheduler).
  3. **Browser posting** (Ahmed's standing instruction): where no API route works, Claude in Chrome opens the platform's website in his signed-in Chrome and uploads the post the way a person would. Before using it on a platform, read the platform's current rules and record the risk in an ADR. Skip it where the rules explicitly threaten suspension for scripting the website: X's automation rules do, so on X use its API, or list the post for Ahmed as a one-minute manual post.
- **Safeguards for browser posting:** his own accounts and original content only; a human pace (a few posts a day per platform, spaced out); stop at any CAPTCHA, verification or warning and list it for Ahmed, never work around it; never automate likes, follows, comments or DMs; keep a posting log with the live link and a screenshot; if a platform limits or warns the account, stop browser posting there and switch to manual uploads. Scheduled posting needs the laptop on and Chrome running (Phase 1.12 routines).
- **Calendar and veto:** the week's calendar appears in the daily report at least 24 hours ahead, and posts go out on schedule unless Ahmed vetoes one (silence means approved), so nothing waits for him.
- **Labels:** mark AI-generated or AI-edited realistic media wherever a platform requires it.
- **Community:** reply to comments and messages as ByteVibeHQ, honestly and helpfully. Never pretend to be a customer, never argue, and put anything sensitive on Ahmed's list. No bots, no follow/unfollow tricks, no automated mass DMs, no fake engagement or bought followers: those get accounts banned.
- **Exports project:** a clean output home, `D:\Projects\SIR Media\` (or a folder inside the Content Studio; decide in Phase 3):
  - `brand/` (logos, fonts, colors, voice) · `templates/` · `campaigns/<YYYY-MM>-<name>/` (brief, scripts, sources)
  - `exports/<platform>/<YYYY-MM>/<YYYY-MM-DD>-<slug>/` holding the final file, `caption-ar.txt`, `caption-en.txt` and `metadata.json` (platform, aspect ratio, duration, hashtags, music license, status, post URL)
  - `raw/` is temporary. Disk is tight, so finished campaigns are archived to Google Drive and local raw footage is removed after the archive is verified.
- **Analytics loop:** weekly performance review that feeds the next calendar.

**8.3 Jobs agent: find paid work, do it, and build things that earn.** `D:\Projects\Jobs` already holds Ahmed's CV and job material; it becomes the home for this work. Ahmed wants an agent that works the way he would: it finds work it can do, does it to the SIR standard, and finds or builds projects that bring money in.

- **Foundations:** polish sirahmed8 (GitHub profile, portfolio site, pinned repos with live demos); a one-page ATS-friendly CV in English and Arabic; LinkedIn profile copy; profiles and gigs on platforms that are free to join (Khamsat, Mostaql, Fiverr and similar; skip anything that charges to apply).
- **Find work, every day:** search jobs and freelance requests (Indeed MCP, Wuzzuf, LinkedIn, Mostaql, Khamsat, Upwork, Fiverr requests) through official tools or normal browsing. The job-feed scorer (7.4) ranks each one by fit, pay, time to deliver and client quality.
- **Apply and win:** a tailored proposal or cover letter for each good match. The agent sends it itself where the platform allows that; where the terms forbid automated applying (LinkedIn and some others), it leaves the application ready and lists it for Ahmed. Never invent experience, skills or reviews.
- **Do the work:** each accepted job gets a folder in `Jobs/clients/<client>/` with the brief, a plan, deliverables built and reviewed to the SIR standard, and a delivery note. Deliver on time, handle revisions, track payment. Use AI help only where the client allows it, and say so honestly if asked.
- **Build income that runs on its own:** every week, look for one small product the team can build and sell with no upfront cost, judged by evidence of demand, time to first income, reuse of existing code, and platform rules: website packages for local businesses, templates and starter kits, n8n workflow packs, browser extensions, small paid tools or micro-SaaS on the the shared standards kit, digital study and productivity packs. Build the best one, launch it, measure it, and drop it if nothing sells within a month.
- **Off-limits:** academic work other students would hand in as their own, fake reviews or accounts, spam, and anything that breaks a platform's terms.
- **Tracking:** an application and client tracker plus an income ledger in `Jobs` (real numbers only), shown in the Command Center.

**8.4 Company.**

- Business plan, brand book, pricing.
- Service contract templates, marked "review with a lawyer".
- An Egypt company-formation checklist (verify current requirements for Ahmed's situation with GAFI or an accountant). Keep income records from the first payment, for taxes.
- A sales kit for SIR Business: demo videos, one-pager, pitch deck, pricing sheet.

**8.5 Weekly business report:** what shipped, what was posted, leads, applications, revenue against the 1,200 EGP target, next week's plan.

**8.6 Obour Institute study assistant** (`study-coach`; rule 14 applies).

- Homes: `D:\Projects\Obour Institute Second Year 1st term` and the Obour Institute folder in Google Drive (find it). Keep both in the same structure: `<course>/{syllabus, lectures, sheets, assignments, past-exams, study-kit}`.
- Ahmed signs in to the institute site himself; Claude in Chrome then downloads course materials. Never store his password in files.
- Clean up: consistent file names, duplicates removed, everything filed per course and synced to Drive.
- Deadlines (assignments, quizzes, exams) go into TickTick and the calendar, with reminders.
- Per course, a study kit: summaries, key concepts, worked examples, Anki-ready flashcards, practice quizzes, and a revision plan before each exam. Explain anything on request.
- Assignments: guide, explain, and review Ahmed's drafts with feedback. Don't take graded quizzes or exams for him, and don't produce work he'd submit as entirely his own unless the institute allows that kind of AI help.

**8.7 `Learning` and `AI_Models_Hub`.** Inventory both. Organize `Learning` into tracks with a progress tracker. `AI_Models_Hub` likely holds large model files: report sizes, move exact duplicates to quarantine (never delete them), and make it Ollama's single model folder.
