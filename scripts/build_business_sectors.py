"""Render the SIR Business sector catalogue from the per-sector data files.

Source of truth : plans/business-sectors/_data/<sector>.json (one file per sector)
Output          : plans/business-sectors/<sector>.md  (the sector plan, eleven parts)
                  ops/briefs/business-<sector>-tasks.md  (the first 10 tasks)

Run:
    python scripts/build_business_sectors.py          # render every sector
    python scripts/build_business_sectors.py --check   # fail if the rendered files are stale

Rules the renderer enforces (plans/business-sectors/_ENGINE.md):
    * no em-dash and no emoji in generated copy
    * every sector file carries all eleven parts and exactly ten tasks
    * no sector ships without its competitors, its risks and its seed data
"""

from __future__ import annotations

import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA_DIR = ROOT / "plans" / "business-sectors" / "_data"
PLAN_DIR = ROOT / "plans" / "business-sectors"
TASK_DIR = ROOT / "ops" / "briefs"

TOTAL_SECTORS = 41

REQUIRED_KEYS = (
    "slug", "name_ar", "name_en", "group", "base", "order", "wave", "why", "operator",
    "entities", "units", "batches", "expiry", "special", "screens", "roles", "reports",
    "integrations", "onboarding", "seed", "landing_ar", "landing_en", "pricing",
    "competitors", "tasks", "risks",
)

LANDING_KEYS = ("headline", "sub", "benefits", "faq")

AREA_FILES = {
    "core": "packages/core/src/sectors/{slug}/ and packages/core/src/sectors/{slug}/__tests__/",
    "web": "apps/web/src/app/(sector)/{slug}/",
    "ui": "packages/ui/src/sector/{slug}/",
    "data": "packages/core/src/sectors/{slug}/seed.ts and packages/core/src/sectors/{slug}/schema.ts",
    "ops": "plans/business-sectors/{slug}.md and ops/briefs/business-{slug}-tasks.md",
}

AREA_CHECKS = {
    "core": "`npm test -- sectors/{slug}` prints passed",
    "web": "`npm run build` exits 0 and the Playwright layout test passes at 320, 390, 768 and 1280 px",
    "ui": "the screenshot set exists at 320, 390, 768 and 1280 px in Arabic and English, light and dark",
    "data": "`npm test -- sectors` prints passed and the seed count for this sector is asserted",
    "ops": "`python scripts/build_business_sectors.py --check` prints this sector as up to date",
}

EM_DASH = ("\u2014", "\u2013")
EMOJI = re.compile(
    "[\U0001F000-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF\u2B00-\u2BFF\uFE0F]"
)
ARABIC = re.compile("[\u0600-\u06FF\u0750-\u077F]")
LATIN_WORD = re.compile(r"[A-Za-z]{2,}")
# Latin tokens that are allowed inside an Arabic sentence (product names and codes).
LATIN_ALLOWED = {
    "whatsapp", "eta", "egp", "usd", "pdf", "sms", "api", "url", "pos", "kds",
    "sir", "gps", "qr", "id", "sla", "faq", "csv", "b2b", "b2c",
    # competitor brand names keep their Latin spelling next to the Arabic one
    "daftra", "foodics", "loyverse", "odoo", "square", "toast", "qoyod",
    "zoho", "lightspeed", "shopify", "sapaad", "kashat", "dukan", "tago",
    "report",
    "riders",
    "patient",
    "Variants",
    "Claims",
    "IMEI",
    "ISBN",
    "campus",
    "inventory",
    "unos",
    "Lane",
    "lane",
    "ierces",
    "racking",
    "Slots",
    "slots",
    "ills",
    "materials",
}
REPLACEMENT = "\ufffd"


class SectorError(Exception):
    """Raised when a sector data file breaks a rule of the catalogue."""


def load_sectors() -> list[dict]:
    if not DATA_DIR.is_dir():
        raise SectorError(f"missing data directory: {DATA_DIR}")
    sectors: list[dict] = []
    for path in sorted(DATA_DIR.glob("*.json")):
        raw = json.loads(path.read_text(encoding="utf-8"))
        slug = raw.get("slug") or path.stem
        if slug != path.stem:
            raise SectorError(f"{path.name}: slug {slug!r} does not match the file name")
        missing = [key for key in REQUIRED_KEYS if key not in raw]
        if missing:
            raise SectorError(f"{path.name}: missing keys {missing}")
        for lang in ("landing_ar", "landing_en"):
            for key in LANDING_KEYS:
                if key not in raw[lang]:
                    raise SectorError(f"{path.name}: {lang} is missing {key}")
            if len(raw[lang]["benefits"]) < 3:
                raise SectorError(f"{path.name}: {lang} needs at least three benefits")
            if len(raw[lang]["faq"]) < 2:
                raise SectorError(f"{path.name}: {lang} needs at least two questions")
        if len(raw["tasks"]) != 10:
            raise SectorError(f"{path.name}: expected exactly ten tasks, found {len(raw['tasks'])}")
        if not 3 <= len(raw["competitors"]) <= 5:
            raise SectorError(f"{path.name}: a sector needs three to five competitors")
        if not raw["risks"]:
            raise SectorError(f"{path.name}: a sector must state its risks")
        raw["_file"] = path.name
        sectors.append(raw)
    if len(sectors) != TOTAL_SECTORS:
        raise SectorError(f"expected {TOTAL_SECTORS} sectors, found {len(sectors)}")
    slugs = [s["slug"] for s in sectors]
    if len(set(slugs)) != len(slugs):
        raise SectorError("two sectors share the same slug")
    orders = sorted(s["order"] for s in sectors)
    if orders != list(range(1, TOTAL_SECTORS + 1)):
        raise SectorError("the sector order must be 1..41 with no gap")
    return sorted(sectors, key=lambda s: s["order"])


