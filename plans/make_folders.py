import os, subprocess
from products import PRODUCTS
NEW = {"sir-controller","sir-content-creation-studio","sir-modpack","sir-mods-for-gta-v","sir-portfolio","sir-study","sir-hagoozat","sir-obour-hub","sir-home","sir-laptop-manager","sir-jobs","sir-negm-furniture","sir-odysseus"}
for p in PRODUCTS:
    if p["slug"] not in NEW:
        continue
    d = os.path.join("D:/Projects", p["folder"])
    os.makedirs(os.path.join(d, ".sir"), exist_ok=True)
    os.makedirs(os.path.join(d, "prompts"), exist_ok=True)
    plan = open(p["slug"] + ".md", encoding="utf-8").read()
    def w(rel, t):
        with open(os.path.join(d, rel), "w", encoding="utf-8", newline="\n") as f:
            f.write(t)
    w(".sir/PLAN.md", plan)
    w("AGENTS.md", "# AGENTS.md: %s\n\nPart of the SIR product family. Owner: Ahmed Alaa (@sirahmed8). Read by Claude Code, Codex, OpenCode, Kilo, Antigravity.\n\n1. Read D:/Projects/_SIR/NEXT.md, D:/Projects/AGENTS.md (workspace laws), .sir/PLAN.md (the big plan), then .sir/CHECKPOINT.md.\n2. Work the first unchecked box in PLAN section 8. Tick it only with evidence. Update the checkpoint after every box.\n3. Standard and modules: D:/Projects/_SIR/standard/. Shared code: D:/Projects/SIR Platform.\n4. Never ask Ahmed; if a permission blocks you, put the single command in D:/Projects/_SIR/NEXT.md and continue.\n5. Nothing fake, no hype, no secrets in git, owner/admin checks only on the server.\n" % p["display"])
    w("CLAUDE.md", "@AGENTS.md\n")
    w("GEMINI.md", "@AGENTS.md\n")
    w(".sir/CHECKPOINT.md", "# CHECKPOINT: %s\nUpdated 2026-10-29 (created by HQ)\n\n## State\nFolder, plan and instruction files created. No code yet. Replaces: %s.\n\n## Next step\nStart PLAN section 8, milestone M0 (after SIR Platform has the packages this product needs; see NEXT.md order).\n" % (p["display"], p["replaces"]))
    w("prompts/PRODUCT_PROMPT.md", "# %s: product prompt\n\n%s\n\nFull plan: .sir/PLAN.md. Old project to port from: %s (see D:/Projects/_SIR/ops/inventory/).\n" % (p["display"], p["mission"], p["replaces"]))
    w(".gitignore", "node_modules/\n.env\n.env.*\n!.env.example\n.next/\ndist/\nout/\n*.log\n")
    subprocess.run(["git", "-C", d, "init", "-q", "-b", "main"])
    print("created", p["folder"])
