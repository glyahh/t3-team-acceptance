"""页面渲染的验收脚本。不导入查询模块，避免和查询任务互相等待。"""
import unittest

from item_page import render_page


class ItemPageTests(unittest.TestCase):
    def test_renders_current_page(self):
        # AC-005：给定查询结果时，页面能看到当前页名称、页码和总数。
        page = render_page(
            {
                "items": [{"name": "Alpha"}],
                "page": 1,
                "page_size": 1,
                "total": 2,
            }
        )
        self.assertIn("Alpha", page["text"])
        self.assertEqual(page["page"], 1)
        self.assertEqual(page["total"], 2)
        self.assertEqual(page["count"], 1)

    def test_rejects_result_without_items(self):
        # 结果不是字典，或没有条目列表时必须拒绝。
        with self.assertRaises(ValueError):
            render_page([])
        with self.assertRaises(ValueError):
            render_page({"page": 1, "total": 0})


if __name__ == "__main__":
    unittest.main()
