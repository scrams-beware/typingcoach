# === Stage 10: Быстрые фильтры ===
# Project: TypingCoach
from datetime import datetime


def _parse_date(value):
    if isinstance(value, datetime):
        return value
    for fmt in ("%Y-%m-%d", "%d.%m.%Y", "%m/%d/%Y", "%d/%m/%Y"):
        try:
            return datetime.strptime(value, fmt)
        except ValueError:
            continue
    return None


def _days_between(start, end):
    return (end - start).days


def _is_overdue(due, now):
    if due is None:
        return False
    return _days_between(due, now) < 0


def _is_this_week(due, now):
    if due is None:
        return False
    start = now.replace(hour=0, minute=0, second=0, microsecond=0)
    end = start + __import__("datetime").timedelta(days=7)
    return _days_between(due, start) >= 0 and _days_between(due, end) <= 0


def _is_today(due, now):
    return due is not None and due.date() == now.date()


def exercise_due_filters(exercises, now=None):
    now = now or datetime.now()
    overdue = [e for e in exercises if _is_overdue(e.get("due"), now)]
    this_week = [e for e in exercises if _is_this_week(e.get("due"), now)]
    today = [e for e in exercises if _is_today(e.get("due"), now)]
    return {"today": today, "this_week": this_week, "overdue": overdue}
