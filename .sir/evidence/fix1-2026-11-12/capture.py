"""Self-audit of the rebuilt Control Room page (task ci-sir-20261112-0901-fix1-fix1).

Opens the generated page (ops/public/dashboard.html, the same bytes as the artifact) at
320/390/768/1280 px in Arabic and English, light and dark, walks all seven views and records
screenshots plus the overflow and clipping counts.

Run: python .sir/evidence/fix1-2026-11-12/capture.py
"""
import json
import os
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tests"))

from playwright_support import chromium_ready, node_path  # noqa: E402

_NODE = node_path()
if _NODE:
    os.environ.setdefault("PLAYWRIGHT_NODEJS_PATH", _NODE)

from playwright.sync_api import sync_playwright  # noqa: E402

PAGE = (ROOT / "ops" / "public" / "dashboard.html").resolve()
WIDTHS = [320, 390, 768, 1280]
LANGS = ["ar", "en"]
THEMES = ["light", "dark"]
VIEWS = ["now", "projects", "tools", "checks", "ideas", "owner", "accounts"]

PROBE = """() => {
  const overflow = document.documentElement.scrollWidth > document.documentElement.clientWidth
    || document.body.scrollWidth > document.body.clientWidth;
  const clipped = Array.from(document.querySelectorAll('h1,h2,h3,p,span,li,td'))
    .filter(el => el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1)
    .map(el => el.tagName + ':' + (el.textContent || '').slice(0, 40));
  return { overflow, clipped };
}"""


def main():
    if not chromium_ready():
        print("Chromium is not installed for Playwright; no evidence captured")
        return 1
    results = []
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            page = browser.new_page()
            page.goto(PAGE.as_uri(), wait_until="networkidle")
            page.evaluate("() => { window.speechSynthesis.speak = () => {}; }")
            for width in WIDTHS:
                page.set_viewport_size({"width": width, "height": 900})
                for theme in THEMES:
                    page.evaluate(f'document.documentElement.dataset.theme = "{theme}"')
                    for lang in LANGS:
                        page.evaluate("l => { window.store('cr-lang', l); window.applyLang(); window.renderNav(); window.render(); }", lang)
                        page.wait_for_timeout(120)
                        for view in VIEWS:
                            page.evaluate("v => window.setView(v)", view)
                            page.wait_for_timeout(80)
                            probe = page.evaluate(PROBE)
                            results.append({
                                "width": width, "theme": theme, "lang": lang, "view": view,
                                "overflow": probe["overflow"], "clipped": probe["clipped"],
                            })
                        page.evaluate("v => window.setView(v)", "now")
                        page.wait_for_timeout(80)
                        shot = HERE / f"{width}-{lang}-{theme}.png"
                        page.screenshot(path=str(shot), full_page=False)
            page.close()
        finally:
            browser.close()
    bad = [r for r in results if r["overflow"] or r["clipped"]]
    (HERE / "results.json").write_text(json.dumps({"runs": len(results), "failures": bad, "all": results}, indent=1), encoding="utf-8")
    print(f"{len(results)} runs, {len(bad)} with overflow or clipped text")
    for row in bad[:10]:
        print("  ", row["width"], row["lang"], row["theme"], row["view"], row["clipped"][:3])
    return 0 if not bad else 1


if __name__ == "__main__":
    sys.exit(main())
