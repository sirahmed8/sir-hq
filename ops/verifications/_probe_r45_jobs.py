"""Probe SIR Jobs r45 fixes: AR placeholders + dir=auto on search inputs, 390px screenshot."""
import json, os
from playwright.sync_api import sync_playwright

OUT = r"D:/Projects/_SIR/ops/verifications/evidence"
os.makedirs(OUT, exist_ok=True)

JS = r"""
() => {
  const ids = ['pipeline-search', 'jobs-search', 'palette-input', 'prop-personal-note'];
  const out = {};
  for (const id of ids) {
    const el = document.getElementById(id);
    if (el) out[id] = {placeholder: el.getAttribute('placeholder'), aria: el.getAttribute('aria-label'), dirAttr: el.getAttribute('dir'), dirCss: getComputedStyle(el).direction};
    else out[id] = null;
  }
  const contacts = ['contact-name','contact-role','contact-company','contact-notes'];
  for (const id of contacts) {
    const el = document.getElementById(id);
    if (el) out[id] = {placeholder: el.getAttribute('placeholder'), dirAttr: el.getAttribute('dir'), dirCss: getComputedStyle(el).direction};
    else out[id] = null;
  }
  return JSON.stringify({lang: document.documentElement.lang, htmlDir: document.documentElement.dir, vw: window.innerWidth, docOverflowX: document.documentElement.scrollWidth > window.innerWidth + 1, inputs: out});
}
"""

with sync_playwright() as p:
    b = p.chromium.launch(executable_path=r"C:/Program Files/Google/Chrome/Application/chrome.exe")
    results = {}
    for lang, w, tag in [("ar", 390, "390-ar"), ("en", 390, "390-en"), ("ar", 320, "320-ar")]:
        pg = b.new_page(viewport={"width": w, "height": 844})
        pg.add_init_script("localStorage.setItem('sir_jobs_lang','%s');" % lang)
        pg.goto("http://127.0.0.1:3456/", wait_until="domcontentloaded")
        pg.wait_for_timeout(1500)
        # open openings view for jobs-search visibility
        try:
            pg.evaluate("document.querySelector('[data-view=\"openings\"]')?.click() || document.getElementById('tab-openings')?.click()")
        except Exception as e:
            pass
        pg.wait_for_timeout(800)
        m = pg.evaluate(JS)
        pg.screenshot(path=os.path.join(OUT, "r45-jobs-%s.png" % tag), full_page=False)
        results[tag] = m
        pg.close()
    b.close()
    print(json.dumps(results, indent=2, ensure_ascii=False))
