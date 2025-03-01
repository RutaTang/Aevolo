from abc import ABC, abstractmethod
from typing import List

from aevolo.individual.abc import IndividualABC


class GenerationABC[C, F](ABC):
    @abstractmethod
    def __init__(self, population: List[IndividualABC[C, F]]):
        pass

    @abstractmethod
    def get_best_individual(self) -> IndividualABC[C, F]:
        pass

    @abstractmethod
    def get_best_individual_fitness(self) -> F:
        pass

    @abstractmethod
    def get_population(self) -> List[IndividualABC[C, F]]:
        pass

    @abstractmethod
    def get_population_chromosomes(self) -> List[C]:
        pass

    @abstractmethod
    def get_population_fitness(self) -> List[F]:
        pass

    @abstractmethod
    def get_population_size(self) -> int:
        pass
