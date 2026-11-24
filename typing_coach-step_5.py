# === Stage 5: Связанная сущность ===
# Project: TypingCoach
"""TypingCoach attempt module.

Each attempt records a single typing run performed on an exercise: the
identifier of the exercise it targeted, the timestamp it started, the
number of characters typed correctly, the number of errors made, and the
number of seconds the user spent typing.
"""

from datetime import datetime


class Attempt:
    """A single typing attempt against a given exercise."""

    def __init__(self, exercise_id, correct_chars=0, errors=0, duration=0.0):
        self.exercise_id = exercise_id
        self.started_at = datetime.now()
        self.correct_chars = correct_chars
        self.errors = errors
        self.duration = duration

    def set_finished(self, correct_chars, errors, duration):
        self.correct_chars = correct_chars
        self.errors = errors
        self.duration = duration

    @property
    def wpm(self):
        minutes = self.duration / 60.0
        if minutes <= 0:
            return 0.0
        return round(self.correct_chars / 5.0 / minutes, 1)

    def to_dict(self):
        return {
            "exercise_id": self.exercise_id,
            "started_at": self.started_at.isoformat(),
            "correct_chars": self.correct_chars,
            "errors": self.errors,
            "duration": self.duration,
            "wpm": self.wpm,
        }


def create_attempt(exercise_id):
    attempt = Attempt(exercise_id)
    return attempt


def finish_attempt(attempt, correct_chars, errors, duration):
    attempt.set_finished(correct_chars, errors, duration)
    return attempt
