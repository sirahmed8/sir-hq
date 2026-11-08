"""Builds D:/Projects/_SIR/ops/dashboard.html (the SIR Control Room page) from the real project files.
Run: python D:/Projects/_SIR/plans/generate_dashboard.py, then HQ republishes the artifact (same file path).
AHome is private: counts and status only, never task text or notes."""

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

ROOT = os.environ.get("SIR_ROOT", "D:/Projects")
OPS = os.environ.get("SIR_OPS", os.path.normpath(os.path.join(HERE, "..", "ops")))
BRAND = json.load(io.open(os.path.join(HERE, "brand.json"), encoding="utf-8"))
ORDER = json.load(io.open(os.path.join(HERE, "order.json"), encoding="utf-8"))
WAVEMAP = json.load(io.open(os.path.join(HERE, "waves.json"), encoding="utf-8"))
SHORT = {
    "web": "Web",
    "pwa": "PWA",
    "windows": "Win",
    "macos": "Mac",
    "linux": "Linux",
    "android": "Andr",
    "ios": "iOS",
    "ipados": "iPad",
    "wearos": "Wear",
    "watchos": "Watch",
    "android_tv": "ATV",
    "tvos": "tvOS",
    "android_auto": "Auto",
    "carplay": "CarP",
    "widgets": "Widg",
    "browser_ext": "Ext",
    "docker": "Dock",
}
WAVE_NAMES = {
    1: "AHome first",
    2: "Automations",
    3: "Friend's project",
    4: "AI and content",
    5: "Earn the most",
    6: "Other paying products",
    7: "Extract and polish",
    8: "Optional, last",
}


def lines(path):
    try:
        return io.open(path, encoding="utf-8").read().splitlines()
    except OSError:
        return []


def clean(s):
    return re.sub(r"\*\*|`", "", s).strip()


def git(folder, *args):
    try:
        return subprocess.run(
            ["git", "-C", folder] + list(args),
            capture_output=True,
            text=True,
            timeout=20,
        ).stdout.strip()
    except Exception:
        return ""


def parse_tasks(folder, private):
    ms, cur = [], None
    for ln in lines(os.path.join(folder, ".sir", "TASKS.md")):
        m = re.match(r"## (M\d) (.*)", ln)
        if m:
            cur = dict(name=m.group(1) + " " + m.group(2), items=[])
            ms.append(cur)
        elif cur and (
            m2 := re.match(r"- \[([ x])\] (T-\d+) \| owner: [^|]+\| (.*)", ln)
        ):
            text = re.sub(r"\s*\| depends:.*", "", m2.group(3)).replace("(kit) ", "")
            cur["items"].append(
                dict(
                    id=m2.group(2),
                    done=m2.group(1) == "x",
                    text="" if private else text[:240],
                )
            )
    return ms


def checkpoint_now(folder):
    out, on = [], False
    for ln in lines(os.path.join(folder, ".sir", "CHECKPOINT.md")):
        if ln.startswith("## Now"):
            on = True
            continue
        if on and ln.startswith("## "):
            break
        if on and ln.strip():
            out.append(clean(ln.lstrip("- ")))
    return " ".join(out)[:420]


def section_items(path, wanted):
    """Open items (- [ ]) under the given '## ' headings only."""
    out, on = [], False
    for ln in lines(path):
        if ln.startswith("## "):
            on = any(ln.startswith("## " + w) for w in wanted)
            continue
        if on and ln.startswith("- [ ]"):
            out.append(clean(ln[5:])[:320])
    return out


def attention():
    out = []
    for x in section_items(OPS + "/OWNER_ACTIONS.md", ["Open"]):
        out.append(dict(level="warn", tag="Needs you now", text=x))
    for x in section_items(OPS + "/AGENT_QUEUE.md", ["Now"]):
        out.append(dict(level="info", tag="Agents are on it", text=x))
    for x in section_items(OPS + "/OWNER_ACTIONS.md", ["Optional"]):
        out.append(dict(level="mute", tag="When you like", text=x))
    unread = sum(1 for ln in lines(OPS + "/bus/sir-hq.md") if ln.startswith("- [ ]"))
    if unread:
        out.append(
            dict(
                level="info",
                tag="Reports for HQ",
                text=f"{unread} project report(s) waiting for HQ review in ops/bus/sir-hq.md.",
            )
        )
    return out


def archived_count():
    try:
        r = subprocess.run(
            [
                "gh",
                "repo",
                "list",
                "sirahmed8",
                "--limit",
                "100",
                "--json",
                "isArchived",
                "-q",
                "[.[]|select(.isArchived)]|length",
            ],
            capture_output=True,
            text=True,
            timeout=5,
        )
        if r.returncode == 0 and r.stdout.strip().isdigit():
            return int(r.stdout.strip())
    except Exception:
        pass
    return 31


