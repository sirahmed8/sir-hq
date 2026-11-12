# Archived dashboard pipeline scripts

These scripts belong to the retired Control Room page (the `const D = {...}` page with `const $ =`)
and to the retired generator modules. They do not match any file in `plans/` any more and they
crash or report nothing useful against the rebuilt page.

Archived here on 2026-11-12 (task ci-sir-20261112-0901-fix1-fix1):

- `split_dashboard_modules.py`, `split_generator_modules.py`: one-shot patches that split the old
  generator into small modules.
- `audit_control_numbers.py`, `check_git_hashes.py`: audit helpers that read the old page format
  (`const D = {...}; const $ =`) out of `ops/dashboard.html`.
- `update-dashboard-data.mjs` (+ its test): memory helper that patched the old page data block.

The live pipeline is now:

- `plans/dashboard_page.py` plus `plans/dashboard_parts/*.html` (the page template, one concern per part)
- `plans/dashboard_feeds.py`, `plans/dashboard_repos.py`, `plans/dashboard_notes.py` (read-only feeds)
- `plans/generate_dashboard.py` (writes the artifact, its mirrors and `ops/artifact/CHANGED.txt`)

Nothing here is imported or executed. Kept only so the history of the old page stays readable.
Do not run these scripts.
