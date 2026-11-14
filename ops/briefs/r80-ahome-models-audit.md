# AHome: local AI models audit

Owner request (2026-11-14): check whether AHome's local AI needs more/different Ollama models for its features (chat, voice/STT, vision/photos, smart home commands, escalation).
1. Inventory AHome AI features in apps/local-core (smart_ai_router.py, ai_profiles.py, ollama_stream.py, telegram gateway, voice/photo handling).
2. For each feature list which model(s) it uses and whether qwen3.5:9b covers it; flag gaps (e.g. embeddings, vision, whisper/STT, TTS).
3. Recommend concrete models to pull (ollama pull) with size/RAM impact on a 24GB RTX4050 laptop; do NOT pull multi-GB models without noting RAM cost - prefer small ones.
4. Private rule: AHome content never leaves the PC - local models only.
5. Write findings to .sir/CHECKPOINT.md and commit.
