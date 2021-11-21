from singleton import Singleton
from data_structures import School, GROUP, TEACHERS, CLASSES
import string


class Schedule:
    def __init__(self, max_lessons):
        self.time_table = [[], [], [], [], []]
        for day in self.time_table:
            for _ in range(int(max_lessons)):
                day.append(dict())

    def get_lessons_from_hour(self, day: int, hour: int):
        return self.time_table[day][hour]

    def set_lessons_from_hour(self, day: int, hour: int, lessons):
        self.time_table[day][hour] = lessons

    def append_lesson_to_lessons_from_hour(self, day: int, hour: int, lesson_key: string, lesson_value):
        self.time_table[day][hour][lesson_key] = lesson_value

    def print_schedule(self):
        for day in self.time_table:
            for hour in day:
                print(hour)
            print("\n")


class Algorithm(metaclass=Singleton):
    def __init__(self, school: School):
        self.school = school
        self.schedule = Schedule(school.max_lessons_per_day_for_school)
        self.prepare_time_table_new()

    # TODO convert ifs from statement to addittional func with crucial conditions for schedule to be valid
    def prepare_time_table_new(self):
        for day in range(5):
            for hour in range(int(school.max_lessons_per_day_for_school)):
                for group in self.school.groups:
                    if len(group.list_of_subjects) != 0 and hour < group.max_lessons_per_day:
                        lesson_value = group.list_of_subjects.pop()
                        self.schedule.append_lesson_to_lessons_from_hour(day=day,
                                                                         hour=hour,
                                                                         lesson_key=group.name,
                                                                         lesson_value=lesson_value)


if __name__ == "__main__":
    school = School(school_class_data=GROUP, teachers_data=TEACHERS, classes_data=CLASSES)
    alg = Algorithm(school)
    alg.schedule.print_schedule()
