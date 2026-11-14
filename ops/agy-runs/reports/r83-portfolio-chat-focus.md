# r83-portfolio-chat-focus — report

## Task
Scout finding approved by HQ, queued as brief `r83-portfolio-chat-focus` (HQ auto-approved: clear defect). Source: `ops/SUGGESTIONS.md` entry `sug-ai-chat-toggle-unmounts-on-open--814d358f` (2026-11-14, severity high, category bug, Status now flipped to done after the fix shipped).

Finding: AI chat toggle unmounts on open so keyboard focus is dropped to `<body>` and never moved into the dialog; on close, focus is not restored to the toggle, forcing keyboard users to re-tab through the whole page to reach the chat input.

## What I found (reproduce)

File: `/d/Projects/SIR Portfolio/src/components/AIChat.tsx` (the AI chat widget of the portfolio site; used from `/d/Projects/SIR Portfolio/src/app/[lang]/page.tsx:44`).

Code shape (before fix):
- Floating toggle rendered only when closed: `{!isOpen && (<button className="ai-chat-toggle" ...>)}` - src/components/AIChat.tsx.
- Chat window rendered only when open: `{isOpen && (<div className="ai-chat-window" role="dialog" aria-modal="false" ...>)}` - src/components/AIChat.tsx.
- No focus effect at all. The only effect listened for `Escape` on `window` when open.

Evidence trail: scout line `src/components/AIChat.tsx:342-358 ({!isOpen && <button>} unmounts, no focus effect)`; tab probe `D:/Projects/_SIR/ops/scout-evidence/tabprobe.py`; scout JSON `D:/Projects/_SIR/ops/scout-evidence/scout-portfolio-a11y.json` (en-home tab walk).

Reproduction run (before fix) - built static site served by `node scripts/serve.mjs 4519` over `out/` (port 4519, like the scout probe), Playwright, viewport 390x844, page `/en/`:

```
CLOSED tab stops: ... stop 1 'Skip to content', stop 2 'Ahmed Alaa', stop 3 'العربية', stop 4 'Switch to dark theme', stop 5 'Menu', stop 6 'See my work ->'
--- open chat via toggle click ---
AFTER OPEN activeElement: {'y': 14912, 'tag': 'body', 'txt': 'Skip to content\nAhmed Alaa\nالع...', 'focused': True}
DIALOG STATE: {'rect': [-49.6, 420.4], 'display': 'flex', 'vis': 'visible'}
--- press Tab (should move INTO dialog) ---
AFTER TAB1: {'y': 14912, 'tag': 'button', 'txt': 'What is SIR AI?', 'focused': False}
--- press Escape ---
AFTER ESCAPE activeElement: {'y': 14912, 'tag': 'body', ..., 'focused': True}
```

Before-fix behaviour confirmed:
1. After clicking the toggle to open, `document.activeElement` was `<body>` (`focused: True` means the check was `el === document.body`) - focus dropped to body on unmount of the toggle and never moved into the dialog.
2. Pressing Tab moved focus into the dialog but landed on the first focusable in DOM order - the quick-question chip button "What is SIR AI?" - not the message input.
3. Pressing Escape closed the dialog and focus ended on `<body>` again; nothing restored it to the toggle.

## Fix (cause, not the report)

`/d/Projects/SIR Portfolio/src/components/AIChat.tsx`:
- Added refs: `toggleRef = useRef<HTMLButtonElement>(null)`, `inputRef = useRef<HTMLTextAreaElement>(null)`, and `wasOpenRef = useRef(false)`.
- Added focus effect on `isOpen`:
  - open -> `inputRef.current?.focus()` (message textarea inside the dialog);
  - close and we were open -> `toggleRef.current?.focus()` (toggle remounts when closed, so the ref resolves after commit).
  - `wasOpenRef` transition tracking keeps a mount-with-closed-state from stealing focus.
- Toggle button got `ref={toggleRef}`, `aria-expanded={isOpen}`, `aria-haspopup="dialog"`; dialog keeps `role="dialog"`, `aria-modal="false"`, `aria-label`.

