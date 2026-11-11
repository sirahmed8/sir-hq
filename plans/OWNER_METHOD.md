# How Ahmed thinks, decides and delegates (version 2, 2026-11-11)
Source: all 136 messages he typed in the HQ chat, 2026-10-29 to 2026-11-11 (read in full, screenshots counted by what he said about them). Audience: every manager after Claude (Antigravity, any CLI) and the SIR AI product ("think like him"). Companion files: `ops/OWNER_REQUEST_LEDGER.md` (every request with status), `ops/OWNER_STANDING_REQUESTS.md` (short digest), `AGENTS.md` (the laws). No private data of anyone is written here.

## 1. Who he is, in one paragraph
Ahmed is a second-year computer science student who builds with AI. He says it plainly: "أنا مش متخصص في ولا تراك، أنا بس فايب كودر بالاي اي". He is the owner and the boss of a large team of AI tools; he is not the worker. He talks in long, voice-like Egyptian Arabic (often dictated, with English tool names mixed in), sends 5 to 20 screenshots at once, writes late at night or from bed (he uses AnyDesk to watch the PC from his phone), and leaves for hours expecting to "find lots of things done". He pays for few things, so he treats usage limits like money and wants the system to hunt free quota by itself. His products are meant to earn money and to be a portfolio; one private project (AHome) is for him and his partner and is held to a different, higher privacy line.

## 2. The picture in his head (his mental model of the system)
1. **He is the Boss, nothing more.** "أنا بس اللي هو الرئيس اللي بيدير كل ال AI ده". He wants to be contacted only for "حالات طارئة جدا جدا جدا", and only through Telegram.
2. **HQ manager (Claude now, "the one after you" later: probably Antigravity) = his deputy.** Thinks for him, assigns, reviews, keeps the plan, hands over cleanly. Not a builder (since 2026-11-09), but may use its own subagents and may use any tool to remove a blocker.
3. **Builders = a pool of tools ranked by cost.** Antigravity (Gemini 3.8) first, then free CLIs (Kilo, OpenCode, Devin CLI, ZCode with GLM), Pro accounts after resets, Codex, and Claude last because its usage burns in minutes. He counts accounts (19 free ones across two Chrome profiles) and expects them to be used up one after another, with the manager switching accounts and profiles itself (a Haiku operator on the screen).
4. **Haiku (lowest effort) = the hands.** It drives the screen so expensive models do not. It must be smart enough to recover from a stuck box or a retry button without asking.
5. **Background automations on the laptop, not in a chat.** Everything recurring (Telegram listener, smart alerts, reminders, Fajr plan, watchdog, autopilot) must be a Windows background job that survives closing Claude or Antigravity, hides its windows, and pauses when he launches a game.
6. **Every product is a separate project with its own chat/agent,** its own name, icon, Firebase project and private repo, all rebuilt from zero in a shared family look. The manager sees all of them; project agents see their own.
7. **Telegram is the only channel to him,** in short clean Arabic. The Control Room page is his dashboard and must match reality.
8. **The end state:** products that run themselves with AI (support bot, AI features, marketing, SEO), subscriptions that are fair to users, and he only plugs in the paid domain, cloud and payment gateway.

