"""Studies the build order and writes plans/waves.json + plans/WAVE_STUDY.md. Ahmed (2026-10-30): AHome first, then the projects that make money, then the rest.
Scores are 0-5 judgements from the Phase 3 inventories (ops/PORTFOLIO.md, ops/inventory/*.md): they rank, they do not predict. Edit SCORES and re-run."""
import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
W = dict(speed=3, revenue=3, ready=2, free=2, ahmed=1, effort=-2)
# speed: how soon one paying customer or paid job can exist. revenue: money per customer x reachable customers. ready: legacy code and assets close to shippable.
# free: independence from the SIR Platform kit (5 = none needed). ahmed: his stated priority. effort: 1 small .. 4 very large.
SCORES = {
    "sir-jobs": dict(speed=5, revenue=3, ready=3, free=5, ahmed=4, effort=2, why="Finds and drafts paid freelance and remote work; the first-1,200-EGP goal depends on it; needs no platform kit."),
    "sir-negm-furniture": dict(speed=4, revenue=2, ready=4, free=4, ahmed=3, effort=2, why="A client project: delivery is paid work. Small static site, existing code, light platform use."),
    "sir-portfolio": dict(speed=3, revenue=2, ready=2, free=5, ahmed=3, effort=1, why="Free site, but it is the storefront that makes freelance and product sales credible. Smallest effort."),
    "sir-business": dict(speed=3, revenue=5, ready=3, free=2, ahmed=4, effort=4, why="One restaurant plan is 450 to 1,950 EGP a month, so one customer passes the first milestone. Restaurant is the most complete old app."),
    "sir-hagoozat": dict(speed=2, revenue=4, ready=3, free=2, ahmed=5, effort=3, why="Large Egyptian market, but two-sided (players and pitch owners) so the first payer is slower; Pro is 59 EGP a month."),
    "sir-obour-hub": dict(speed=2, revenue=3, ready=4, free=2, ahmed=5, effort=3, why="Closest to shippable (CI, 47 tests, live), small paying audience; proves the kit on the web path that Hagoozat reuses."),
    "sir-content-creation-studio": dict(speed=3, revenue=3, ready=3, free=2, ahmed=4, effort=2, why="Makes the videos for ByteVibeHQ channels, which is a second income line; Pro tier later."),
    "sir-controller": dict(speed=2, revenue=3, ready=2, free=3, ahmed=3, effort=3, why="Gamer market in Egypt and the Gulf; needs a UI stack decision and driver licence checks first."),
    "sir-ai": dict(speed=1, revenue=2, ready=2, free=3, ahmed=3, effort=3, why="Feeds the platform's AI gateway idea; paid tier is far off."),
    "sir-mods-for-gta-v": dict(speed=1, revenue=2, ready=3, free=3, ahmed=3, effort=3, why="Supporter tier only, and a game-licence risk to clear first."),
    "sir-modpack": dict(speed=1, revenue=2, ready=3, free=3, ahmed=3, effort=3, why="Supporter tier only; large payload; community-driven."),
    "sir-life": dict(speed=1, revenue=3, ready=0, free=2, ahmed=4, effort=3, why="New product with no old code; cloud backup is the only paid part."),
    "sir-laptop-manager": dict(speed=0, revenue=0, ready=3, free=5, ahmed=4, effort=2, why="Internal. It makes every agent's setup consistent but earns nothing itself."),
    "sir-study": dict(speed=0, revenue=0, ready=3, free=5, ahmed=4, effort=2, why="Personal study organiser; saves Ahmed time, earns nothing."),
    "sir-odysseus": dict(speed=0, revenue=1, ready=1, free=3, ahmed=2, effort=3, why="Upstream-derived AGPL distribution; donations only."),
}
FIXED = {"ahome": (1, "Ahmed's first pick: private, local, independent of the platform kit, runs today and is improved in place."),
         "sir-platform": (2, "Prerequisite for every web product. Build only the slice the next wave needs (M0 to M2) in step with the quick-cash projects.")}
