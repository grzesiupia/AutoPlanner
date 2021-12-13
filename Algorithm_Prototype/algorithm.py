"""
    Module algorithm.py is responsible of creating final schedule.
"""
# pylint: disable=C0301, W0511, R1735, C0116, R0913, R0912, R0914, R0915, R1721
import copy
import random
import numpy as np
from joblib import Parallel, delayed

from data_structures import School
from teachers import TEACHERS
from groups import GROUP
from classrooms import CLASSES, CLASSES_REQ


class Schedule:
    """
        Class Schedule is used as api of module data_structures.py for Algorithm.
    """
    def __init__(self, max_lessons, list_of_classrooms: set):
        self.max_lessons = max_lessons
        self.list_of_classrooms = list_of_classrooms
        self.time_table = self.__set_time_table()
        self.busy_teachers_table = self.__set_busy_teachers_table()
        self.free_classrooms_table = self.__set_free_classrooms_table()

    def __set_time_table(self):
        temp = [[], [], [], [], []]
        for day in temp:
            for _ in range(int(self.max_lessons)):
                day.append(dict())
        return temp

    def __set_free_classrooms_table(self):
        temp = [[], [], [], [], []]
        for day in temp:
            for _ in range(int(self.max_lessons)):
                day.append(self.list_of_classrooms.copy())
        return temp

    def __set_busy_teachers_table(self):
        temp = [[], [], [], [], []]
        for day in temp:
            for _ in range(int(self.max_lessons)):
                day.append(set())
        return temp

    def get_lessons_from_hour(self, day: int, hour: int):
        """
        Get dict of lessons from particular hour of the day
        @param day: day to read lessons from
        @param hour: hour to read lessons from
        @return:
        """
        return self.time_table[day][hour]

    def set_lessons_from_hour(self, day: int, hour: int, lessons):
        self.time_table[day][hour] = lessons

    def append_lesson_to_lessons_from_hour(self, day: int, hour: int, group_name: str, lesson_value, classroom=None):
        """
        Append lesson to dict of lessons in particular hour of the day
        @param day: day to append lesson
        @param hour:  hour to append lesson
        @param group_name: name of group which lesson is appended
        @param lesson_value: [subject_name, teacher_name] assigned for this lesson
        @param classroom: classrom assigned for this lesson
        """
        self.time_table[day][hour][group_name] = [*lesson_value, classroom]

    def print_teacher_schedule(self, teacher):
        """
        Prints schedule for particular teacher
        @param teacher: teacher for whom schedule is printed
        """
        for day in self.time_table:
            for hour in day:
                for group, values in hour.items():
                    if values[1] == teacher:
                        print(hour[group])
                    else:
                        print('-----')
            print("\n")

    def print_schedule(self):
        """
        Prints full schedule of whole school
        """
        for day in self.time_table:
            for hour in day:
                print(hour)
            print("\n")

    def print_group_schedule(self, group: str):
        """
        Prints schedule for particular class
        @param group: group for which schedule is printed
        """
        for day in self.time_table:
            for hour in day:
                if group in hour:
                    print(hour[group])
                else:
                    print('-----')
            print("\n")

    def is_teacher_busy(self, teacher: str, day: int, hour: int) -> bool:
        """
        Check if teacher is busy in particular hour of the day
        @param teacher: name of teacher to check
        @param day: day to check
        @param hour: hour to check
        @return: if teacher in busy_table return teacher name else return None
        """
        return teacher in self.busy_teachers_table[day][hour]

    def is_classroom_busy(self, classroom: int, day: int, hour: int) -> bool:
        """
        Check if classroom is busy in particular hour of teh day
        @param classroom: classroom number
        @param day: day to check
        @param hour: hour to check
        @return: if classroom in busy_table return classroom number else None
        """
        return classroom not in self.free_classrooms_table[day][hour]

    def make_teacher_busy(self, teacher: str, day: int, hour: int):
        """
        Adds teacher to busy table
        @param teacher: teacher name
        @param day: day to assign
        @param hour: hour to assign
        """
        self.busy_teachers_table[day][hour].add(teacher)

    # classes_with_preferences musi mieć postać słownika postaci {sala: preferencja, ...} ({int: str, ...})
    def pop_correct_classroom(self, required_type_of_classroom: str, classrooms_with_type: dict, day: int, hour: int):
        """
        Checks if for particular hour in the day, there is free classroom of required type
        @param required_type_of_classroom: type of required classroom e.g.:'wf'
        @param classrooms_with_type: dict of classrooms
        @param day: day to check
        @param hour: hour to check
        @return: number of picked classroom or none if there is none available
        """
        # If no free classroom in table of available classrooms there is no valid classroom
        if len(self.free_classrooms_table[day][hour]) == 0:
            return None
        # Iterate throgh free classrooms in particular hour in the day
        for classroom in self.free_classrooms_table[day][hour]:
            if required_type_of_classroom == classrooms_with_type[classroom.class_number]:
                # If required type of classroom is same as type of classroom in iteration
                # number of this classroom is returned
                self.free_classrooms_table[day][hour].remove(classroom)
                return classroom.class_number
        # If there is no type of classroom as needed in free classrooms list none is returned
        return None


