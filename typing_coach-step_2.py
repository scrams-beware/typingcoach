# === Stage 2: Проверка полей ===
# Project: TypingCoach
import re

FIELD_NAME = "name"
FIELD_LAYOUT = "layout"
FIELD_LENGTH = "length"
FIELD_DIFFICULTY = "difficulty"

VALID_LAYOUTS = ("qwerty", "dvorak", "colemak")
VALID_DIFFICULTIES = ("easy", "medium", "hard")
MIN_NAME_LENGTH = 1
MAX_NAME_LENGTH = 60
MIN_LENGTH = 1
MAX_LENGTH = 500


class ExerciseValidationError(Exception):
    pass


def normalize_text(value):
    text = str(value).strip()
    text = re.sub(r"\s+", " ", text)
    text = text.lower()
    return text


def normalize_layout(value):
    layout = normalize_text(value)
    if layout not in VALID_LAYOUTS:
        raise ExerciseValidationError(
            "Invalid layout. Allowed values: " + ", ".join(VALID_LAYOUTS)
        )
    return layout


def normalize_difficulty(value):
    difficulty = normalize_text(value)
    if difficulty not in VALID_DIFFICULTIES:
        raise ExerciseValidationError(
            "Invalid difficulty. Allowed values: "
            + ", ".join(VALID_DIFFICULTIES)
        )
    return difficulty


def validate_name(value):
    name = normalize_text(value)
    if len(name) < MIN_NAME_LENGTH:
        raise ExerciseValidationError("Name must contain at least one character.")
    if len(name) > MAX_NAME_LENGTH:
        raise ExerciseValidationError(
            "Name must not exceed " + str(MAX_NAME_LENGTH) + " characters."
        )
    return name


def validate_length(value):
    length = int(normalize_text(value))
    if length < MIN_LENGTH:
        raise ExerciseValidationError(
            "Length must be at least " + str(MIN_LENGTH).
            format(MIN_LENGTH=MIN_LENGTH)
        )
    if length > MAX_LENGTH:
        raise ExerciseValidationError(
            "Length must not exceed " + str(MAX_LENGTH).format(MAX_LENGTH=MAX_LENGTH)
        )
    return length


def validate_layout(value):
    return normalize_layout(value)


def validate_difficulty(value):
    return normalize_difficulty(value)


def validate_exercise_field(field_name, value):
    validator = {
        FIELD_NAME: validate_name,
        FIELD_LAYOUT: validate_layout,
        FIELD_LENGTH: validate_length,
        FIELD_DIFFICULTY: validate_difficulty,
    }.get(field_name)
    if validator is None:
        raise ExerciseValidationError(
            "Unknown field: " + field_name
        )
    return validator(value)
