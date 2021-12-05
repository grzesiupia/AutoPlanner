"""
    Module algorithm.py is responsible of creating final schedule.
"""
# pylint: disable=C0301, W0511, R1735, C0116, R0913
import random

from data_structures import School, GROUP, TEACHERS, CLASSES, CLASSES_REQ


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
        self.remain_lessons_num = self.prepare_time_table()  # Must be 0 when algorithm finishes
        # zmienna uzupełniona w evaluate_time_table -> count_all_breaks
        # w tym słowniku mamy liczbę okienek w ciągu tygodnia dla każdej grupy
        self.group_breaks_num = {group_name: 0 for group_name, group in self.school.groups.items()}
        # zmienna uzupełniona w evaluate_time_table -> count_all_breaks
        # w tym słowniku mamy liczbę okienek w ciągu tygodnia dla każdego nauczyciela
        self.teacher_breaks_num = {teacher.name: 0 for teacher in self.school.teachers.values()}

        self.evaluation = 0.0
        self.evaluate_time_table()

    def prepare_time_table(self) -> int:
        """

        @return:
        """
        # Ta zmienna będzie również zwracana, jeżeli będzie na końcu różna od zera to znaczy, że plan jest niepoprawny
        # oznacza ona liczbę zajęć, które ni chuja nie dało się nigdzie podpiąć.
        unassigned_subject_num = 0
        # Pętla po wszystkich zajęciach na samej górze, czyli dla każdej lekcji sprawdzimy każdą możliwą godzinę
        # lekcyjną. Wydaje się też optymalne.
        for subject in self.school.list_of_all_subjects:
            # Żeby nie tworzyć nadmiaru kolejnych pętli for to zrobiłem tu coś takiego: możliwych godzin lekcyjnych
            # jest zawsze 5*max_w_dniu, możemy z góry wyznaczyć konkretną liczbę iteracji w JEDNEJ pętli.

            # Zmienne poniżej będą zmieniane w pętli.
            day = 0
            hour = 0
            # wypakowanie zmiennej subject, żeby czytelniej było
            group_name = subject[0]
            subject_name = subject[1]
            teacher_name = subject[2]
            # self.school.list_of_all_subjects jest za dużo danych
            # classroom_preference = subject[3] na ten moment zawsze None
            # Jest 5 dni w tygodniu mordko, co nie? Mnożymy razy maksymalną liczbę godzin lekcyjnych w dniu i mamy jedną
            # pętlę zamiast dwóch.
            for _ in range(int(self.school.max_lessons_per_day_for_school * 5)):
                # Kluczem w słowniku zwracanym w funkcji get_lessons_from_hour jest grupa, dlatego, jeżeli nie ma
                # takiego klucza, to znaczy, że na tą godzinę grupa nie ma na razie zaplanowanych zajęć. Sprawdzane
                # jest również czy nauczyciel jest zajęty.
                if group_name not in self.schedule.get_lessons_from_hour(day, hour) and \
                        not self.schedule.is_teacher_busy(teacher_name, day, hour):
                    # classroom_temp ma mieć w sobie nazwę pasującej sali lekcyjnej, jeżeli, żadna sala nie pasuje w
                    # tej jednostce lekcyjnej, to classroom_temp przyjmuje wartość None
                    classroom_temp = self.schedule.pop_correct_classroom(
                        required_type_of_classroom=self.school.get_req_name(subject_name),
                        classrooms_with_type=self.school.classrooms_data,
                        day=day,
                        hour=hour)
                    # Jeżeli classroom_temp przyjmie wartość None, to ta godzina lekcyjna jest do dupy i sprawdzamy
                    # nie dodajemy lekcji do tej godziny.
                    if classroom_temp is not None:
                        self.schedule.append_lesson_to_lessons_from_hour(day,
                                                                         hour,
                                                                         group_name,
                                                                         [subject_name, teacher_name],
                                                                         classroom=classroom_temp)
                        # jeżeli udało się dodać, to przerywamy szukanie odpowiedniego terminu i przechodzimy do
                        # następnej klasy
                        self.schedule.make_teacher_busy(teacher=teacher_name, day=day, hour=hour)
                        break

                # Tutaj kontrolujemy, którą mamy godzinę i, który mamy dzień
                day += 1
                if day == 5:
                    day = 0
                    hour += 1
                    # Jeżeli nie udało się przydzielić się lekcji do żadnej godziny, to wypadałoby to jakoś
                    # zasygnalizować -> zwiększamy więc wartość zmiennej unassigned_subject_num, która oznacza
                    # ile takich lekcji jest w sumie
                    if hour == self.school.max_lessons_per_day_for_school:
                        unassigned_subject_num += 1
                        # Ten break w sumie nie potrzebny, ale przynajmniej widać, że z tego poziomu zawsze rozpocznie
                        # się następna iteracja.
                        break
        # Kozak by było, gdyby ta zmienna miała zawsze wartość 0
        return unassigned_subject_num

    # funkcja oceny
    def evaluate_time_table(self,
                            group_break_significance=10,
                            teacher_break_significance=2,
                            tough_lessons_significance=3):
        # w celu zwiększenia czytelności kodu, iteracja przez dni i godziny została umieszczona w osobnej metodzie
        # _start_evaluation, metoda ta wykonuje następujące czynności:
        # 1. policz okienka i uzupełnij nimi self.group_breaks_num oraz self.teacher_breaks_num (tylko uzupełnia!)
        self._start_evaluation(tough_lessons_significance)

        # wpływ okienek na ocenę planu zajęć (okienka dla grup)
        for group_name, breaks_num in self.group_breaks_num.items():
            self.evaluation -= breaks_num * group_break_significance

        # wpływ okienek na ocenę planu zajęć (okienka dla nauczycieli)
        for teacher_name, breaks_num in self.teacher_breaks_num.items():
            self.evaluation -= breaks_num * teacher_break_significance

    def _start_evaluation(self, tough_lessons_significance):
        for day in self.schedule.time_table:
            # ten słownik służy do zapamiętywania poprzedniej iteracji, jeżeli wartość wynosi
            # 0 - lekcje się jeszcze nie rozpoczęły
            # -1 - na poprzedniej lekcji było okienko
            # 1 - na poprzedniej lekcji były zajęcia
            groups_memo = {group_name: 0 for group_name in self.school.groups}
            teacher_memo = {teacher.name: 0 for teacher in self.school.teachers.values()}
            group_name_to_tough_lessons_num = {group_name: 0 for group_name in self.school.groups}
            for hour in day:
                for group_name in groups_memo:
                    if group_name in hour:
                        if groups_memo[group_name] == -1:
                            # tu mamy okienko
                            self.group_breaks_num[group_name] += 1
                        groups_memo[group_name] = 1
                    elif groups_memo[group_name] == 0:
                        # tutaj lekcje się nie rozpoczęły
                        pass
                    else:
                        # kolejny z rzędu brak zajęć albo większe okienko, albo koniec lekcji
                        groups_memo[group_name] = -1

                    # ===============================================================================================
                    # ==== Początek części pętli odpowiedzialnej za uwzględnienie trudnych przedmiotów w ocenie planu
                    # zostało to umieszczone tutaj, żeby nie tworzyć dwa razy kolosalnej pętli
                    # upewniamy się tylko czy w danej godzinie grupa ma zajęcia
                    if group_name in hour:
                        if hour[group_name][0] in self.school.list_of_tough_subjects:
                            group_name_to_tough_lessons_num[group_name] += 1
                    # ==== Koniec części pętli odpowiedzialnej za uwzględnienie trudnych przedmiotów w ocenie planu
                    # ===============================================================================================

                # tutaj liczenie okienek, ale dla nauczycieli
                for teacher_name in teacher_memo:
                    teachers_in_hour = {lesson_values[1] for group_name, lesson_values in hour.items()}
                    if teacher_name in teachers_in_hour:
                        if teacher_memo[teacher_name] == -1:
                            # tu mamy okienko
                            self.teacher_breaks_num[teacher_name] += 1
                        teacher_memo[teacher_name] = 1
                    elif teacher_memo[teacher_name] == 0:
                        # tutaj lekcje się nie rozpoczęły
                        pass
                    else:
                        # kolejny z rzędu brak zajęć albo większe okienko, albo koniec lekcji
                        teacher_memo[teacher_name] = -1
            # =====================================================================================================
            # ========== Ta część znowu odpowiada za uwzględnienie trudnych przedmiotów w ocenie planu
            for group_name, tough_lessons_num in group_name_to_tough_lessons_num.items():
                # sub to różnica faktycznej liczby trudnych przedmiotów z preferowaną maksymalną liczbą trudnych
                # przedmiotów
                sub = self.school.groups[group_name].max_tough_lessons_per_day - tough_lessons_num
                if 0 > sub:
                    # sub jest tutaj zawsze ujemna, dlatego jest dodawanie
                    self.evaluation += tough_lessons_significance * sub
            # =====================================================================================================

    @staticmethod
    def shuffle_list_of_subjects(base_list: list, num: int):
        copy_of_list = base_list.copy()
        length_of_list = len(base_list)
        indexes = []
        for index in range(length_of_list):
            indexes.append(index)
        random.shuffle(indexes)
        for _ in range(length_of_list - num):
            indexes.pop()
        ordered_list = indexes.copy()
        ordered_list.sort()
        for pos, index in enumerate(ordered_list):
            base_list[index] = copy_of_list[indexes[pos]]


