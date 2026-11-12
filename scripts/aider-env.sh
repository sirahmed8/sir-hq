# Sourced by cli-run2.sh: sets the provider key/base for an Aider pool entry (keys come from the ignored _local/api-keys.env, never printed).
aider_env() {
  local model="$1"
  set -a; . D:/Projects/_SIR/_local/api-keys.env; set +a
  case "$model" in
    gemini/*) export GEMINI_API_KEY="$GOOGLE_AI_STUDIO_KEY" ;;
    nvidia_nim/*) export NVIDIA_NIM_API_KEY="$NVIDIA_API_KEY" ;;
    openai/@cf/*) export OPENAI_API_BASE="https://api.cloudflare.com/client/v4/accounts/$CLOUDFLARE_ACCOUNT_ID/ai/v1" OPENAI_API_KEY="$CLOUDFLARE_API_TOKEN" ;;
    openai/GLM-5.3) export OPENAI_API_BASE="https://api.sambanova.ai/v1" OPENAI_API_KEY="$SAMBANOVA_API_KEY" ;;
  esac
}
