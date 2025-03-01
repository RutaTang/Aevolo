import random
from typing import List
from unittest import TestCase

from aevolo.crossover.abc import CrossoverABC
from aevolo.evolver.ga import GABuilder
from aevolo.individual.abc import IndividualABC
from aevolo.generation.abc import GenerationABC
from aevolo.generation.basic import BasicGeneration
from aevolo.mutator.abc import MutatorABC
from aevolo.selector.abc import SelectorABC


# TODO: finish test
class TestGAEvolver(TestCase):
    def test_evolve(self):
        class MyIndividual(IndividualABC):
            def __init__(self):
                super().__init__()
                self.chromosome = []
                self.fitness = 0
                self.construct()

            def construct(self):
                self.chromosome = [random.randint(1, 9) for _ in range(3)]
                self.fitness = sum(self.chromosome)

            def get_chromosome(self) -> List[int]:
                return self.chromosome

            def set_chromosome(self, chromosome: List[int]):
                self.chromosome = chromosome

            def get_fitness(self) -> float:
                return sum(self.chromosome)

            def __str__(self):
                return f'Chromosome: {self.chromosome}, Fitness: {self.get_fitness()}'

        class MySelector(SelectorABC):
            def select(self, population: List[MyIndividual]) -> List[MyIndividual]:
                # tournament selection
                selected = []
                while len(selected) < len(population):
                    tournament = random.sample(population, 2)
                    selected.append(max(tournament, key=lambda x: x.get_fitness()))
                return selected

        class MyCrossover(CrossoverABC):
            def cross(self, population: List[MyIndividual]) -> List[MyIndividual]:
                crossed = []
                while len(crossed) < len(population):
                    parent1 = random.choice(population)
                    parent2 = random.choice(population)
                    if random.random() < self.get_rate():
                        # exchange the first half of the chromosome
                        child = MyIndividual()
                        chromosome = parent1.get_chromosome()[
                                     :len(parent1.get_chromosome()) // 2] + parent2.get_chromosome()[
                                                                            len(parent2.get_chromosome()) // 2:]
                        child.set_chromosome(chromosome)
                        crossed.append(child)
                    else:
                        crossed.append(random.choice([parent1, parent2]))
                return crossed

            def get_rate(self) -> float:
                return 0.5

        class MyMutator(MutatorABC):
            def mutate(self, population: List[MyIndividual]) -> List[MyIndividual]:
                mutated = []
                for individual in population:
                    if random.random() < self.get_rate():
                        chromosome = individual.get_chromosome()
                        chromosome[random.randint(0, len(chromosome) - 1)] = random.randint(1, 9)
                        individual.set_chromosome(chromosome)
                    mutated.append(individual)
                return mutated

            def get_rate(self) -> float:
                return 0.3

        ga_builder = GABuilder()
        ga_builder.set_individual_cls(MyIndividual)
        ga_builder.set_generation_cls(BasicGeneration)
        ga_builder.set_population_n(10)
        ga_builder.set_generations_n(10)
        ga_builder.set_selector(MySelector())
        ga_builder.set_crossover(MyCrossover())
        ga_builder.set_mutator(MyMutator())
        ga = ga_builder.build()
        info = ga.evolve()
        print(info.initial_info)
        print(info.generations_info)
        print(info.final_info)
        print(info.get_info())
