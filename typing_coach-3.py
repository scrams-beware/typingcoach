# === Stage 3: Хранилище в памяти ===
# Project: TypingCoach
import uuid


class Exercise:
    def __init__(self, name, layout, length, difficulty):
        self.id = str(uuid.uuid4())
        self.name = name
        self.layout = layout
        self.length = length
        self.difficulty = difficulty

    def to_dict(self):
        return {
            'id': self.id,
            'name': self.name,
            'layout': self.layout,
            'length': self.length,
            'difficulty': self.difficulty,
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            name=data['name'],
            layout=data['layout'],
            length=data['length'],
            difficulty=data['difficulty'],
        )


class ExerciseStore:
    def __init__(self):
        self._exercises = {}

    def add(self, name, layout, length, difficulty):
        exercise = Exercise(name, layout, length, difficulty)
        self._exercises[exercise.id] = exercise
        return exercise

    def get(self, exercise_id):
        return self._exercises.get(exercise_id)

    def list(self):
        return list(self._exercises.values())