def get_ci_status():
    repos = [
        ("AHome", "sirahmed8/ahmed-and-habiba"),
        ("SIR Negm Furniture", "sirahmed8/sir-negm-furniture"),
        ("SIR HQ", "sirahmed8/sir-hq"),
        ("SIR Jobs", "sirahmed8/sir-jobs"),
        ("SIR Study", "sirahmed8/sir-study"),
        ("SIR Laptop Manager", "sirahmed8/sir-laptop-manager"),
    ]
    ci = []
    for name, repo in repos:
        try:
            r = subprocess.run(
                ["gh", "run", "list", "-R", repo, "--limit", "1", "--json", "conclusion,status,databaseId,headBranch,name,url"],
                capture_output=True,
                text=True,
                timeout=5
            )
            if r.returncode == 0 and r.stdout.strip():
                runs = json.loads(r.stdout.strip())
                if runs:
                    latest = runs[0]
                    ci.append({
                        "name": name,
                        "repo": repo,
                        "status": latest.get("conclusion") or latest.get("status") or "unknown",
                        "id": latest.get("databaseId"),
                        "url": latest.get("url")
                    })
                else:
                    ci.append({"name": name, "repo": repo, "status": "none", "id": None, "url": None})
            else:
                ci.append({"name": name, "repo": repo, "status": "none", "id": None, "url": None})
        except Exception:
            ci.append({"name": name, "repo": repo, "status": "none", "id": None, "url": None})
    return ci


def main():
    projects = []
    for p in PRODUCTS:
        folder = ROOT + "/" + p["folder"]
        if not os.path.isfile(folder + "/.sir/TASKS.md"):
            continue
        private = p["slug"] == "ahome"
        st = json.load(io.open(folder + "/.sir/status.json", encoding="utf-8"))
        ms = parse_tasks(folder, private)
        items = [i for m in ms for i in m["items"]]
        done = sum(i["done"] for i in items)
        yml = "\n".join(lines(folder + "/.sir/project.yml"))
        arch = re.search(r"archetype: (.*)", yml)
        status = (
            "done"
            if items and done == len(items)
            else "building"
            if done > 2
            else "ready"
        )
        projects.append(
            dict(
                slug=p["slug"],
                name="AHome (private)" if private else p["display"],
                wave=WAVEMAP.get(p["slug"], 9),
                order=ORDER.index(p["slug"]) if p["slug"] in ORDER else 99,
                color=BRAND.get(p["slug"], {}).get("color", "#64748B"),
                arch="private, details withheld"
                if private
                else (arch.group(1) if arch else ""),
                status=status,
                done=done,
                total=len(items),
                milestones=[dict(name=m["name"], items=m["items"]) for m in ms],
                next=[]
                if private
                else [i["id"] + " " + i["text"][:150] for i in items if not i["done"]][
                    :4
                ],
                now="" if private else checkpoint_now(folder),
                mission="Private. Counts only." if private else p["mission"][:260],
                repo=(
                    "private repo (not pushed from HQ)"
                    if private
                    else "github.com/sirahmed8/" + p["repo"] + " (private)"
                ),
                folder="withheld" if private else "D:\\Projects\\" + p["folder"],
                commit=git(folder, "log", "-1", "--format=%cs") if not private else "",
                sync=(
                    ""
                    if private
                    else (
                        "in sync"
                        if "ahead" not in git(folder, "status", "-sb").split("\n")[0]
                        and "behind" not in git(folder, "status", "-sb").split("\n")[0]
                        else "not in sync"
                    )
                ),
                required=sum(1 for v in st["platforms"].values() if v == "required"),
                matrix=None if private else st["platforms"],
            )
        )
    projects.sort(key=lambda x: (x["wave"], x["order"]))
    waves = {}
    for pr in projects:
        w = waves.setdefault(
            pr["wave"],
            dict(
                wave=pr["wave"],
                name=WAVE_NAMES.get(pr["wave"], ""),
                done=0,
                total=0,
                projects=[],
            ),
        )
        w["done"] += pr["done"]
        w["total"] += pr["total"]
        w["projects"].append(pr["slug"])
    active = []
    try:
        active = json.load(io.open(OPS + "/active.json", encoding="utf-8"))
    except Exception:
        pass
    nxt = next(
        (pr for pr in projects if pr["status"] != "done" and pr["status"] == "ready"),
        None,
    )
    log = [
        ln[2:][:260] for ln in lines(OPS + "/MISSION_LOG.md") if ln.startswith("- 20")
    ][-14:]
    data = dict(
        generated=datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
        projects=projects,
        waves=sorted(waves.values(), key=lambda w: w["wave"]),
        attention=attention(),
        active=active,
        nextStart=(nxt["name"] if nxt else ""),
        log=log[::-1],
        repos=dict(
            new_private=len([p for p in projects if p["matrix"]]),
            archived=archived_count(),
        ),
        platforms=[dict(key=k, name=n, short=SHORT[k]) for k, n in PLATFORM_NAMES],
        ci=get_ci_status(),
        remote_access=[
            {"name": "SIR Jobs", "port": 3456, "url": "https://ahmed.tail9e9aa7.ts.net:3456/", "desc": "Pipeline & Staged Opportunities"},
            {"name": "SIR Study", "port": 3300, "url": "https://ahmed.tail9e9aa7.ts.net:3300/START_HERE.html", "desc": "SAD Exam Cram & Live Countdown"},
            {"name": "SIR Laptop Manager", "port": 8765, "url": "https://ahmed.tail9e9aa7.ts.net:8765/", "desc": "Ops UI & Hardware Gauges"},
            {"name": "SIR Control Room", "port": 8899, "url": "https://ahmed.tail9e9aa7.ts.net:8899/dashboard.html", "desc": "Portfolio Ground Truth"},
        ],
    )
    tpl = io.open(
        os.path.join(HERE, "dashboard_template.html"), encoding="utf-8"
    ).read()
    out = tpl.replace("/*__DATA__*/{}", json.dumps(data, ensure_ascii=False))
    io.open(OPS + "/dashboard.html", "w", encoding="utf-8", newline="\n").write(out)
    print("dashboard.html", len(out), "bytes,", len(projects), "projects")


if __name__ == "__main__":
    main()
