from abc import ABC, abstractmethod
from .data_type import Settlement, Coordinates


class StorageAPI(ABC):
    @abstractmethod
    def get_settlements(self, settlement) -> list[Settlement]:
        pass

    @abstractmethod
    def get_coordinates(self, settlement_id: int) -> Coordinates:
        pass