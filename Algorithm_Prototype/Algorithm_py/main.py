

IB = {
    "matematyka": [8, "Marek Markowski", ""],
    "fizyka": [6, "Paulina Paulinowska", "308"],
    "j.polski": [4, "Zbigniew Zbigniewski", ""],
    "biologia": [2, "Bogdan Bogdanowicz", "200"],
    "chemia": [1, "Marianna Mania", "201"],
    "wf": [4, "Włodzimierz Włodzimski", "Sala gimnastyczna"],
    "religia": [2, "Ksiądz Robak", ""]
}


IA = {
    "matematyka": [6, "Marcjanna Milik", ""],
    "fizyka": [2, "Paulina Paulinowska", "308"],
    "j.polski": [4, "Barbara Barbarowicz", ""],
    "biologia": [2, "Bogdan Bogdanowicz", "200"],
    "chemia": [1, "Marianna Mania", "201"],
    "wf": [4, "Włodzimierz Włodzimski", "Sala gimnastyczna"],
    "religia": [2, "Ksiądz Robak", ""]
}


ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class SchoolClass:
    def __init__(self, dictionary, lessons_per_week):
        self.max_lessons_per_day = int(lessons_per_week / 5 + 1)
        self.min_lessons_per_day = int(lessons_per_week / 5 - 1)
        self.max_tough_subjects_per_day = int(sum([dictionary[x][0] for x in dictionary if x in ToughSubjects]) / 5) + 1
        self.subjects = dictionary


def make_schedule(list_of_school_classes: SchoolClass, schedule):

    for school_class_object in list_of_school_classes:
        for day in schedule:
            for lesson in day:
                lesson.append(key for key in school_class_object.subjects)

    print(schedule)

    return schedule


if __name__ == "__main__":

    schedule_for_week = []

    for _ in range(5):
        schedule_for_week.append([[]])

    list_of_received_school_classes = [IB, IA]
    list_of_school_class_objects = []

    for l in list_of_received_school_classes:
        list_of_school_class_objects.append(SchoolClass(l, sum([l[x][0] for x in l])))

    make_schedule(list_of_school_class_objects, schedule_for_week)
