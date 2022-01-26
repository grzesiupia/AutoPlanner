from classrooms import CLASSES
from groups import GROUP
from teachers import TEACHERS
from algorithm import Population
from data_structures import School, Group, Teacher, Classroom


def test_evolution(groups_data=GROUP, teachers_data=TEACHERS, classrooms_data=CLASSES):
    population_size = 10
    num_of_generations = 100
    num_of_mutations = 20

    population = Population(groups_data=groups_data, teachers_data=teachers_data, classrooms_data=classrooms_data)
    population.new_population(number_of_instances=population_size)
    before_evolution = population.get_best_specimen().evaluation
    population.evolute(num_of_generations, num_of_mutations)
    after_evolution = population.get_best_specimen().evaluation

    assert before_evolution < after_evolution, "Before evaluation is not smaller than after evaluation"
    print("Evaluation before evolution is smaller than after evolution")


def test_data_structures(groups_data=GROUP, teachers_data=TEACHERS, classrooms_data=CLASSES):
    school = School(groups_data, teachers_data, classrooms_data)
    assert len(school.groups) == len(groups_data), "Groups copied incorrectly to dict of class Group"
    assert len(school.classrooms) == len(classrooms_data), "Classrooms copied incorrectly to dict of class Classroom"
    assert len(school.teachers) == len(teachers_data), "Teachers copied incorrectly to dict of class Teacher"
