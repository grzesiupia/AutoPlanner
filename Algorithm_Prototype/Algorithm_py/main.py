Dictionary = {
    "matematyka": 6,
    "fizyka": 2,
    "j.polski": 4,
    "biologia": 2,
    "chemia": 1,
    "wf": 4,
    "religia": 2
}


ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class SchoolClass:
    def __init__(self, lessons_per_week):
        self.max_lessons_per_day = int(lessons_per_week / 5 + 1)
        self.min_lessons_per_day = int(lessons_per_week / 5 - 1)
        self.max_tough_subjects_per_day = sum([Dictionary[x] for x in Dictionary if x in ToughSubjects])


if __name__ == "__main__":
    t = SchoolClass(sum(Dictionary.values()))
    print(t.max_tough_subjects_per_day, t.max_lessons_per_day, t.min_lessons_per_day)
