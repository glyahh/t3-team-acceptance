"""将库存查询结果接入页面渲染。"""

from item_page import render_page
from query_api import query_items


def show_inventory(items, q=None, page=1, page_size=10):
    query = query_items(items, q=q, page=page, page_size=page_size)
    page_text = render_page(query)["text"]
    return {
        "query": query,
        "page_text": page_text,
        "total": query["total"],
    }
