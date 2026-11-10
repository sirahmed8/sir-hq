# Inventory: non-product folders (2026-10-29, scout, read-only)

## Jobs (`D:\Projects\Jobs`, 4.3 MB, not a git repo, no backup)
Job search and apply pipeline: CV, scrapers (`jobspy_scraper.py`), tracker, `automations/playwright_auto_apply.py` (unattended submit), `email_and_apply_pilot.py`. Weekly run set in `sidecar.json` (Antigravity, Sat 09:00 Cairo); no Windows scheduled task.
- Stale: moved from `D:\Jobs` (path gone); old path in 11 files and `sidecar.json` `workspace_uris`.
- **Fake-data risk:** root `applications_tracker.json` has 111 rows, 102 say "Applied" with no submission field (no evidence of any submission); `tracker/applications_tracker.json` (12 rows) is fully duplicated in the root.
- Personal data: CVs in `cv/` and a PDF in the root; no remote, so nothing public. No secrets found.
- Decision: keep; fix paths, dedupe trackers, relabel unproven rows "Unverified", `git init` (private) and add to the backup set. Phase 8 builds the real jobs agent on top (honest applications only).

## Learning (`D:\Projects\Learning`, 166 KB, no git)
Toolchain smoke tests from 2026-08-20 (`A.py`, `A.cpp`, `A.dart`, `A.exe`). Decision: move to `old projects\Learning`.

## AI_Models_Hub (a model store, not a project)
`ollama/blobs` about 9.7 GB; `rag/index.sqlite` 5 MB used by the Laptop manager RAG; `huggingface`, `models`, `torch`, `voice_clones` are empty. Decision: keep; remove the four empty dirs; add a README saying it is not a project.

## sirahmed8 (PUBLIC profile repo, 18 commits, clean)
Tracked: README, AGENTS/CLAUDE/GEMINI (identical 24 KB internal directives, in a public repo), legal pages, icons. No secrets. Phone and email in README lines 10 and 168-169 (owner decision).
- Links: 18 of 19 product URLs return 200; `sir-odysseus-app.web.app` 404; two github-readme-stats 503.
- Accuracy: "Tele Gateway v1.0.0" vs repo "4.0"; missing Negm Furniture, Merged sites, AHome (private: must not be listed), Laptop manager, Jobs.
- Hype and unverified claims: "Seamless" (line 91), emoji headers (lines 73, 157), "8+ Production Applications", "Sub-48h velocity", "Recognized in Global AI Developer Ecosystems", "Invited ... Agensi.io" (lines 150-161). Followers badge is a real count.
- Decision: rewrite the README after the portfolio is final (Phase 3.4/8): remove hype, unverifiable claims and emoji headers; untrack the internal directive files from the public repo; AHome is never listed.

## old projects (top level)
`SIR Tele Gateway/` 75 MB: private repo (verified), last commit 2026-10-25, 8 uncommitted items, `.venv` with 1,497 files, no retired-note README. Three files hold [removed] strings (39 chars): `app/index.html:1137`, `web/static/auth-popup.html:116`, `web/static/js/dashboard.js:265` (probably Firebase web config: verify and restrict the key; not printed). `Desktop_SIR_Tele_Gateway/` has 3 .lnk files pointing to a path that no longer exists.
Decision: commit/branch the 8 dirty items, add a pointer README, delete the dead shortcuts and the regenerable `.venv`. Sprint Day 27 decides revive vs archive.
