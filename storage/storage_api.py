from abc import ABC, abstractmethod


class StorageAPI(ABC):
    @abstractmethod
    def get_settlements(self, settlement) -> []:
        pass
