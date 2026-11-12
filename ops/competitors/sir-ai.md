# Competitor Matrix: SIR AI

**Version:** 1.0.0 (stays 1.0.0 while under development)  
**Research Date:** 2026-11-12  
**Source:** `.sir/plans/COMPETITOR_MATRIX.md` (GitHub API verified licences/stars; aggregator prices marked unverified)  
**Method:** Web search + official pages; third-party prices = "unverified"; GitHub API for licences/stars on 2026-11-12  

---

## 1. Direct & Near Competitors (8)

| # | Product | What It Is | Licence | Pricing (Source Quality) | Strongest 3 Features | Weakest 3 Flaws | What We Copy | What We Do Better |
|---|---------|------------|---------|--------------------------|----------------------|-----------------|--------------|-------------------|
| 1 | **Teamily AI** (teamily.ai) | Group-chat messenger where humans and always-on AI agents share one thread; persistent memory; proactive agents; Gmail, X, Slack, GitHub connectors | Closed (proprietary planning engine) | Not stated on About page (unverified) | Shared memory across chats; sub-agent teams; proactive summaries | Personal-life scope weak (built for groups); no desktop agent or phone remote; "5M users" = company press release (unverified) | Shared memory with privacy boundaries per context; proactive check-ins | Single-owner personal agent with desktop that runs local CLIs; explicit P0–P3 privacy tiers; phone remote included |
| 2 | **AgentsRoom** (agentsroom.dev) | Desktop agent workspace for many projects/agents; split view; 14 agent roles | Closed (packaged Electron in `legacy/`) | Free: 2 projects, 6 parallel agents. Pro: EUR 7.99/mo or 75/yr (terms) — homepage says EUR 9.99/mo (conflict). Team: EUR 15.99/seat, 3-seat min. BYO key, no markup (own site) | Split view of parallel agents; project cockpit; BYO key with no markup | Conflicting prices on own pages; desktop only, no phone remote; no personal memory or life tasks | Split view of running agents; clear caps per plan | Phone remote + memory across days; personal + work in one place; free CLI agents included (not just BYO) |
| 3 | **OpenClaw** (openclaw.ai) | Self-hosted personal assistant: Gateway routes WhatsApp, Telegram, Slack, Discord to AI that runs shell commands & browsers; skills = folders with SKILL.md; ClawHub registry | MIT (GitHub API) | Free (self-host; you pay hosting + model API) | 394k⭐ (GitHub API 2026-11-12); broad channel list (WhatsApp, Telegram, Slack, Discord, Signal); skill format people already write | Self-hosting burden for normal users; community skill security risk real; sources say not production-hardened | Messaging gateway for WhatsApp/Telegram; SKILL.md-style skills idea | Hosted account, no server setup; skills run in sandbox with per-skill permissions; no shell access by default |
| 4 | **Personal.ai** | Memory-first personal AI: knowledge trained into personal model; messaging automation; Slack/email links | Closed | ~USD 40/mo personal (third-party roundups, unverified) | Long-term memory product story | Only proprietary model; memory trapped in trained weights (hard to inspect/correct); price unclear | Memory the user can read/correct as plain notes | Memory stored as readable records with edit/export/delete in two taps; no proprietary model lock-in |
| 5 | **Poke** (poke.com) | Text-message AI assistant over iMessage, SMS, Telegram, limited WhatsApp; approved Apple Messages for Business (June 2026 per sources) | Closed | Free tier; Pro USD 19/mo; Ultra USD 199/mo (third-party, unverified). Acquired by Cognition 2026-07-23; post-2026 pricing not published | Zero-app setup: just text it; human option for calls | Closed; ownership change = plan uncertainty; dependent on messaging platform rules | Text-first quick replies from WhatsApp/Telegram | Owner keeps data on own machine/models; no ownership risk from sale of assistant |
| 6 | **Lindy** (lindy.ai) | No-code AI agents & executive assistant; many integrations | Closed | Plus USD 29.99/user/mo (3,000 credits), Pro 99.99, Max 199.99; no permanent free plan (third-party Oct 2026, unverified) | Easy agent builder; many integrations; voice calls | Credit pricing unpredictable; no free plan; cloud only | Visual builder for automations | Free local CLI agents included; flat monthly cost, not metered per credit |
| 7 | **n8n** (n8n.io) | Workflow automation with many nodes + AI steps | Sustainable Use License (fair-code, NOT open source) | Cloud: no free plan, trial 1,000 executions; Starter ~EUR 20 or USD 24/mo for 2,500 exec (conflicting, unverified) | 400+ integrations; visual workflow editor; self-host option | Licence forbids offering as core of product you sell without commercial deal; execution pricing | Use as worker behind SIR AI, not as product; export workflows as JSON | Automations written in plain words by assistant, with safe sandbox; n8n optional, never core |
| 8 | **Smithery + Official MCP Registry** | Smithery: directory + hosted MCP connection proxy. Official registry at registry.modelcontextprotocol.io (Anthropic, GitHub, Microsoft backed) | Smithery: public directory. Official: open | Smithery hosted connections reportedly shut down 2026-10-31 after Arcade acquisition (one guide, conflicting reports). Official registry free | Huge catalogue (est. 6,000–27,000 servers, unverified) | 2026 scan reportedly found findings in 22/100 servers; hosted proxy dependency broke users | Connector marketplace built on official registry | Own connector broker on official registry; per-user OAuth tokens encrypted server-side; never a third-party proxy holding user tokens |

