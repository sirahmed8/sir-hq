# firebase-ai-logic-basics

## Summary
Guide for integrating Firebase AI Logic (formerly "Vertex AI for Firebase") — client-side SDK access to Gemini models for web/Android/iOS/Flutter/Unity — covering setup (`firebase init ailogic` provisions the backend), model selection (Gemini Developer API free tier vs Agent Platform/Blaze), core capabilities (text, multimodal, chat sessions, streaming, image gen "Nano Banana", googleSearch grounding), advanced features (structured JSON output, on-device hybrid inference), and production hardening (mandatory App Check + debug tokens for dev/CI, Remote Config for model names).

## When to use / when NOT
Use when adding Gemini-powered features to an app through Firebase AI Logic. Do NOT use older model names (gemini-2.0-pro/flash are shutdown — always check the models doc); do NOT treat `flutterfire configure` as sufficient — `firebase init ailogic` is REQUIRED or calls fail PERMISSION_DENIED. Not for server-side-only Gemini use (plain google-genai SDK may fit better).

## Inputs, outputs, tools
- Inputs: target platform (web/Android/iOS/Flutter/Unity), chosen provider (Developer API default; Agent Platform for enterprise scale/Blaze), app with Firebase project.
- Outputs: initialized AI Logic service + platform SDK integration code (per references: usage_patterns_web/android, ios_setup, flutter_setup).
- Tools: `npx -y firebase-tools@latest init ailogic`, `projects:list`, `apps:list`; firebase JS SDK (`npm install firebase@latest`); App Check (reCAPTCHA Enterprise); Remote Config; references/*.md per platform.

## 5 most important rules
1. ALWAYS run `npx firebase-tools init ailogic` — without it the service is not provisioned and calls return PERMISSION_DENIED; flutterfire configure does NOT enable AI Logic.
2. Default to Gemini Developer API (free tier prototyping); Agent Platform Gemini API only when enterprise scale/Blaze is required.
3. NEVER use deprecated model names — check the official models doc for current names before writing code; prefer Remote Config for model names so updates need no redeploy.
4. App Check is MANDATORY for safe production use; for local dev/CI use debug tokens (web `FIREBASE_APPCHECK_DEBUG_TOKEN`, Android DebugAppCheckProviderFactory, iOS AppCheckDebugProviderFactory), register the UUID in console, and store CI tokens as secrets.
5. Files >20MB must go through Cloud Storage for Firebase (pass URLs), not inline data (HTTP 413); use generateContentStream for streaming UX and JSON schema for structured output.

## Risks / owner needs
Blaze plan needed for Agent Platform and image generation; App Check setup needs console access; API keys/quota are owner-managed. On-device hybrid requires Chrome setup.

## Category and tags
Category: ai. Tags: firebase, gemini, ai-logic, llm, multimodal, app-check, mobile.

## Revisions
Identical across claude/codex/cursor/gemini-plugin/kilo/opencode/windsurf; claude copy used.
