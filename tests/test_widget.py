import unittest

from src.widget import add


class WidgetTests(unittest.TestCase):
    def test_add(self):
        self.assertEqual(add(2, 3), 5)

    @unittest.skip("rounding is biased — see FIXME in src/widget.py")
    def test_rounding(self):
        pass


if __name__ == "__main__":
    unittest.main()