---

## 2. Open-Source Cousins (Cloned Read-Only in `legacy/agentic-os-research/`)

| Product | Licence (GitHub API) | Stars (API) | Strongest 3 | Weakest 3 | Use for SIR AI |
|---------|---------------------|-------------|-------------|-----------|----------------|
| **Hermes Agent** (NousResearch) | MIT | 262,772 | Skills from experience; persistent memory; gateway (Telegram, Discord, Slack, WhatsApp, Signal, CLI); cron scheduler | Developer-heavy setup; large (400 MB clone) | Skill creation loop; cron scheduling ideas |
| **Goose** (Block, AAIF) | Apache-2.0 | 56,470 | Desktop + CLI + API from one core; MCP tools; provider list | Large (651 MB); desktop-first, not phone | Desktop packaging + MCP model |
| **OpenHands** (All-Hands-AI) | MIT | 93,266 | Sandboxed code execution; event stream; agent abstraction | Coding-only focus; heavy runtime | Sandbox + event-stream design |
| **mem0** (mem0ai) | Apache-2.0 | 68,836 | add()/search() memory API; per-user/session/agent scope; Python/JS SDKs; MCP server | Fact extraction quality model-dependent; cloud upsell | Memory layer design |
| **Letta** (MemGPT) | Apache-2.0 | 25,420 | Agent-owned memory tiers; Postgres/SQLite | Heavy runtime for personal app; cloud pricing unclear | Memory tier vocabulary |
| **Obsidian** (closed app, free core) | Proprietary; plugins/graph free | N/A | Plain Markdown files; graph of linked notes; huge plugin ecosystem; users trust plain files | Not an agent; sync paid (~USD 4–5/mo, unverified); commercial licence conflicts in sources | Linked-notes memory view; plain-file export |

---

## 3. Build-First Ranking (From Research)

1. **Memory as readable, correctable, exportable linked plain notes** (Obsidian + mem0 pattern; Personal.ai weakness) — without it SIR AI is just a chat box
2. **Desktop agent running free CLI agents, showing steps in one place** (AgentsRoom pattern without lock-in) — partly built (`packages/cli-bridge`)
3. **Phone remote with approvals & quick replies** (Poke pattern, own backend) — partly built (commands, approvals, Telegram verbs)
4. **Connector marketplace on official MCP registry with per-user token vault** (replace Smithery dependency)
5. **Automations: built-in scheduler first; n8n as optional worker only** (licence forbids selling as product)
6. **Onboarding: one step to start (Google sign-in → install desktop)** (Teamily/Poke bar)
7. **Owner analytics page, server-checked owner role only**
8. **Pricing: generous free tier + clear Pro line, EGP first** (AgentsRoom/Lindy show how confusing credit/seat pricing feels)

