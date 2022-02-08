from .weather_api import WeatherAPI
from .weather_data import WeatherInfo
import requests
import json
from types import SimpleNamespace

class WeatherService(WeatherAPI):
    def get_weather_data(self, lat: float, lon: float):
        response = requests.get(f"https://api.weather.yandex.ru/v2/forecast?lat={lat}&lon={lon}&lang=ru_RU", headers={'X-Yandex-API-Key': 'b15dc6f6-9adc-430f-a304-ebbc0778b981'})
        data = json.loads(response.text, object_hook=lambda d: SimpleNamespace(**d))
        result = []
        for num, day in enumerate(data.forecasts):
            result.append(WeatherInfo(
                day_number = num,
                morning=day.parts.morning,
                day=day.parts.day,
                night=day.parts.night,
                evening=day.parts.evening,
            ))
        return result