# device-hub (android-device-hub)

## Summary
Instructions for the Android Device Hub sidecar (android-cli plugin): a loopback web server (`android sidecar run device-hub`) whose pane lists/starts/stops/creates/removes AVDs and mirrors any emulator or adb-connected physical device (video + touch/keyboard/mouse input). For agent inspection it documents `android layout` (UI tree: text, IDs, bounds, states), `android screen capture --annotate` + `screen resolve` (tap annotated boxes), `adb shell input` for actions, plus the full HTTP API (/api/devices, /api/jobs, /api/start|stop|create|remove) and its quirks.

## When to use / when NOT
Use when the user wants to see/interact with a device screen (tell them to open the pane and click Mirror — the agent can't see the video), or to check which devices exist / start-stop emulators. For scripted work prefer `android emulator`/`adb` directly — CLI ops show up in the pane anyway. Don't use the pane's proxied URL (needs user browser creds).

## Inputs, outputs, tools
- Inputs: device serial/id, profile name, job actions.
- Outputs: device/job JSON, screenshots with annotated element boxes, UI layout trees.
- Tools: sidecar HTTP API on 127.0.0.1 (port changes each restart — read from sidecar.log), `android layout|screen|emulator` CLI, `adb` (devices/shell input/wait-for-device).

## 5 most important rules
1. You cannot see the mirrored video — inspect via `android layout` first (fast, text), screenshot only when needed (takes seconds).
2. Input you send appears live in the user's mirror; screenshots/layout don't disturb an open mirror.
3. Find the port from the sidecar log's last "listening" line; call 127.0.0.1 directly, never the proxied pane URL.
4. Actions are async jobs — POST returns job_id, poll GET /api/jobs; don't run concurrent jobs on the same device (server doesn't serialize).
5. "Unauthorized" physical device = user must accept the USB-debugging prompt; secure windows (banking/DRM) capture black.

## Risks / things needing the owner
Real device control — taps/typing affect whatever the user has open. `POST /api/remove` deletes AVDs (force flag bypasses checks); stop before remove. adb connect tunnels expose devices on localhost ports.

## Category / tags
mobile · android, emulator, adb, device-hub, sidecar, tooling

## Revisions
Five tools hold it (codex, cursor, gemini-plugin, kilo, opencode, windsurf — no claude); codex copy chosen, all ~7818 bytes identical.
