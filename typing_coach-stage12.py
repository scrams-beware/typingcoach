# === Stage 12: Слияние записей ===
# Project: TypingCoach
def merge_exercises(exercise_a, exercise_b, field_names):
    """Return a new exercise record by taking the winning value for each field.

    The winner is decided by the rule in FIELD_RULES; unknown fields fall back
    to exercise_a. The input records are never mutated.
    """
    FIELD_RULES = {
        "title":      max,   # longer title wins
        "layout":    lambda x, y: x,  # keep the first layout
        "length":    max,   # longer text wins
        "difficulty": max,   # harder difficulty wins
    }

    def normalize(value):
        if isinstance(value, str):
            return value.lower()
        return value

    result = dict(exercise_a)
    for field in field_names:
        rule = FIELD_RULES.get(field, lambda x, y: x)
        winner = rule(exercise_a[field], exercise_b[field])
        result[field] = winner
    return result


def merge_attempts(attempt_a, attempt_b, field_names):
    """Return a new attempt record by taking the winning value for each field.

    The winner is decided by the rule in FIELD_RULES; unknown fields fall back
    to attempt_a. The input records are never mutated.
    """
    FIELD_RULES = {
        "wpm":    max,   # faster speed wins
        "errors": min,   # fewer errors wins
        "accuracy": max, # higher accuracy wins
        "duration": min, # shorter duration wins
    }

    def normalize(value):
        if isinstance(value, str):
            return value.lower()
        return value

    result = dict(attempt_a)
    for field in field_names:
        rule = FIELD_RULES.get(field, lambda x, y: x)
        winner = rule(attempt_a[field], attempt_b[field])
        result[field] = winner
    return result
