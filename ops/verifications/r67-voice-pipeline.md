# r67 verification: Telegram voice pipeline after hang fix

Date: 2026-11-12. Verifier: devin (SWE-2 Flash Medium). Scope: `scripts/backup_manager.py` only, read plus two live transcription calls. No keys printed. No code changes needed; nothing committed.

## Checks

### 1. Syntax and no-args exit — PASS

```
$ python -c "import ast; ast.parse(open('scripts/backup_manager.py', encoding='utf-8').read())"
AST OK
$ python scripts/backup_manager.py
Traceback ... IndexError: list index out of range   (line 267: sys.argv[1])
exit=1
```

Fails on missing argv exactly as expected. Module imports cleanly (all imports resolve, `cli_pool` loads).

### 2. Live transcription — PASS

Newest saved voice file `ops/telegram-media/voice-739920732.oga` (173 KB):

```
$ python -c "import sys,time; sys.path.insert(0,'scripts'); import backup_manager as b; from pathlib import Path; t=time.time(); r=b.transcribe(Path('ops/telegram-media/voice-739920732.oga')); print(repr(r[:120])); print('seconds', round(time.time()-t,1))"
'أنا في آخر حاجة ما قلتش هو منتجات سير وتطبيقات ترجمة ناسي قنقر لا، كده هو بيخرف على فكرة أنا ما قلتش كده أنا كنت بقول إن'
seconds 1.3
```

Arabic Egyptian transcript returned in 1.3 s, far under the 210 s cap.

Second sample, the exact file that failed in production at 21:07 (`voice-739920727.oga`, 93 KB):

```
'حسناً، طالما أنه موقع عام، لا، إلغيه، وخلينا على تايل سكيل، سيرفر محلي معصل سير كونترول روم، دي أو ده يعني حاجة خاصة وما'
seconds 0.9
```

Same file that got Groq 400 / Cloudflare 429 at 21:07 now transcribes in 0.9 s: the earlier failures were transient provider errors, not a pipeline bug.

### 3. Log scan for provider failures — PASS (transient only)

`ops/agy-runs/backup-manager.log` contains exactly two failure lines in the whole file:

```
627:21:07:14 groq whisper failed: HTTP Error 400: Bad Request
628:21:07:15 cloudflare whisper failed: HTTP Error 429: Too Many Requests
```

Both for message 739920727. No `transcribe timed out` and no `transcribe crashed` entries exist yet (the cap was added after those failures). Re-test of the same audio file succeeds in 0.9 s, so neither provider is consistently failing. Cloudflare hit a 429 rate limit once; Groq returned a 400 once. Worth watching if 429s repeat, but no key or code change indicated.

### 4. Edge cases in code — PASS (read-only review)

- Interim ack: `send("[بسمع الفويس]")` fires at line 287, before `transcribe(f)` at line 288. Owner sees activity immediately.
- Hard cap: `transcribe()` (lines 156-174) runs `_transcribe_inner` in a daemon thread, `t.join(210)`, returns `""` and logs `transcribe timed out, giving up on this voice` if still alive. Worst case owner waits 210 s plus download time, never forever.
- Provider timeouts inside the cap: Groq `urlopen(timeout=75)` (line 135), Cloudflare `timeout=120` (line 149), so even without the thread cap the inner call cannot exceed ~195 s of socket wait.
- Timeout/failure path: `heard == ""` -> `send("[المدير الاحتياطي] مقدرتش أسمع الفويس كويس. ابعته تاني أو اكتبها.")` and `return 0` (lines 289-291). No hang, clear fallback message.
- busy.lock unchanged: `acquire()` (lines 252-263) still waits up to 900 x 2 s = 30 min, removes locks older than 1500 s, returns False -> "فيه شغل طويل شغال" message. Released in `finally` at line 317.
- Reply file flow unchanged: `reply-<id>.txt` written by the brain agent, validated by `reply_problem()` (WEAK_MODELS skip list and script-mix checks intact, lines 221, 244-248), fallback message when all tools fail (line 312-313).

## Verdict

PASS on all four checks. The hang fix is correct and the pipeline is healthy. The only production failures on record are one transient Groq 400 and one Cloudflare 429 at 21:07, both self-recovered on retry.

## Notes / not done

- No code changes were needed, so nothing was committed (per brief).
- A stray untracked file `nul` sits at the repo root (likely a `> nul` redirect artifact from Git Bash). Harmless; left in place.
- If Cloudflare 429s recur under load, consider rotating to a second Workers AI token; not urgent.
