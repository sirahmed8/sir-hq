"""Ahmed's build order (decided 2026-11-01). Overrides the score study (wave_study.py is kept as background only).
Writes waves.json (slug -> wave), order.json (full order) and WAVE_STUDY.md. Run, then generate_plans.py and generate_kit.py."""

import io
import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))
WAVES = [
    (1, "AHome (private, first)", ["ahome"]),
    (
        2,
        "Automations that make his life easier",
        ["sir-study", "sir-jobs", "sir-laptop-manager"],
    ),
    (
        3,
        "Friend's project: handoff pack only (no accounts created by Ahmed)",
        ["sir-negm-furniture"],
    ),
    (4, "AI and content", ["sir-ai", "sir-content-creation-studio"]),
    (
        5,
        "Products that earn the most",
        ["sir-business", "sir-hagoozat", "sir-education-hub"],
    ),
    (6, "Other paying products", ["sir-modpack", "sir-mods-for-gta-v", "sir-life"]),
    (
        7,
        "Last on purpose: extract and polish after everything else is built",
        ["sir-portfolio"],
    ),
    (8, "Optional, last (derived from x360ce, not Ahmed's own)", ["sir-controller"]),
]
REMOVED = {
    "sir-odysseus": "Not Ahmed's project (Odysseus upstream). Source moved to SIR AI/legacy as a read-only reference; folder moved to old projects; repo archived."
}


def main():
    waves, order = {}, []
    for w, _, slugs in WAVES:
        for s in slugs:
            waves[s] = w
            order.append(s)
    io.open(os.path.join(HERE, "waves.json"), "w", encoding="utf-8").write(
        json.dumps(waves, indent=1)
    )
    io.open(os.path.join(HERE, "order.json"), "w", encoding="utf-8").write(
        json.dumps(order, indent=1)
    )
    out = [
        "# BUILD ORDER (Ahmed, 2026-11-01)",
        "",
        "Order of waves, one project chat at a time. HQ opens a project chat, reviews its reports, and asks Ahmed to approve before the next project starts.",
        "",
        "| Wave | Why | Projects (in order) |",
        "|---|---|---|",
    ]
    for w, why, slugs in WAVES:
        out.append(f"| {w} | {why} | " + ", ".join(slugs) + " |")
    out += [
        "",
        "## Decisions behind it",
        "- AHome first (his pick). Then the automations that save him time: SIR Study, SIR Jobs, SIR Laptop Manager (not sites or apps, so no platform kit needed).",
        "- SIR Negm Furniture belongs to a friend: HQ prepares a complete handoff pack in the project repo (docs, plan, a prompt for the friend's own AI agent); no GitHub, Firebase or Cloudflare accounts are created for it by Ahmed.",
        "- SIR AI and SIR Content Creation Studio next, then the products expected to earn the most (Business, Hagoozat, Education Hub), then the other paying ones.",
        "- the shared kit and SIR Portfolio are last on purpose. Each product keeps its shared concerns (owner auth, signed webhooks, billing fallback, AI proxy, legal pack, tokens and UI) in separate internal packages with tests; the shared kit is then built by extracting and unifying the best versions, and SIR Portfolio shows the real finished products.",
        "- SIR Controller derives from x360ce (not Ahmed's own work): optional, last.",
        "- Removed: " + "; ".join(f"{k}: {v}" for k, v in REMOVED.items()),
        "",
        "The earlier score-based study (revenue, readiness, effort) is in `wave_study.py` for background.",
    ]
    io.open(
        os.path.join(HERE, "WAVE_STUDY.md"), "w", encoding="utf-8", newline="\n"
    ).write("\n".join(out) + "\n")
    print(json.dumps(waves))


if __name__ == "__main__":
    main()
