# === Stage 4: Редактирование записей ===
# Project: TypingCoach
ALLOWED_FIELDS = ("name", "layout", "length", "difficulty")
VALID_LAYOUTS = ("en", "ru")
VALID_DIFFICULTIES = ("easy", "medium", "hard")


def validate_update_fields(fields):
    if not isinstance(fields, (list, tuple, set)):
        raise ValueError("fields must be a list, tuple, or set")
    invalid = fields - ALLOWED_FIELDS
    if invalid:
        raise ValueError(f"Unknown field(s): {', '.join(sorted(invalid))}")
    return list(fields)


def validate_name(name):
    if not isinstance(name, str):
        raise TypeError("name must be a string")
    if not name.strip():
        raise ValueError("name must not be empty")
    return name.strip()


def validate_layout(layout):
    if not isinstance(layout, str):
        raise TypeError("layout must be a string")
    if layout not in VALID_LAYOUTS:
        raise ValueError(f"layout must be one of {VALID_LAYOUTS}")
    return layout


def validate_length(length):
    if isinstance(length, bool) or not isinstance(length, int):
        raise TypeError("length must be an integer")
    if length <= 0:
        raise ValueError("length must be a positive integer")
    return length


def validate_difficulty(difficulty):
    if not isinstance(difficulty, str):
        raise TypeError("difficulty must be a string")
    if difficulty not in VALID_DIFFICULTIES:
        raise ValueError(f"difficulty must be one of {VALID_DIFFICULTIES}")
    return difficulty


def apply_update(exercise, fields):
    new_fields = validate_update_fields(fields)
    if "name" in new_fields:
        exercise["name"] = validate_name(exercise["name"])
    if "layout" in new_fields:
        exercise["layout"] = validate_layout(exercise["layout"])
    if "length" in new_fields:
        exercise["length"] = validate_length(exercise["length"])
    if "difficulty" in new_fields:
        exercise["difficulty"] = validate_difficulty(exercise["difficulty"])
    return exercise
