# Smoke Test: devin status report

## cli_pool.py status output
```
available        kilo|kilo/kilo-auto/free                                ok
cooling 48 min   opencode|opencode/big-pickle                            usage limit
available        devin|swe-2-flash-medium                                ok
available        cursor|auto                                             usage limit
available        pi|groq/openai/gpt-oss-120b                             ok
available        pi|radius/recursive/flint                               ok
available        kilo|kilo/nvidia/nemotron-3-ultra-550b-a55b:free        ok
cooling 49 min   opencode|opencode/glm-5.3-flash-free                    usage limit
available        opencode|opencode/deepseek-v4.1-flash-free              usage limit
available        opencode|opencode/minimax-m3.1-flash-free               usage limit
available        opencode|opencode/mimo-v2.6-flash-free                  usage limit
available        opencode|opencode/nemotron-3.5-lightning-free           ok
cooling 48 min   opencode|opencode/flint-40b-free                        usage limit
available        opencode|opencode/longcat-2.5-free                      usage limit
available        opencode|opencode/beam-free                             ok
available        agy|gemini-3.8-flash-low                                usage limit
available        agy|gemini-3.8-flash-medium                             usage limit
available        agy|gemini-3.8-flash-high                               usage limit
cooling 50 min   agy|gpt-oss-120b-medium                                 usage limit
cooling 51 min   agy|claude-sonnet-4-6                                   usage limit
cooling 52 min   cline|reflection/beam-free                              usage limit
available        aider|groq/openai/gpt-oss-120b                          ok
available        aider|nvidia_nim/nvidia/nemotron-3-ultra-550b-a55b      ok
cooling 927 min  aider|openai/@cf/openai/gpt-oss-120b                    daily free neurons used up (Cloudflare 10000/day)
available        aider|gemini/gemini-flash-lite-latest                   ok
available        aider|gemini/gemini-flash-latest                        ok
```

## model-pool.json devin entry
```json
"devin|swe-2-flash-medium": {
  "last_pick": 1794558684.9856603,
  "until": 0,
  "why": "ok",
  "last_ok": 1794558724.2630599
}
```

Devin did not answer a test prompt in this run; this report only records its pool status as available (ok).