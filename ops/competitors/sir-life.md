# Competitor study: SIR Life (daily life OS, prayer-aware routines and habits)

Category: Muslim daily companion apps, habit trackers, task managers, food and water trackers, wellness apps.
Research date: 2026-11-12. Method: official pages opened directly (webfetch) on 2026-11-12, app store listings and official help or pricing pages, plus the earlier SIR Life benchmark already in `plans/sir-life-DEEP.md`. Nothing below was tested as a user; every strength and flaw is read from the vendor's own public pages, so treat it as "what the vendor claims" or "what the page shows", never as an audited fact.

Truth rules for this file:

1. Every number that belongs to a competitor is their own claim or a listed price, written as such. We did not verify a single user, streak, prayer calculation or health record.
2. Anything not read on a page we opened today is tagged "(unsourced, verify)" and must not be copied into public copy, a store listing, a legal page or a comparison page.
3. Competitor prices are third-party prices. Our prices are a different thing: see `plans/sir-life.md` section 7.
4. No assets, text or code are copied from any competitor.

Canonical file for SIR Life. The older `plans/competitors/sir-life.md` (r44, 2026-11-10) is superseded by this file and must not be quoted as current.

---

## 1. The ten that matter

| # | Competitor | Market | What it is | Strengths (from its own pages) | Flaws (from its own pages) | Our edge | Ideas to steal | Source |
|---|---|---|---|---|---|---|---|---|
| 1 | Muslim Pro | Global, Egypt included | Prayer times, Qibla, Quran, dhikr, mosque finder, AI features, verified prayer times | Very complete daily Muslim toolkit: prayer alerts, Qibla, Quran reading, dhikr counters, events, verified times option, widgets, calendar export, in-app support for prayer calculation questions | Free tier is ad-supported and carries a large premium upsell surface; exact Premium price was not readable on the pages opened today "(unsourced, verify)"; feature-dense rather than calm; health-style reminders are not the centre | A calmer daily routine, not a content library; local-first private data; no ads; prayer-aware habits that respect quiet hours; EGP-first fair pricing | Verified-times option, Qibla, dhikr counter, fasting countdown, calendar export, widgets | https://support.muslimpro.com/hc/en-us/articles/360007233392-What-Are-the-Features-of-Muslim-Pro (opened 2026-11-12) |
| 2 | Athan (Prayer Times) | Global | Prayer times app with Quran, athkar, dhikr, goals, widgets and Qibla | Strong native-app feel: prayer notifications, home screen widgets, Quran and adhkar, habit goals and streaks, Qibla direction, customization of sounds and appearance, Arabic support | Positioning is an Islamic utility app, not a life organiser; subscription and in-app purchase details were not readable on the opened pages "(unsourced, verify)"; no expense, food, gym or medicine modules | One daily screen that plans the whole day around prayer instead of only alerting for it; Arabic-first Egyptian copy; local data; bundled life modules | Widget prayer row, goal streaks, customizable alert sounds, dhikr counter | https://play.google.com/store/apps/details?id=com.islamic.athan and https://apps.apple.com/us/app/athan-prayer-times-quran/id704447617 (opened 2026-11-12) |
| 3 | AlAdhan API | Global data source, not a consumer app | Open prayer-time calculation API and client libraries | Important as a best-in-class data reference: multiple calculation methods including Egyptian General Authority, Umm al-Qura, Muslim World League, ISNA and more; Hijri calendar, Qibla and Sunnah times in one API; client SDKs for several platforms | It is infrastructure, not a product: no reminders, habits, food, expenses, accounts or UX; self-hosted or hosted limits and terms were not fully read today "(unsourced, verify)" | We can use it to validate our own calculation engine and as an offline reference, while keeping the runtime independent so users are not locked to one API | Method list, calculation parameters, Hijri conversion, Qibla bearing math, client SDK patterns | https://aladhan.com/prayer-times-api and https://aladhan.com/calculation-methods (opened 2026-11-12) |
| 4 | Habitica | Global | Gamified habit and task manager with social quests | Habit and todo tracking with XP, levels, parties, guilds, boss battles and pets; free tier exists with optional subscription; strong habit-history visualisations | RPG framing can feel childish for a prayer-aware life tool; guilt and punishment mechanics can hurt consistency; no prayer times, Quran, food, expenses or Arabic-first local data | Forgiving streaks with rest days and freezes; private by default; Arabic-first; connects habits to prayer and daily routine instead of a game avatar | Habit history heatmap, party accountability later, free core with fair paid sync | https://habitica.com/static/features and https://habitica.com/static/pricing (opened 2026-11-12) |
| 5 | Streaks | Apple ecosystem | Premium habit tracker, one-time purchase | Beautiful, focused design; 24 tracked habits; Apple Health and Watch integration; one-time App Store price listed at $5.99 | Apple-only: no Android, Windows, Linux, web or PWA path found on the opened pages; no prayer, Quran, expenses, food or medicine; small habit cap | Cross-platform from one codebase; Arabic-first; broader life modules; local-first with optional encrypted sync; fair subscription only for sync and backup | One-time-price honesty, clean habit cards, Health-style integrations later | https://streaksapp.com/ and https://apps.apple.com/us/app/streaks/id963034692 (opened 2026-11-12) |
| 6 | Fabulous | Global | Coaching-style routines and habit journeys | Strong onboarding and routine structure; daily coaching, journeys, community and reminders; subscription model is explicit on the App Store listing | Premium auto-renewing subscription is the main path "(unsourced, verify)" for exact price; coaching content is cloud-delivered rather than private local data; not Arabic-first | Free core routines that stay useful offline; no dark-pattern countdowns; user data stays on device unless they choose sync; Egyptian Arabic copy | Routine builder, daily plan structure, gentle coaching prompts | https://apps.apple.com/us/app/fabulous-habit-tracker/id985873238 and https://www.fabulous.co/ (opened 2026-11-12) |
| 7 | Todoist | Global | Task manager with reminders, projects and a habit extension | Mature task model, cross-platform clients, natural-language quick add, reminders and integrations; Habit Tracker extension adds streaks to tasks | Habits are an extension rather than a first-class forgiving system; no prayer times, Quran, health or expense modules; pricing is USD-first; streaks can reset sharply when a task is postponed | Habits are native, prayer-aware and forgiving; Arabic-first; one place for routine, tasks, water, medicine, food and expenses; EGP pricing | Quick add, natural-language dates, projects/labels, reliable reminders | https://todoist.com/pricing and https://todoist.com/features/habit-tracker (opened 2026-11-12) |
| 8 | TickTick | Global | All-in-one tasks, calendar, habits, pomodoro and notes | Very broad feature set: lists, kanban, calendar, habits, pomodoro, countdowns, Eisenhower matrix, AI assistant; Premium upgrade page lists a yearly price | Premium gates advanced habit and countdown power features; free tier limits habit count; still task-first rather than prayer-and-health-first; Arabic quality not verified today "(unsourced, verify)" | More core habits free; prayer-aware daily planner; health modules; Arabic-first Egyptian copy; local-first privacy | Eisenhower matrix for weekly review, countdowns for exams and bills, pomodoro inside focus mode, kanban for habit projects | https://ticktick.com/features and https://ticktick.com/upgrade (opened 2026-11-12) |
| 9 | Headspace | Global | Meditation, sleep, stress and coaching app | Strong content library for meditation, sleep, stress and focus; official annual pricing page lists a subscription | Subscription-led; annual price shown on the sleep page was $69.99 at read time, main plan pricing should be rechecked "(unsourced, verify)"; content app rather than personal tracker; account and cloud model | Calm tools that work offline and private: breathing, meditation timers, sleep sounds, eye rest, journaling; AI optional and off by default; no required content subscription | Sleep stories later, breathing patterns, focus sounds, daily check-in prompts | https://www.headspace.com/sleep and https://www.headspace.com/ (opened 2026-11-12) |
| 10 | MyFitnessPal | Global | Food, calorie, macro, water and exercise tracker | Huge food database, barcode and voice logging, macro and nutrient tracking, exercise logging, Premium tier | Premium annual price listed at $79.99 on the official blog; free tier is ad-supported; database is US-centric; health data lives in a cloud account; not prayer-aware | Local-first food and water log with Arabic-friendly entry later; bundled with prayer routine rather than another subscription; export and delete always available; no medical claims | Barcode logging later, macro rings, water reminders, exercise log | https://blog.myfitnesspal.com/myfitnesspal-premium/ and https://www.myfitnesspal.com/ (opened 2026-11-12) |

