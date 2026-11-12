"""Regression test for the R19-M3 size and structure rule.

The Control Room page template lives in plans/dashboard_parts/*.html (one concern per part) and the
generator with its read-only feeds lives in small modules under plans/. This test pins that contract:
every part and every module stays under 300 lines, the parts still concatenate to the assembled
mirror plans/dashboard_template.html, and that mirror is not stale.

Run: python -m pytest tests/test_r19_m3_modular_split.py -q
"""
import io
import sys
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLANS = HERE.parent / "plans"
sys.path.insert(0, str(PLANS))

import dashboard_page  # noqa: E402

MAX_LINES = 300


def _lines(path):
    with io.open(path, encoding="utf-8") as f:
        return len(f.read().splitlines())


class ModularSplitTest(unittest.TestCase):
    def test_parts_concatenate_to_the_assembled_mirror(self):
        self.assertEqual(
            dashboard_page.assemble(),
            dashboard_page.mirror_text(),
            "plans/dashboard_parts must concatenate to plans/dashboard_template.html",
        )

    def test_mirror_is_not_stale(self):
        self.assertEqual(
            dashboard_page.assemble(),
            dashboard_page.mirror_text(),
            "plans/dashboard_template.html is stale; run python plans/generate_dashboard.py",
        )

    def test_assembled_template_is_a_whole_page(self):
        template = dashboard_page.assemble()
        self.assertTrue(template.lstrip().startswith("<!doctype html>"), "the page must start with a doctype")
        self.assertTrue(template.rstrip().endswith("</html>"), "the page must end with </html>")
        self.assertEqual(template.count(dashboard_page.PLACEHOLDER), 1, "the page needs exactly one data placeholder")
        self.assertEqual(template.count("<script>"), template.count("</script>"), "every script block must be closed")

    def test_each_part_is_under_300_lines(self):
        big = []
        for name in dashboard_page.PARTS:
            n = _lines(PLANS / "dashboard_parts" / name)
            if n > MAX_LINES:
                big.append((name, n))
        self.assertEqual(big, [], f"template parts over {MAX_LINES} lines: {big}")

    def test_every_part_exists(self):
        missing = [name for name in dashboard_page.PARTS if not (PLANS / "dashboard_parts" / name).is_file()]
        self.assertEqual(missing, [], f"missing template parts: {missing}")

    def test_python_modules_are_under_300_lines(self):
        big = []
        for py in sorted(PLANS.glob("dashboard_*.py")):
            n = _lines(py)
            if n > MAX_LINES:
                big.append((py.name, n))
        self.assertEqual(big, [], f"python modules over {MAX_LINES} lines: {big}")

    def test_generator_file_is_under_300_lines(self):
        n = _lines(PLANS / "generate_dashboard.py")
        self.assertLess(n, MAX_LINES, f"generate_dashboard.py is {n} lines; must be under {MAX_LINES}")


if __name__ == "__main__":
    unittest.main()
