from abc import ABC, abstractmethod
from uuid import UUID
from domain.entities.indicator import Indicator

class IndicatorRepository(ABC):

    #@abstractmethod
    #def save(self, indicator: Indicator) -> None:
    #    pass

    @abstractmethod
    def get(self) -> list[Indicator] | None:
        pass