class Population:
    def __init__(self):
        self.population = []

    def new_population(self, n=100):
        for _ in range(n):
            temp = Algorithm(School(groups_data=GROUP,
                                    teachers_data=TEACHERS,
                                    classrooms_data=CLASSES,
                                    classroom_req=CLASSES_REQ))
            self.population.append([temp, temp.evaluation])
        self.population.sort(key=lambda a: a[1], reverse=True)

    def kill_worse_half(self):
        n = len(self.population) // 2
        self.population = self.population[:n]

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

    def evolute(self, number_of_generation: int, number_of_mutation: int):
        for _ in range(number_of_generation):
            self.kill_worse_half()
            self.reproduce(number_of_mutation)


if __name__ == "__main__":
    p = Population()
    p.new_population(n=10)
    print(p.population)
    print(p.get_best_specimen().teacher_breaks_num, "\n")
    print(p.get_best_specimen().evaluation)
    p.evolute(5000, 10)
    print(p.get_best_specimen().schedule.print_group_schedule('IA'))
    print(p.get_best_specimen().teacher_breaks_num)
    print(p.get_best_specimen().evaluation)


# TODO 1.zrozumienie co tu sie dzieje
# TODO 2.poprawa komentarzy
# TODO 3.make docstring
# TODO 6.get dane do planu z backendu w jsonie
# TODO 7.send grafik dla nauczyela, plan zajec klasy i calej szkoly do jsona
# TODO 8.struktura danych z VLO
