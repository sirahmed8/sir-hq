import unittest
import os
import sys
import tempfile

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "plans"))
from tasks_parser import parse_tasks_file


class TestTasksParser(unittest.TestCase):
    def test_counts_checkboxes(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write("## M1\n- [x] done\n- [ ] todo\n- [X] also done\n")
            name = f.name
        try:
            total, done = parse_tasks_file(name)
            self.assertEqual(total, 3)
            self.assertEqual(done, 2)
        finally:
            os.unlink(name)

    def test_empty_file(self):
        with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as f:
            f.write("")
            name = f.name
        try:
            total, done = parse_tasks_file(name)
            self.assertEqual((total, done), (0, 0))
        finally:
            os.unlink(name)

    def test_missing_file(self):
        total, done = parse_tasks_file("Z:/does/not/exist/TASKS.md")
        self.assertEqual((total, done), (0, 0))


if __name__ == "__main__":
    unittest.main()
