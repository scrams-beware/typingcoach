# === Stage 1: Каркас модуля ===
# Project: TypingCoach
from dataclasses import dataclass, field
from enum import Enum
from typing import List


class Layout(Enum):
    ENGLISH = "en"
    RUSSIAN = "ru"


class Difficulty(Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


@dataclass(frozen=True)
class Exercise:
    name: str
    layout: Layout
    length: int
    difficulty: Difficulty


def create_sample_exercises() -> List[Exercise]:
    return [
        Exercise(name="Hello world", layout=Layout.ENGLISH, length=50, difficulty=Difficulty.EASY),
        Exercise(name="Practice makes perfect", layout=Layout.ENGLISH, length=80, difficulty=Difficulty.MEDIUM),
        Exercise(name="Раскладка", layout=Layout.RUSSIAN, length=40, difficulty=Difficulty.EASY),
        Exercise(name="Сложный текст", layout=Layout.RUSSIAN, length=120, difficulty=Difficulty.HARD),
    ]


def main() -> None:
    exercises = create_sample_exercises()
    for index, exercise in enumerate(exercises, start=1):
        print(f"Exercise #{index}: {exercise.name}")
        print(f"  Layout: {exercise.layout.value}")
        print(f"  Length: {exercise.length}")
        print(f"  Difficulty: {exercise.difficulty.value}")
        print()


if __name__ == "__main__":
    main()
