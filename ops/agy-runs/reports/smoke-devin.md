# Smoke Test: Devin Status Report

## cli_pool.py status output
```
available        kilo|kilo/kilo-auto/free                                ok
cooling 23 min   opencode|opencode/big-pickle                            usage limit
available        devin|swe-2-flash-medium                                ok
available        cursor|auto                                             failed fast (exit 1)
available        pi|groq/openai/gpt-oss-120b                             ok
available        pi|radius/recursive/flint                               ok
available        kilo|kilo/nvidia/nemotron-3-ultra-550b-a55b:free        ok
cooling 23 min   opencode|opencode/glm-5.3-flash-free                    usage limit
available        opencode|opencode/deepseek-v4.1-flash-free              usage limit
available        opencode|opencode/minimax-m3.1-flash-free               usage limit
available        opencode|opencode/mimo-v2.6-flash-free                  usage limit
available        opencode|opencode/nemotron-3.5-lightning-free           ok
available        opencode|opencode/flint-40b-free                        ok
available        opencode|opencode/longcat-2.5-free                      usage limit
available        opencode|opencode/beam-free                             ok
cooling 111 min  kilo|kilo/openrouter/free                               needs setup/auth or tools refused
cooling 111 min  opencode|openrouter/openrouter/free                     needs setup/auth or tools refused
available        agy|gemini-3.8-flash-low                                usage limit
available        agy|gemini-3.8-flash-medium                             usage limit
available        agy|gemini-3.8-flash-high                               usage limit
cooling 24 min   agy|gpt-oss-120b-medium                                 usage limit
cooling 24 min   agy|claude-sonnet-4-6                                   usage limit
cooling 25 min   cline|reflection/beam-free                              usage limit
available        aider|groq/openai/gpt-oss-120b                          ok
available        aider|nvidia_nim/nvidia/nemotron-3-ultra-550b-a55b      ok
cooling 1169 min aider|openai/@cf/openai/gpt-oss-120b                    daily free neurons used up (Cloudflare 10000/day)
available        aider|gemini/gemini-flash-lite-latest                   ok
available        aider|gemini/gemini-flash-latest                        ok
```

## Devin entry from model-pool.json
```json
"devin|swe-2-flash-medium": {
  "last_pick": 1794543789.4822404,
  "until": 0,
  "why": "ok",
  "last_ok": 1794543820.6216588
}
```

Devin (swe-2-flash-medium) is available (`until: 0`, `why: ok`) and was last picked at timestamp 1794543789.48 with last successful run at 1794543820.62.

Devin did not answer a test prompt in this run; this verification was performed by Kilo checking the pool status.