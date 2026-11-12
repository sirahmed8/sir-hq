# Usage limits of every AI tool in the SIR pool (2026-11-12)

Read from vendor docs (checked 2026-11-12), from runner logs under `ops/agy-runs/cli-*.log` (banner text and round headers), and from `ops/ACCOUNT_LEDGER.md`. No test messages were sent to any tool to measure quota. Rows marked "inferred" are not stated by the vendor.

## Table

| Tool and model (pool entry) | Free quota | Reset rule | Last observed limit hit | Expected return |
|---|---|---|---|---|
| Kilo `kilo/kilo-auto/free` | 200 requests per hour per IP (Kilo docs) | rolling hour (per docs) | "Too Many Requests: Free model usage limit reached" in r42, log mtime 2026-11-12 03:15 UTC | within about 1 hour of the last hit (inferred from the rolling window) |
| OpenCode `opencode/big-pickle` (stealth, free for a limited time) | not stated by vendor | not stated | "Free usage limit reached. Connect a provider or subscribe to OpenCode Go" in r42, 2026-11-12 02:58 | unknown, inferred daily |
| OpenCode `opencode/longcat-2.5-free` | 100 requests per day (OpenCode docs) | per day (docs say "per day") | not seen in logs | next day |
| OpenCode other `-free` models (glm-5.3-flash, deepseek-v4.1-flash, minimax-m3.1-flash, mimo-v2.6-flash, flint-40b, beam-free, nemotron-3.5-lightning-free) | "free for a limited time", no number stated | not stated | "Free usage limit reached" for glm and deepseek, 2026-11-10 22:22 (r19) and 2026-11-11 (r14) | unknown, inferred daily |
| OpenRouter `:free` models (opencode `openrouter/openrouter/free`, `openrouter/nvidia/nemotron-3-ultra-550b-a55b:free`) | 20 requests per minute and 50 requests per day for the whole account, all `:free` models together. 1,000 per day only after the account has bought 10 USD of credits (owner rule: no payment, stays at 50) | per day; reset time not in the docs, inferred 00:00 UTC | "Rate limit exceeded: free-models-per-day" in r18 (2026-11-10 21:33) and r19 (22:20) | next 00:00 UTC (inferred) |
| Devin CLI `swe-2-flash-medium` (Free plan) | "light quota" plus unlimited inline edits; SWE-2 in slow mode (usagepricing summary) | not stated | no quota banner in 47 rounds; only permission refusals before the runner moved to dangerous mode | unknown, quota is shared across Devin products |
| Antigravity `agy` (Gemini 3.8, Claude, GPT-OSS), per Google account | Pro accounts: 5-hour window and weekly limit per model group | 5-hour window and weekly window (shown in Settings > Models) | a7medorabe7 weekly 10% left, reset in about 4d6h at 2026-11-09 (ledger); a01083835229 weekly 0% at 2026-11-09 night, reset about 5d; sirahmedalaa2006 "Model quota reached", refresh 11/17 02:36 | per account, see ledger rows; approx. 2026-11-13 to 2026-11-17 |
| Codex CLI (`codex|gpt-6-luna`, not on PATH) | ChatGPT plan monthly limit | monthly | "You've hit your usage limit ... try again at Nov 27th, 2026 9:08 AM" (r36, log line 883) | 2026-11-27 09:08 local, from the banner |
| Gemini CLI (`gemini|default`) | Google sign-in: 1,000 requests per user per day (Gemini CLI docs). API key: 250 per day | per day | not a quota problem: `IneligibleTierError ... migrate to the Antigravity suite` (r36 notes) | not usable with this account; no return date |
| Qwen CLI (local Ollama) | unlimited (local) | none | none | none. Qwen OAuth free tier was discontinued 2026-04-15 (Alibaba) |
| Goose, Crush, Aider with local Ollama (`qwen3:4b`, `qwen3:8b`) | unlimited, limited only by the 6 GB GPU and RAM | none | none | none |
| Claude (HQ manager, Anthropic) | weekly allowance; "Fable reset" free once | weekly, resets Sunday 02:00 (ACCOUNT_ROTATION.md) | weekly 54% used at 2026-11-10 | Sunday 02:00; Fable reset expires 2026-11-17 09:59 GMT+2 |
| Cline (`cline|default`) | not verified | not verified | "Unauthorized, re-authenticate" (r36) | not usable until the owner signs in once |
| Kimi (`kimi|default`) | not verified | not verified | "No model configured. Run kimi and use /login" (r36) | not usable until the owner signs in once |
| Copilot (OpenCode GitHub Copilot login) | not verified | not verified | none | not verified |

## Who works when (owner rule, 2026-11-12)

1. Claude and Anthropic first. This is HQ and only as far as the weekly allowance allows (until 2026-11-23 per the owner).
2. The free CLIs and models, in the order of `scripts/cli_pool.py` POOL: Kilo auto-free, OpenCode free models (big-pickle, glm, deepseek, minimax, mimo, nemotron-3.5-lightning, flint, longcat, beam), Devin, then the OpenRouter free models (shared 50 per day), then Antigravity accounts, then local Ollama (qwen3 4b and 8b, goose, crush). Local models are the only pool for AHome (`--local` in the runner).
3. Haiku agents last. Never Sonnet.

## Rules that the runner now enforces

- An OpenRouter daily-cap message puts every `openrouter/` entry on cooldown until 00:00 UTC, because they share one account cap.
- Limit and setup checks read error lines only, so worker output that mentions "quota" or "unauthorized" no longer puts a model on cooldown.
- AHome tasks use local models only (AGENTS.md law). Earlier AHome rounds (cli-r14-ahome, cli-r18-ahome-phone, cli-r21-ahome, cli-audit-ahome-*) ran through outside free models; flag for the owner.
