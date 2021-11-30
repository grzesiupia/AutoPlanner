from singleton import Singleton
from data_structures import School, GROUP, TEACHERS, CLASSES, CLASSES_REQ
import string


class Schedule:
    def __init__(self, max_lessons, list_of_classrooms: set):
        self.time_table = [[], [], [], [], []]
        for day in self.time_table:
            for _ in range(int(max_lessons)):
                day.append(dict())

        self.busy_teachers_table = [[], [], [], [], []]
        for day in self.busy_teachers_table:
            for _ in range(int(max_lessons)):
                day.append(set())

        self.free_classrooms_table = [[], [], [], [], []]
        for day in self.free_classrooms_table:
            for _ in range(int(max_lessons)):
                day.append(list_of_classrooms.copy())

    def get_lessons_from_hour(self, day: int, hour: int):
        return self.time_table[day][hour]

    def set_lessons_from_hour(self, day: int, hour: int, lessons):
        self.time_table[day][hour] = lessons

    def append_lesson_to_lessons_from_hour(self, day: int, hour: int, lesson_key: string, lesson_value, classroom=None):
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

    # do sprawdzenia czy nauczyciel na tą godzinę lekcyjną jest zajęty
    def is_teacher_busy(self, teacher: str, day: int, hour: int) -> bool:
        return teacher in self.busy_teachers_table[day][hour]

    # do sprawdzenia czy sala na tą godzinę lekcyjną jest zajęta
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
        # Zabieramy pierwszą sale z brzegu.
        free_classroom = self.free_classrooms_table[day][hour].pop()
        # Tworzymy zbiór sal w których będziemy przechowywać sprawdzone już sale
        checked_classrooms = set()
        # Poniższa pętla będzie wykonywać się tak długo, aż sala nie będzie okej.
        while classes_with_req[free_classroom] != req:
            # sala, która okazała się być niewłaściwa, zapisywana jest do checked_classrooms
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
    def __init__(self, school_: School):
        self.school = school_
        classrooms_temp = set()
        for classroom in self.school.classes:
            classrooms_temp.add(classroom.class_number)
        self.schedule = Schedule(school_.max_lessons_per_day_for_school, classrooms_temp)
        self.remain_lessons_num = self.prepare_time_table()

        # Jestem w szoku, że to działa, praktycznie niczego nie poprawiałem, trochę jest tu tylko rzeczy do
        # optymalizacji, dlatego też będzie dużo komentarzy.

    def prepare_time_table(self) -> int:
        # Ta zmienna będzie również zwracana, jeżeli będzie na końcu różna od zera to znaczy, że plan jest niepoprawny
        # oznacza ona liczbę zajęć, które ni chuja nie dało się nigdzie podpiąć.
        unassigned_subject_num = 0
        # Pętla po wszystkich zajęciach na samej górze, czyli dla każdej lekcji sprawdzimy każdą możliwą godzinę
        # lekcyjną. Wydaje się też bardziej optymalne.
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
            # Nie jest to potrzebne, ale zostawiam, żeby było widać, że należy zoptymalizować - w
            # self.school.list_of_all_subjects jest za dużo danych
            # classroom_preference = subject[3]  # na ten moment zawsze None
            # Jest 5 dni w tygodniu mordko, co nie? Mnożymy razy maksymalną liczbę godzin lekcyjnych w dniu i mamy jedną
            # pętle zamiast dwóch.
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
                                                                         [subject_name,
                                                                          teacher_name],
                                                                         classroom=classroom_temp)
                        # jeżeli udało się dodać to przerywamy szukanie odpowiedniego terminu, i przechodzimy do
                        # następnej klasy
                        break

                # Tutaj kontrolujemy, którą mamy godzinę i, który mamy dzień
                day += 1
                if day == 5:
                    day = 0
                    hour += 1
                    # Jeżeli nie udało się przydzielić się lekcji do żadnej godziny to wypadałoby to jakoś
                    # zasygnalizować -> zwiększamy więc wartość zmiennej unassigned_subject_num, która oznacza
                    # ile takich lekcji jest w sumie
                    if hour == self.school.max_lessons_per_day_for_school:
                        unassigned_subject_num += 1
                        # Ten break w sumie nie potrzebny, ale przynajmniej widać, że z tego poziomu zawsze rozpocznie
                        # się następna iteracja.
                        break
        # Kozak by było, gdyby ta zmienna miała zawsze wartość 0
        return unassigned_subject_num

    @staticmethod
    def shuffle_list_of_subjects(base_list: list, n: int):
        import random
        copy_of_list = base_list.copy()
        length_of_list = len(base_list)
        indexes = []
        for index in range(length_of_list):
            indexes.append(index)
        random.shuffle(indexes)
        for _ in range(length_of_list - n):
            indexes.pop()
        ordered_list = indexes.copy()
        ordered_list.sort()
        j = 0
        for index in ordered_list:
            base_list[index] = copy_of_list[indexes[j]]
            j += 1


if __name__ == "__main__":
    school = School(school_class_data=GROUP, teachers_data=TEACHERS, classes_data=CLASSES, classroom_req=CLASSES_REQ)
    alg = Algorithm(school)
    alg.schedule.print_group_schedule("IA")
