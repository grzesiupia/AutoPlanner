"""
    Module algorithm.py is responsible of creating final schedule.
"""
# pylint: disable=C0301, W0511, R1735, C0116, R0913
import random

from singleton import Singleton
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
        return self.time_table[day][hour]

    def set_lessons_from_hour(self, day: int, hour: int, lessons):
        self.time_table[day][hour] = lessons

    def append_lesson_to_lessons_from_hour(self, day: int, hour: int, lesson_key: str, lesson_value, classroom=None):
        self.time_table[day][hour][lesson_key] = [*lesson_value, classroom]

    def print_schedule(self):
        for day in self.time_table:
            for hour in day:
                print(hour)
            print("\n")

    def print_group_schedule(self, group: str):
        for day in self.time_table:
            for hour in day:
                if group in hour:
                    print(hour[group])
                else:
                    print('-----')
            print("\n")

    # do sprawdzenia, czy nauczyciel na tą godzinę lekcyjną jest zajęty
    def is_teacher_busy(self, teacher: str, day: int, hour: int) -> bool:
        return teacher in self.busy_teachers_table[day][hour]

    # do sprawdzenia, czy sala na tą godzinę lekcyjną jest zajęta
    def is_classroom_busy(self, classroom: int, day: int, hour: int) -> bool:
        return classroom not in self.free_classrooms_table[day][hour]

    # do wskazania w planie, że jakiś nauczyciel jest zajęty
    def make_teacher_busy(self, teacher: str, day: int, hour: int):
        self.busy_teachers_table[day][hour].add(teacher)

    # classes_with_preferences musi mieć postać słownika postaci {sala: preferencja, ...} ({int: str, ...})
    def pop_correct_classroom(self, req: str, classes_with_req: dict, day: int, hour: int):
        # Jeżeli na daną godzinę nie ma wolnych sal to długość zbioru self.free_classrooms_table[day][hour] będzie
        # wynosić 0. Co sprawia, że nie ma żadnej poprawnej sali.
        if len(self.free_classrooms_table[day][hour]) == 0:
            return None
        # Zabieramy pierwszą salę z brzegu.
        free_classroom = self.free_classrooms_table[day][hour].pop()
        # Tworzymy zbiór sal, w których będziemy przechowywać sprawdzone już sale
        checked_classrooms = set()
        # Poniższa pętla będzie wykonywać się tak długo, aż sala nie będzie okej.
        while classes_with_req[free_classroom] != req:
            # sala, która okazała się niewłaściwa, zapisywana jest do checked_classrooms
            checked_classrooms.add(free_classroom)
            # jeżeli sprawdziliśmy cały zbiór free_classrooms_table[day][hour], to zwracamy None
            if len(self.free_classrooms_table[day][hour]) == 0:
                # przywracamy do free_classrooms_table[day][hour] sale, które zostały wcześniej zabrane
                self.free_classrooms_table[day][hour].update(checked_classrooms)
                return None
            # bierzemy kolejną salę
            free_classroom = self.free_classrooms_table[day][hour].pop()
        # przywracamy niewykorzystane sale do free_classrooms_table[day][hour]
        self.free_classrooms_table[day][hour].update(checked_classrooms)
        # zwracamy poprawną sae
        return free_classroom


class Algorithm(metaclass=Singleton):
    """
        Class Algorithm is main class of generator.
    """
    def __init__(self, school_: School):
        self.school = school_
        classrooms_temp = set()
        for classroom in self.school.classes:
            classrooms_temp.add(classroom.class_number)
        self.schedule = Schedule(school_.max_lessons_per_day_for_school, classrooms_temp)
        # if at the end this is 0 schedule is valid else schedule is trash
        self.remain_lessons_num = self.prepare_time_table()

        # zmienna uzupełniona w evaluate_time_table -> count_all_breaks
        # w tym słowniku mamy liczbę okienek w ciągu tygodnia dla każdej grupy
        self.group_breaks_num = {group.name: 0 for group_name, group in self.school.groups.items()}
        # zmienna uzupełniona w evaluate_time_table -> count_all_breaks
        # w tym słowniku mamy liczbę okienek w ciągu tygodnia dla każdego nauczyciela
        self.teacher_breaks_num = {teacher.name: 0 for teacher in self.school.teachers}

        self.evaluation = 0.0
        self.evaluate_time_table()

        # Jestem w szoku, że to działa, praktycznie niczego nie poprawiałem, trochę jest tu tylko rzeczy do
        # optymalizacji, dlatego też będzie dużo komentarzy.

    def prepare_time_table(self) -> int:
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
            # classroom_preference = subject[3]  # na ten moment zawsze None
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
                    classroom_temp = self.schedule.pop_correct_classroom(self.school.get_req_name(subject_name),
                                                                         self.school.classes_data,
                                                                         day,
                                                                         hour)
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
            teacher_memo = {teacher.name: 0 for teacher in self.school.teachers}
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


if __name__ == "__main__":
    school = School(school_class_data=GROUP, teachers_data=TEACHERS, classes_data=CLASSES, classroom_req=CLASSES_REQ)
    alg = Algorithm(school)
    print(alg.teacher_breaks_num)
    print(alg.group_breaks_num)
    print(alg.evaluation)

# TODO 1.zrozumienie co tu sie dzieje
# TODO 2.poprawa komentarzy
# TODO 3.make docstring
# TODO 4.funkcja oceny
# TODO 5.genetyka
# TODO 6.get dane do planu z backendu w jsonie
# TODO 7.send grafik dla nauczyela, plan zajec klasy i calej szkoly do jsona
# TODO 8.struktura danych z VLO
