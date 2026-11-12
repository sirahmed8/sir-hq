# Archived dashboard pipeline scripts

These two one-shot scripts patched the retired Control Room generator (the `const D = {...}` page
and its `dashboard_main.py` / `dashboard_data.py` module split). They were used once to split the
old pipeline into small modules and they no longer match any file in `plans/`.

The live pipeline is now:

- `plans/dashboard_page.py` plus `plans/dashboard_parts/*.html` (the page template, one concern per part)
- `plans/dashboard_feeds.py`, `plans/dashboard_repos.py`, `plans/dashboard_notes.py` (read-only feeds)
- `plans/generate_dashboard.py` (writes the artifact, its mirrors and `ops/artifact/CHANGED.txt`)

Nothing here is imported or executed. Kept only so the history of the old page stays readable.
Do not run these scripts.
