"""Builds D:/Projects/_SIR/ops/dashboard.html (the SIR Control Room) from the real project files.
Run: python D:/Projects/_SIR/plans/generate_dashboard.py   (after generate_kit.py). AHome details are withheld on purpose (private)."""
import datetime
import io
import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from products import PRODUCTS  # noqa: E402
from kit_platforms import PLATFORM_NAMES  # noqa: E402

ROOT = "D:/Projects"
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
SHORT = {"web": "Web", "pwa": "PWA", "windows": "Win", "macos": "Mac", "linux": "Linux", "android": "Andr", "ios": "iOS", "ipados": "iPad", "wearos": "Wear",
         "watchos": "Watch", "android_tv": "ATV", "tvos": "tvOS", "android_auto": "Auto", "carplay": "CarP", "widgets": "Widg", "browser_ext": "Ext", "docker": "Dock"}
def attention():
    """Needs attention comes from the real files: ops/OWNER_ACTIONS.md (needs Ahmed), ops/AGENT_QUEUE.md (agents), and unread inbox messages."""
    out = []
    def lines(path):
        try:
            return io.open(path, encoding="utf-8").read().splitlines()
        except OSError:
            return []
    def clean(s):
        return re.sub(r"\*\*|`", "", s).strip()
    for ln in lines("D:/Projects/_SIR/ops/OWNER_ACTIONS.md"):
        if ln.startswith("- [ ]"):
            out.append(("warn", "Needs you", clean(ln[5:])[:260]))
    for ln in lines("D:/Projects/_SIR/ops/AGENT_QUEUE.md"):
        if ln.startswith("- [ ]"):
            out.append(("info", "Agents are on it", clean(ln[5:])[:260]))
    unread = 0
    for f in os.listdir("D:/Projects/_SIR/ops/bus"):
        if f.endswith(".md") and f != "README.md":
            unread += sum(1 for ln in lines("D:/Projects/_SIR/ops/bus/" + f) if ln.startswith("- [ ]"))
    if unread:
        out.append(("info", "Project messages", f"{unread} unread message(s) between projects in ops/bus."))
    done = [clean(ln[5:])[:200] for ln in lines("D:/Projects/_SIR/ops/OWNER_ACTIONS.md") if ln.startswith("- [x]")][:2]
    for d in done:
        out.append(("ok", "Done", d))
    return out


def parse_tasks(folder):
    segs, cur = [], None
    t = io.open(os.path.join(folder, ".sir", "TASKS.md"), encoding="utf-8").read()
    for ln in t.splitlines():
        m = re.match(r"## (M\d) (.*)", ln)
        if m:
            cur = dict(name=m.group(1) + " " + m.group(2), done=0, total=0, next=[])
            segs.append(cur)
        elif cur and (m2 := re.match(r"- \[([ x])\] (T-\d+) \| owner: [^|]+\| (.*)", ln)):
            cur["total"] += 1
            if m2.group(1) == "x":
                cur["done"] += 1
            else:
                cur["next"].append(m2.group(2) + " " + re.sub(r"\s*\| depends:.*", "", m2.group(3)).replace("(kit) ", "")[:150])
    return segs


def archived_count():
    try:
        out = subprocess.run(["gh", "repo", "list", "sirahmed8", "--limit", "100", "--json", "isArchived", "-q", "[.[]|select(.isArchived)]|length"], capture_output=True, text=True, timeout=60)
        return int(out.stdout.strip())
    except Exception:
        return 30


def main():
    projects, ms_tot = [], {}
    for p in PRODUCTS:
        folder = os.path.join(ROOT, p["folder"])
        if not os.path.isfile(os.path.join(folder, ".sir", "TASKS.md")):
            continue
        segs = parse_tasks(folder)
        st = json.load(io.open(os.path.join(folder, ".sir", "status.json"), encoding="utf-8"))
        priv = p["slug"] == "ahome"
        for s in segs:
            k = s["name"].split()[0]
            a = ms_tot.setdefault(k, dict(name=s["name"], done=0, total=0))
            a["done"] += s["done"]
            a["total"] += s["total"]
        nxt = [n for s in segs for n in s["next"]][:3]
        projects.append(dict(
            name="AHome (private)" if priv else p["display"], wave=p["wave"], status=st["status"], color=BRAND.get(p["slug"], {}).get("color", "#64748B"),
            arch="private, details withheld" if priv else re.search(r"archetype: (.*)", io.open(os.path.join(folder, ".sir", "project.yml"), encoding="utf-8").read()).group(1),
            done=sum(s["done"] for s in segs), total=sum(s["total"] for s in segs), segs=[dict(name=s["name"], done=s["done"], total=s["total"]) for s in segs],
            required=sum(1 for v in st["platforms"].values() if v == "required"), next=[] if priv else nxt,
            repo="private repo, not pushed from HQ" if priv else "github.com/sirahmed8/" + p["repo"] + " (private)", folder="withheld" if priv else "D:\\Projects\\" + p["folder"],
            mission="Private home project of two people. Nothing else is shown here." if priv else p["mission"][:210], matrix=None if priv else st["platforms"]))
    projects.sort(key=lambda x: (x["wave"], x["name"]))
    log = [ln[2:] for ln in io.open("D:/Projects/_SIR/ops/MISSION_LOG.md", encoding="utf-8").read().splitlines() if ln.startswith("- 2026")][-5:]
    data = dict(generated=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"), projects=projects, milestones=sorted(ms_tot.values(), key=lambda m: m["name"]),
                attention=[dict(level=l, tag=tg, text=x) for l, tg, x in attention()], log=[x[:230] for x in log], repos=dict(new_private=len([p for p in projects if p["matrix"]]), archived=archived_count()),
                platforms=[dict(key=k, name=n, short=SHORT[k]) for k, n in PLATFORM_NAMES])
    tpl = io.open(os.path.join(HERE, "dashboard_template.html"), encoding="utf-8").read()
    out = tpl.replace("/*__DATA__*/{}", json.dumps(data, ensure_ascii=False))
    io.open("D:/Projects/_SIR/ops/dashboard.html", "w", encoding="utf-8", newline="\n").write(out)
    print("dashboard.html", len(out), "bytes,", len(projects), "projects")


if __name__ == "__main__":
    main()
