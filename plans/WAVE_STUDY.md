# BUILD ORDER (Ahmed, 2026-11-01)

Order of waves. HQ opens a project chat, reviews its reports, and starts the next project when the finished one meets the definition of done in `PERPETUAL_LOOP.md` (Ahmed, 2026-11-08: agents do not stop; he is told on Telegram, he is not asked and nothing waits for him). Chats running at the same time: at most 2 while `LOW_USAGE_MODE.md` is active (2026-11-10), otherwise as many as the quota allows, at most 5.

Priority override (Ahmed, 2026-11-08, newest): SIR Study comes first among wave 2 because of his exams (coaching only), and SIR AI ("Jarvis" for his laptop) starts right after the wave 2 projects, before the Negm plans. The wave numbers in `waves.json` and `order.json` are unchanged on purpose (changing them regenerates every plan); this paragraph wins where the table differs.

| Wave | Why | Projects (in order) |
|---|---|---|
| 1 | AHome (private, first) | ahome |
| 2 | Automations that make his life easier | sir-study, sir-jobs, sir-laptop-manager |
| 3 | Friend's project: PLANS and handoff pack only. No build work, chat, CI or deploy until Ahmed says so (2026-11-09) | sir-negm-furniture |
| 4 | AI and content | sir-ai, sir-content-creation-studio |
| 5 | Products that earn the most | sir-business, sir-hagoozat, sir-obour-hub |
| 6 | Other paying products | sir-modpack, sir-mods-for-gta-v, sir-life |
| 7 | Last on purpose: extract and polish after everything else is built | sir-platform, sir-portfolio |
| 8 | Optional, last (derived from x360ce, not Ahmed's own) | sir-controller |

## Decisions behind it
- AHome first (his pick). Then the automations that save him time: SIR Study, SIR Jobs, SIR Laptop Manager (not sites or apps, so no platform kit needed).
- SIR Negm Furniture belongs to a friend: HQ prepares a complete handoff pack in the project repo (docs, plan, a prompt for the friend's own AI agent); no GitHub, Firebase or Cloudflare accounts are created for it by Ahmed.
- SIR AI and SIR Content Creation Studio next, then the products expected to earn the most (Business, Hagoozat, Obour Hub), then the other paying ones.
- SIR Platform and SIR Portfolio are last on purpose. Each product keeps its shared concerns (owner auth, signed webhooks, billing fallback, AI proxy, legal pack, tokens and UI) in separate internal packages with tests; SIR Platform is then built by extracting and unifying the best versions, and SIR Portfolio shows the real finished products.
- SIR Controller derives from x360ce (not Ahmed's own work): optional, last.
- Removed: sir-odysseus: Not Ahmed's project (Odysseus upstream). Source moved to SIR AI/legacy as a read-only reference; folder moved to old projects; repo archived.

The earlier score-based study (revenue, readiness, effort) is in `wave_study.py` for background.
