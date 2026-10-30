# WAVE STUDY (2026-10-30)

Rule from Ahmed: start with AHome, then the projects that make money, then the rest, in a studied order, not random.

Method: each project gets 0-5 scores from the Phase 3 inventories (`ops/PORTFOLIO.md`, `ops/inventory/`). Total = 3 x speed to first EGP + 3 x revenue size + 2 x legacy readiness + 2 x independence from the kit + 1 x Ahmed's priority - 2 x effort. Scores are judgements that rank projects; they do not forecast income. Edit `SCORES` in `plans/wave_study.py` and re-run when facts change.
Wave rules: AHome and SIR Platform are fixed. A project with independence 4+ and speed 3+ is quick cash (wave 2). Otherwise revenue under 2 means internal or personal (wave 5), total 25+ is wave 3, the rest of the paying products wave 4.

| Project | Speed | Revenue | Ready | Free of kit | Ahmed | Effort | Total | Wave | Why |
|---|---|---|---|---|---|---|---|---|---|
| sir-jobs | 5 | 3 | 3 | 5 | 4 | 2 | **40** | 2 | Finds and drafts paid freelance and remote work; the first-1,200-EGP goal depends on it; needs no platform kit. |
| sir-negm-furniture | 4 | 2 | 4 | 4 | 3 | 2 | **33** | 2 | A client project: delivery is paid work. Small static site, existing code, light platform use. |
| sir-portfolio | 3 | 2 | 2 | 5 | 3 | 1 | **30** | 2 | Free site, but it is the storefront that makes freelance and product sales credible. Smallest effort. |
| sir-business | 3 | 5 | 3 | 2 | 4 | 4 | **30** | 3 | One restaurant plan is 450 to 1,950 EGP a month, so one customer passes the first milestone. Restaurant is the most complete old app. |
| sir-content-creation-studio | 3 | 3 | 3 | 2 | 4 | 2 | **28** | 3 | Makes the videos for ByteVibeHQ channels, which is a second income line; Pro tier later. |
| sir-hagoozat | 2 | 4 | 3 | 2 | 5 | 3 | **27** | 3 | Large Egyptian market, but two-sided (players and pitch owners) so the first payer is slower; Pro is 59 EGP a month. |
| sir-obour-hub | 2 | 3 | 4 | 2 | 5 | 3 | **26** | 3 | Closest to shippable (CI, 47 tests, live), small paying audience; proves the kit on the web path that Hagoozat reuses. |
| sir-controller | 2 | 3 | 2 | 3 | 3 | 3 | **22** | 4 | Gamer market in Egypt and the Gulf; needs a UI stack decision and driver licence checks first. |
| sir-mods-for-gta-v | 1 | 2 | 3 | 3 | 3 | 3 | **18** | 4 | Supporter tier only, and a game-licence risk to clear first. |
| sir-modpack | 1 | 2 | 3 | 3 | 3 | 3 | **18** | 4 | Supporter tier only; large payload; community-driven. |
| sir-ai | 1 | 2 | 2 | 3 | 3 | 3 | **16** | 4 | Feeds the platform's AI gateway idea; paid tier is far off. |
| sir-laptop-manager | 0 | 0 | 3 | 5 | 4 | 2 | **16** | 5 | Internal. It makes every agent's setup consistent but earns nothing itself. |
| sir-study | 0 | 0 | 3 | 5 | 4 | 2 | **16** | 5 | Personal study organiser; saves Ahmed time, earns nothing. |
| sir-life | 1 | 3 | 0 | 2 | 4 | 3 | **14** | 4 | New product with no old code; cloud backup is the only paid part. |
| sir-odysseus | 0 | 1 | 1 | 3 | 2 | 3 | **7** | 5 | Upstream-derived AGPL distribution; donations only. |
| ahome | fixed | | | | | | | 1 | Ahmed's first pick: private, local, independent of the platform kit, runs today and is improved in place. |
| sir-platform | fixed | | | | | | | 2 | Prerequisite for every web product. Build only the slice the next wave needs (M0 to M2) in step with the quick-cash projects. |

## Order Ahmed opens chats in
- **Wave 1: AHome (your pick):** ahome
- **Wave 2: quick cash and the kit slice:** sir-platform, sir-jobs, sir-negm-furniture, sir-portfolio
- **Wave 3: first subscription products:** sir-business, sir-content-creation-studio, sir-hagoozat, sir-obour-hub
- **Wave 4: next paying products:** sir-controller, sir-modpack, sir-mods-for-gta-v, sir-ai, sir-life
- **Wave 5: internal and personal tools:** sir-laptop-manager, sir-study, sir-odysseus

## Dependencies that fix the order
- Every web product (Negm, Portfolio, Obour Hub, Hagoozat, Business portal, Life) needs SIR Platform packages: owner-auth, signed-webhook, billing fallback, ui kit. Build those first, only as far as the next project needs.
- SIR Obour Hub proves the kit on the web path before Hagoozat reuses it. SIR Business is the largest revenue and the largest build, so its Restaurant mode starts as soon as the kit is proven.
- AHome runs today with daemons: its chat must keep the services up and snapshot data before any change.
- A project may be pulled earlier when Ahmed gets a customer for it; the order changes, the kits do not.
