# Antigravity operator guide: start a new agent chat and send a prompt

Status: partly verified on 2026-11-08. Steps 1 to 3 were tested. The prompt was not sent yet (see "Blockers seen").

## Click path

1. Open the app. Use `open_application` with "Antigravity" (not "Antigravity IDE" for chats). The window opens maximized, dark theme. The left sidebar has "New Conversation", "Automations", "Customizations", and a "Projects" list. The top right has "Open IDE".
2. Start a chat. Click "New Conversation" in the top-left of the sidebar (about x=60, y=97 in full-size coordinates). The main area shows "Hi Sir, what can we get done today?".
3. Pick the model. The model chip sits at the bottom of the input box, left side, labelled "Gemini 3.0 Flash High" (about x=580, y=766 full-size). Click it, and a menu opens with "Model" as heading. Options seen: Gemini 3.0 Flash High (selected), Claude Sonnet 4.6 (Thinking), Claude Opus 4.6 (Thinking), GPT-OSS 120B (Medium). "Gemini 3.8 Flash (High)" was NOT in the list, so keep the closest option and record that. Press Escape to close.
4. Set the workspace. The input bar has a "Projects" dropdown and a "Local Checkout" dropdown above the box. Check that the project is D:\Projects if it asks.
5. Paste the prompt. Click the input box (about x=800, y=733 full-size). Put the text on the clipboard with `write_clipboard`, then press ctrl+v, then check with a screenshot that the text is there, then press Return.
6. Wait up to 90 seconds. Then check for the done marker: `ls D:/Projects/_SIR/ops/agy-runs/done/hello.done`. The chat should run `python D:/Projects/_SIR/scripts/agy-done.py hello ok test-chat-works` through its terminal tool. That script writes the marker file.

## What the states look like

- Finished: the chat shows a reply starting with "DONE", and the marker file exists.
- Failed: the chat shows an error or a tool-call failure in red. No marker file. Read the error text and retry once.
- Out of credits or quota: a banner or notice about usage limits, or the model chip shows an unavailable state. The "View Usage" item in the model menu shows usage. Do not buy anything. Switch to another model, or record the blocker in OWNER_ACTIONS.
- Sign-in needed: a login screen or account prompt. Stop there and report it. Never type passwords or 2FA codes.

## Blockers seen (2026-11-08)

- The Windows overlay "Windhawk" (not in the computer-use allowlist) kept taking focus. Clicks and key presses were blocked with "Windhawk is not in the allowed applications". Clicking the chat area once brought Antigravity back to the front.
- Key presses (ctrl+v) were aborted by a user interrupt, so the prompt was not pasted and not sent.
- Fix to try: close or hide Windhawk, then repeat steps 2 to 6. Adding Windhawk to the allowlist is a separate permission and needs the user's yes.

## Lessons from the first test (2026-11-08, Ahmed finished the paste by hand; the chat ran and wrote hello.done)
- The app is "Antigravity" (the agent manager, left sidebar: New Conversation, Automations, Customizations). Chats live under the project "Projects" (D:\Projects). The model picker is at the bottom left of the input box and shows "Gemini 3.8 Flash High": check it before sending; do not change it.
- After clicking New Conversation, CLICK INSIDE THE INPUT BOX ("Ask anything, @ to mention, / for actions") first, then paste with ctrl+v, take a 0.4 scale screenshot to confirm the text is in the box, then press Enter. Pasting without a click lands nowhere.
- Get the paste text with: write_clipboard of the contents of the task's `ops/briefs/<name>.prompt.txt` (made by `python D:/Projects/_SIR/scripts/agy-task.py <name> <brief> <cwd>`).
- If a keypress is "aborted by a user interrupt", Ahmed is touching the keyboard: wait 10 seconds and retry once, then report instead of looping.
- Windhawk may steal focus: if clicks are blocked with "not in the allowed applications", press Escape once, click the Antigravity title bar, retry; report if it persists.
- A finished chat shows "Worked for Ns" and the reply; the completion marker `ops/agy-runs/done/<name>.done` is the real signal (the manager's watcher wakes on it). The operator does not wait for it: after Enter and one confirming screenshot, return.
- One task = one new conversation. Name is in the prompt. Never reuse a chat for a different task.

## Working recipe (verified 2026-11-08 by the manager, chat "Execute DS QA Prompt" started)
- Screen coordinate frame is 1456x819 (screenshots at scale 0.5 show 728x409: double the numbers). New Conversation button about (90,97); input box about (700,733).
- Do NOT paste from the clipboard: it can hold an old screenshot and attach an image. Instead, click New Conversation, click the input box, then use the `type` action with ONE short line: "Read D:/Projects/_SIR/ops/briefs/<name>.prompt.txt completely and do exactly what it says." The full brief lives in that file. Confirm with a 0.5-scale screenshot (text in the box, model chip "Gemini 3.8 Flash High"), press Return, confirm the chat shows "Working".
- The model chip must say Gemini 3.8 Flash High. If a new conversation shows another model, click the chip and pick Gemini 3.8 Flash High before sending.

## Batch notes (2026-11-08)
- A draft left in the input box survives "New Conversation" and the next typed text is appended to it (two tasks in one chat). Before typing, make sure the box is empty: click the box, ctrl+a, BackSpace (system key combos are granted). Never type a second task onto an unsent draft.
- Operator runs get "user interrupt" aborts whenever Ahmed touches mouse or keyboard; a batch of five took 3 of 5. The manager starts the remaining chats itself.
- The typed text is the skills line from ops/briefs/_SKILLS_LINE.txt (renders as chips) + the pointer sentence.

## Handling errors and interrupts (operator and troubleshooter rules)
- Do each start as ONE `computer_batch` call: [open/focus Antigravity, click New Conversation, click input box, ctrl+a, BackSpace, type text, screenshot(0.4)], then a second call [Return, screenshot(0.4)]. Fewer calls leaves fewer chances for an abort.
- If an action is aborted ("user interrupt" or focus stolen by Windhawk/Claude): take a 0.4 screenshot, wait 15 seconds, redo the whole batch once. After two failures report the task name and move on; the manager does not retry in a loop.
- Troubleshooter job (run by a Haiku helper only when the batch watcher prints ATTENTION): open Antigravity, look at each chat in the sidebar that has no done marker (ops/agy-runs/done); if it shows an error, stalled or a permission question, answer it (continue / approve), and if it is dead start the same task again in a new conversation. Never type passwords or codes. Report one line per task.

## Always queue a second message (Ahmed, 2026-11-08)
The first prompt often ends after planning or scanning. So after pressing Return on the task prompt, type the line in `ops/briefs/_CONTINUE_LINE.txt` into the same chat's input box and press Return again: it is delivered when the agent stops, and the agent carries on. It is harmless if the agent already finished. The troubleshooter also sends this line to any chat that stopped without a done marker.

## Chats are now one per project (Ahmed organised them, 2026-11-08)
Sidebar chats: "SIR Study", "AHome", "SIR Jobs", "SIR Laptop manager", "SIR Control Room". Never create others. To re-task a chat: click it, click its input box, type "Read D:/Projects/_SIR/ops/briefs/<slug>-standing.prompt.txt completely and do exactly what it says." (slugs: study, ahome, jobs, laptop, control-room), Return, then type the content of ops/briefs/_CONTINUE_LINE.txt and Return. For a plain nudge type only: continue