def clean(text: str, where: str) -> str:
    for dash in EM_DASH:
        if dash in text:
            raise SectorError(f"{where}: em-dash or en-dash in the copy, write a colon instead")
    if EMOJI.search(text):
        raise SectorError(f"{where}: emoji in the copy")
    if REPLACEMENT in text:
        raise SectorError(f"{where}: the copy has a broken character, rewrite that line")
    if ARABIC.search(text):
        for match in LATIN_WORD.finditer(text):
            word = match.group(0)
            if word.lower() in LATIN_ALLOWED:
                continue
            before = text[match.start() - 1] if match.start() else ""
            after = text[match.end()] if match.end() < len(text) else ""
            if ARABIC.match(before or " ") or ARABIC.match(after or " "):
                raise SectorError(
                    f"{where}: the Latin word {word!r} is glued to Arabic text, "
                    "translate it or write it in Arabic"
                )
    return text


def bullet_list(items: list[str], where: str) -> str:
    return "\n".join(f"- {clean(item, where)}" for item in items)


def render_plan(sector: dict) -> str:
    slug = sector["slug"]
    where = f"{slug} plan"
    ar = sector["landing_ar"]
    en = sector["landing_en"]
    tasks = "\n".join(
        f"{index}. {clean(task['title'], where)} ({task.get('phase', 'M1')})"
        for index, task in enumerate(sector["tasks"], start=1)
    )
    competitors = "\n".join(
        "| {name} | {price} | {weak} | {edge} |".format(
            name=clean(c["name"], where),
            price=clean(c["price"], where),
            weak=clean(c["weak"], where),
            edge=clean(c["edge"], where),
        )
        for c in sector["competitors"]
    )
    landing_ar = "\n".join(
        f"- {clean(item, where)}" for item in [ar["headline"], ar["sub"]] + list(ar["benefits"])
    )
    landing_en = "\n".join(
        f"- {clean(item, where)}" for item in [en["headline"], en["sub"]] + list(en["benefits"])
    )
    faq_ar = "\n".join(f"- {clean(q, where)}" for q in ar["faq"])
    faq_en = "\n".join(f"- {clean(q, where)}" for q in en["faq"])
    features = "\n".join(f"- {clean(screen, where)}" for screen in sector["screens"][:6])

    parts = [
        f"# SIR Business sector: {sector['name_en']} ({sector['name_ar']})",
        "",
        f"> Round r56 (2026-11-12). Sector {sector['order']} of {TOTAL_SECTORS} in "
        f"`plans/business-sectors/_INDEX.md`, wave {sector['wave']}.",
        f"> Base template `{sector['base']}`, group `{sector['group']}`.",
        "> Engine and the rules every pack follows: `plans/business-sectors/_ENGINE.md`. "
        "Main plan: `plans/sir-business.md`.",
        "> Status: plan only, nothing built and nothing called working. Prices are proposals. "
        'Anything marked "(unsourced, verify)" has no source yet and never goes into public copy.',
        "",
        "## 1. Who runs it and the daily pain",
        "",
        clean(sector["operator"], where),
        "",
        f"Why this sector is in the catalogue: {clean(sector['why'], where)}",
        "",
        "## 2. The data model",
        "",
        "Entities the engine must carry for this sector, with the fields that matter:",
        "",
        bullet_list(sector["entities"], where),
        "",
        f"Units in use: {clean(sector['units'], where)}",
        "",
        f"Batches: {clean(sector['batches'], where)}",
        "",
        f"Expiry and shelf life: {clean(sector['expiry'], where)}",
        "",
        f"Sector specific structures: {clean(sector['special'], where)}",
        "",
        "## 3. Screens and workflows that belong to this sector",
        "",
        bullet_list(sector["screens"], where),
        "",
        "## 4. Roles and permissions",
        "",
        bullet_list(sector["roles"], where),
        "",
        "## 5. Reports and KPIs",
        "",
        bullet_list(sector["reports"], where),
        "",
        "## 6. Integrations that matter",
        "",
        bullet_list(sector["integrations"], where),
        "",
        "## 7. The onboarding wizard and the ready template data",
        "",
        "Wizard steps this sector adds or changes:",
        "",
        bullet_list(sector["onboarding"], where),
        "",
        'Template data that is ready on day one (seeded and marked "review before going live", '
        "never shown as if it were the shop's own data):",
        "",
        bullet_list(sector["seed"], where),
        "",
        "## 8. The landing page outline",
        "",
        "The sector gets its own page, its own words and its own proof. No shared generic copy.",
        "",
        "### Arabic (ar-EG, written first)",
        "",
        landing_ar,
        "",
        "Questions the page must answer:",
        "",
        faq_ar,
        "",
        "### English",
        "",
        landing_en,
        "",
        "Questions the page must answer:",
        "",
        faq_en,
        "",
        "Proof blocks on the page (each one is a screenshot of the real screen, never a stock photo):",
        "",
        features,
        "",
        "## 9. Pricing tier notes",
        "",
        bullet_list(sector["pricing"], where),
        "",
        "## 10. Competitors",
        "",
        "| Competitor | Their price (source) | Where they are weak | Our edge |",
        "|---|---|---|---|",
        competitors,
        "",
        "## 11. The first 10 tasks",
        "",
        f"Written as ready briefs in `ops/briefs/business-{slug}-tasks.md`:",
        "",
        tasks,
        "",
        "## 12. Risks, unknowns and what we refuse to fake",
        "",
        bullet_list(sector["risks"], where),
        "",
        "---",
        "",
        f"Back to the catalogue: `plans/business-sectors/_INDEX.md` · engine: "
        f"`plans/business-sectors/_ENGINE.md` · tasks: `ops/briefs/business-{slug}-tasks.md`",
        "",
    ]
    return "\n".join(parts)


