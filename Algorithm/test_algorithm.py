from .classrooms import CLASSES_OLD
from .groups import GROUP_OLD
from .teachers import TEACHERS_OLD
from .algorithm import Population


def test_evolution(groups_data=GROUP_OLD, teachers_data=TEACHERS_OLD, classrooms_data=CLASSES_OLD):
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
