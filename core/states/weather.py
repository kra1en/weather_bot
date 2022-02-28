from aiogram.dispatcher.filters.state import StatesGroup, State


class WeatherStates(StatesGroup):
    show_weather = State()
    search_settlement = State()