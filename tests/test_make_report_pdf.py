"""Tests for scripts/deliver/make-report-pdf.py (A4 PDF reports, Arabic/RTL aware)."""
import importlib.util
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / "scripts" / "deliver" / "make-report-pdf.py"
FIXTURE = ROOT / "tests" / "fixtures" / "report_sample_ar.md"

spec = importlib.util.spec_from_file_location("make_report_pdf", SCRIPT)
mrp = importlib.util.module_from_spec(spec)
spec.loader.exec_module(mrp)


def test_build_html_rtl_for_arabic():
    doc = mrp.build_html(FIXTURE, None)
    assert 'dir="rtl"' in doc
    assert "lang=\"ar\"" in doc
    assert "ملخص تنفيذي" in doc  # markdown rendered to html
    assert "@page" in doc and "size: A4" in doc


def test_build_html_ltr_for_english(tmp_path):
    src = tmp_path / "en.md"
    src.write_text("# Hello\n\nPlain English report.\n", encoding="utf-8")
    doc = mrp.build_html(src, None)
    assert 'dir="ltr"' in doc


def test_render_pdf_arabic_sample(tmp_path):
    pytest.importorskip("playwright.sync_api")
    pytest.importorskip("markdown_it")
    pytest.importorskip("pypdf")
    from playwright_support import chromium_ready
    if not chromium_ready():
        pytest.skip("Chromium is not installed for Playwright")
    out = tmp_path / "report.pdf"
    mrp.render_pdf(mrp.build_html(FIXTURE, None), out)
    data = out.read_bytes()
    assert data[:5] == b"%PDF-"
    assert len(data) > 10000
    # fonts embedded (Chromium subsets and embeds them) and text is extractable
    assert data.count(b"/FontFile") >= 1
    assert data.count(b"/ToUnicode") >= 1
    from pypdf import PdfReader
    reader = PdfReader(str(out))
    assert len(reader.pages) >= 1
    w, h = reader.pages[0].mediabox.width, reader.pages[0].mediabox.height
    assert abs(w - 595) < 2 and abs(h - 842) < 2  # A4 in points
