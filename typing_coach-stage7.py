# === Stage 7: Текстовый поиск ===
# Project: TypingCoach
def highlight_matches(text, pattern):
    """Return text with matched substrings wrapped in ANSI highlight codes.

    Matching is case-insensitive. Non-matching characters are prefixed with a
    space so that wrapped runs stay column-aligned when printed.
    """
    if not pattern:
        return text
    lowered = text.lower()
    needle = pattern.lower()
    start = 0
    end = 0
    result = []
    while True:
        index = lowered.find(needle, start)
        if index == -1:
            break
        end = index + len(needle)
        result.append(" " * (index - start))
        result.append("\033[7m" + text[index:end] + "\033[0m")
        start = end
    result.append(" " * (len(text) - start))
    return "".join(result)


def find_exercise(title, layout, length, difficulty, query):
    """Case-insensitive search across an exercise's text fields.

    Returns the first exercise whose title, layout, length, or difficulty
    contains the query, or None when nothing matches.
    """
    fields = (title, layout, length, difficulty)
    lowered = [field.lower() for field in fields]
    needle = query.lower()
    for index in range(len(lowered)):
        if needle in lowered[index]:
            return fields[index]
    return None


if __name__ == "__main__":
    exercises = [
        ("Quick Brown Fox", "qwerty", 60, "easy"),
        ("Parallel Lines", "colemak", 80, "hard"),
        ("Practice Makes Perfect", "dvorak", 100, "medium"),
    ]
    user_input = input("Search: ").strip()
    match = find_exercise(*exercises, user_input) if user_input else None
    if match is None:
        print("No match found.")
    else:
        print("Match:", match)
        print(highlight_matches(", ".join(exercises), user_input))
