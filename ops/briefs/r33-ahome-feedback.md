# Owner feedback, round 33 (2026-11-11 night, from a long voice/chat message plus phone screenshots). Read AGENTS.md, .sir/CHECKPOINT.md, ops/WORKER_PREAMBLE.md (from D:/Projects/_SIR) first. Fix every item below at the root, verify each one on screen at 390 px before ticking it. Self-audit loop after: find at least 10 more defects nobody listed.

Rules: source under apps/ only, never open the vault/messages/notes/photos, no private data leaves this machine, no pull requests (commit and push to main), version stays 1.0.0, never revert another tool's edits.

## Navigation and structure
1. "حياتنا" page tab bar: when the page opens, the active tab is not scrolled into view (it is cut off / you have to scroll sideways to see the full active tab). Fix: always scroll the active tab fully into view on mount and on every tab change.
2. The owner wants "حياتنا" and "يومنا" (today/home) merged into one coherent page instead of two separate destinations, so everything about the couple's life and today's tasks/notes/reminders connect in one clear flow. Before coding: write a short section map in .sir/plans/r33-merge-hayatna-yawmna.md (what moves where, why, at most two taps to anything), get the owner's intent right (reread .sir/plans/r15-our-life.md first), then build it. Remove the duplicate "حياتنا" entries if two different destinations still share that name after the merge.
3. The "more tabs" bottom sheet: it has an opening animation but no closing animation, and the owner found it has only ONE open gear icon (hamburger) and a separate "More" tab that open the exact same sheet - pick one entry point, remove the duplicate, and give the sheet a matching spring close animation back into its trigger.
4. Side/settings panel sliding in from the right opens with its content effectively cut off on the left in some screens (text/table columns like "Zero-Data-Loss Quarantine", startup apps list) - these are on the Laptop Manager/Control Room side, different project; for AHome specifically: any right-aligned panel (settings, context menu "..." overflow in chat) must open fully on screen, never clipped or requiring horizontal scroll to read its own labels. The chat's "..." overflow menu currently opens toward the left edge and gets clipped - make it open toward the right (RTL-correct) and fully visible.

## AI chat and normal chat
5. AI chat keyboard bug: opening the keyboard (to type) and then dismissing it scrolls the message list UP and it stays scrolled, so the latest messages are hidden - it should behave like a normal chat: when the keyboard closes, the view returns to showing the latest message, no manual scroll needed.
6. The AI input box is a large rectangle; shrink and restyle it to match the compact, polished input box used in the normal chat page, and keep both consistent and good-looking.
7. Voice recorder in the AI page: input box is still oversized there and the open/record transition has no animation yet (should grow out of the input box like elsewhere in the app, smooth, no jump).
8. Reply preview: its background color does not match the message input box's own background - make them consistent (same surface color/theme token).

## Bidi / RTL-LTR text and input
9. Both the normal chat input and the AI chat input must detect the script being typed (Arabic vs Latin) and set the text direction and caret side accordingly in real time: Arabic text starts and types from the right, Latin from the left, exactly like WhatsApp/Telegram's own composer. Today it is inconsistent (sometimes starts on the wrong side).
10. Any message/bubble that mixes Arabic and English content must render each run in its own correct direction (bdi isolation) so mixed content is never scrambled or reordered oddly. Audit every place rendering message text/content for this.

## Emoji / stickers / GIFs panel
11. The three tabs (emoji, stickers, GIFs) in that panel: the tab bar is too small and the active tab's label/icon is not centered inside the active pill - fix sizing and centering, make the bar feel as premium as the rest of the app.
12. GIFs tab: GIFs are still not loading / not functional - make it actually fetch and show real GIFs (e.g. via Tenor or Giphy's free API, server-side key, no GIF ever shown that errors; failed ones must be hidden, not shown as "content not available").
13. Stickers tab: current stickers are weak. Source real, well-known free sticker packs (a legitimate free sticker/GIF provider's packs - Giphy/Tenor sticker packs are the simplest route) so the panel offers actual popular packs, not placeholder art.

## Calls and notifications
14. Voice call: pressing call shows a connected-call screen immediately with no ringing state and no ringback tone while waiting for the other person to answer - add a real ringing/ringback state (sound + UI) before a call connects.
15. Video call: tapping "video call" is currently falling back to a voice call screen - fix so video call actually opens the video call UI.
16. Add user-choosable notification sound AND call ringtone settings (distinct from each other), on top of the OS default, so each user can pick how new messages and incoming calls sound.
17. Dynamic Island: expanding it into the search view currently fades/glitches (it visibly disappears and reappears) instead of smoothly growing taller/wider from its current collapsed shape to fit the larger search content - fix so every Dynamic Island state change is one continuous grow/shrink spring, never a fade-out/fade-in swap.

## Games / fun integrations
18. When a game invite (e.g. XO/tic-tac-toe) is sent in chat, the actual game should render and be playable INSIDE the chat bubble/thread (like Telegram/Messenger game cards), not just post a text notice - every game and interactive feature already in the app should be reachable and playable directly from within a chat message, no separate navigation required.
19. "Question" / poll-style messages sent in chat currently render as a plain text bubble - give them a distinct, well-designed card UI (options, vote counts/avatars, a clear visual difference from a normal text message).

## Biometric lock
20. Face ID / Touch ID / passkey re-registration bug: after enabling the lock in settings and registering successfully once, opening the app can still fail recognition and prompt to "register again" even though a valid registration already exists - find and fix the root cause (likely a credential ID / relying-party mismatch, a stale stored credential reference, or a race on first load) so registering once in Settings is enough; never require re-registering on a normal app open. Add a regression test that simulates this exact flow (register in settings, kill and relaunch the app, verify unlock works without re-registering).

## General
21. Native-app feel across the whole web app: disable the default browser text-selection and the default browser right-click context menu, and provide the app's own context menu with sensible, in-app actions appropriate to what was right-clicked (and a generic "refresh" when nothing specific applies). This must not block normal input editing (users must still be able to select/edit text inside actual input fields).
22. Self-audit loop afterward: open every page/tab/sheet at 320/390/768/1280, Arabic and English, light and dark, and find at least 10 more real defects nobody listed above, fix them, before/after evidence in .sir/evidence/r33/.

Finish: update .sir/CHECKPOINT.md, append one line to D:/Projects/_SIR/ops/bus/sir-hq.md, commit and push, CI green.
