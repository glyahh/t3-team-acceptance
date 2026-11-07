"""查询接口的验收脚本。这里没有实现，实现必须由开发任务写到工作区。"""
import unittest

from query_api import query_items


class QueryItemsTests(unittest.TestCase):
    def setUp(self):
        self.items = [
            {"name": "Alpha"},
            {"name": "Beta"},
            {"name": "Alpine"},
        ]

    def test_rejects_page_below_one(self):
        # AC-001：页码从 1 开始，0 不能查。
        with self.assertRaises(ValueError):
            query_items(self.items, q=None, page=0, page_size=10)

    def test_rejects_page_size_out_of_range(self):
        # AC-002：页大小只允许 1 到 100。
        with self.assertRaises(ValueError):
            query_items(self.items, q=None, page=1, page_size=0)
        with self.assertRaises(ValueError):
            query_items(self.items, q=None, page=1, page_size=101)

    def test_rejects_non_string_query(self):
        # AC-003：查询条件要么省略，要么是字符串。
        with self.assertRaises(ValueError):
            query_items(self.items, q=1, page=1, page_size=10)

    def test_pagination_and_filter(self):
        # AC-004：过滤后分页，总数不随页码变小。
        first = query_items(self.items, q="al", page=1, page_size=1)
        second = query_items(self.items, q="al", page=2, page_size=1)
        self.assertEqual(first["total"], 2)
        self.assertEqual(first["page"], 1)
        self.assertEqual(first["page_size"], 1)
        self.assertEqual(len(first["items"]), 1)
        self.assertEqual(len(second["items"]), 1)
        self.assertEqual(second["total"], 2)
        self.assertNotEqual(first["items"][0]["name"], second["items"][0]["name"])


if __name__ == "__main__":
    unittest.main()
