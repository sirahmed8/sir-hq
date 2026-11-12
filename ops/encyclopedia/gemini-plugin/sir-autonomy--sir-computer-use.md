# sir-computer-use

Tools: gemini-plugin (sir-autonomy). Source: C:\Users\a7med\.gemini\config\plugins\sir-autonomy\skills\sir-computer-use\SKILL.md (27 lines, read in full)

## Summary
Full native Windows desktop control modeled on Claude Computer Use / OpenAI Operator: screenshots, mouse move/click/drag/scroll, Unicode+Arabic text typing, key/hotkey presses, window listing/focus, app launching, and atomic batch sequences — via `sir_computer_*` tools or `sir_ctl.py computer` CLI. Runs on Ahmed's laptop without permission prompts.

## When to use / not use
Use when a task genuinely needs OS-level GUI control — apps without APIs, legacy software, OS dialogs, or visual verification of desktop tools. NOT for anything achievable via CLI/files/API (those are cheaper and safer), web-only tasks (use sir-browser), or headless environments.

## Inputs, outputs, dependencies
Input: desktop intents (screenshot path, click coords, type text, key/hotkey, window title/hwnd, batch sequences). Output: screenshots, action confirmations. Needs: the sir-autonomy MCP tools or `python D:\Projects\_SIR\tools\sir-autonomy\sir_ctl.py computer <cmd>`; Windows session with the bridge running.

## Key rules
1. Screenshot → decide → act loop: capture full-res screenshot, identify target, then click/type — pixel coordinates are the addressing scheme (no accessibility refs like sir-browser).
2. `sir_computer_batch` runs sequences atomically — use for multi-step GUI flows where partial execution would leave inconsistent state.
3. Unicode/Arabic typing is supported — relevant for Arabic-language apps and RTL UI automation.
4. Window management is handle/title-based: list windows first to get titles/bounds/handles, then focus by title_or_hwnd.

## Risks / owner items
- Same zero-prompt blast radius as sir-browser but worse: arbitrary clicks/keystrokes can delete files, send messages, change system settings — there is no undo and no gate.
- Coordinate-based clicking breaks with resolution/DPI changes, window moves, or UAC-secure desktops (screenshots may not capture elevated windows).
- Race conditions: the screen can change between screenshot and click — verify state after actions.
- Keystroke injection into password fields or secure desktops is a credential-theft-shaped capability; agents must never type into auth prompts.

## Category and tags
automation, ops — computer-use, windows, desktop-automation, mcp, high-privilege.

## Revision note
Single plugin revision; desktop counterpart to sir-browser in the sir-autonomy suite.
