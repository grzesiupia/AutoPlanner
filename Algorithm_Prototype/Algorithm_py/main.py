import json

IB = {
    "matematyka": [8, "Marek Markowski", ""],
    "fizyka": [6, "Paulina Paulinowska", "308"],
    "j.polski": [4, "Zbigniew Zbigniewski", ""],
    "biologia": [2, "Bogdan Bogdanowicz", "200"],
    "chemia": [1, "Marianna Mania", "201"],
    "wf": [4, "Wlodzimierz Wlodzimski", "Sala gimnastyczna"],
    "religia": [2, "Ksiadz Robak", ""]
}

IA = {
    "matematyka": [6, "Marcjanna Milik", ""],
    "fizyka": [2, "Paulina Paulinowska", "308"],
    "j.polski": [4, "Barbara Barbarowicz", ""],
    "biologia": [2, "Bogdan Bogdanowicz", "200"],
    "chemia": [1, "Marianna Mania", "201"],
    "wf": [4, "Wlodzimierz Wlodzimski", "Sala gimnastyczna"],
    "religia": [2, "Ksiadz Robak", ""]
}

ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class SchoolClass:
    def __init__(self, name_of_class, dictionary, lessons_per_week):
        self.name = name_of_class
        self.max_lessons_per_day = int(lessons_per_week / 5 + 1)
        self.min_lessons_per_day = int(lessons_per_week / 5 - 1)
        self.max_tough_subjects_per_day = int(sum([dictionary[x][0] for x in dictionary if x in ToughSubjects]) / 5) + 1
        self.subjects = dictionary


def make_schedule(list_of_school_classes, schedule):
    for day in schedule:
        for h in range(6):
            day.append([])
            for school_class_object in list_of_school_classes:
                for lesson in school_class_object.subjects:
                    if school_class_object.subjects[lesson][0] > 0:
                        day[h].append([school_class_object.name, lesson, school_class_object.subjects[lesson]])
                        school_class_object.subjects[lesson][0] -= 1
                        break
    return schedule


def print_schedule(schedule):
    f = open('output.json', 'w')
    f.write(json.dumps(schedule))
    f.close()


if __name__ == "__main__":

    schedule_for_week = []

    for _ in range(5):
        schedule_for_week.append([])

    list_of_received_school_classes = [('IB', IB), ('IA', IA)]
    list_of_school_class_objects = []

    for l in list_of_received_school_classes:
        list_of_school_class_objects.append(SchoolClass(l[0], l[1], sum([l[1][x][0] for x in l[1]])))

    print_schedule(make_schedule(list_of_school_class_objects, schedule_for_week))

