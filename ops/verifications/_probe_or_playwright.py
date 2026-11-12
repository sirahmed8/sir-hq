"""Minimal Playwright probe for or.html Simplex SVG at 320/390 px."""
import json, os
from playwright.sync_api import sync_playwright

OUT = r"D:/Projects/_SIR/ops/verifications/evidence"
os.makedirs(OUT, exist_ok=True)

JS = r"""
() => {
  const svg = document.querySelector('svg[viewBox="0 0 620 220"]');
  const wrap = svg ? svg.parentElement : null;
  const cs = wrap ? getComputedStyle(wrap) : null;
  const r = svg ? svg.getBoundingClientRect() : null;
  return JSON.stringify({
    vw: window.innerWidth,
    docScrollW: document.documentElement.scrollWidth,
    pageOverflow: document.documentElement.scrollWidth > window.innerWidth + 1,
    svg: r ? {w: Math.round(r.width), h: Math.round(r.height), left: Math.round(r.left), right: Math.round(r.right)} : null,
    wrap: wrap ? {tag: wrap.tagName, class: String(wrap.className).slice(0,60), clientW: wrap.clientWidth, scrollW: wrap.scrollWidth, csOverflowX: cs ? cs.overflowX : null} : null,
    svgStyle: svg ? svg.getAttribute('style') : null
  });
}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r"C:/Program Files/Google/Chrome/Application/chrome.exe")
    results = {}
    for w, d in [(320, "rtl"), (390, "ltr"), (768, "ltr"), (1280, "ltr")]:
        pg = b.new_page(viewport={"width": w, "height": 900})
        pg.goto("http://127.0.0.1:3300/or.html", wait_until="domcontentloaded")
        try:
            pg.evaluate("document.body.dir = '%s'" % d)
        except Exception:
            pass
        pg.wait_for_timeout(500)
        m = pg.evaluate(JS)
        pg.screenshot(path=os.path.join(OUT, "r45-or-%d-%s.png" % (w, d)), full_page=False)
        results["%d-%s" % (w, d)] = m
        pg.close()
    b.close()
print(json.dumps(results, indent=2, ensure_ascii=False))