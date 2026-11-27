# === Stage 11: Поиск дубликатов ===
# Project: TypingCoach
from typing import Iterable, List, Optional


def normalize_layout(layout: str) -> str:
    """Return a canonical form for a keyboard layout value."""
    if layout is None:
        return ""
    return layout.strip().lower()


def normalize_title(title: str) -> str:
    """Return a canonical form for an exercise title."""
    if title is None:
        return ""
    return " ".join(title.strip().lower().split())


def normalize_length(length: int) -> int:
    """Return a canonical form for an exercise length.

    Missing or negative lengths collapse to 0 so that exercises with
    unspecified length compare as equal.
    """
    if length is None:
        return 0
    try:
        return int(length)
    except (TypeError, ValueError):
        return 0


def normalize_difficulty(difficulty: str) -> str:
    """Return a canonical form for a difficulty value."""
    if difficulty is None:
        return ""
    return difficulty.strip().lower()


def exercise_key(exercise: dict) -> tuple:
    """Build a normalization key from an exercise mapping."""
    return (
        normalize_title(exercise.get("title")),
        normalize_layout(exercise.get("layout")),
        normalize_length(exercise.get("length")),
        normalize_difficulty(exercise.get("difficulty")),
    )


def is_duplicate(a: dict, b: dict) -> bool:
    """Return True when exercises a and b share the same normalized fields."""
    return exercise_key(a) == exercise_key(b)


def find_duplicates(exercises: Iterable[dict]) -> List[List[dict]]:
    """Group exercises into clusters of duplicates.

    Each returned list contains at least two exercises that are
    duplicates of one another under the normalized field comparison.
    """
    groups: dict[tuple, List[dict]] = {}
    for exercise in exercises:
        groups.setdefault(exercise_key(exercise), []).append(exercise)

    duplicates = [
        members
        for members in groups.values()
        if len(members) > 1
    ]
    return duplicates


def find_duplicate_pairs(exercises: Iterable[dict]) -> List[tuple]:
    """Return every pair of exercises that are duplicates of each other."""
    pairs = []
    for group in find_duplicates(exercises):
        for first in range(len(group)):
            for second in range(first + 1, len(group)):
                pairs.append((group[first], group[second]))
    return pairs
