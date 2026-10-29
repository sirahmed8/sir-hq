"""Appends the MERGE PROJECT notice to AGENTS.md of every product folder that has legacy/ or materials/. Idempotent."""
import os
from generate_plans import MERGE
from products import PRODUCTS
MARK = "## MERGE PROJECT"
for p in PRODUCTS:
    d = os.path.join("D:/Projects", p["folder"])
    f = os.path.join(d, "AGENTS.md")
    if p["slug"] not in MERGE or not os.path.isfile(f):
        continue
    t = open(f, encoding="utf-8").read()
    if MARK in t:
        continue
    t += "\n" + MARK + "\nThis folder merges several old projects (complete code, git history and structure) that were moved into `legacy/` (or `materials/`). Read `legacy/README.md` and `.sir/PLAN.md` section 0 first. Port everything of value into the new clean structure with high quality code, fully configured, deployed and pushed in production mode; never edit legacy code except to read; when M6 is done move `legacy/*` to `D:/Projects/old projects/`.\n"
    open(f, "w", encoding="utf-8", newline="\n").write(t)
    print("notice:", p["folder"])
