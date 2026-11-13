# r73-laptop-ollama-single-instance

Found by the backup-manager session 2026-11-13: two Ollama servers were listening on the same port area - the normal user one plus a second server started by SIR Laptop Manager ops_ui (pythonw pid 7548, seen by the local-ai teammate). The duplicate loaded a second copy of the model in RAM (about 3 GB) and made local AI slower and riskier on a 24 GB laptop.

## Do
1. Find every place in SIR Laptop Manager (ops_ui and any helper) that starts `ollama serve` or the Ollama app. Make it check http://127.0.0.1:11434/api/tags first and never start a second server.
2. If it needs a server, reuse the existing one; if it must start one, start only when nothing answers and stop it on exit.
3. Add a test that simulates "already running" and asserts no second spawn.
4. Keep the user's env: OLLAMA_MAX_LOADED_MODELS=2, OLLAMA_NUM_PARALLEL=1, OLLAMA_CONTEXT_LENGTH=16384, OLLAMA_FLASH_ATTENTION=1, OLLAMA_KV_CACHE_TYPE=q8_0. Do not change the user env.
5. Local checks: project's tests, linters; commit and push to main. CI is red only because of the Actions quota flag, so local green is the gate.
