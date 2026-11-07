"""渲染内存库存查询结果。"""


def render_page(result):
    if not isinstance(result, dict) or not isinstance(result.get("items"), list):
        raise ValueError("result must be a dictionary with an items list")

    items = result["items"]
    names = [
        str(item["name"])
        for item in items
        if isinstance(item, dict) and "name" in item
    ]
    return {
        "text": "\n".join(names),
        "page": result.get("page"),
        "total": result.get("total"),
        "count": len(items),
    }
