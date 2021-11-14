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
        "matematyka": 8,
        "fizyka": 4,
        "j.polski": 6,
        "biologia": 2,
        "chemia": 1,
        "wf": 2,
        "religia": 2
    },
    'IA': {
        "matematyka": 6,
        "fizyka": 2,
        "j.polski": 4,
        "biologia": 4,
        "chemia": 3,
        "wf": 4,
        "religia": 2
    },
    'IC': {
        "matematyka": 5,
        "fizyka": 4,
        "j.polski": 4,
        "biologia": 2,
        "chemia": 4,
        "wf": 4,
        "religia": 2
    },
    'ID': {
        "matematyka": 6,
        "fizyka": 2,
        "j.polski": 7,
        "biologia": 3,
        "chemia": 2,
        "wf": 4,
        "religia": 1
    }
}

ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class School:
    def __init__(self, school_class_data: dict, teachers_data: dict, classes_data: dict):
        self.school_name = None
        self.classes = classes_data
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

    def __set_lessons_per_week(self):
        count = 0
        for key, value in self.subjects.items():
            count += value
        return count

    def __set_max_lessons_per_day(self):
        return self.lessons_per_week / 5 + 1

    def __set_min_lessons_per_day(self):
        return self.lessons_per_week / 5 - 1

    def __set_max_tough_lessons_per_day(self):
        count = 0
        for key, value in self.subjects.items():
            if key in ToughSubjects:
                count += value
        return count / 5


if __name__ == "__main__":
    school = School(school_class_data=SCHOOL_CLASSES, teachers_data=TEACHERS, classes_data=CLASSES)
    print(school.teachers[1].name)
