# API keys status, 2026-11-12

Values are stored only in _SIR/_local/api-keys.env (gitignored, verified with git check-ignore).

| Service | Status | Detail |
|---|---|---|
| Groq | blocked | Signed in, but the key form shows a Cloudflare "Verify you are human" CAPTCHA. Not completed. No key created. |
| Cerebras | blocked | Signed in, but key generation opens a billing choice (Pay as You Go or Limited Credits). Not chosen. No new key created. Existing "Default Key" is masked and its full value is not readable without that step. |
| Google AI Studio | done | Key created in the imported project "11Players" on free tier. Var: GOOGLE_AI_STUDIO_KEY |
| NVIDIA NIM | done | Key generated (name NVIDIABuild-Autogen-29, valid 12 months). Var: NVIDIA_API_KEY |
| Cloudflare Workers AI | done | API token "sir-workers-ai-read" with only Workers AI: Read, all accounts, no expiration. Account ID noted. Vars: CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID |
| Mistral | blocked | Not signed in: console redirected to the login page. Owner must sign in. |
| SambaNova | blocked | Not signed in: redirected to sign-up page. Account creation is owner-only. |
| Hugging Face | blocked | Page asked for password re-confirmation ("Confirm your identity"). Not entered. |
| OpenRouter | skipped | Already has keys per instructions. |

Variables present in the file: GOOGLE_AI_STUDIO_KEY, NVIDIA_API_KEY, CLOUDFLARE_API_TOKEN, CLOUDFLARE_ACCOUNT_ID.
Missing: GROQ_API_KEY, CEREBRAS_API_KEY, MISTRAL_API_KEY, SAMBANOVA_API_KEY, HF_TOKEN.