## 3. How he decides (patterns that repeat)
- **End state first, details by screenshot.** He states the vision ("كل حاجة بتدير نفسها") and then finds 5 to 20 defects per screenshot. He never lists them all. A screenshot is a sample: find the siblings yourself ("انا عايز الاي يكتشفهم لوحده").
- **Cost-aware ordering.** Exhaust the cheapest/free source first, keep the strongest scarce model for last; switch accounts even if quota remains if that saves idle time ("No bro switch even if still there is quota"). He adjusts the order live when he learns something (an account holds Argon, one is a paid account, GLM stopped giving free quota).
- **He reasons aloud and corrects himself.** "Ask-me" is rare: he states a plan, then amends it a message later. Treat the latest message as the rule and merge it with older ones; do not ask which one wins unless they truly clash.
- **Parallel over serial.** "ليه نركز على مشروع واحد واحنا عندنا ادوات مجانية كتير؟ بدل ما نبطئ التقدم نسرعه". Six projects run together; the limit is quota and one writer per project, not attention.
- **Visible results beat green tests.** "ما هو طبيعي مش هيطلع اخطاء لان مفيش تعديلات على الكود". Each round must change something he can see (animation, layout, flow, backend logic) and be checked on screen.
- **He decides fast and reversibly,** and expects the manager to do the same: choose, log, continue. Reversible choices never wait for him.
- **Truth over flattery.** If something is not real or not finished, say so. He corrects hype ("المفروض كل المشاريع مفيش حاجة شغالة لان هنبدأهم من الصفر").
- **Spend where it matters.** Sonnet 5.5 for SIR AI and SIR Portfolio (his own words), free agents for the rest, Fable only when he chooses it. Context window size affects his choice of model, so tell him the trade-off in one line when it matters.

## 4. How he delegates
- **Gives outcomes, not steps.** "اتصرف", "فكر مكاني", "ما توقفش الا وانت مخلص", "ما تستناش مني برومت، اعمل برومت لنفسك".
- **Hands over authority completely.** Wants agents on full access, rules that stop an agent from continuing changed or deleted ("any rule that makes the agent stop, change it"), and owner-action lists kept tiny.
- **Wants a chain of command, not a messenger.** HQ writes the brief file, the project chat reads it, and HQ tells him only the one-line result. He does not want to paste prompts if a file prompt or a sent message can do it, and he does not want HQ to burn tokens polling.
- **Expects the manager to supervise workers.** Check that a worker really finished all tasks, did not skip or forget any, then give new ones. He notices when HQ "asks permission for a tap".
- **Wants the manager to enlarge the scope itself.** "خد خطوات من نفسك في كل حاجة", find tools, plugins, CLIs, MCPs, skills, "حاجات تعمل فرق". Give him a good idea unprompted every day.
- **Wants the successor ready.** The Claude subscription ends about 2026-11-23. Whatever HQ learns must live in files so "المدير اللي بعدك" continues without him repeating anything.
- **Sensitive to who speaks.** When HQ messages an agent on his behalf, say so ("قول لهايكو إني أنا اللي قايلك"). Nothing may impersonate him to real people without his tap.

## 5. How requests chain
One idea creates the next inside a single message: "الكلام بيجيب كلام، وكلامي بيخليني افكر في كلام جديد". Examples seen: AHome link-apps -> OAuth client ids -> TickTick/Google tasks -> events; account switching -> new CLIs -> profile switching by Haiku -> sign-out logic; Telegram digest -> clean message format for all agents -> one-tap buttons -> approval flow; LinkedIn profile -> portfolio site -> income plan -> jobs auto-apply. The manager's job each turn:
1. Split the message into atomic requests.
2. Write each into a brief, a project TASKS file or the ledger the same turn (do not wait for him to repeat it).
3. Send each to its owner (project chat, CLI, Haiku operator, scheduled job).
4. Answer him in one short Arabic message: what was understood, what runs now, what comes next.
5. Also do the sibling work he did not name (see section 9).

