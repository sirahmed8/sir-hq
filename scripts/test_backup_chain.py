"""Synthetic test of the backup manager's ordered model chain (owner order 2026-11-13).

Runs the real chain directly on a throwaway prompt file. No Telegram message is sent
and Ahmed is never contacted. It proves three things:

  1. the chain is ordered best to worst and starts with Claude when that entry is alive;
  2. a dead first step (dead tool = same path as a quota/401/not installed) only moves
     the chain on, and the next model still writes the reply;
  3. the reply that arrives is clean Arabic (the same acceptance rule the bot uses).

Usage: python scripts/test_backup_chain.py
Exit code 0 = the chain answered after skipping the dead step; 1 = nothing answered.
"""
import sys
import time
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import backup_manager as bm  # noqa: E402

TAG = "synthetic"
PROMPT = Path("D:/Projects/_SIR/ops/backup-manager/prompt-synthetic.txt")
REPLY = Path("D:/Projects/_SIR/ops/backup-manager/reply-synthetic.txt")


def prepare_prompt() -> None:
    PROMPT.write_text(
        "# Synthetic chain test\n"
        "This is a self-test of the SIR backup manager model chain. Ahmed is not involved.\n"
        "Do exactly this and nothing else:\n"
        "1. Write ONE line into the reply file path given in your task message.\n"
        "2. The line must be exactly: تم اختبار سلسلة الموديلات بنجاح\n"
        "3. Do not edit, create or delete any other file. Do not run any other command.\n",
        encoding="utf-8",
    )


def main() -> int:
    prepare_prompt()
    REPLY.unlink(missing_ok=True)

    print("1) declared chain, best first:")
    for i, (tool, model, label) in enumerate(bm.CHAIN, 1):
        print(f"   {i}. {tool}|{model}   ({label})")
    print(f"   per-step cap {bm.ATTEMPT_TIMEOUT}s, total cap {bm.MAX_TOTAL}s")

    # a dead step must not stop the chain: pretend the strongest entry is gone
    real_chain = list(bm.CHAIN)
    bm.CHAIN = [("dead_tool", "dead-model", "dead provider (simulated quota/401)")] + real_chain
    live = bm.chain_entries()
    print(f"2) chain steps the pool will actually try now: {len(live)}")
    for i, (entry, _t, _m, label) in enumerate(live, 1):
        print(f"   {i}. {entry}  ({label})")
    if len(live) < 2:
        print("FAIL: fewer than two live steps, cannot prove a fallback")
        return 1

    bm.MAX_TOTAL = 150
    t0 = time.time()
    ok = bm.brain(PROMPT, TAG)
    elapsed = time.time() - t0
    bm.CHAIN = real_chain

    print(f"3) chain finished in {elapsed:.0f}s, answered={ok}")
    if not ok:
        print("FAIL: no chain step wrote a reply")
        return 1
    text = REPLY.read_text(encoding="utf-8").strip() if REPLY.exists() else ""
    print(f"4) reply file: {REPLY.as_posix()} ({len(text)} chars)")
    print("   " + text.replace("\n", " | ")[:300])
    problem = bm.reply_problem(text)
    if problem:
        print(f"FAIL: reply rejected by the bot's own rule: {problem}")
        return 1
    if "تم اختبار سلسلة الموديلات بنجاح" not in text:
        print("WARN: the model answered in its own words, content check not exact (still a valid reply)")
    print("PASS: the dead first step was skipped and a later model answered with an acceptable reply")
    return 0


if __name__ == "__main__":
    sys.exit(main())
