from dataclasses import dataclass

@dataclass
class WeatherInfo:
    day_number: int
    morning: object
    day: object
    evening: object
    night: object
