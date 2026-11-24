# === Stage 6: Фильтрация записей ===
# Project: TypingCoach
from datetime import date


def filter_exercises(exercises, layout=None, date_range=None):
    """Filter exercises by layout and/or date range.

    Args:
        exercises: list of exercise records (dicts).
        layout: optional string to match the "layout" field.
        date_range: optional dict with "from" and/or "to" date strings
            (format "YYYY-MM-DD") applied to the "created" field.

    Returns:
        list of exercise records matching the given criteria.
    """
    if date_range is None:
        date_range = {}
    from_date = date_range.get("from")
    to_date = date_range.get("to")

    def parse_date(value):
        return date.fromisoformat(value)

    def in_range(exercise):
        created = parse_date(exercise["created"])
        if from_date is not None and created < parse_date(from_date):
            return False
        if to_date is not None and created > parse_date(to_date):
            return False
        return True

    result = []
    for exercise in exercises:
        if layout is not None and exercise.get("layout") != layout:
            continue
        if not in_range(exercise):
            continue
        result.append(exercise)
    return result
