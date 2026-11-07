"""接线验收。查询和页面都进入需求分支之后，这条测试才能运行。"""
import unittest

from wired_page import show_inventory


class WiredPageTests(unittest.TestCase):
    def test_page_uses_query(self):
        # AC-006：页面上的条目来自同一次过滤和分页，而不是另一份列表。
        items = [
            {"name": "Alpha"},
            {"name": "Beta"},
            {"name": "Alpine"},
        ]
        shown = show_inventory(items, q="al", page=1, page_size=1)
        self.assertEqual(shown["total"], 2)
        self.assertEqual(shown["query"]["page"], 1)
        self.assertEqual(shown["query"]["page_size"], 1)
        self.assertEqual(len(shown["query"]["items"]), 1)
        self.assertIn(shown["query"]["items"][0]["name"], shown["page_text"])


if __name__ == "__main__":
    unittest.main()
