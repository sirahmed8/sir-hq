# Free tools organization (owner order 2026-11-13)

Rule: no two tools share the same upstream API/provider/account. Two tools on one
provider spend one shared quota, so the second adds nothing. The worker pool
(`scripts/cli_pool.py`) now holds exactly one entry per provider, strongest first.
The Telegram backup-manager chain (`scripts/backup_manager.py` CHAIN) walks the
same providers best to worst so Ahmed always gets an answer.

## Active pool (one tool per provider)

| Order | Pool entry | Provider / account | Notes |
|---|---|---|---|
| 1 | `kilo|kilo/kilo-auto/free` | Kilo free router | serves Nemotron and frontier models |
| 2 | `opencode|opencode/big-pickle` | OpenCode Zen free tier | |
| 3 | `devin|swe-2-flash-medium` | Devin / Cognition free plan | this session's model |
| 4 | `aider|groq/openai/gpt-oss-120b` | Groq API key | fast, small quota |
| 5 | `aider|nvidia_nim/nvidia/nemotron-3-ultra-550b-a55b` | NVIDIA NIM key | |
| 6 | `agy|claude-sonnet-4-6` | Google Antigravity account | quota windows, rotates accounts |
| 7 | `aider|openai/@cf/openai/gpt-oss-120b` | Cloudflare Workers AI | ~10k free neurons/day, shared per account |
| 8 | `cline|reflection/beam-free` | Beam via Cline | needs one owner sign-in, thinking high |
| 9 | `pi|radius/recursive/flint` | Recursive flint via Radius | |

Local (this PC, no provider): `qwen`, `goose`, `crush` via Ollama — background and
AHome-only work, never the coding pool (owner order: local models are not for coding).

## Removed duplicates (same provider as a kept entry)

- `kilo|kilo/nvidia/nemotron-3-ultra-550b-a55b:free` — same NVIDIA quota as the aider NIM entry; Kilo auto already fronts it.
- `opencode|opencode/glm-5.3-flash-free`, `deepseek-v4.1-flash-free`, `minimax-m3.1-flash-free`, `mimo-v2.6-flash-free`, `nemotron-3.5-lightning-free`, `flint-40b-free`, `longcat-2.5-free`, `beam-free` — all OpenCode Zen free tier, one quota; `big-pickle` is the kept representative. The small ones also mix Chinese/Russian into Arabic replies.
- `agy|gemini-3.8-flash-low/medium/high`, `agy|gpt-oss-120b-medium` — same Antigravity account quota as `claude-sonnet-4-6`; one entry per account.
- `aider|gemini/gemini-flash-lite-latest`, `aider|gemini/gemini-flash-latest` — same Google AI Studio key as nothing else kept; Gemini CLI itself is ineligible for Code Assist individuals, so the key stays unused for now.
- `cursor|auto`, `pi|groq/openai/gpt-oss-120b` — Cursor needs its own plan; Groq is already covered by the aider Groq entry (same API key quota).

## Installed but out of the pool (leftovers — owner decides keep or delete)

- **Codex CLI** — ChatGPT account quota exhausted until ~2026-11-27, then usable again.
- **Gemini CLI** — installed, but Google says Code Assist individuals must migrate to Antigravity; unusable as-is.
- **Kimi Code CLI** — logged in but the account has no Kimi Code plan (`provider.auth_error`).
- **Cline** — signed in, only the free `beam-free` model is wired (pool entry 8); the default model is paid and never used.
- **ZCode (GLM)** — signed out since 2026-11-11; sign-in stays with the owner. GLM also reachable through OpenCode/Kilo pool models.
- **Aider extra providers** — SambaNova removed (billing), HuggingFace skipped (paid credits), Groq/NVIDIA/Cloudflare/Gemini keys live in `_local/api-keys.env` (gitignored).
- **DeepSeek Harness (dsh)** — the desktop app Ahmed used on 2026-11-13; its account hit "Insufficient Balance". Kept installed; not in the pool.
- **Factory (factory-desktop)** and **Bionic** — desktop apps, running; not CLI pool tools.
- **OpenClaw** — multi-channel gateway, running; its Telegram channel uses a different bot token than the SIR manager bot, so no conflict. WhatsApp channel was not present in `channels list`.
- **Hermes Agent** — the intended primary manager app; gateway runs on local `qwen3.5:9b` (see `ops/HQ_CHECKPOINT.md` 2026-11-13 16:50 note).

## Best tool for talking to the local AI

Direct Ollama HTTP API (`http://127.0.0.1:11434`) is the proven path: a real
`think:false` generation answered in ~3 s on 2026-11-13. `ollama run` CLI works but
interactive/thinking modes are slow for chat. **Pick: the Ollama API** (used by
Hermes, OpenClaw and AHome local-core already). `aider` remains the best CLI wrapper
when a tool must drive Ollama with files; `goose`/`crush`/`qwen` CLIs are installed
but unproven for chat (goose not on PATH in minimal envs, qwen CLI arg quirks).
