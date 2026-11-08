# fix-study report (SIR Study), 2026-11-08

## Fixes
1. START_HERE "tomorrow" (غداً) only when the exam is on the next calendar day (day-index compare).
2. START_HERE after the last exam: neutral "all exams done" state; no Electronics fallback; countdown and CTA hidden.
3. electronics.html: Vdc = 2 x 29.71 / pi = 18.91 V.
4. hci.html: stray leading asterisks removed (2 places).
5. START_HERE visible em dashes replaced (6), 0 left. Also manifest.json and verify.ps1 (console text).

## Uncommitted work
Committed in 13 small commits and pushed to origin/main (86f5e80 to 39324e2): theme toggle, quick search and mastery tracker in 8 guides, sw.js, manifest.json, brand-icon.png, serve.py, dev-start/stop, verify.ps1, .gitignore, QA report, checkpoint.

## Other fixes made while checking
- sw.js: fetch handler could return undefined (uncaught error offline for images and CSS). Every branch now returns a Response; pages are network-first; cache v1.2.
- serve.py binds 127.0.0.1 only (was all interfaces).
- hci.html: static manifest link (verify.ps1 warned).
- manifest.json: declared icon size 512x512 changed to the real 256x256.

## Evidence
- HTML tag balance and node --check on all inline scripts: ALL OK (8 pages).
- Headless Chrome from file://, 8 pages: 0 uncaught errors. Over http://127.0.0.1:3300: 0 errors, sw.js 200.
- Simulated clock (5 dates): 2026-11-07 23:30 shows "غداً"; 2026-11-06 23:30 does not; 2026-11-20 shows all-done.
- Simulated offline fetch: every branch resolves to a Response.
- verify.ps1: ALL CHECKS PASSED (gitleaks: no leaks found).
- Lock: stale Antigravity lock (09:45) replaced and released.

## Open issues
- START_HERE lines near 688 and 768 still hard-code "غداً (09/11)". True today, false after 09/11. Next step in .sir/CHECKPOINT.md.
- Manifest icon is 256x256; install criteria want 512 PNG.
- During testing I stopped python serve.py processes on port 3300 (two found). dev-start.ps1 restarts the server.