class Algorithm:
    """
        Class Algorithm is main class of generator.
    """
    def __init__(self, school_instance: School):
        self.school = school_instance
        self.schedule = Schedule(school_instance.max_lessons_per_day_for_school, school_instance.classrooms_set)
        self.remain_lessons_num = self.prepare_schedule()  # Must be 0 when algorithm finishes
        # count of brakes for each group
        self.group_breaks_num = {group_name: 0 for group_name, group in self.school.groups.items()}
        # # count of brakes for each teacher
        self.teacher_breaks_num = {teacher.name: 0 for teacher in self.school.teachers.values()}
        self.evaluation = 0.0
        self.evaluate_schedule_rating()

    def prepare_schedule(self) -> int:
        """
        This func produces already valid bot not good schedule for whole school.
        Before adding of lesson to schedule it checks if group doesn't already have lesson in this hour
        and if teacher assigned is not busy.
        @return: Number of unassigned lessons. Have to be 0 for valid schedule
        """
        unassigned_lesson_num = 0  # lessons left unassigned - schoud be 0 at the end

        for lesson in self.school.list_of_all_subjects:  # Try to add every lesson to schedule
            # indexes to iterate through in the loop
            day = 0
            hour = 0

            # Extract for better code clarity
            group_name = lesson[0]
            subject_name = lesson[1]
            teacher_name = lesson[2]
            # classroom_preference = lesson[3] for now not usable

            for _ in range(int(self.school.max_lessons_per_day_for_school * 5)):  # range of max lessons in week
                # Check if group doesn't have already assigned lesson and if teacher is free in this hour
                if group_name not in self.schedule.get_lessons_from_hour(day, hour) and \
                        not self.schedule.is_teacher_busy(teacher_name, day, hour):
                    # classroom_to_assign is a number of classroom which met requirement and assigned to this lesson
                    # if no classroom meeting requirement free -> classroom_to_assign = None
                    classroom_to_assign = self.schedule.pop_correct_classroom(
                        required_type_of_classroom=self.school.get_req_name(subject_name),
                        classrooms_with_type=self.school.classrooms_data,
                        day=day,
                        hour=hour)

                    # If classroom_to_assign is None then this lesson is not valid for this hour
                    if classroom_to_assign is not None:
                        # Add lesson to schedule
                        self.schedule.append_lesson_to_lessons_from_hour(day,
                                                                         hour,
                                                                         group_name,
                                                                         [subject_name, teacher_name],
                                                                         classroom=classroom_to_assign)
                        # Make teacher assigned, busy in this hour
                        self.schedule.make_teacher_busy(teacher=teacher_name, day=day, hour=hour)
                        break

                # Control of day and hour in schedule
                day += 1
                if day == 5:
                    day = 0
                    hour += 1

                    # If we are here that means we couldn't append lesson to schedule, then unassigned_lesson_num++
                    if hour == self.school.max_lessons_per_day_for_school:
                        unassigned_lesson_num += 1

        # If unassigned_lesson_num != 0 schedule is not valid
        return unassigned_lesson_num

    def evaluate_schedule_rating(self,
                                 group_break_importance=10,
                                 teacher_break_importance=2,
                                 tough_lessons_importance=3):
        """
        This func evaluates schedule rating basing on markers like: no brakes for groups etc.
        Best and wanted rating is 0. Throug evaluation points are added for every inconvenience.
        @param group_break_importance: points added to rating when group have brake in middle of lessons
        @param teacher_break_importance: points added to rating when teacher have brake in middle of lessons
        @param tough_lessons_importance: points added to rating when group have too many tough lessons per day
        """
        self._start_evaluation_new(tough_lessons_importance)

        # Evaluation of minus points for breaks of groups
        for group_breaks in self.group_breaks_num.values():
            self.evaluation -= group_breaks * group_break_importance

        # Evaluation of minus points for brakes of teachers
        for teacher_breaks in self.teacher_breaks_num.values():
            self.evaluation -= teacher_breaks * teacher_break_importance

    def _start_evaluation_new(self, tough_lessons_importance):
        time_table = np.array(self.schedule.time_table)

        # memo's for checking
        groups_memo = {group.name: 0 for group in self.school.groups.values()}
        teacher_memo = {teacher.name: 0 for teacher in self.school.teachers.values()}
        tough_lessons_memo = {group: 0 for group in self.school.groups}
        group_lessons_per_day_memo = {group: [] for group in groups_memo}

        # make memo's zeros copies for fast reset
        groups_memo_zeros = copy.deepcopy(groups_memo)
        teacher_memo_zeros = copy.deepcopy(teacher_memo)
        tough_lessons_memo_zeros = copy.deepcopy(tough_lessons_memo)
        group_lessons_per_day_memo_zeros = copy.deepcopy(group_lessons_per_day_memo)

        def count_teacher_breaks(teacher):
            if teacher in teachers_in_hour:
                if teacher_memo[teacher] == -1:
                    # this means break
                    self.teacher_breaks_num[teacher] += 1
                teacher_memo[teacher] = 1
            elif teacher_memo[teacher] == 0:
                # lessons haven't started yet
                pass
            else:
                # break or end of work
                teacher_memo[teacher] = -1

        def count_group_brakes(group, lesson_hour):
            if group in lesson_hour:
                if groups_memo[group] < 0:
                    # this means break
                    self.group_breaks_num[group] += 1
                groups_memo[group] = 1
            elif groups_memo[group] == 0:
                # it means lessons haven't started yet
                pass
            else:
                # end of lessons per day or increase break
                groups_memo[group] = -1
            # check if subject of class is tough
            if group in lesson_hour:
                if lesson_hour[group][0] in self.school.list_of_tough_subjects:
                    tough_lessons_memo[group] += 1

        def count_tough_lessons():
            for group, tough_lessons_num in tough_lessons_memo.items():
                diff_tough_lessons = self.school.groups[group].max_tough_lessons_per_day - tough_lessons_num
                if 0 > diff_tough_lessons:
                    # diff_tough_lessons is always nagative value
                    self.evaluation += tough_lessons_importance * diff_tough_lessons

        def check_teared_lessons_and_count(group, lesson_hour):
            # if there is few same subject in a day for group check if they are next to each other
            if group in lesson_hour:
                subject = lesson_hour[group][0]
                if subject in group_lessons_per_day_memo[group]:
                    if group_lessons_per_day_memo[group][hour - 1] == subject:
                        # they are next to each other no action needed
                        pass
                    else:
                        if subject == 'wf':
                            self.evaluation -= 50
                        # subjects are teared decrease evaluation value
                        else:
                            self.evaluation -= 10
                    # if more than 3 of type in day
                    if group_lessons_per_day_memo[group].count(subject) > 2:
                        self.evaluation -= 15
                    group_lessons_per_day_memo[group].append(subject)
                else:
                    group_lessons_per_day_memo[group].append(subject)
            else:
                group_lessons_per_day_memo[group].append("-")

        def check_easy_lessons():
            for group in group_lessons_per_day_memo:
                list_of_subjects = group_lessons_per_day_memo[group]
                if "-" in list_of_subjects:
                    list_of_subjects.remove("-")
                if "wf" in list_of_subjects:
                    lesson_index = list_of_subjects.index("wf")
                    if lesson_index == 0 or lesson_index == len(list_of_subjects):
                        # easy subject on start or end of the day
                        pass
                    else:
                        # subjects are teared decrease evaluation value
                        self.evaluation -= 15

        hour = 0
        for lesson in time_table.flatten():  # squash time_table to decrease time complexity
            # Reset hours, memo's (simulate day change), check tough lessons per day

            # Count for teacher
            teachers_in_hour = [lesson_values[1] for lesson_values in lesson.values()]
            for teacher in teacher_memo:
                count_teacher_breaks(teacher=teacher)

            # Count for groups
            for group in groups_memo:
                count_group_brakes(group=group, lesson_hour=lesson)
                check_teared_lessons_and_count(group=group, lesson_hour=lesson)

            hour += 1

            if hour == self.school.max_lessons_per_day_for_school:
                count_tough_lessons()
                check_easy_lessons()

                # reset values
                hour = 0
                groups_memo = copy.deepcopy(groups_memo_zeros)
                teacher_memo = copy.deepcopy(teacher_memo_zeros)
                tough_lessons_memo = copy.deepcopy(tough_lessons_memo_zeros)
                group_lessons_per_day_memo = copy.deepcopy(group_lessons_per_day_memo_zeros)

    @staticmethod
    def shuffle_list_of_subjects(base_list: list, num: int):
        copy_of_list = copy.deepcopy(base_list)
        length_of_list = len(base_list)
        indexes = [i for i in range(length_of_list)]
        samples = random.sample(indexes, num)
        samples_shuffle = copy.deepcopy(samples)
        random.shuffle(samples_shuffle)
        for i, sample in enumerate(samples):
            base_list[sample] = copy_of_list[samples_shuffle[i]]

    def print_teachers_breaks_count(self):
        print(self.teacher_breaks_num)

    def print_groups_breaks_count(self):
        print(self.group_breaks_num)


