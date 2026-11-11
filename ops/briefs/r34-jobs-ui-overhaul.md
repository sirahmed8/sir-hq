SIR Jobs, round 34 (2026-11-11): full UI/UX overhaul, owner reports the dashboard feels broken and hard to use on his phone. Read AGENTS.md, .sir/CHECKPOINT.md, ops/WORKER_PREAMBLE.md, standard/OWNER_DEFAULTS.md (read items 14-16 especially: native-app feel, bidi text, personalization/locale) first.

Rules: no pull requests, commit and push to main after every item, CI green, one writer per project, truth rule (verify every claim on screen at 320/390/768/1280, Arabic and English, light and dark before saying it's fixed).

1. Click-target audit: the owner found many buttons do not respond to taps, with elements stacked under other elements (z-index/overflow bug). Audit every interactive element on every view: no element may have a 0-size or covered hit area, no absolutely-positioned element may sit on top of a button without pointer-events being intentional. Add a browser test that tab-clicks every visible button/link on each route and asserts a real click handler fires (no silent no-ops).
2. The top bar is cluttered (menu, logo, title, a settings pill, a search button, an unlabeled number, an EGP figure in a dark blob, "Tailnet Connected" as loose text, all different heights/weights) - already flagged before; if round 22's fix regressed, redo it: one compact toolbar, numbers in labelled chips of one consistent height/radius, connection status as a small dot+label.
3. Settings/preferences language toggle (and anywhere similar): never show literal "(RTL)"/"(LTR)" suffixes to the user - just "English" / "العربية". Same rule for any other technical direction label leaking into copy anywhere in the app.
4. Mixed Arabic/English text (prices, chips like "USD / EGP", job titles) must render with correct bidi isolation (<bdi> per run) - audit every place this could scramble.
5. Currency: auto-detect the visitor's region/locale for the default currency display instead of relying only on a manual picker; keep the manual override.
6. Native-app feel: disable default text selection and the browser context menu site-wide (not inside real form inputs), add the app's own context menu with relevant actions.
7. Full visual redesign pass: the owner's words are "broken, tired, cheap" (UI/UX وحش مضروب وتعبان ورديء) - simplify the information density, align spacing to a 4/8px grid, make every card/button feel premium and consistent with the rest of the SIR family (spring animations, consistent radii, consistent chip styles). Remove any duplicate navigation entries that open the same destination.
8. Self-audit loop: two clean cycles at 320/390/768/1280, Arabic/English, light/dark, before/after evidence in .sir/evidence/r34/.

Finish: update .sir/CHECKPOINT.md, append one line to D:/Projects/_SIR/ops/bus/sir-hq.md, commit and push.
