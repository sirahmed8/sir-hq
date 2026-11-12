# Free AI coding tools and models, ranked (research 2026-11-12)

Sources: vendor docs and pricing pages read through search on 2026-11-12, plus local logs. Items marked "not verified" were not read from the vendor page in this pass. No accounts were created and no keys were requested.

## Ranked list

1. **OpenCode free models, new in the pool: `opencode/nemotron-3.5-lightning-free`, `opencode/beam-free`.** Free "for a limited time" (no number stated). Headless: `opencode run -m <id> "<task>"`. Can edit files: yes, proven (see the AI_TOOLS_CONTROL.md section). Risk: Beam keeps data 30 days; Nemotron is NVIDIA trial use, do not send personal or confidential data. Never for AHome.
2. **Local Ollama models** (qwen3:8b, qwen3:4b, already in the pool): unlimited, private, runs on the RTX 4050 6 GB. Headless via the qwen, goose and crush branches. Can edit files: yes for qwen3 (qwen3:4b proven in r36). Risk: slow and weaker on hard work. This is the only pool allowed for AHome.
3. **Kilo auto-free** (`kilo/kilo-auto/free`, already in the pool): 200 requests per hour per IP, no credits needed. Headless: `kilo run --auto`. Can edit files: yes. Risk: rolling-hour limit reached in r42.
4. **OpenCode big-pickle and other stealth free models** (already in the pool): quota not stated. Risk: stealth models may use data for training (privacy page). Not for private work.
5. **OpenRouter `:free` models** (already in the pool): 50 requests per day for the account, 20 per minute; 1,000 per day only after buying 10 USD (not allowed by the owner). Headless via OpenCode. Risk: the 50 per day is shared by every free model on the account. The runner now puts all of them on cooldown together.
6. **Devin CLI free plan** (already in the pool): "light quota", SWE-2 in slow mode. No quota banner seen in 47 rounds. Risk: quota not published, shared across Devin products.
7. **Gemini via Antigravity accounts** (already in the pool): Pro accounts with 5-hour and weekly windows; usage per account in ACCOUNT_LEDGER.md.

Rejected or blocked in this pass:
- **Qwen Code OAuth free tier**: discontinued 2026-04-15 by Alibaba (sources: inventivehq, Reddit r/LLMDevs, Yahoo tech). Only the local Ollama route still works.
- **GitHub Models**: retired 2026-07-30 (GitHub docs). Not usable.
- **Gemini CLI with the current Google login**: `IneligibleTierError`, the client is no longer supported. Gemini CLI with an AI Studio key: 250 requests per day (Gemini CLI docs), but needs a key (see owner list).

## Needs the owner (one tap, each needs a new account or a key)

Agents will not create accounts or request keys. The owner decides each one.

- **Groq** (console.groq.com): free tier with no card. 14,400 requests per day on llama-3.1-8b-instant, 1,000 per day on 70B models, 30 requests per minute (Groq rate-limit docs, grizzlypeaksoftware summary). Headless via OpenAI-compatible base URL in opencode, crush or qwen. Can edit files: expected, not tested. Daily reset at UTC midnight (inferred).
- **Cerebras** (cloud.cerebras.ai): free tier about 1,000,000 tokens per day, 30 requests per minute (getaiperks summary; Cerebras docs say the first purchase unlocks higher limits). Risk: the daily-cap figure comes from a third-party summary, not the vendor page.
- **Cloudflare Workers AI**: 10,000 Neurons per day free on Workers Free, reset 00:00 UTC (Cloudflare docs). Needs a Cloudflare account. Headless via API token.
- **NVIDIA NIM** (build.nvidia.com): 1,000 free credits and 40 requests per minute on the free developer account (NVIDIA forum posts, not the vendor page). Needs an account.
- **Mistral La Plateforme**: free tier with no card (blog summary, not verified on the pricing page). Needs an account and a phone number.
- **Hugging Face Inference Providers**: monthly credits; figures conflict across sources (0.10 USD per month vs 100K credits), so not verified. Needs an account.
- **SambaNova Cloud**: free tier applied when no payment method is linked; limits are on the rate-limit docs page (not read in full). Needs an account.
- **Google AI Studio API key** for Gemini CLI: 250 requests per day on the free unpaid tier (Gemini CLI docs). Needs a key on the project's own GCP project (AGENTS.md rule).
- **Google Jules**: free entry tier of 15 tasks per rolling 24 hours (Jules usage-limits page, cited by activepieces). Asynchronous cloud agent, not a headless CLI, so it does not fit cli-run2.sh. Needs a Google sign-in on a new service.
- **Kiro** (AWS): free tier of 50 credits per month (kiro.dev pricing). Needs an AWS Builder ID account.

Not verified in this pass (no time to read the vendor pages): Warp, Amp free mode, Zed, Windsurf (IDE only; the survey says no CLI), Copilot free allowance, Kimi free membership.
