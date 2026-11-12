# API keys status, 2026-11-12

Values are stored only in _SIR/_local/api-keys.env (gitignored, verified with git check-ignore).

| Service | Status | Detail |
|---|---|---|
| Groq | done (2026-11-12, owner solved CAPTCHA) | Key "sir-autogen-2026-11-12", no expiration. Var: GROQ_API_KEY |
| Cerebras | blocked | API access needs a payment method ("Add payment method" to activate keys, $5 credit offered). No free option offered. Skipped, no key created. |
| Google AI Studio | done | Key created in the imported project "11Players" on free tier. Var: GOOGLE_AI_STUDIO_KEY |
| NVIDIA NIM | done | Key generated (name NVIDIABuild-Autogen-29, valid 12 months). Var: NVIDIA_API_KEY |
| Cloudflare Workers AI | done | API token "sir-workers-ai-read" with only Workers AI: Read, all accounts, no expiration. Account ID noted. Vars: CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID |
| Mistral | blocked | Free plan: "New key" is disabled until the org upgrades. Upgrade not taken. Var not set. |
| SambaNova | blocked | Signed-in onboarding wizard asks for profile, payment and credits. Not completed. Var not set. |
| Hugging Face | done (2026-11-12) | Read-only token "sir-readonly-2026-11-12". Var: HF_TOKEN |
| OpenRouter | skipped | Already has keys per instructions. |

Variables present in the file: GOOGLE_AI_STUDIO_KEY, NVIDIA_API_KEY, CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID.
Added 2026-11-12: HF_TOKEN, GROQ_API_KEY.
Missing: CEREBRAS_API_KEY (needs payment method), MISTRAL_API_KEY (needs upgrade), SAMBANOVA_API_KEY (needs onboarding and payment).
