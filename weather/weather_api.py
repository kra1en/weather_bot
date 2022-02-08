from abc import ABC, abstractmethod
from .weather_data import WeatherInfo
from storage.data_type import Coordinates


class WeatherAPI(ABC):
    @abstractmethod
    def get_weather_data(self, coordinates: Coordinates) -> list[WeatherInfo]:
        pass