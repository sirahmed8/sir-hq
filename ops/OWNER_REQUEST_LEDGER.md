# Owner request ledger (built 2026-11-11 from all 136 messages of the HQ chat)
One line per distinct request or standing rule. Status is what files show today, not what a chat claimed: DONE (file or script exists and is referenced), PARTLY, OPEN, RULE (standing rule, lives in a law file), DECLINED (blocked by a rule, with the reason). Column "Captured" says where it lives; **NOT CAPTURED** means no plan, brief, queue entry or project TASKS line carries it yet (grep over ops, briefs, plans, standard and the `.sir` folders of SIR AI, Portfolio, Jobs, Laptop, Study on 2026-11-11). Status of "done" is unverified by a reviewer unless stated. No private data is recorded here. AHome items are kept at category level only (its details stay in the AHome repo).

## A. How HQ and agents must work (rules)
| Date | Request | Status | Captured in |
|---|---|---|---|
| 10-29 | Remove the "only Ahmed can do" section; agents do those things | RULE | AGENTS.md laws, `ops/OWNER_ACTIONS.md` |
| 10-29 | Every project: new name, new private repo, plan from zero; legacy kept as source; HQ prepares, one chat per project builds | RULE | AGENTS.md, `plans/MASTER_REBUILD_PLAN.md` |
| 10-30 | Never delete `legacy\`; each project deep-scans and improves its plan first | RULE | AGENTS.md, `plans/AGENT_PROTOCOL.md` |
| 10-30 | Only AHome/Habiba data is private; keys may be handled and rotated by agents | RULE | AGENTS.md "Security and privacy" |
| 10-30 | Agents use the computer, Chrome and apps for any task; figure it out | RULE | `plans/COMPUTER_USE.md` |
| 10-30 | Projects talk to each other and all know the main plan | DONE | `ops/bus/`, `plans/MAIN_PLAN.md` |
| 10-30 | Subagents with model and effort chosen by task level | DONE | `plans/MODEL_ROUTING.md` |
| 11-01 | No pull requests; merge to main | RULE | AGENTS.md |
| 11-07 | Claude is manager and reviewer; Antigravity builds; no stopping; manager also invents tasks | RULE | AGENTS.md "Who does what" |
| 11-07 | Owner-actions list more free: agents act, not ask | DONE | `ops/OWNER_ACTIONS.md` rewritten 11-11 |
| 11-08 | Agents never stop; only usage stops them; find bugs by themselves | RULE | `plans/PERPETUAL_LOOP.md` |
| 11-08 | Real improvements every round, not "tests pass" | RULE | `plans/IMPROVEMENT_DOCTRINE.md` |
| 11-09 | Everything stays at version 1.0.0 | RULE | AGENTS.md |
| 11-09 | Nothing is "working" until verified; projects start from zero | RULE | AGENTS.md truth rule |
| 11-09 | Premium Gemini quality from any model | RULE | `plans/GEMINI_QUALITY_CHARTER.md` |
| 11-09 | Review every project at all screen sizes and all files, then fix, clean, improve | RULE | `plans/IMPROVEMENT_DOCTRINE.md` |
| 11-09 | AHome exempt from commercial/legal standards but best quality | RULE | AGENTS.md |
| 11-10 | Manager sees all projects (one HQ folder), agents get full access; no approval gates | PARTLY | AGENTS.md, `plans/AI_TOOLS_CONTROL.md`; GLM full-access setting is his, not HQ's |
| 11-10 | Telegram messages for all agents: clean, short, organized | DONE | `ops/WORKER_PREAMBLE.md` rule 12 |
| 11-10 | Think like me, take initiative, suggest, think outside the box | PARTLY | this method file, `ops/DAILY_RHYTHM.md`; behavior, needs daily proof |
| 11-11 | Manager analyses how he thinks and puts it in plans for SIR AI and the next manager | DONE | `plans/OWNER_METHOD.md` v2, `ops/briefs/r25-sir-ai.md` |
| 11-11 | Work on several projects at once, not one | PARTLY | queue runs 2 at once (LOW_USAGE_MODE); tension with his wish, not decided |

## B. Models, accounts, usage
| Date | Request | Status | Captured in |
|---|---|---|---|
| 11-07 | Use AgentsRoom, then retire it; Claude manages, Antigravity builds | DONE | `ops/AGENTSROOM_RETIRED.md` |
| 11-08 | Haiku (low effort) drives the screen, switches accounts, presses continue/retry, checks once for all | DONE | `plans/ANTIGRAVITY_OPERATOR.md`, `ops/ACCOUNT_ROTATION.md` |
| 11-08 | Switch accounts proactively; track each reset in a ledger | DONE | `ops/ACCOUNT_LEDGER.md`, `ops/agy-accounts-usage.md` |
| 11-09 | Order: Gemini 3.8 on Pro, then free accounts, then Argon/Claude 5.5 account, OpenCode/Kilo, Codex late, HQ last; never Claude 4.x | DONE | `ops/ACCOUNT_ROTATION.md` |
| 11-09 | Find and install more free CLIs (Devin, GLM/ZCode, Windsurf, others) | PARTLY | Devin and ZCode installed (HQ_CHECKPOINT); Windsurf never mentioned: **NOT CAPTURED** |
| 11-09 | Remind him the best moment for the weekly Claude Reset | DONE | scheduled task SIR_Reminder_Claude_Reset (Wed 13:00) |
| 11-09 | Background services must survive closing Antigravity/Claude | DONE | `scripts/hq_autopilot.py`, `scripts/install-hq-tasks.ps1` |
| 11-10 | When free tools run out, manager continues with Sonnet/Haiku; sign out and use the 19 accounts across two Chrome profiles | PARTLY | ACCOUNT_ROTATION "How switching happens without the owner"; needs reliable Haiku run |
| 11-10 | Read when ChatGPT/Codex monthly quota renews (Haiku opens ChatGPT) | OPEN | Codex date is an open promise in HQ_CHECKPOINT; the ChatGPT renewal check: **NOT CAPTURED** |
| 11-11 | When GLM free quota ends, reassign what it was doing to another worker | OPEN | Queue still lists GLM-era tasks; reassignment not written: **NOT CAPTURED** |
| 11-11 | Tell sub-agents to continue after the 5-hour reset and self-prompt | PARTLY | autopilot, `ops/hq_manager_tick.py` |

## C. Automation, laptop, background jobs
| Date | Request | Status | Captured in |
|---|---|---|---|
| 11-08 | Smart wake-up for the manager when work finishes | DONE | `scripts/smart-wake.sh`, `hq_autopilot.py`, `hq_watchdog.py` |
| 11-09 | No flashing CMD windows anywhere | PARTLY | `scripts/run-hidden.vbs`, brief r22-laptop; needs on-screen proof |
| 11-09 | Open Claude, Antigravity, Chrome at boot; close all when a game from D:\Games starts; reopen after | PARTLY | `SIR Laptop Manager/.sir/GAMES_TUNING.md`, brief r24-games; unverified |
| 11-09 | Laptop Manager: safe disk cleanup, empty folders, caches | PARTLY | `scripts/pc-cleanup-tier1.ps1`, `ops/PC_CLEANUP_DRYRUN.md`; C: and D: still nearly full (OWNER_ACTIONS) |
| 11-09 | Update all programs and CLIs, retry on errors | OPEN | `ops/briefs/queued-laptop-updates.md` (queued, not run) |
| 11-10 | Restore the listener, smart alert and reminder counter as background tasks | DONE | `scripts/deliver/*`, `ops/telegram-listener.log` |
| 11-10 | Disk-low Telegram message needs a clean-up button and quick-reply buttons | PARTLY | r12/r15 laptop briefs; end-to-end tap not verified |
| 11-10 | Telegram bot with tap buttons for status, queue, clean disk, approvals | DONE | `ops/telegram-actions.json`, `scripts/deliver/send-buttons.mjs` |
| 11-11 | Stop the sound that started playing on the laptop (a court/law recording) | OPEN | **NOT CAPTURED** (no brief, no note) |
| 11-11 | Recurring duties must be OS jobs, not Claude crons, so closing Claude does not stop them | PARTLY | `SIR_HQ_Duties` done; WhatsApp digest still a chat cron (DAILY_RHYTHM) |

## D. Personal assistant (Telegram, WhatsApp, mail, TickTick, health)
| Date | Request | Status | Captured in |
|---|---|---|---|
| 11-08 | All projects report to him in Telegram in short Arabic | DONE | `scripts/deliver/send-telegram.mjs`, AGENTS.md |
| 11-09 | SIR Jobs sends only NEW jobs | PARTLY | Jobs r15/r16 briefs; recheck after r24 |
| 11-09 | Watch WhatsApp, Telegram, class groups, email; reply drafts; one-tap approval | PARTLY | `plans/INBOX_ASSISTANT.md`; digest as chat cron every 2 h |
| 11-10 | Follow all cohort/department groups, archived groups, work-recording groups and job groups, summarise the week | PARTLY | DAILY_RHYTHM mentions "batch groups, archive, work and job groups"; per-group list not written |
| 11-10 | Read his notes except the "Accounts" note; use the "Habobty" project too | OPEN | rule in DAILY_RHYTHM; Habobty project: **NOT CAPTURED** |
| 11-10 | Update TickTick tasks and plans with current work and what is new | OPEN | HQ_CHECKPOINT line "owner request, not started"; not in queue |
| 11-10 | Create the OAuth client ids (TickTick, Google Tasks) himself, not asked of Ahmed | DONE | OWNER_ACTIONS item 2 (ids in a local ignored file) |
| 11-10 | AHome app connections must work on tap (link account) | PARTLY | brief r21-ahome; needs on-device proof |
| 11-11 | Day from Fajr to Isha on real prayer times: Fajr plan, Isha summary, health/sport check-ins | DONE | `ops/DAILY_RHYTHM.md`, `scripts/hq_duties.py`, `ops/duties/` |
| 11-11 | Be a personal advisor: suggest videos, articles, tools, habits, not only report | PARTLY | DAILY_RHYTHM "one outside recommendation"; quality unverified |
| 11-11 | Job messages must also reach Telegram (not only a local file); first-round applications with preliminary acceptance | PARTLY | `ops/briefs/r24-jobs-apply.md` (queued) |
| 11-11 | Real weekly income target researched, not the old 1200 EGP guess | OPEN | brief r24 item 8 -> `SIR Jobs/.sir/INCOME_MODEL.md` |
| 11-09 | Ask Haiku to do lectures/quizzes on the college portal | DECLINED | graded work is Tier 3; only a read-only digest of uploads is allowed (AGENTS.md) |

## E. Products and quality (screens, motion, structure)
| Date | Request | Status | Captured in |
|---|---|---|---|
| 11-08 | AHome: round of UI/UX fixes from screenshots (motion in the composer, sheets, tabs, banners, merge pages) | PARTLY | `AHome/.sir/R14_CHECKLIST.md`, briefs r18/r21; details private |
| 11-09 | Telegram bot messages: simple, no tech talk, better replies, no emoji | DONE | WORKER_PREAMBLE rule 12 |
| 11-09 | PDF reports ordered, no half-empty pages | OPEN | **NOT CAPTURED** (no brief names it) |
| 11-09 | Control Room fully Arabic when Arabic; model names current; artifact and local site identical | PARTLY | briefs r19/r22-control; artifact republish still an open promise |
| 11-09 | Each product: own icon, favicon, logo in the nav bar; desktop folder icons | PARTLY | `scripts/make-icons-and-desktop.ps1`; per-product check not done |
| 11-09 | No yellow buttons anywhere; fix cards, colors, spacing | PARTLY | brief r22-jobs/r22-study |
| 11-09 | Many settings go into a small settings window; many tabs into a simple side menu; RTL/LTR correct | RULE | `plans/LESSONS_UI.md`, r11 briefs |
| 11-09 | All tab bars: swipe between tabs, centered when few, sized to text | RULE | `plans/LESSONS_UI.md`, `IMPROVEMENT_DOCTRINE.md` |
| 11-09 | Update notice appears once and buttons work | PARTLY | AHome round briefs |
| 11-09 | Every site/app has a support AI and modern AI features that run it | RULE | `plans/OPERATIONS_PLAYBOOK_ALL.md`, `standard/` |
| 11-09 | Win-win subscriptions, ready to plug a paid domain, cloud and gateway | RULE | `standard/24-launch-package.md` |
| 11-09 | SEO and AI-answer visibility ahead of competitors for every product and for him | RULE | `plans/VISIBILITY_PLAN_ALL.md` |
| 11-09 | Legal pages by country; no fake data; every platform covered | RULE | `plans/MARKET_GRADE_CHECKLIST.md` |
| 11-09 | Negm Furniture: improve plans only, hand to the friend later | RULE | AGENTS.md |
| 11-09 | A new project per old product with new Firebase project and repo (rename if the name differs) | RULE | SIR AI checkpoint "Names (rule 13)" |
| 11-10 | Host every product on two hosts (Firebase and Vercel) so one failing leaves the other | PARTLY | Portfolio has `vercel.json` and `firebase.json`; `standard/03` names Cloudflare + Firebase: **NOT CAPTURED** as a rule |
| 11-10 | Deploy to hosts, install to the phone by adb, check GitHub errors after each AHome round | DONE | brief r18-ahome-phone (verified 27/27 by HQ 11-10) |
| 11-10 | Fingerprint/face unlock should detect the user and device and personalise | OPEN | AHome round; detail private |
| 11-11 | GPT-style tests: AHome next rounds with self-audit loop | PARTLY | brief r21-ahome |

## F. SIR AI, SIR Portfolio, LinkedIn
| Date | Request | Status | Captured in |
|---|---|---|---|
| 11-10 | SIR AI: general personal-assistant product (not private to him); Sonnet 5.5 agent works on it | PARTLY | `SIR AI/.sir/CHECKPOINT.md`, brief r25; M1 slice deployed, sign-in unverified live |
| 11-11 | Put the manager's way of working, CLIs and delegation into SIR AI plans | DONE | brief r25-sir-ai, OWNER_METHOD |
| 11-11 | SIR Portfolio: personal site with hosted links to all products, social numbers, contact, CV; Sonnet 5.5 agent | PARTLY | `SIR Portfolio/.sir/CHECKPOINT.md` (deployed, quality sweep) |
| 11-11 | Portfolio content: honest titles (software engineer / AI operator), remove GPA and invented activities, find NVIDIA MCP certificate in local files, robust reader of his local notes | PARTLY | Portfolio `content/` pipeline with 604 tests; each correction unverified: **NOT CAPTURED** as a checklist |
| 11-11 | LinkedIn profile rewrite using real info | DONE | OWNER_ACTIONS 04:40 (text only; English level, birthday, Arabic headline left to him) |
| 11-11 | LinkedIn: first public post, job-search settings and alerts, watch LinkedIn jobs, connect with important people and companies | OPEN | **NOT CAPTURED** (only a general line in `plans/MARKETING_PLAN_ALL.md`) |
| 11-11 | Link-tree and other socials: use later for Content Studio; do not touch now | RULE | noted in this ledger only |
| 11-11 | Verify the Vercel host for SIR AI and Portfolio, and a download/app location for SIR AI | OPEN | Portfolio has vercel.json; SIR AI Vercel and app locations not in TASKS: **NOT CAPTURED** |
| 11-11 | Start a ChatGPT-quota check (see B) | OPEN | **NOT CAPTURED** |

## G. One-off tasks he gave (older)
| Date | Request | Status | Captured in |
|---|---|---|---|
| 10-30 | Revoke old Telegram bot tokens, sign in to Cloudflare | PARTLY | archived OWNER_ACTIONS; token rotation is an agent job, current status unknown |
| 10-30 | Update TickTick notes and plans, except private family notes | OPEN | see D |
| 11-07 | Mods (dashboard) for the Control Room: any chat may improve it | DONE | `_SIR/mods/`, `ops/DASHBOARD_URL.txt` |
| 11-08 | Fix the two Control Room copies so both show the same truth | PARTLY | r19/r22 control; republish open |
| 11-09 | Give a prompt to the Laptop Manager chat to finish its old tasks | DONE | `ops/briefs/finish-all.prompt.txt` |
| 11-10 | Add the Control Room "Needs attention" refresh | DONE | `scripts/refresh-control-room.py` |

## Uncaptured open requests (for the manager to queue)
1. Stop the unknown audio playing on the laptop (find the process or tab, close it, add a guard in Laptop Manager).
2. ChatGPT/Codex renewal dates: have Haiku read both and write them in `ops/ACCOUNT_LEDGER.md`.
3. LinkedIn growth pack: first post draft, job alerts and filters that match a Vibe Coder profile, jobs watch, connection list of relevant companies and people (as drafts, he taps to send).
4. Two-host rule: every web product ships to Firebase Hosting and Vercel, with a check that both answer; add to `standard/03-data-backend.md` and each product TASKS.
5. Portfolio truth checklist: titles, numbers, certificate source (NVIDIA MCP), removed GPA and activities, reader robustness for messy notes; verify live.
6. Reassign everything the dead GLM/ZCode free quota was doing (Study r20, AHome help), and list which worker owns each project now.
7. TickTick refresh: current tasks and plans from the real project state (skip the Accounts note; include the Habobty project), through a Haiku or Antigravity operator.
8. Ordered, clean PDF reports (no half-empty pages) for the owner deliveries.
9. Windsurf (and any other strong free coding CLI): evaluate, install if free, add to the rotation; plus the "per-group WhatsApp list" (cohort, archive, work and job groups) so the digest covers every group.
10. SIR AI hosting and delivery: Vercel mirror, app/download locations, and the Telegram bot token owner step; then tell him exactly where the product lives.
| 11-13 | Keep D as is until tasks finish; then move space D->C via AOMEI; audit D and remove system/agent folders; keep tools at max throughput | OPEN | HQ_CHECKPOINT 03:05 note; r72-d-drive-org-plan queued (plan only) |

| 11-12 | Screenshot of "Ran 7 commands" modal (backup manager activation); confirm manager running and report state | DONE | this ledger; reply file |

| 11-12 | خلص اخر المهام الي بعتهالك ف التيلي هنا وخلي عندك context window لشات تيليجرام عشان تبقى فاهم الشات عادي | DONE | reply-739920726; backup manager reviewed recent chat context |
- 2026-11-12 21:15 voice: transcriber misses English words; asked about Telegram bot profile photo quality task -> queued r66-bot-profile-photo
- 2026-11-12 21:18 voice: wants clean organized Telegram message format, no symbols inside words; verify transcription is not hallucinating -> fixed whisper prompt bias + added reply cleaner in backup_manager.py

| 11-12 | Voice: transcription sometimes hangs, keep developing it; keep workers finishing tasks and queue new ones so they never run dry | DONE | backup_manager.py transcribe hard cap + interim message; queued r67-build-sir-portfolio and r67-voice-pipeline-verify |

- 22:05 Ahmed asked why messages arrive empty and why the ack has brackets; also asked progress on the 11 open tasks. Root cause found and fixed (see HQ_CHECKPOINT).
2026-11-13 02:30 | backup-manager | AHome mobile UI report (3 screenshots): avatar zoom slider broken, crop/zoom awkward, inputs hidden under keyboard, buttons broken, toggle knobs overflow. Queued r71-ahome-profile-editor-fixes to free agents.
2026-11-13 02:36 | backup-manager | Same report, source-level causes verified in AHome source and added to brief r71 so the free agent does not guess: slider painted by min-h-[44px] on a 4px range input, crop editor inline instead of a sheet, keyboard hook only in chat, toggle drag leaves an inline transform. Prompt regenerated, Cloudflare aider model cooled for the day.
| 11-13 | Ahmed freed space on C: (deleted FIFA), leave D: as-is until current tasks finish, then move space from D: to C: and clean/organize D:; run agents at max power and review everything | IN PROGRESS | queued r72-d-drive-org-plan (read-only D: audit + move plan); autopilot running r68 and r71 | 
2026-11-13 02:55 | backup-manager | Same report: implemented and pushed (AHome main 212af85): crop sheet is a real modal, pinch zoom + two-finger pan, rotation pan remap, keyboard screens keep scrolling with --kb room, toggle drag styles always cleared, duplicate dead CSS rule removed. tsc/eslint/9 node tests/next build green; local-core bot tests 14/14. 320/390 px dev-page screenshots in AHome .sir/evidence/r71-20261113 (gitignored). CI fails by quota flag not by code. On-phone check OPEN: phone was locked, installed APK is stale.
- 2026-11-14 00:15 | backup-manager | Ahmed: Hi | DONE | رد مختصر بالحالة الحالية (3 مهام شغالة، الطابور ماشي)
- 2026-11-14 01:35 | backup-manager | Ahmed: اي الدنيا | DONE | status reply; queued sir-ai-agentic-os-02 (phase 2 chat stream parser)
| 11-14 01:30 | backup-manager | Ahmed: اي الدنيا (status check) | DONE | ملخص حالة مختصر: الطابور خلص،مهمة جديدة اتضافت لـ SIR AI، والمساحة على C و D واصلت انخفاض |
- 2026-11-14 01:55 | backup-manager | Ahmed burst: AHome profile save broken, calling hardcoded (no ringing), video no camera, noise cancellation, GIF picker hardcoded categories/broken search/thumbnails, games XO plays self/no invite/notifications/cropped UI, Portfolio: remove SIR Negm Furniture -> Negm Furniture, SIR Obour Hub -> SIR Education Hub, navbar SP -> logo; SIR AI progress question | IN PROGRESS | queued r74, r75, r76, r77; SIR AI active (agentic-os-02, runnable-adapters-01)
