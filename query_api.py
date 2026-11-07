"""按名称过滤并分页返回内存库存条目。"""


def query_items(items, q=None, page=1, page_size=10):
    if not isinstance(page, int) or isinstance(page, bool) or page < 1:
        raise ValueError("page must be an integer of at least 1")
    if (
        not isinstance(page_size, int)
        or isinstance(page_size, bool)
        or not 1 <= page_size <= 100
    ):
        raise ValueError("page_size must be an integer from 1 to 100")
    if q is not None and not isinstance(q, str):
        raise ValueError("q must be a string or None")

    query = q.casefold() if q is not None else None
    filtered = [
        item
        for item in items
        if query is None or query in item.get("name", "").casefold()
    ]
    start = (page - 1) * page_size

    return {
        "items": filtered[start : start + page_size],
        "page": page,
        "page_size": page_size,
        "total": len(filtered),
    }
