"""Independent r82 verification probe: serve SIR Study, check closed drawer
visibility/tab-order at 390px, screenshot closed + open states."""
import os, subprocess, sys, time
from urllib.request import urlopen
from urllib.error import URLError

ROOT = r"D:\Projects\SIR Study"
PORT = 3311
BASE = f"http://127.0.0.1:{PORT}"
EVID = r"D:\Projects\_SIR\ops\verifications\evidence"

proc = subprocess.Popen([sys.executable, os.path.join(ROOT, "scripts", "serve.py")],
                        cwd=ROOT, env=dict(os.environ, SIR_STUDY_PORT=str(PORT)),
                        stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
try:
    for _ in range(75):
        try:
            urlopen(BASE + "/START_HERE.html", timeout=1)
            break
        except (URLError, OSError):
            time.sleep(0.4)
    else:
        print("SERVER NEVER ANSWERED"); sys.exit(1)

    os.environ.setdefault("PLAYWRIGHT_NODEJS_PATH", r"C:\Program Files\nodejs\node.exe")
    from playwright.sync_api import sync_playwright
    with sync_playwright() as p:
        browser = p.chromium.launch()
        page = browser.new_page(viewport={"width": 390, "height": 844})
        page.goto(BASE + "/START_HERE.html", wait_until="networkidle")
        page.wait_for_timeout(400)

        st = page.evaluate("""() => {
          const d = document.getElementById('side-drawer');
          const cs = getComputedStyle(d);
          return {visibility: cs.visibility, pe: cs.pointerEvents,
                  open: d.classList.contains('open'),
                  display: cs.display, transform: cs.transform};
        }""")
        print("CLOSED:", st)

        hits = []
        for _ in range(30):
            page.keyboard.press("Tab")
            inside = page.evaluate("document.getElementById('side-drawer').contains(document.activeElement)")
            if inside:
                hits.append(page.evaluate("document.activeElement.id || document.activeElement.className"))
        print("TAB STOPS INSIDE DRAWER (closed):", hits)
        # also check aria-hidden
        print("aria-hidden attr:", page.evaluate("document.getElementById('side-drawer').getAttribute('aria-hidden')"))

        page.screenshot(path=os.path.join(EVID, "r82-study-390-closed.png"), full_page=False)

        page.click("#btn-menu-drawer")
        page.wait_for_timeout(500)
        st2 = page.evaluate("""() => {
          const d = document.getElementById('side-drawer');
          const cs = getComputedStyle(d);
          return {visibility: cs.visibility, pe: cs.pointerEvents,
                  open: d.classList.contains('open'),
                  focusInside: d.contains(document.activeElement)};
        }""")
        print("OPEN:", st2)
        page.screenshot(path=os.path.join(EVID, "r82-study-390-open.png"), full_page=False)

        # guide page check
        page.goto(BASE + "/or.html", wait_until="networkidle")
        page.wait_for_timeout(400)
        st3 = page.evaluate("""() => {
          const d = document.getElementById('side-drawer');
          const cs = getComputedStyle(d);
          return {visibility: cs.visibility, pe: cs.pointerEvents, open: d.classList.contains('open')};
        }""")
        print("GUIDE CLOSED:", st3)
        hits2 = []
        for _ in range(30):
            page.keyboard.press("Tab")
            inside = page.evaluate("document.getElementById('side-drawer').contains(document.activeElement)")
            if inside:
                hits2.append(page.evaluate("document.activeElement.id || document.activeElement.className"))
        print("TAB STOPS INSIDE DRAWER (guide, closed):", hits2)
        browser.close()
finally:
    proc.terminate()
    try:
        proc.wait(timeout=5)
    except Exception:
        proc.kill()
print("DONE")