---

## 4. Facts That Must Not Be Claimed

- Any competitor price marked "unverified" must not appear in SIR AI copy
- Star counts are snapshots from 2026-11-12, not claims about SIR AI
- No SIR AI feature is "live" from this file — status stays in `.sir/CHECKPOINT.md` and `.sir/TASKS.md`
- Licences and star counts from GitHub API, not aggregator blogs
- No repos >150 MB or non-open licence cloned; referenced through docs only
- Refresh matrix every quarter and whenever a competitor changes owner

---

## 5. Ideas to Steal (Tagged in `.sir/plans/FEATURE_IDEAS.md`)

| Idea | Source | Tag |
|------|--------|-----|
| Memory as plain linked Markdown notes | Obsidian, Personal.ai weakness | `[cite: Obsidian]` `[cite: Personal.ai weakness]` |
| Graph view of memory filtered by project/person | Obsidian | `[cite: Obsidian]` |
| Memory tiers matching privacy tiers P0–P3 | Original | `[original]` |
| "Why do you think this?" button on every fact | Original | `[original]` |
| One-tap export all memory as Markdown + JSON | mem0 export pattern | `[cite: mem0 export pattern]` |
| Weekly memory review card (5 unsure facts) | Original | `[original]` |
| Per-context memory boundaries (work/family/study) | Teamily AI | `[cite: Teamily AI]` |
| Skill memory: successful task → reusable skill file | Hermes Agent | `[cite: Hermes Agent]` |
| Agent-owned memory tiers (core in context, archive on demand) | Letta | `[cite: Letta]` |
| Forget-by-topic ("forget everything about project X") | Original | `[original]` |
| Connector catalogue from official MCP registry + verified badge | Smithery / official MCP registry | `[cite: Smithery / official MCP registry]` |
| Per-user OAuth tokens encrypted server-side; no third-party proxy | Smithery shutdown lesson | `[cite: Smithery shutdown lesson]` `[original]` |
| Five connection states + one retry button | Original | `[original]` |
| Permission scopes in plain words before consent | Original | `[original]` |
| Read-only connector default; write needs explicit approval | Poke approvals | `[cite: Poke approvals idea]` `[original]` |
| Google Workspace pack (Calendar, Gmail, Drive, Tasks) | Teamily AI connectors | `[cite: Teamily AI connectors]` |
| Connector health page (last success, error codes) | Original | `[original]` |
| Local MCP servers on desktop for files/apps | Goose MCP model | `[cite: Goose MCP model]` |
| Connector sharing between user's devices via account | Original | `[original]` |
| Scan connector listings for risky scopes | Smithery security scan finding | `[cite: Smithery security scan finding]` |
| Built-in scheduler (daily plan, check-ins, weekly review @ prayer times) | Hermes Agent cron | `[cite: Hermes Agent cron]` `[original]` |
| Plain-words automations ("every Sunday at 9...") | Original | `[original]` |
| n8n as optional worker (webhooks); never sold as product | n8n | `[cite: n8n]` |
| Automation run history with single "why" line | Lindy builder | `[cite: Lindy builder]` `[original]` |
| Dry-run mode (preview before real run) | Original | `[original]` |
| Daily automation budget with 80% warning | Original | `[original]` |
| Pause automations during game/heavy task (game-mode) | Original | `[original]` |
| Export automation as JSON | Original | `[original]` |
| Phone remote: live desktop task list + pause/resume/approve | Poke-style quick replies | `[cite: Poke-style quick replies]` |
| Quick-reply Web Push: "Send/Edit/Later" | Original | `[original]` |
| Telegram verbs: /status /pause /resume /tasks /approve | Poke text-first | `[cite: Poke text-first]` |
| Voice note in Telegram → task | Poke text-first | `[cite: Poke text-first]` `[original]` |
| Watch complication: next plan item + check-in time | Original | `[original]` |
| Car mode: read-aloud summary, voice-only approvals | Original | `[original]` |
| TV/large-screen read-only today's plan | Original | `[original]` |
| QR pairing (10 min expiry, single use) | Original | `[original]` |
| Offline queue on phone (idempotency keys) | Original | `[original]` |
| Phone shows "desktop asleep" → wake via relay | Original | `[original]` |
| One sign-in → install desktop app (platform detected) | Teamily AI one-step start | `[cite: Teamily AI one-step start]` `[original]` |
| Installer checks for free CLI agents, offers install from official sources | Original | `[original]` |
| Setup stepper locked until step validates | Original | `[original]` |
| First-run "tell me about your week" voice/text fills profile <2 min | Personal.ai learns from you | `[cite: Personal.ai learns from you]` |
| Empty-state cards explain future state (no fake data) | Original | `[original]` |
| Install-size + disk-space check before download (Windows) | Original | `[original]` |
| Owner page: active users, retention, funnel, AI spend, error heatmap, CSV export | Original | `[original]` |
| Free tier useful daily: 1 desktop, 1 phone, free CLIs, memory limit | AgentsRoom free tier bar | `[cite: AgentsRoom free tier as the bar to beat]` |
| Pro priced in EGP first (e.g., 149 EGP/mo) with regional display | Original | `[original]` |
| No credit meter on Pro; fair-use limits written plainly | Lindy credit complaints | `[cite: Lindy credit complaints]` |
| Annual shown as monthly equivalent + yearly total | AgentsRoom EUR 75/yr | `[cite: AgentsRoom EUR 75/yr]` |
| Paid buttons "coming soon" + email lead until gateway keys | Original | `[original]` |
| Cancel in one tap in Settings | Original | `[original]` |
| One timeline: assistant steps + CLI agent + files touched + cost | AgentsRoom split view | `[cite: AgentsRoom split view]` `[original]` |
| Live "thinking" lane: short line per step, collapsible | Original | `[original]` |
| Free CLI activity as one feed, colour per CLI | Original | `[original]` |
| Rate-limit/quota switch shown as plain line | Original | `[original]` |
| Pause/stop any step from timeline (desktop/phone) | Poke approvals | `[cite: Poke approvals]` `[original]` |
| Single JSON config (`sirai.config.json`) read/written by settings UI | Original | `[original]` |
| Config validation with Zod; red line in settings on invalid | Original | `[original]` |
| Config changes sync via account with version + undo | Original | `[original]` |
| Secrets never in JSON; secret store shows "set/not set" | Original | `[original]` |
| Motion: micro <180ms, morph <300ms, press scale 0.98 | emil-motion-impeccable | `[original]` |
| Bilingual ar/en with logical CSS + bdi isolation | Original | `[original]` |
| Dark/light WCAG AA contrast checked in sweep | Original | `[original]` |
| Five states on every list | Master directive | `[original]` |
| Native right-click/long-press menu (native kept on inputs) | Round 27 work | `[original]` |
| Zero horizontal scroll at 320/390/768/1280/1920 | Original | `[original]` |

---

## 6. Verification Notes

- GitHub API called 2026-11-12 for licences/stars (see `.sir/plans/COMPETITOR_MATRIX.md` source lines)
- Aggregator prices explicitly marked "unverified" — must not appear in SIR AI marketing
- Smithery shutdown report from one guide (conflicting) — treat as risk, not fact
- Poke acquisition by Cognition 2026-07-23 per sources — post-2026 pricing unknown
- n8n Sustainable Use License text summary: forbids selling as core product without commercial deal
- All claims carry source link or "(unsourced, verify)"
- Matrix to be refreshed quarterly and on competitor ownership change