CUT = [(2, 0), (3, 22), (4, 17), (5, 11), (6, -99)]  # wave 2 = quick cash (top by speed, set below), then by total


def total(s):
    return sum(W[k] * s[k] for k in W)


def main():
    rows = sorted(((slug, s, total(s)) for slug, s in SCORES.items()), key=lambda r: -r[2])
    waves = {slug: w for slug, (w, _) in FIXED.items()}
    for slug, s, t in rows:
        if s["free"] >= 4 and s["speed"] >= 3:
            waves[slug] = 2          # quick cash, no platform dependency
        elif s["revenue"] < 2:
            waves[slug] = 5          # internal and personal tools: no revenue of their own
        elif t >= 25:
            waves[slug] = 3          # first subscription products
        else:
            waves[slug] = 4          # next paying products
    io.open(os.path.join(HERE, "waves.json"), "w", encoding="utf-8").write(json.dumps(waves, indent=1))
    names = {1: "Wave 1: AHome (your pick)", 2: "Wave 2: quick cash and the kit slice", 3: "Wave 3: first subscription products", 4: "Wave 4: next paying products", 5: "Wave 5: internal and personal tools"}
    out = ["# WAVE STUDY (2026-10-30)", "", "Rule from Ahmed: start with AHome, then the projects that make money, then the rest, in a studied order, not random.", "",
           "Method: each project gets 0-5 scores from the Phase 3 inventories (`ops/PORTFOLIO.md`, `ops/inventory/`). Total = 3 x speed to first EGP + 3 x revenue size + 2 x legacy readiness + 2 x independence from the kit + 1 x Ahmed's priority - 2 x effort. Scores are judgements that rank projects; they do not forecast income. Edit `SCORES` in `plans/wave_study.py` and re-run when facts change.",
           "Wave rules: AHome and SIR Platform are fixed. A project with independence 4+ and speed 3+ is quick cash (wave 2). Otherwise revenue under 2 means internal or personal (wave 5), total 25+ is wave 3, the rest of the paying products wave 4.", "",
           "| Project | Speed | Revenue | Ready | Free of kit | Ahmed | Effort | Total | Wave | Why |", "|---|---|---|---|---|---|---|---|---|---|"]
    for slug, s, t in rows:
        out.append(f"| {slug} | {s['speed']} | {s['revenue']} | {s['ready']} | {s['free']} | {s['ahmed']} | {s['effort']} | **{t}** | {waves[slug]} | {s['why']} |")
    for slug, (w, why) in FIXED.items():
        out.append(f"| {slug} | fixed | | | | | | | {w} | {why} |")
    out += ["", "## Order Ahmed opens chats in"]
    for w in sorted(set(waves.values())):
        members = [s for s, ww in sorted(waves.items(), key=lambda kv: (-(total(SCORES[kv[0]]) if kv[0] in SCORES else 99), kv[0])) if ww == w]
        out.append(f"- **{names[w]}:** " + ", ".join(members))
    out += ["", "## Dependencies that fix the order", "- Every web product (Negm, Portfolio, Obour Hub, Hagoozat, Business portal, Life) needs SIR Platform packages: owner-auth, signed-webhook, billing fallback, ui kit. Build those first, only as far as the next project needs.",
            "- SIR Obour Hub proves the kit on the web path before Hagoozat reuses it. SIR Business is the largest revenue and the largest build, so its Restaurant mode starts as soon as the kit is proven.",
            "- AHome runs today with daemons: its chat must keep the services up and snapshot data before any change.", "- A project may be pulled earlier when Ahmed gets a customer for it; the order changes, the kits do not."]
    io.open(os.path.join(HERE, "WAVE_STUDY.md"), "w", encoding="utf-8", newline="\n").write("\n".join(out) + "\n")
    print(json.dumps(waves))


if __name__ == "__main__":
    main()
