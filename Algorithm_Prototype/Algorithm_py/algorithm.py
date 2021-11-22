from singleton import Singleton
from data_structures import School, Group, GROUP, TEACHERS, CLASSES
import string


class Schedule:
    def __init__(self, max_lessons):
        self.time_table = [[], [], [], [], []]
        for day in self.time_table:
            for _ in range(int(max_lessons)):
                day.append(dict())

        self.busy_table = [[], [], [], [], []]
        for day in self.busy_table:
            for _ in range(int(max_lessons)):
                day.append(set())

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
        self.prepare_time_table()

    # TODO convert ifs from statement to additional func with crucial conditions for schedule to be valid
    def prepare_time_table(self):
        for hour in range(int(school.max_lessons_per_day_for_school)):
            for group in self.school.groups:
                for day in range(len(self.schedule.time_table)):
                    if self.statement(day, hour, group):
                        lesson_value = group.list_of_subjects.pop()
                        self.schedule.append_lesson_to_lessons_from_hour(day=day,
                                                                         hour=hour,
                                                                         lesson_key=group.name,
                                                                         lesson_value=lesson_value)

    def shuffle_list_of_subjects(self, base_list: list, n: int):
        import random
        copy_of_list = base_list.copy()
        length_of_list = len(base_list)
        indexes = []
        for index in range(length_of_list):
            indexes.append(index)
        random.shuffle(indexes)
        for _ in range(length_of_list-n):
            indexes.pop()
        ordered_list = indexes.copy()
        ordered_list.sort()
        j = 0
        for index in ordered_list:
            base_list[index] = copy_of_list[indexes[j]]
            j += 1

    def statement(self, day: int, hour: int, group: Group) -> bool:
        if len(group.list_of_subjects) != 0 and hour < group.max_lessons_per_day:
            return True
        else:
            return False


if __name__ == "__main__":
    school = School(school_class_data=GROUP, teachers_data=TEACHERS, classes_data=CLASSES)
    alg = Algorithm(school)
    alg.schedule.print_schedule()
