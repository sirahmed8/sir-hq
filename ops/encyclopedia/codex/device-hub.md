# device-hub

- Tool: `codex`
- Category: media
- Source: `C:\Users\a7med\.codex\skills\device-hub\SKILL.md`
- SKILL.md size: 7818 chars

## What it does

Instructions for working with the Android Device Hub sidecar, which lists, starts, stops, creates and removes Android Virtual Devices (AVDs), lists physical devices connected to adb, and lets the user mirror and control any of them (video, touch, keyboard, mouse wheel) in the Device Hub pane. Also explains how to inspect and interact with the screen the user is mirroring, with `android layout`, `android screen` and `adb`.

## Structure (headings inside SKILL.md)

- Android Device Hub Skill
- When to use it
- Inspecting the mirrored screen
- Finding the server
- HTTP API
- Read
- Actions
- Mirroring
- Guidelines
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - `POST /api/remove` `{"device": "<avd id>", "force": false}`: delete an AVD. Stop it first; this is not checked. `force` deletes

## Key rules (verbatim lines from SKILL.md)

1. - "Unauthorized" means the user must accept the "Allow USB debugging?" prompt on the device.
2. 1. Check `GET /api/devices` (or `android emulator list` and `adb devices`) before starting a device, to avoid starting one that is
3. 2. Do not start several jobs on the same device at once (e.g. start and remove): the server does not serialize them.
4. 3. After starting an emulator for the user to look at, tell them they can mirror it from the Device Hub pane.

## Files inside the skill

- (SKILL.md only)
