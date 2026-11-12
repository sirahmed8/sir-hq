# SIR Controller - Refresh Log (rule 20)

## 2026-11-12 (r61, opencode; PLANNING ONLY, no build authorized)

Re-read before work: D:/Projects/AGENTS.md, ops/WORKER_PREAMBLE.md, plans/PRODUCT_DIRECTION_2026-11-12.md, plans/sir-controller.md, plans/sir-controller-DEEP.md, ops/briefs/sir-controller-tasks.md, ops/competitors/sir-controller.md, ops/TICKTICK_MAP.md (SIR Controller rows: unsigned-webhook blast radius note, x360ce mapping note), project folder read-only (AGENTS.md, .sir/CHECKPOINT.md, .sir/TASKS.md; legacy not re-read this round beyond inventory pointers; nothing run), ops/bus/team.md (no prior r61 work; two unrelated DONE lines for r60).

### Web research performed 2026-11-12 (real fetches, no search-engine scraping)

- github.com/nefarius/ViGEmBus (fetched): archived 2023-11-02, "THIS PROJECT HAS BEEN RETIRED", BSD-3-Clause, 4.2k stars; production-signed 1.22.0 is the last line; Win10/11 only since 1.17.
- docs.nefarius.at/projects/ViGEm/End-of-Life/ (fetched): ViGEm retired after trademark conflict; successor **Nefarius VirtualPad** is a commercial framework, "available to business partners" only. No open successor.
- docs.nefarius.at/projects/VirtualPad/ (fetched): confirms partner-only commercial status.
- learn.microsoft.com timeBeginPeriod (fetched): per-process since Windows 10 2004; Windows 11: occluded/minimized window-owning processes do not get high resolution. Consequence: the legacy "0.5 ms timer for your games" claim is false; plan rule 12 added.
- GitHub API search (2026-11-12): x360ce/x360ce active (pushed 2026-11-11, ~2,949 stars, no licence file via API); Jays2Kings/DS4Windows archived 2021-10-24 (3.0k stars); active forks ds4windowsapp/DS4Windows (GPL-3.0, 239 stars, pushed 2026-03-01) and CircumSpector/DS4Windows (505 stars, 2025-02-03); PadForge hifihedgehog/PadForge (.NET 10, SDL3, pushed 2026-11-12, 325 stars, licence NOASSERTION). ds4windows.org advertises v3.3.3 and links an archived fork; treated as untrusted source.
- x360ce/x360ce licence: API 404, no licence file detected; competitor matrix MIT row tagged "(unsourced, verify)"; M0 audit is a hard gate.
- exitlag.com/pricing fetched: JS-rendered, no numbers captured; ExitLag pricing stays "(unsourced, verify)".
- paymob.com reachable (200); fawry.com pricing returned HTTP 403; both gateways stay "(unsourced, verify)" for fees.
- DuckDuckGo/Bing scraping returned no usable results; no claims were sourced from them.

### Changes made

1. `ops/competitors/sir-controller.md` - rewritten: section 0 platform facts (ViGEmBus retired, per-process timer, Nagle=TCP-only, DS4Windows fragmentation, PadForge, x360ce active); matrix expanded with PadForge + ds4windowsapp rows; complaints section tagged unsourced; feature-checklist table vs category best; 12 sourcing tasks (was 10), all linked or tagged.
2. `plans/sir-controller.md` - rewritten: status set to PLANNING ONLY per owner order 2026-11-12; new section 4 "Research findings 2026-11-12"; rules 11-12 added (ViGEmBus as pinned prerequisite, timer honesty); features section demoted false claims (0.5 ms game-wide timer cut; GPU/DWM tweaks demoted to experimental; rapid-fire restricted to single-player); new sections: 7 screens (11 desktop + 7 portal), 8 Firestore data model (10 collections + local-only rule), 9 API list (10 endpoints), 10 AI features (fallback chain, grounded assistant), 11 security/privacy, 12 monetisation, 13 launch/marketing (12-week, $0 organic), 14 platform matrix retained, 17 milestones M0-M6 with acceptance tests, 19 risks R1-R12 + open questions Q1-Q5 each with recommended answer; DEEP plan items reconciled (timer claim corrected).
3. `ops/briefs/sir-controller-tasks.md` - expanded 10 -> 48 tasks (A1-A10 ready to hand unchanged in order; B11-B16 licence/legal; C17-C30 driver/engine; D31-D38 optimizer; E39-E43 portal/billing/owner; F44-F48 AI/quality/release), every task with Files, acceptance test and skills from ops/SKILLS_INDEX.md. Header states PLANNING ONLY and no start before owner authorization.
4. `plans/sir-controller-REFRESH-LOG.md` - created (this file).
5. ops/bus/team.md - START line appended 19:42.

### Not done / open

- No project folder, repo, code, Firebase, TickTick or Desktop changes were made (brief forbids them).
- Prices for ExitLag, Hone, Paymob, Fawry, sircontroller.app domain and code-signing cert: still "(unsourced, verify)"; sourcing tasks listed in competitor file.
- x360ce licence file not yet read directly (needs repo clone or raw fetch; scheduled as task B11).
- Legacy `.sir/TASKS.md` kit rows T-004..T-020 unchanged; the new 48-task queue in the briefs file is the forward plan.
- TickTick map row for SIR Controller not edited this round (read-only usage; no status change authorized).
- Recommended build order when owner authorizes: A1 -> A2 -> A4 -> B11/B12 -> C17 onwards; M0 licence gate first, always.
