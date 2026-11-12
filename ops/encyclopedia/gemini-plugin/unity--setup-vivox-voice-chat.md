# setup-vivox-voice-chat

- Tool: `gemini-plugin` (plugin: `unity`)
- Category: build
- Source: `C:\Users\a7med\.gemini\config\plugins\unity\skills\setup-vivox-voice-chat\SKILL.md`
- SKILL.md size: 8784 chars

## What it does

Adds and configures in-game voice and text chat with Unity Vivox. Use when the user asks about voice chat, microphone permissions, mute controls, proximity voice, team and lobby channels, or direct messages.

## When to use (from skill text)

- 4. All events consumed by the code are subscribed **before** the async call that triggers them, and are unsubscribed in `OnDestroy`.

## Structure (headings inside SKILL.md)

- Unity Vivox — Voice & Text Chat
- Documentation Map
- Detailed References
- Initialization Order (Do Not Skip Steps)
- Joining Channels
- Text Messaging
- Required Event Subscriptions
- Access Tokens (Brief)
- Validation
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Init, sign-in, and access tokens:** [references/init-and-login.md](references/init-and-login.md)
- - If Unity Authentication (`AuthenticationService`) is not used, the player identity falls back to a per-session GUID — display names still work but you lose cross-session identity. See [references/init-and-login.md](references/init-and-login.md) for the Vivox Access Token (VAT) alternative.
- 8. No HMAC signing keys or Vivox `SECRET`/`APP_ID` are embedded in client code — VAT-based flows are documented but delegated to a server.

## Key rules (verbatim lines from SKILL.md)

1. 4. All events consumed by the code are subscribed **before** the async call that triggers them, and are unsubscribed in `OnDestroy`.
2. 7. Android builds request `RECORD_AUDIO` at runtime before joining an audio channel; iOS builds have `NSMicrophoneUsageDescription` in the plist.

## Files inside the skill

- `references/events-and-participants.md` — "Events, Participants, and Lifecycle"
- `references/init-and-login.md` — "Initialization and Login"
- `references/text-chat.md` — "Text Chat"
- `references/troubleshooting.md` — "Troubleshooting and Platform Notes"
- `references/voice-channels.md` — "Voice Channels"