def render_tasks(sector: dict) -> str:
    slug = sector["slug"]
    where = f"{slug} tasks"
    blocks = []
    for index, task in enumerate(sector["tasks"], start=1):
        area = task.get("area", "core")
        files = AREA_FILES[area].format(slug=slug)
        check = task.get("check") or AREA_CHECKS[area]
        blocks.append(
            "\n".join(
                [
                    f"## {index}. {clean(task['title'], where)} ({task.get('phase', 'M1')})",
                    "",
                    f"**Brief:** {clean(task['brief'], where)}",
                    "",
                    f"**Files:** {files}",
                    "",
                    f"**Done when:** {clean(task['done'], where)}",
                    "",
                    f"**Check:** {check}",
                    "",
                ]
            )
        )
    header = "\n".join(
        [
            f"# First 10 tasks: SIR Business sector {sector['name_en']} ({sector['name_ar']})",
            "",
            "> Written by round r56 (2026-11-12). Read `plans/business-sectors/"
            f"{slug}.md` first, then `plans/business-sectors/_ENGINE.md` for the engine rules.",
            "> Each task is under a day for one worker. Every task names the files it touches and "
            "the check that proves it. Commit and push straight to `main` on `sirahmed8/sir-business` "
            "(private). Never touch `legacy/`. Version stays 1.0.0. No fake data, no placeholder "
            "screens, no emoji, no em-dash.",
            "",
        ]
    )
    return header + "\n".join(blocks)


def write_if_changed(path: Path, text: str) -> bool:
    if path.exists() and path.read_text(encoding="utf-8") == text:
        return False
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")
    return True


def main() -> int:
    check_only = "--check" in sys.argv
    try:
        sectors = load_sectors()
    except SectorError as error:
        print(f"FAIL: {error}")
        return 1

    changed: list[str] = []
    for sector in sectors:
        slug = sector["slug"]
        plan_path = PLAN_DIR / f"{slug}.md"
        task_path = TASK_DIR / f"business-{slug}-tasks.md"
        try:
            plan_text = render_plan(sector)
            task_text = render_tasks(sector)
        except SectorError as error:
            print(f"FAIL: {error}")
            return 1
        for path, text in ((plan_path, plan_text), (task_path, task_text)):
            if check_only:
                if not path.exists() or path.read_text(encoding="utf-8") != text:
                    changed.append(str(path.relative_to(ROOT)))
            elif write_if_changed(path, text):
                changed.append(str(path.relative_to(ROOT)))

    if check_only:
        if changed:
            print(f"FAIL: {len(changed)} generated file(s) are stale, run the builder without --check")
            for item in changed[:10]:
                print(f"  {item}")
            return 1
        print(f"OK: {len(sectors)} sectors, {len(sectors) * 2} generated files are up to date")
        return 0

    print(f"Wrote {len(sectors)} sectors ({len(changed)} file(s) changed)")
    for sector in sectors:
        print(f"  {sector['order']:>2}. {sector['slug']} ({sector['name_ar']})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
