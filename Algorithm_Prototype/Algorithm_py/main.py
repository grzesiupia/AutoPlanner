import itertools
from random import shuffle

IB = {
    "matematyka": [8, "Marek Markowski", "211"],
    "fizyka": [4, "Paulina Paulinowska", "308"],
    "j.polski": [6, "Zbigniew Zbigniewski", "205"],
    "biologia": [2, "Bogdan Bogdanowicz", "200"],
    "chemia": [1, "Marianna Mania", "201"],
    "wf": [2, "Wlodzimierz Wlodzimski", "Sala gimnastyczna"],
    "religia": [2, "Ksiadz Robak", "104"]
}

IA = {
    "matematyka": [6, "Marcjanna Milik", "212"],
    "fizyka": [2, "Paulina Paulinowska", "308"],
    "j.polski": [4, "Barbara Barbarowicz", "206"],
    "biologia": [4, "Bogdan Bogdanowicz", "200"],
    "chemia": [3, "Marianna Mania", "201"],
    "wf": [4, "Mieczysław Monciak", "Sala gimnastyczna"],
    "religia": [2, "Ksiadz Robak", "104"]
}

IC = {
    "matematyka": [5, "Michalina Miś", "213"],
    "fizyka": [4, "Paulina Paulinowska", "308"],
    "j.polski": [4, "Barbara Barbarowicz", "205"],
    "biologia": [2, "Bogdan Bogdanowicz", "200"],
    "chemia": [4, "Marianna Mania", "201"],
    "wf": [4, "Mieczysław Monciak", "Sala gimnastyczna"],
    "religia": [2, "Ksiadz Robak", "104"]
}

ID = {
    "matematyka": [6, "Marcelina Korcz", "212"],
    "fizyka": [2, "Paulina Paulinowska", "308"],
    "j.polski": [7, "Halina Makłowicz", "204"],
    "biologia": [3, "Bogdan Bogdanowicz", "200"],
    "chemia": [2, "Marianna Mania", "201"],
    "wf": [4, "Wlodzimierz Wlodzimski", "Sala gimnastyczna"],
    "religia": [1, "Ksiadz Robak", "104"]
}

ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class SchoolClass:
    def __init__(self, name_of_class, dictionary, lessons_per_week):
        self.name = name_of_class
        self.max_lessons_per_day = int(lessons_per_week / 5 + 1)
        self.avg_lessons_per_day = int(lessons_per_week / 5)
        self.min_lessons_per_day = int(lessons_per_week / 5 - 1)
        self.days_to_increase_lessons = int(lessons_per_week % 5)
        self.max_tough_subjects_per_day = int(sum([dictionary[x][0] for x in dictionary if x in ToughSubjects]) / 5) + 1
        self.subjects = dictionary


def all_distinct(lis):
    return len(set(lis)) == len(lis)


def validate_schedule(dict_data_to_schedule, list_of_school_classes):
    val = [x for x in dict_data_to_schedule]
    temp_teacher = []
    temp_classroom = []
    for x in range(25):
        temp_teacher.clear()
        temp_classroom.clear()
        for y in val:
            temp_teacher.append(dict_data_to_schedule[y][x][1])
            temp_classroom.append(dict_data_to_schedule[y][x][2])
        if not all_distinct(temp_teacher):
            return False
        if not all_distinct(temp_classroom):
            return False
    print_schedule(dict_data_to_schedule)
    return True


def prepare_data(list_of_school_classes):
    list_of_all_subjects_for_class = {}

    for school_class in list_of_school_classes:
        temp = []
        for subject in school_class.subjects:
            while school_class.subjects[subject][0] > 0:
                temp.append([subject, *school_class.subjects[subject][1:]])
                school_class.subjects[subject][0] -= 1
        list_of_all_subjects_for_class[school_class.name] = temp

    list_of_all_subjects_for_class_sh = list_of_all_subjects_for_class.copy()

    temp = {}
    while True:
        temp.clear()
        for school_class in list_of_school_classes:
            shuffle(list_of_all_subjects_for_class_sh[school_class.name])
            temp[school_class.name] = list(list_of_all_subjects_for_class_sh[school_class.name])
        if validate_schedule(temp, list_of_school_classes):
            print("jest git")
            break


def print_schedule(schedule):
    file = open('output.json', 'w')
    schedule_str = ""
    for i in range(25):
        for x in schedule:
            schedule_str += (str(i) + " " + str(x) + " " + str(schedule[x][i]) + "\t\t\t")
        schedule_str += "\n"
        if (i+1) % 5 == 0:
            schedule_str += "\n"
    file.write(schedule_str)
    file.close()


if __name__ == "__main__":

    list_of_received_school_classes = [('IB', IB), ('IA', IA), ('IC', IC), ('ID', ID)]
    list_of_school_class_objects = []

    for l in list_of_received_school_classes:
        list_of_school_class_objects.append(SchoolClass(l[0], l[1], sum([l[1][x][0] for x in l[1]])))

    prepare_data(list_of_school_class_objects)