### Second ring found on 2026-11-12, kept for the record

| Competitor | Note | Link |
|---|---|---|
| Loop Habit Tracker | Open-source Android habit tracker; useful as a reference for streaks, widgets and reminders. Claims not audited today "(unsourced, verify)". | https://github.com/iSoron/uhabits |
| Daylio | Mood and activity journal; relevant to the mood/energy journal module. Pricing and features "(unsourced, verify)". | https://daylio.net/ |
| WaterMinder | Water reminder app; relevant to the water module only. Features "(unsourced, verify)". | https://waterminder.com/ |
| Pillars | Muslim habit and prayer app mentioned in earlier SIR Life research; pages not opened today "(unsourced, verify)". | https://pillars.app/ |
| Athan Pro / Muslim Pro widgets | Widget and complication patterns matter more than the apps themselves; verify before copying any visual asset. | App store listings above |

---

## 2. What the category actually looks like

Read from the pages opened on 2026-11-12, not from an aggregator.

1. **Muslim apps are feature-dense, not calm.** Muslim Pro and Athan prove that prayer times, Qibla, Quran, dhikr, widgets and notifications are table stakes. They also show the clutter risk: the daily life organiser must be quieter than the content library.
2. **Habit trackers sell streaks, we should sell forgiveness.** Habitica gamifies habits, Streaks makes them beautiful, Todoist and TickTick attach them to tasks. None of the opened pages showed a prayer-aware, health-aware, forgiving streak model as the centre of the product.
3. **The best habit UX is small and disciplined.** Streaks proves a small habit set can feel premium. TickTick proves breadth is possible but pushes power features behind Premium. SIR Life should be broad but keep the daily screen small.
4. **Food and water are separate subscriptions elsewhere.** MyFitnessPal proves users accept a paid tracker for food. Our edge is not a bigger food database on day one; it is one calm place for prayer, habits, water, medicine, food and expenses without five subscriptions.
5. **Arabic-first is still under-served.** The opened competitors are global-first. Egyptian Arabic copy, RTL-first layout, EGP pricing and Cairo prayer defaults are real differentiation, not decoration.
6. **Local-first privacy is the gap.** None of the opened consumer pages made "health and daily data stays on this device unless you choose sync" a headline. For a product that tracks prayer, medicine, food and mood, that is the trust promise.

