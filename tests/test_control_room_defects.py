# tests/test_control_room_defects.py
# Browser test for Control Room defect 8 self-audit loop.
# Opens ops/public/dashboard.html at 320/390/768/1280 px, light and dark.
# Asserts: no horizontal scroll, no clipped text, one name per page, no tile with fake data.
# Requires Playwright (not installed in this sandbox; not in CI .github/workflows/verify.yml).
# CI green gate remains `python -m compileall plans scripts` + `python plans/generate_dashboard.py`.

import pathlib

import pytest

try:
    from playwright.sync_api import sync_playwright
except Exception:  # playwright absent
    sync_playwright = None

pytestmark = pytest.mark.skipif(
    sync_playwright is None,
    reason="Playwright not installed in this sandbox; run where playwright is available",
)

DASHBOARD = pathlib.Path("ops/public/dashboard.html").resolve().as_uri()
WIDTHS = [320, 390, 768, 1280]
THEMES = ["light", "dark"]

FAKE_TILE_VALUES = {"0/16", "0", "17", "5", "170", "7", "10"}

DUPLICATE_NAMES = {
    "Gemini Handover": "Handover",
    "CI & Remote": "CI",
}


def _page_snapshot(page, width, theme):
    page.set_viewport_size({"width": width, "height": 900})
    page.evaluate(f'document.documentElement.dataset.theme = "{theme}"')
    return page.content()


def test_no_horizontal_scroll_all_widths_themes():
    if sync_playwright is None:
        pytest.skip("playwright not installed")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            page = browser.new_page()
            try:
                page.goto(DASHBOARD, wait_until="networkidle")
                page.evaluate("() => { window.speechSynthesis.speak = () => {}; }")
                for width in WIDTHS:
                    for theme in THEMES:
                        _page_snapshot(page, width, theme)
                        overflow = page.evaluate(
                            "() => document.documentElement.scrollWidth > document.documentElement.clientWidth || "
                            "document.body.scrollWidth > document.body.clientWidth"
                        )
                        assert not overflow, f"horizontal scroll at {width}px {theme}"
            finally:
                page.close()
        finally:
            browser.close()


def test_one_name_per_page():
    if sync_playwright is None:
        pytest.skip("playwright not installed")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            page = browser.new_page()
            try:
                page.goto(DASHBOARD, wait_until="networkidle")
                text = page.content()
                for alias, canonical in DUPLICATE_NAMES.items():
                    assert alias not in text, f"duplicate name '{alias}' present; use '{canonical}' only"
            finally:
                page.close()
        finally:
            browser.close()


def test_no_fake_tile_data():
    if sync_playwright is None:
        pytest.skip("playwright not installed")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            page = browser.new_page()
            try:
                page.goto(DASHBOARD, wait_until="networkidle")
                for width in WIDTHS:
                    for theme in THEMES:
                        _page_snapshot(page, width, theme)
                        tiles = page.locator(".tile").all()
                        for tile in tiles:
                            value = tile.inner_text().strip()
                            assert value not in FAKE_TILE_VALUES, f"fake tile value '{value}' at {width}px {theme}"
            finally:
                page.close()
        finally:
            browser.close()


def test_no_clipped_text():
    if sync_playwright is None:
        pytest.skip("playwright not installed")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True, args=["--mute-audio"])
        try:
            page = browser.new_page()
            try:
                page.goto(DASHBOARD, wait_until="networkidle")
                for width in WIDTHS:
                    for theme in THEMES:
                        _page_snapshot(page, width, theme)
                        clipped = page.evaluate(
                            "() => Array.from(document.querySelectorAll('h1,h2,h3,p,span,li,td')).some(el => "
                            "el.scrollWidth > el.clientWidth + 1 || el.scrollHeight > el.clientHeight + 1)"
                        )
                        assert not clipped, f"clipped text at {width}px {theme}"
            finally:
                page.close()
        finally:
            browser.close()
