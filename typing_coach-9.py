# === Stage 9: Постраничный вывод ===
# Project: TypingCoach
def paginate(items, page, per_page):
    """Return the slice of items for a given page and page size.

    ``page`` is 1-based. ``per_page`` is the number of items per page.
    Out-of-range pages return an empty list.
    """
    if per_page <= 0:
        return []
    if page <= 0:
        return []
    start = (page - 1) * per_page
    return items[start:start + per_page]


def page_metadata(items, page, per_page):
    """Return a small dictionary describing the pagination state.

    Contains the total number of pages and the number of items on the
    current page.
    """
    total = len(items)
    total_pages = (total + per_page - 1) // per_page if per_page > 0 else 0
    current_page = min(page, total_pages) if total_pages > 0 else 0
    per = per_page if current_page > 0 else 0
    start = (current_page - 1) * per
    current_count = len(items[start:start + per])
    return {
        "page": current_page,
        "per_page": per,
        "total_pages": total_pages,
        "total_items": total,
        "current_page_count": current_count,
    }


def build_page_url(base_url, page, per_page):
    """Build a query-string URL pointing to a specific page.

    The current page is always reflected in the query string so links
    are self-describing.
    """
    query = "page=" + str(page)
    if per_page > 0:
        query += "&per_page=" + str(per_page)
    separator = "&" if "?" in base_url else "?"
    return base_url + separator + query