---

## 3. Our edge, stated as five promises

1. **A calm daily screen, not a feed.** Today shows prayer times, the next task, habits due, water and medicine reminders, and one reflection prompt. Everything else is one tap away.
2. **Prayer-aware without being preachy.** Prayer times shape the day plan, adhan alerts respect quiet hours, fasting countdown appears only when relevant, and religious text is cited rather than invented.
3. **Forgiving consistency.** Habits use rest days, freezes and "keep going" states instead of shame mechanics. A missed day is data, not a failure narrative.
4. **Private by default.** Local storage first, optional encrypted sync, no ads, no location tracking beyond a chosen city, health data never used for ads or sold.
5. **One fair subscription.** Free covers the daily organiser; Pro covers encrypted multi-device sync, backup, Telegram quick logging and priority support. EGP-first pricing with USD support, and "Subscriptions launching soon" until payment keys exist.

---

## 4. Sourcing tasks still open

Each under one hour; none blocks the plan, all block public claims.

1. Recheck Muslim Pro Premium price on its official pricing page and record the number with a link and date.
2. Recheck Headspace main subscription price; the $69.99 seen today was on the sleep page.
3. Recheck Fabulous and Athan subscription or IAP details on their official pages.
4. Read the Pillars app pages and decide whether it belongs in the main ten or stays second ring.
5. Check App Store and Google Play ratings and review counts for the main ten, and record them with dates before any comparison page is written.

---

## 5. Second pass, 2026-11-12 evening (what is new)

Same truth rules as section 0: pages opened today, vendor claims are vendor claims, anything unread is "(unsourced, verify)".

### 5.1 Muslim Pro moved while we were not looking

