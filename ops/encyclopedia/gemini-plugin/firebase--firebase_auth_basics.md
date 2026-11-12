# firebase_auth_basics

- Tool: `gemini-plugin` (plugin: `firebase`)
- Category: security
- Source: `C:\Users\a7med\.gemini\config\plugins\firebase\skills\firebase_auth_basics\SKILL.md`
- SKILL.md size: 4179 chars

## What it does

Set up and configure Firebase Authentication.

## Structure (headings inside SKILL.md)

- Prerequisites
- Core Concepts
- Users
- Identity Providers
- Tokens
- Workflow
- 1. Provisioning
- 2. Client Setup & Usage
- 3. Security Rules
- (none)

## Tools / MCPs it needs

- none declared

## Risks / cautions found in text

- - **Email/Password**: Basic email and password authentication.
- - **ID Token**: Short-lived (1 hour), verifies identity.
- - **Refresh Token**: Long-lived, used to get new ID tokens.
- 1. Enable the desired Sign-in providers (e.g., Email/Password, Google).

## Key rules (verbatim lines from SKILL.md)

1. - **Firebase Project**: Created via
2. - **Firebase CLI**: Installed and logged in (see `firebase-basics`).
3. - `uid`: Unique identifier.

## Files inside the skill

- `references/client_sdk_android.md` — "Firebase Authentication on Android (Kotlin)"
- `references/client_sdk_web.md` — "Firebase Authentication Web SDK"
- `references/flutter_setup.md` — "Firebase Auth & Google Sign-In for Flutter"
- `references/ios_setup.md` — "Firebase Auth iOS Setup Guide"
- `references/security_rules.md` — "Authentication in Security Rules"