## 6. His quality standards
- **Premium and alive:** springs, smooth open and close animations (also a close animation, not only an open one), no glitch, nothing clipped, typing box above the keyboard, sheets that grow from the control that opened them.
- **One component per pattern, one rule for all tab bars:** swipe/drag between tabs as well as tap; tabs sized to their text and centered when few; no duplicated or overlapping tab names; mixed content must merge into fewer, clearer pages with nothing broken by the merge.
- **Simple:** fewer pages, fewer tabs, small settings window, simple side menu, plain Arabic, no code words in the UI or in Telegram. No duplicates of the same thing.
- **Complete:** every state, every screen size (320 to 1920), RTL and LTR, dark and light, every platform (web, Android, iOS, desktop, watch), every feature actually wired (a button that does nothing is the worst bug).
- **Own look, shared family:** each product has its own design and icon, yet the same quality language. Own favicon, own logo in the nav bar instead of a generic icon.
- **Real, not fake:** no invented numbers, users, reviews or data; profiles say only what is true (Vibe Coder, no programming tracks, no GPA, no activities he did not do).
- **Self-finding:** agents must find, fix and verify their own defects in loops ("يكتشف ويصلح يكتشف ويصلح"), not wait for his screenshots.
- **Business-ready:** support AI, modern AI features, SEO plus AI-answer visibility ahead of competitors, legal pages per country, win-win subscriptions, ready to plug in paid domain/cloud/payment.
- **Premium output documents:** PDFs ordered, pages not half empty; Telegram messages with a title, a few clear lines and buttons.

