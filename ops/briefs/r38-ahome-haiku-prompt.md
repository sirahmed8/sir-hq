You are the builder for AHome (folder D:/Projects/AHome, you are opened inside it). The owner decided on 2026-11-12 that a Claude Haiku session does AHome work, because local models are too weak and free outside CLIs must never touch AHome.

Read first: D:/Projects/AGENTS.md (note the AHome exception line), D:/Projects/_SIR/ops/WORKER_PREAMBLE.md, ./AGENTS.md, .sir/CHECKPOINT.md, .sir/UI_RULES.md, D:/Projects/_SIR/ops/LESSONS.md, D:/Projects/_SIR/standard/OWNER_DEFAULTS.md.

HARD RULES: work only in source under apps/ and tests. NEVER open the vault, messages, notes, photos, calendar data or any file holding private content; never print private content; no private data in screenshots (use empty or seeded demo state). No pull requests: commit and push straight to main after each finished item; CI must be seen green (gh run list) before you call anything done; version stays 1.0.0; never revert another tool's edits; run git status and git log -5 first. Nothing is marked done without evidence (command output, screenshot at 390 px, test). Be efficient: read ranges, not whole files. Never set system or security settings.

TASKS: the owner's own words are in D:/Projects/_SIR/ops/briefs/r38-ahome-feedback2.md (items 1-12 incl. addendum) and .sir/OWNER_FEEDBACK_2026-11-11.md. A free CLI marked those 'done' earlier but the owner still sees the defects, so treat every 'done' as unverified: reproduce each defect first on the running app at 390 px (serve the web app locally, headless Playwright, muted, always close the browser), then fix at the root.

Order:
1) tab bar vanishing and page zoom bug (item 8);
2) Dynamic Island: continuous spring grow for search, one search icon, never overlapping the composer (items 5 and 9);
3) voice recorder bar growing from the input, AI chat uses the SAME recorder component, local transcript button calling only the existing local AI service (if no local speech model exists, wire all five UI states with a clear honest error and retry) (items 2, 3, 4);
4) biometric card centered and mixed-language labels isolated (item 1);
5) Profile tab in Settings with photo, name, nickname, bio shown in chat headers (item 10);
6) calm page spacing (item 11);
7) games hub redesign and 3D improvements (item 12, short decision file first for the 3D approach);
8) at least ten more defects from your own audit loop at 320/390/768/1280, Arabic and English, light and dark.
Follow ops/LESSONS.md (one entry point per sheet, spring open AND close, bidi per character, own context menu, nothing stuck to neighbours).

Do as many items as possible with quality, committing after each. Update .sir/CHECKPOINT.md after every item with the exact next step, add one line to D:/Projects/_SIR/ops/bus/sir-hq.md, evidence under .sir/evidence/r38/. When you stop, write a final report to D:/Projects/_SIR/ops/agy-runs/reports/r38-ahome-haiku.md in plain words: items done with commit ids and CI result, items not done and why.

UPDATE 2026-11-12 15:00 (read before continuing): GitHub Actions minutes for the account are used up, so every CI run fails in about 3 seconds with zero steps (that is the quota, not your code; see D:/Projects/_SIR/ops/ci-quota-exhausted.flag and WORKER_PREAMBLE rule 18). Instead of "CI green", run the full local verification (tests, lint, type check, build) and keep the passing output in .sir/CHECKPOINT.md, then commit and push to main. Do not loop on CI. You may already have commits (git log -5) and uncommitted edits in the working tree: inspect them, finish, test locally, commit, continue the item list in order. Write the final report to D:/Projects/_SIR/ops/agy-runs/reports/r38-ahome-haiku.md.

CONTINUATION 2026-11-12 17:20 (round AHome R9): your first pass is in ops/agy-runs/reports/r38-ahome-haiku.md (items 1 to 6 done, 7 partly, 8 not done). Continue in this order, local verification only (Actions quota flag), commit after each item, report to ops/agy-runs/reports/r39-ahome-haiku.md in plain words:
A) Item 7: the raw WebGL2 layer for the 3D games per .sir/decisions/r38-3d-engine.md, per-game pause and restart, levels, high-score chips from real saved scores only (no fake numbers), sounds off by default.
B) Item 8: the audit loop at 320/390/768/1280, Arabic and English, light and dark; fix at least ten real defects; fix the known flake r15_reply_voice by finding its root cause (layer must be opaque when recording).
C) Re-check the owner's earlier list in .sir/OWNER_FEEDBACK_2026-11-11.md one by one on screen (keyboard scroll in AI chat, emoji/GIF/sticker panel, ringing state, video call opening the video UI, polls card, game invites playable in chat, notification sounds) and fix what is still broken.
D) Real transcription check is blocked until the PC core runs; document exactly what is needed.
Never touch private content; keep evidence under .sir/evidence/r39/.

CONTINUATION 2026-11-12 18:00 (round AHome R10, owner phone screenshots, plain list). Same rules, local verification only, commit after each item, report to ops/agy-runs/reports/r40-ahome-haiku.md:
1. Ghost or friends mode (the hidden mode): when it is on, today, life, tasks and every other private screen were still visible. Find the root cause and make hidden mode actually hide them (and everything else that should hide), with a regression test.
2. The toggle switches look wrong (stretched, oval, knob out of place). Rebuild them as Apple-style switches: pill track 51x31, round 27 px knob with soft shadow, spring slide, correct RTL direction, 44 px tap target, accessible role switch.
3. Profile: remove the 'nickname' field and the word for it entirely (the partner gives the nickname from their side, a person does not set their own). Keep name, bio, photo, and keep the colour choice in the Profile (owner confirmed). When a profile is not saved yet, the sheet must say the person has not created a profile yet, using the name or role: 'Habiba has not created her profile yet' and 'Ahmed has not created his profile yet', never the phrase about 'this device'.
4. Voice recorder bar: its left and right edges are cut off (looks incomplete). Fix the clipping, make the entrance and exit animation smooth, and fix the glitch in the AI chat composer animation too.
5. Chat: remove the white scrollbar in the chat and AI chat lists (scroll by touch and wheel without a visible bar).
6. Remove the green online dot wherever hidden mode applies (no presence dots at all while hidden), and make sure hidden mode also hides the dot in the partner header.
7. Security: GitHub Dependabot shows 9 open alerts (grpc-js high x2, minimatch x2, uuid, glob, fast-xml-parser, grpc-js low x2) in package-lock.json files of apps/web and apps/mobile-capacitor/shell. Update or override the affected packages with minimal safe changes (npm audit fix, overrides), run the full local tests, commit, push. The two Dependabot pull requests were already merged by HQ; pull first.
8. Then continue the unfinished items from your r39 report: the WebGL layer for the other 3D games, per-game pause and levels, the ten-defect audit loop at 320/390/768/1280.
