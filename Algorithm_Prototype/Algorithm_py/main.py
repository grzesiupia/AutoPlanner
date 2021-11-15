import string

CLASSES = {
    100: "biologia",
    101: "fizyka",
    102: "matematyka",
    103: None,
    104: "Chemia",
    105: None,
    200: "wf"
}

TEACHERS = {
    "Janusz Walczuk": {
        'subject': "matematyka",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Krystyna Pawłowicz": {
        'subject': "j.polski",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Robert Lewandowski": {
        'subject': "wf",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Waldemar Kiepski": {
        'subject': "chemia",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Ksiądz Robak": {
        'subject': "religia",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': None,
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': None
        }
    },
    "Snoop Dogg": {
        'subject': "biologia",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Albert Einstein": {
        'subject': "fizyka",
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thusday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    }
}

SCHOOL_CLASSES = {
    'IB': {
        "matematyka": [8, None],
        "fizyka": [4, None],
        "j.polski": [6, None],
        "biologia": [2, None],
        "chemia": [1, None],
        "wf": [2, None],
        "religia": [2, None],
    },
    'IA': {
        "matematyka": [6, None],
        "fizyka": [2, None],
        "j.polski": [4, None],
        "biologia": [4, None],
        "chemia": [3, None],
        "wf": [4, None],
        "religia": [2, None]
    },
    'IC': {
        "matematyka": [5, None],
        "fizyka": [4, None],
        "j.polski": [4, None],
        "biologia": [2, None],
        "chemia": [4, None],
        "wf": [4, None],
        "religia": [2, None]
    },
    'ID': {
        "matematyka": [6, None],
        "fizyka": [2, None],
        "j.polski": [7, None],
        "biologia": [3, None],
        "chemia": [2, None],
        "wf": [4, None],
        "religia": [1, None]
    },
    'IIA': {
        "matematyka": [6, "Janusz Walczuk"],
        "fizyka": [2, "Albert Einstein"],
        "j.polski": [7, "Krystyna Pawłowicz"],
        "biologia": [3, "Snoop Dogg"],
        "chemia": [2, "Waldemar Kiepski"],
        "wf": [4, "Robert Lewandowski"],
        "religia": [1, None]
    }
    
}

ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class Class:
    def __init__(self, class_number, preferred_subject):
        self.class_number = class_number
        self.preferred_subject = preferred_subject


class School:
    def __init__(self, school_class_data: dict, teachers_data: dict, classes_data: dict):
        self.school_name = None
        self.classes = self.__process_classes(classes_data)
        self.school_classes = self.__process_school_classes(school_class_data)
        self.teachers = self.__process_teachers(teachers_data)

    @staticmethod
    def __process_school_classes(school_class_data):
        temp = []
        for school_class, subjects in school_class_data.items():
            temp.append(SchoolClass(name_of_class=school_class, subjects=subjects))
        return temp

    @staticmethod
    def __process_teachers(teachers_data):
        temp = []
        for name, data in teachers_data.items():
            temp.append(Teacher(name=name, data=data))
        return temp

    @staticmethod
    def __process_classes(classes_data):
        temp = []
        for class_number, preferred_subject in classes_data.items():
            temp.append(Class(class_number=class_number, preferred_subject=preferred_subject))
        return temp


class Teacher:
    def __init__(self, name: string, data: dict):
        self.name = name
        self.data = data
        self.subject = self.__set_subject()
        self.work_hours = None

    def __set_subject(self):
        return self.data['subject']

    def __set_work_hours(self):
        return self.data['work_hours']


class SchoolClass:
    def __init__(self, name_of_class: string, subjects: dict):
        self.name = name_of_class
        self.subjects = subjects
        self.lessons_per_week = self.__set_lessons_per_week()
        self.max_lessons_per_day = self.__set_max_lessons_per_day()
        self.min_lessons_per_day = self.__set_min_lessons_per_day()
        self.max_tough_lessons_per_day = self.__set_max_tough_lessons_per_day()
        self.prefered_teachers = self.__set_prefered_teachers()

    def __set_lessons_per_week(self):
        count = 0
        for key, value in self.subjects.items():
            count += value[0]
        return count

    def __set_max_lessons_per_day(self):
        return self.lessons_per_week / 5 + 1

    def __set_min_lessons_per_day(self):
        return self.lessons_per_week / 5 - 1

    def __set_max_tough_lessons_per_day(self):
        count = 0
        for key, value in self.subjects.items():
            if key in ToughSubjects:
                count += value[0]
        return count / 5

    def __set_prefered_teachers(self):
        temp = {}
        for subject, teacher in self.subjects.items():
            if teacher[1] is not None:
                temp[subject] = teacher[1]
        if len(temp) == 0:
            temp = None
        return temp


if __name__ == "__main__":
    school = School(school_class_data=SCHOOL_CLASSES, teachers_data=TEACHERS, classes_data=CLASSES)
    print(school.school_classes[4].prefered_teachers)