class Population:
    """
        Class population is responsible for handling genetic algorithm
    """

    def __init__(self):
        self.population = []

    def new_population(self, number_of_instances=100):
        for _ in range(number_of_instances):
            temp = Algorithm(School(groups_data=GROUP,
                                    teachers_data=TEACHERS,
                                    classrooms_data=CLASSES,
                                    classroom_req=CLASSES_REQ))
            self.population.append([temp, temp.evaluation])
        self.population.sort(key=lambda a: a[1], reverse=True)

    def kill_worse_half(self):
        count_to_kill = len(self.population) // 2
        self.population = self.population[:count_to_kill]

    def get_best_specimen(self):
        return self.population[0][0]

    def reproduce(self, mutation=10):
        temp_list = []
        for specimen in self.population:
            Algorithm.shuffle_list_of_subjects(specimen[0].school.list_of_all_subjects, mutation)
            temp = Algorithm(specimen[0].school)
            temp_list.append([temp, temp.evaluation])
        self.population += temp_list
        self.population.sort(key=lambda a: a[1], reverse=True)

    def parallel_reproduce(self, mutation=10):
        def generate_new_specimens(specimen: [Algorithm, int]):
            Algorithm.shuffle_list_of_subjects(specimen[0].school.list_of_all_subjects, mutation)
            temp = Algorithm(specimen[0].school)
            return [temp, temp.evaluation]

        answer = Parallel(n_jobs=7)(delayed(generate_new_specimens)(specimen) for specimen in self.population)
        self.population += answer
        self.population.sort(key=lambda a: a[1], reverse=True)

    def evolute(self, number_of_generation: int, number_of_mutation: int):
        for _ in range(number_of_generation):
            self.kill_worse_half()
            self.reproduce(number_of_mutation)

    def parallel_evolute(self, number_of_generation: int, number_of_mutation: int):
        for _ in range(number_of_generation):
            self.kill_worse_half()
            self.parallel_reproduce(number_of_mutation)