- Premium is now a bundle: Muslim Pro Premium monthly/yearly includes Qalbox streaming (launched 2022, now the main subscription story) on up to 5 devices for the bundle tier, 2 devices for Muslim Pro-only Premium, and a cheap "No Ads" single-device tier exists. Exact EGP/USD prices were not readable on the opened pages "(unsourced, verify)".
- New in-app AI: "AiDeen", an Islamic Q&A bot answering from Quran and hadith. This is the first major prayer app shipping a religious AI assistant; SIR Life's rule stands - no AI-generated religious text, cited sources only - so this is a differentiation point, not a gap to copy.
- Gamification added: visible prayer/fasting streaks plus "Quests" earning Stars & Crescents. The whole Quran (text, tajweed, memorisation tool, khatam tracker) is now free; Premium adds reciters and offline audio.
- Source: https://www.muslimpro.com/features/, https://www.muslimpro.com/holy-quran-app/, https://support.muslimpro.com/help/en/articles/what-is-the-difference-between-the-free-and-premium-versions-of-muslim-pro (all opened 2026-11-12).

### 5.2 The "life around the salah" positioning is now occupied

Two products opened today already sell the exact frame SIR Life planned:

| Product | What it does (from its own pages today) | Where it beats us | Where it loses |
|---|---|---|---|
| Sahibukum | Prayer times verified from official bodies (MUIS, Kemenag, JAKIM marked "Official"), Qibla with AR mode, halal label scanner (5,732 labels tested claim), Seerah, Regimen planner placing habits/tasks inside prayer windows, Privacy PIN that encrypts Regimen on-device before sync, 12 languages, no ads, no subscription for basics | Privacy PIN + on-device encryption before sync is the closest thing to our local-first promise; prayer-window planning is exactly our Today screen idea | No medicine, expense, food or gym modules; Muslim-only audience; tiny install base (3 App Store ratings) |
| Barakah Planner | "Plan with Purpose": niyyah on tasks, Quran streaks, adhkar, prayer alerts, family shared tasks/lists, medication smart lists, reflections; iOS + Android; free tier + paid | Family features and medication lists we do not have | No local-first privacy claim found, no Arabic-first evidence, subscription-gated breadth |
| Salah Home | Gamified: every prayer earns Dates to build a virtual home; gentle streaks, no punishment | The "forgiving streak" emotion we want, executed as a reward loop | Prayer-only scope, iOS-first, gamified rather than calm |
| Just Pray | 4.9 stars claim, prayer tracking, streaks, "Garden of Deeds", Prayer Focus mode that pauses distracting apps, AI prayer coach | App-blocking at prayer time is a feature we lack; AI coach answers fiqh | Single-focus product, no life modules |
| Deeny / Salah Focus | Lock chosen apps during each adhan until the user confirms they prayed | Phone-friction design for prayer consistency | Single-feature utilities |
| Islamic Tracker | Free no-ads tracker: prayers, Quran, dhikr, zakat, Qibla, streak analytics | Free-no-ads positioning we share | No life modules, narrower |

Sources opened 2026-11-12: https://sahibukum.com/app/, https://sahibukum.com/features/, https://sahibukum.com/compare/islamic-habit-tracker/, https://www.barakahplanner.app/, https://salahhome.com/blog/best-salah-habit-building-apps, https://justprayapp.co/blog/top-10-muslim-prayer-tracker-apps, https://www.islamictracker.com/best-islamic-app.html.

### 5.3 What this means for SIR Life (added to the plan, section 15)

1. "Prayer-aware daily planner" is no longer unique - Sahibukum Regimen and Barakah both do it. The surviving edge is the non-faith half: medicine, water, food, gym, expenses and mood for a daily life, usable by anyone, not only Muslims. Positioning must lead with "your whole day, organised", with prayer as one pillar - not "an Islamic planner".
2. Local-first + encrypted-on-device sync is now table stakes for the privacy claim (Sahibukum Privacy PIN proves users respond to it). Our opt-in per-category sync must be at least as strong and explained in one sentence on the privacy page.
3. Verified/official prayer times matter: Sahibukum badges official timetables. Egypt has an official General Authority timetable - we should source Cairo times officially where possible and show the method, matching the plan's "no invented times" rule.
4. App-blocking/Focus at prayer time (Just Pray, Deeny) is a cheap, loved feature worth a later task.
5. Nobody in the opened set does expenses + medicine + food + gym + mood in one calm local-first app with Arabic-first copy and EGP pricing. That bundle remains the differentiator.
