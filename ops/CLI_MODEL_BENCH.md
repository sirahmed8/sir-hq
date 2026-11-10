# CLI model benchmark (OpenCode and Kilo), 2026-11-09

Task (identical for every model, run non-interactively from each model's own folder under `D:/Projects/_SIR/scratch/bench/<model-slug>/`):
create `slugify.py` (`slugify(text)`: lowercase, runs of non-alphanumeric to one hyphen, Arabic counts as alphanumeric, strip end hyphens) and `test_slugify.py` with 6 pytest tests including an Arabic case; run pytest; print DONE.

All five runs started at the same time (parallel), so seconds are rough. Timeout was 6 minutes each; no run hit it.

## Results

| Model | Seconds | Finished (DONE printed) | Exit code | Tests | pytest (`py -3 -m pytest -q`) | Error text |
|---|---|---|---|---|---|---|
| opencode/glm-5.3-flash-free | 19 | yes | 0 | 6 | 6 passed | none |
| opencode/deepseek-v4.1-flash-free | 29 | yes | 0 | 6 | 6 passed | none |
| opencode/big-pickle | 36 | yes | 0 | 8 | 8 passed | none |
| kilo/kilo-auto/free | 55 | no | 1 | 6 | 6 passed (files written, pytest green) | `pip install pytest -q` auto-rejected by permission; run ended with "pass --auto for autonomous use" |
| kilo/meta/muse-spark-1.3 | 17 | no | 1 | 0 | no files written | `Add credits to continue, or switch to a free model` (not free; skip) |

## Notes
- The default `python` on PATH (msys64, 3.14) has no pytest. `py -3` has pytest and was used for all verification. No installs were made.
- Kilo runs were asked to verify with pytest and tried `pip install pytest`, which was blocked by the permission rule. The code worked anyway. Use `kilo run --auto` only in a folder where that is acceptable.
- Pass/fail was verified by running pytest yourself in each folder, not by trusting the model's "DONE".

## Recommendation (best first)
1. **opencode/glm-5.3-flash-free**: fastest (19 s), finished cleanly, tests pass. Good default for small tasks.
2. **opencode/deepseek-v4.1-flash-free**: 29 s, clean finish, tests pass. Good second opinion.
3. **opencode/big-pickle**: slowest of the three (36 s) but most tests (8). Good when more thorough tests are wanted.
4. **kilo/kilo-auto/free**: code correct, but the run exited 1 because it tried a blocked install and never printed DONE. Use only with `--auto` and a folder where that is OK.
5. **kilo/meta/muse-spark-1.3**: not free on this account ("Add credits"). Do not use.

This is one small task, so treat it as a smoke test, not a quality ranking.

## Start commands (real project folder)
Run from the project folder, with `cd` into it first:

```
cd "D:/Projects/<project>"
opencode run -m opencode/glm-5.3-flash-free "<short task>"
```

For a long prompt, put it in a file and pass its contents through a shell substitution:

```
cd "D:/Projects/<project>"
opencode run -m opencode/glm-5.3-flash-free "$(cat "D:/Projects/_SIR/ops/briefs/<brief>.md")"
```

Kilo equivalent (free router): `kilo run -m kilo/kilo-auto/free "$(cat "<brief-file>")"`. Add `--auto` only when blocked installs are acceptable.

## Raw files
- Per-model folders and logs: `D:/Projects/_SIR/scratch/bench/<model-slug>/` (`run.log`, `status.txt`, generated files).