`/d/Projects/SIR Portfolio/scripts/keyboard-audit.mjs` (regression test in the project's real check):
- New checks per language: AI chat toggle button exists; opening the AI chat moves focus into `.ai-chat-window`; AI chat input receives focus when the chat opens; Escape closes the AI chat; Escape returns focus to the AI chat toggle.

## Verification (real output, commands run)

Reproduction AFTER fix (same probe, rebuilt site, same port/flow):
```
--- open chat via toggle click ---
AFTER OPEN activeElement: {'y': 14912, 'tag': 'textarea', 'txt': 'Your question', 'focused': False}
DIALOG STATE: {'rect': [-49.6, 420.4], 'display': 'flex', 'vis': 'visible'}
--- press Tab (should move INTO dialog) ---
AFTER TAB1: {'y': 14912, 'tag': 'a', 'txt': 'Privacy', ...}
--- press Escape ---
AFTER ESCAPE activeElement: {'y': 14912, 'tag': 'button', 'txt': 'Open AI Assistant', ...}
```
After-fix behaviour confirmed: on open, focus is on the chat textarea; on Escape-close, focus is back on the toggle button (`Open AI Assistant`). (The first Tab after open moved to a page-level link because the disabled send button is skipped in tab order - acceptable, focus was already inside the dialog.)

Checks run in `/d/Projects/SIR Portfolio` (CI quota flag `D:/Projects/_SIR/ops/ci-quota-exhausted.flag` exists since 2026-11-12, so local verification substitutes for CI per worker rule 18):
- `npm run content:check` -> `content check: 0 error(s), 0 warning(s)` (exit 0)
- `npm run typecheck` -> `content check: 0 error(s), 0 warning(s)` + `tsc --noEmit` clean (exit 0)
- `npm test` -> `ℹ tests 847`, `ℹ suites 23`, `ℹ pass 847`, `ℹ fail 0` (exit 0)
- `npm run build` -> success, static export, 25/25 static routes, postbuild ok (exit 0)
- `node scripts/axe.mjs http://127.0.0.1:4519 /d/Projects/SIR Portfolio/.sir/evidence/r83-axe-report.md` -> all listed routes: `0 violation(s), 0 serious or critical` for en/ar x light/dark (exit 0)
- `node scripts/keyboard-audit.mjs http://127.0.0.1:4519 /d/Projects/SIR Portfolio/.sir/evidence/r83-keyboard-audit.md` -> exit 0; new AI chat checks pass for both `en` and `ar`:
  - pass: AI chat toggle button exists
  - pass: opening the AI chat moves focus into the dialog
  - pass: AI chat input receives focus when the chat opens
  - pass: Escape closes the AI chat
  - pass: Escape returns focus to the AI chat toggle
- Keyboard audit report written to `/d/Projects/SIR Portfolio/.sir/evidence/r83-keyboard-audit.md`; axe report to `/d/Projects/SIR Portfolio/.sir/evidence/r83-axe-report.md`.

Screenshots taken during reproduction (Playwright): `/d/Projects/_SIR/scratch/r83-closed.png`, `/d/Projects/_SIR/scratch/r83-after-escape.png`.

## Changes

- `/d/Projects/SIR Portfolio/src/components/AIChat.tsx` (+19 lines): focus effect + refs + aria-expanded/aria-haspopup.
- `/d/Projects/SIR Portfolio/scripts/keyboard-audit.mjs` (+22 lines): four regression checks (EN + AR).
- Evidence reports: `.sir/evidence/r83-keyboard-audit.md`, `.sir/evidence/r83-axe-report.md` (committed with the fix).

Commit: `/d/Projects/SIR Portfolio` repo, `fix(r83): move AI chat focus into dialog on open and restore to toggle on close` (commit b3df4e0), pushed to `origin/main` (`de5a094..b3df4e0  main -> main`).

## Shared lessons checked (touched screen: AI chat)

Read `/d/Projects/_SIR/ops/LESSONS.md` for chat/floating-panel screens: L5 (keyboard dismiss returns to latest message), L6 (consistent input styling), L18 (native-app feel). No existing lesson covered focus move-in/move-out for conditionally mounted panels, so I added:
- `ops/LESSONS.md` -> new lesson `## L52: Dialog and Floating Panel Focus (Move In, Restore Out)`.
- `standard/OWNER_DEFAULTS.md` -> new heading `## Adopted from SIR Portfolio` with the one-line adoption note (reusable fix pattern for floating chats/dialogs).

## Acceptance vs brief

- Reproduce the finding with the evidence above: DONE (probe before/after).
- Fix the cause (not the report): DONE (focus effect + refs; aria wiring).
- Add or update a test where the project has tests: DONE (keyboard-audit regression checks, run green).
- Check the shared lessons in `ops/LESSONS.md` for the touched screens: DONE (read; added L52; adopted in OWNER_DEFAULTS).
- Run the project's checks and CI until green: DONE locally; CI replaced by local verification (quota flag) per rule 18.
- Commit and push to main: DONE (portfolio b3df4e0 pushed).
- Update the project checkpoint: DONE (`/d/Projects/SIR Portfolio/.sir/CHECKPOINT.md` Round r83).
- Write a short report with the real command output: DONE (this file).
- Tick this item in `ops/SUGGESTIONS.md` (Status: done): DONE.

## Still open / unsure

- The chat textarea keeps inline `outline: "none"` (`styles.textarea.outline` in AIChat.tsx), so the visible focus ring while the input is focused comes from the global `:focus-visible` rule only where it is not overridden - that is the separate pending scout finding r84-portfolio-chat-focus-ring (brief r84, Status: pending). I did not fix it here (brief scope was focus management).
- Focus behaviour after sending a message / typing-indicator transitions was not re-probed beyond open/Escape; the effect keys on `isOpen` only.
- Live redeploy on Firebase Hosting and Vercel for the fixed build was not re-run in this round (same note as r78: deploy step pending after push; hosts were verified serving the previous build, and `out/` was rebuilt from the fixed source).

## Recommended next

- Brief r84-portfolio-chat-focus-ring (chat textarea inline outline:none overriding the global :focus-visible ring, WCAG 2.4.7) - already queued in ops/SUGGESTIONS.md, Status: pending.
- Brief r85-portfolio-chat-aria-live (chat messages container missing role=log/aria-live) - already queued, Status: pending.
- Live redeploy of the fixed portfolio build to both hosts (Firebase Hosting + Vercel) and owner phone check of the floating chat.
- Consider applying the L52 focus pattern to the SIR AI floating chat widget (sir-ai-official) and the SIR Jobs/SIR Study chat surfaces when they get their own focus rounds.
