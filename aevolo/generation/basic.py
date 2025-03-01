from typing import List

from aevolo.generation.abc import GenerationABC
from aevolo.individual.abc import IndividualABC


class BasicGeneration[C, F](GenerationABC):

    def __init__(self, population: List[IndividualABC[C, F]]):
        self.population = population

    def get_best_individual(self) -> IndividualABC[C, F]:
        return max(self.population, key=lambda x: x.get_fitness())

    def get_best_individual_fitness(self) -> F:
        return max(self.get_population_fitness())

    def get_population(self) -> List[IndividualABC[C, F]]:
        return self.population

    def get_population_chromosomes(self) -> List[C]:
        chromosomes = []
        for individual in self.population:
            chromosomes.append(individual.get_chromosome())
        return chromosomes

    def get_population_fitness(self) -> List[F]:
        fitness = []
        for individual in self.population:
            fitness.append(individual.get_fitness())
        return fitness

    def get_population_size(self) -> int:
        return len(self.population)

    def __str__(self):
        return "; ".join([f"({i}): {str(individual)}" for i, individual in enumerate(self.population)])
