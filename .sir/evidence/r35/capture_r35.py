# r35 self-audit: Control Room + SIR Laptop Manager dashboards.
# 4 widths x en/ar x light/dark, interaction checks, screenshots to evidence dirs.
import json
import pathlib
import sys

from playwright.sync_api import sync_playwright

OUT_SIR = pathlib.Path(r"D:/Projects/_SIR/.sir/evidence/r35")
OUT_LM = pathlib.Path(r"D:/Projects/SIR Laptop Manager/.sir/evidence/r35")
OUT_SIR.mkdir(parents=True, exist_ok=True)
OUT_LM.mkdir(parents=True, exist_ok=True)

WIDTHS = [320, 390, 768, 1280]
LANGS = ["en", "ar"]
THEMES = ["light", "dark"]

results = {"control_room": [], "laptop_manager": []}


def shoot(page, path):
    page.screenshot(path=str(path), full_page=False)


def audit_page(page, url, lang, theme, width, tag, outdir, checks):
    page.set_viewport_size({"width": width, "height": 844})
    page.goto(url, wait_until="networkidle")
    page.wait_for_timeout(400)
    issues = []
    overflow = page.evaluate(
        "() => document.documentElement.scrollWidth > document.documentElement.clientWidth + 1 || "
        "document.body.scrollWidth > document.body.clientWidth + 1"
    )
    if overflow:
        issues.append("horizontal-page-scroll")
    body_text = page.evaluate("() => document.body.innerText")
    for bad in ("(LTR)", "(RTL)"):
        if bad in body_text:
            issues.append(f"literal-{bad}")
    for name, fn in checks:
        try:
            ok = fn(page)
            if ok is not True:
                issues.append(f"{name}:{ok}")
        except Exception as e:  # noqa: BLE001
            issues.append(f"{name}:EXC {e}")
    shot = outdir / f"{tag}-{width}-{lang}-{theme}.png"
    shoot(page, shot)
    return {"width": width, "lang": lang, "theme": theme, "shot": shot.name, "issues": issues}


def ctx_menu_check(sel):
    def fn(page):
        page.mouse.click(200, 400, button="right")
        page.wait_for_timeout(120)
        open_ = page.evaluate(f"() => {{ const m = document.querySelector('{sel}'); return !!(m && m.classList.contains('open')); }}")
        page.keyboard.press("Escape")
        page.wait_for_timeout(80)
        closed = page.evaluate(f"() => {{ const m = document.querySelector('{sel}'); return !(m && m.classList.contains('open')); }}")
        probs = []
        if not open_:
            probs.append("ctx-missing")
        if not closed:
            probs.append("ctx-stuck")
        return probs or True
    return fn


def run():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            ctx = browser.new_context()
            page = ctx.new_page()
            page.add_init_script("() => { try { window.speechSynthesis.speak = () => {}; } catch(e){} }")

            # ---------- Control Room ----------
            base = "http://127.0.0.1:8899/dashboard.html"
            cr_checks = [
                ("no-dup-menu-btn", lambda pg: "dup-menu-btn" if pg.evaluate("() => !!document.querySelector('#menu-toggle-btn, #txt-menu-btn')") else True),
                ("ctx-menu", ctx_menu_check("#app-context-menu")),
            ]
            for lang in LANGS:
                for theme in THEMES:
                    for w in WIDTHS:
                        url = f"{base}?lang={lang}"
                        page.context.add_init_script(
                            f"() => {{ try {{ localStorage.setItem('sir_theme_mode','{theme}'); localStorage.setItem('sir_theme','{theme}'); }} catch(e){{}} }}"
                        )
                        r = audit_page(page, url, lang, theme, w, "cr", OUT_SIR, cr_checks)
                        results["control_room"].append(r)
            # interaction shots: drawer open + settings open at 390
            page.context.add_init_script("() => { try { localStorage.setItem('sir_theme_mode','dark'); } catch(e){} }")
            page.goto(f"{base}?lang=en", wait_until="networkidle")
            page.set_viewport_size({"width": 390, "height": 844})
            page.wait_for_timeout(300)
            more = page.query_selector("#mobile-menu-trigger") or page.query_selector("nav .nav-tab:last-child")
            try:
                if more:
                    more.click()
                    page.wait_for_timeout(500)
                    shoot(page, OUT_SIR / "cr-interact-drawer-390-en-dark.png")
                    page.keyboard.press("Escape")
                    page.wait_for_timeout(400)
                settings = page.query_selector("#settings-btn")
                if settings:
                    settings.click()
                    page.wait_for_timeout(400)
                    shoot(page, OUT_SIR / "cr-interact-settings-390-en-dark.png")
            except Exception as e:  # noqa: BLE001
                print("CR interact skipped:", e)

            # ---------- SIR Laptop Manager ----------
            base2 = "http://127.0.0.1:8765/"
            lm_checks = [
                ("ctx-menu", ctx_menu_check("#app-context-menu")),
            ]
            for lang in LANGS:
                for theme in THEMES:
                    for w in WIDTHS:
                        url = base2
                        page.context.add_init_script(
                            f"() => {{ try {{ localStorage.setItem('sir_lang','{lang}'); localStorage.setItem('sir_theme','{theme}'); }} catch(e){{}} }}"
                        )
                        # add_init_script accumulates; clear by new context per combo is safer
                        r = audit_page(page, url, lang, theme, w, "lm", OUT_LM, lm_checks)
                        results["laptop_manager"].append(r)
            out = pathlib.Path(r"D:/Projects/_SIR/.sir/evidence/r35/audit-results.json")
            out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")

            # interaction shots at 390
            page.context.add_init_script("() => { try { localStorage.setItem('sir_lang','en'); localStorage.setItem('sir_theme','dark'); } catch(e){} }")
            page.goto(base2, wait_until="networkidle")
            page.set_viewport_size({"width": 390, "height": 844})
            page.wait_for_timeout(500)
            try:
                more = page.query_selector("#btn-bottom-more")
                if more:
                    more.click()
                    page.wait_for_timeout(600)
                    shoot(page, OUT_LM / "lm-interact-drawer-390-en-dark.png")
                    page.evaluate("() => { if (typeof closeMobileDrawer === 'function') closeMobileDrawer(); }")
                    page.wait_for_timeout(500)
                st = page.query_selector("#btn-settings")
                if st:
                    st.click()
                    page.wait_for_timeout(500)
                    shoot(page, OUT_LM / "lm-interact-settings-390-en-dark.png")
                    page.keyboard.press("Escape")
                    page.wait_for_timeout(400)
                page.keyboard.press("Control+k")
                page.wait_for_timeout(400)
                shoot(page, OUT_LM / "lm-interact-palette-390-en-dark.png")
            except Exception as e:  # noqa: BLE001
                print("LM interact skipped:", e)
        finally:
            browser.close()

    out = pathlib.Path(r"D:/Projects/_SIR/.sir/evidence/r35/audit-results.json")
    out.write_text(json.dumps(results, indent=2, ensure_ascii=False), encoding="utf-8")
    bad = [r for rows in results.values() for r in rows if r["issues"]]
    print(f"total runs: {sum(len(v) for v in results.values())}, with issues: {len(bad)}")
    for r in bad:
        print(r)


if __name__ == "__main__":
    sys.exit(run())
