# === Stage 8: Теги ===
# Project: TypingCoach
from dataclasses import dataclass, field
from datetime import datetime


@dataclass
class ExerciseTag:
    name: str


@dataclass
class Exercise:
    title: str
    layout: str
    length: int
    difficulty: str
    tags: list = field(default_factory=list)


class TagRegistry:
    def __init__(self):
        self._tags = set()

    def add(self, exercise: Exercise, tag: str) -> Exercise:
        if not tag:
            raise ValueError("tag name must not be empty")
        self._tags.add(tag)
        if tag not in exercise.tags:
            exercise.tags.append(tag)
        return exercise

    def remove(self, exercise: Exercise, tag: str) -> Exercise:
        if tag in exercise.tags:
            exercise.tags.remove(tag)
            if tag in self._tags:
                self._tags.discard(tag)
        return exercise

    def search(self, tag: str) -> list:
        return [e for e in self._tags if e == tag]


class TagStore:
    def __init__(self):
        self._map = {}

    def add(self, exercise: Exercise, tag: str) -> Exercise:
        if not tag:
            raise ValueError("tag name must not be empty")
        if not isinstance(exercise, Exercise):
            raise TypeError("expected Exercise instance")
        self._map[(id(exercise), tag)] = datetime.now()
        return self.registry.add(exercise, tag)

    def remove(self, exercise: Exercise, tag: str) -> Exercise:
        self._map.pop((id(exercise), tag), None)
        return self.registry.remove(exercise, tag)

    def search(self, tag: str) -> list:
        return self.registry.search(tag)


registry = TagRegistry()
store = TagStore()


def tag_exercise(exercise: Exercise, tag: str) -> Exercise:
    return store.add(exercise, tag)


def untag_exercise(exercise: Exercise, tag: str) -> Exercise:
    return store.remove(exercise, tag)


def find_by_tag(tag: str) -> list:
    return store.search(tag)