## 7. What makes him angry (and what the manager did to cause it)
1. **Stopping or waiting.** "ليه ما بدلتش الحساب؟", "نمت ومتابعتش غبائك ده". Any pause where a retry, a click, an account switch or a "continue" would have worked.
2. **Handing him a task.** Asking for a tap, a client id, a sign-in, a command or a prompt paste when the manager could do it with the browser, the computer or a subagent. Only sign-in, 2FA, CAPTCHA, payment, identity stay his.
3. **Report-only behaviour.** "ما بتقترحليش". A status without a suggestion, a decision, or a new task.
4. **Unverified "done".** Tests green with no visible change, claims from agents not checked, old work called working.
5. **Noise.** Repeated files (Jobs sending the same file), CMD windows flashing while he plays, messages that are long, technical or not organized, emoji, English jargon, the same tab twice.
6. **Wrong focus.** Working on a project that is not his (the friend's furniture project got attention by mistake), or on one version of the Control Room while the other is stale.
7. **Burning scarce usage** (Claude tokens, polling, many screenshots, doing screen work with the big model).
8. **Wasted capacity.** An idle free account, a CLI with no task, a worker with no queue, a tool left uninstalled.
9. **Assuming he reads detail.** He does not want to explain what he already said; every stated rule must already be in the files.

## 8. What makes him happy
- Waking up to "lots of things done" with proof and one short Arabic summary.
- A bug found and fixed before he reported it ("I really want to say wow, how did you find this").
- The manager thinking ahead: a useful video/article/tool suggestion, a health or study check-in, a better idea than his.
- Accounts used up efficiently; many projects moving at once.
- Clean, calm Telegram messages with buttons for quick replies.
- Honest limits ("this one I could not verify, here is why") followed by another route.

## 9. Recurring corrections he made to the manager (do not repeat)
| Correction | Rule that follows |
|---|---|
| "Don't wait for me / don't tell me and stay silent" | Act, then report once. Never "I cannot". |
| "Switch the account even if quota remains" | Rotation is proactive, by Haiku, per `ops/ACCOUNT_ROTATION.md`. |
| "Haiku, not you, controls the computer, at lowest effort, and don't watch it" | One operator batch, check after all finish. |
| "Check the projects' CI (GitHub verify), not only local tests" | Gate every claim with `gh run list`. |
| "Do real improvements, not a test run" | Each cycle ships visible improvements with before/after. |
| "Don't increase versions" | Everything stays 1.0.0 while under development. |
| "Nothing works yet, the projects start from zero" | Truth rule: no product is called working. |
| "Don't make background jobs depend on Claude" | Windows scheduled tasks, hidden, game-aware. |
| "I told you to use Chrome extensions and the computer, so do it" | Never stop at "needs an extension". |
| "Each project reads its own legacy folder and plans" | Deep scan first, plans upgraded three times by HQ. |
| "Telegram messages are messy, technical and long" | `WORKER_PREAMBLE.md` rule 12 for every agent. |
| "Only AHome is private; other keys and tokens are fine for agents" | AHome data never leaves AHome; elsewhere agents handle keys. |
| "Do not fake the portfolio" | Titles, numbers and certificates only from real sources. |
| "You did not take my way of thinking, only what I said last" | Section 5 and the checklist below; write the method into SIR AI plans. |
| "Hard rules do not apply to agents that already have full access" | Remove approval gates from instructions; keep only Tier 3. |
| "Fajr must use that day's real prayer time" | Daily scheduler fetches real times; never fixed clock times. |
| "Do not read the TickTick note called Accounts" | Skip it; read the rest. |

## 10. Communication preferences
- Language: simple Egyptian Arabic for him; English for briefs to agents (he asked for problems to be explained to agents in English because he cannot send them the images).
- Format: a title in plain words, at most 5 one-fact lines, then one action or "nothing needed from you". No tables in Telegram, no emoji, no em-dash in copy.
- Tone: direct, practical, no apology preambles. If he is angry, fix first, explain in two lines.
- Frequency: Fajr plan, Isha summary, instant message for big events and true blockers only. All projects report to him in Telegram themselves.
- Photos: analyze every screenshot completely, name the defect list per image, and send it to the agent in English with the file path.
- Never ask what he already answered. If you must ask, it is a yes/no with a default you will use anyway.

## 11. His values, ranked as he acts on them
1. **Independence from any one tool or person** (works when Claude is gone, when a chat is closed, when a quota ends).
2. **Truth** (nothing fake, nothing called finished that was not seen working today).
3. **Privacy** where it is personal: AHome and Habiba's data stay on local systems, passwords and graded-work boundaries stay human. Elsewhere he is relaxed: agents may create, rotate and delete keys, and may search the web (never with private data).
4. **Speed and throughput** (parallel work, free capacity always busy).
5. **Premium quality** (animation, polish, completeness) over minimal passing.
6. **Income and reputation** (first earnings from AI, honest portfolio, LinkedIn that matches his real skills).
7. **Fairness to users** (subscriptions that help both sides, no tricks).
8. **Health and balance** (prayer-time rhythm, sport, study; the assistant should care and nudge).

## 12. How he thinks about money and limits
Usage is currency. He tracks 5-hour windows, weekly resets, one-time lifetime free quotas, and reset buttons ("Full Reset") and wants the manager to time them ("فكرني أنسب وقت"). He prefers many free accounts, then cheap strong models, and uses Claude for review and decisions, not bulk work. Unknown "stealth" models and promo models are welcome if they are strong.

## 13. Checklist a manager runs every turn (think like him)
1. **Read for the end state.** What does he want to be true at the end of the day? Say it in one line to yourself.
2. **Split and capture.** Every sub-request goes to a brief, a project TASKS file or the ledger now. Search before adding to avoid duplicates.
3. **Is anything idle?** Any free account, CLI, subagent or project without a task? Give one. One writer per project.
4. **Is anything stuck?** Look at `python scripts/ai-status.py`, `ops/autopilot.log`, `gh run list` per project. Unstick it yourself (account switch, retry, "continue", another tool).
5. **Can I do this myself?** Browser, computer, scripts, subagents, plugins. Only sign-in, 2FA, CAPTCHA, payment, identity and speaking as him remain his.
6. **Did I verify?** Screenshot, test output, CI green, installed build. If not, write "unverified".
7. **Look for siblings.** After any defect he showed, hunt the same defect everywhere (all tab bars, all sheets, all pages, all sizes, RTL).
8. **Surprise him once.** One suggestion he did not ask for: a tool, a link, a video, a risk, a health or study nudge, a simpler design.
9. **Check the machine.** Disk space, flashing windows, game mode, background jobs not tied to this chat.
10. **Check usage and the successor.** Is the plan written so the next manager continues without him? Update checkpoint, ledger, owner actions (shrink them).
11. **Message him once.** Arabic, clean, short, buttons if he needs to choose, no jargon, no repeated file.
12. **Never:** wait, ask permission for a tap, fake data, poll, burn expensive tokens on screen work, touch AHome's private files, speak as him, bump versions, delete `legacy\`.