if __name__ == "__main__":
    import time

    POPULATION_SIZE = 10
    NUM_OF_GENERATIONS = 1000
    NUM_OF_MUTATIONS = 20

    p = Population()
    p.new_population(number_of_instances=POPULATION_SIZE)
    print(p.get_best_specimen().evaluation)
    start = time.time()
    p.evolute(NUM_OF_GENERATIONS, NUM_OF_MUTATIONS)
    end = time.time()
    print(f"Nonparallel: {end - start} sec")
    print(p.get_best_specimen().evaluation)
    # print(p.get_best_specimen().schedule.print_group_schedule('1a'))

    p2 = Population()
    p2.new_population(number_of_instances=POPULATION_SIZE)
    print(p2.get_best_specimen().evaluation)
    start = time.time()
    p2.parallel_evolute(NUM_OF_GENERATIONS, NUM_OF_MUTATIONS)
    end = time.time()
    print(f"Parallel: {end - start} sec")
    print(p2.get_best_specimen().evaluation)
    # print(p2.get_best_specimen().schedule.print_group_schedule('1a'))
    # print(p2.get_best_specimen().schedule.print_group_schedule('2a'))

# TODO 1.zrozumienie co tu sie dzieje z parallel
# TODO 2.Rozwiniecie oceny o klasy, i poprawienie punktow


# TODO 6.get dane do planu z backendu w jsonie
# TODO 7.send grafik dla nauczyela, plan zajec klasy i calej szkoly do jsona
