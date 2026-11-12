"""Regression test for the R19-M3 modular split of the dashboard generator and template.

The two single large files (generate_dashboard.py ~1400 lines, dashboard_template.html
~3445 lines) were split into small modules. This test pins the contract that the
module files concatenate back to the original template and that every module is
small (under 300 lines).

Run: python -m pytest tests/test_r19_m3_modular_split.py -q
"""
import io
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
PLANS = HERE.parent / "plans"


def _module_names():
    """Return the ordered list of template module files the generator now loads."""
    src = io.open(PLANS / "dashboard_main.py", encoding="utf-8").read()
    start = src.index("for name in (")
    end = src.index(")", start)
    block = src[start:end]
    names = []
    for line in block.splitlines():
        line = line.strip()
        if line.startswith('"') and line.endswith('",'):
            names.append(line.strip('",'))
    return names


class ModularSplitTest(unittest.TestCase):
    def test_modules_concatenate_to_original_template(self):
        tpl = io.open(PLANS / "dashboard_template.html", encoding="utf-8").read()
        joined = ""
        for name in _module_names():
            joined += io.open(PLANS / name, encoding="utf-8").read()
        self.assertEqual(joined, tpl, "template modules must concatenate to the original template")

    def test_each_module_is_under_300_lines(self):
        big = []
        for name in _module_names():
            n = len(io.open(PLANS / name, encoding="utf-8").read().splitlines())
            if n > 300:
                big.append((name, n))
        self.assertEqual(big, [], f"modules over 300 lines: {big}")

    def test_generator_file_is_under_300_lines(self):
        n = len(io.open(PLANS / "generate_dashboard.py", encoding="utf-8").read().splitlines())
        self.assertLess(n, 300, f"generate_dashboard.py is {n} lines; must be under 300")


if __name__ == "__main__":
    unittest.main()