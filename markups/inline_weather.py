from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class InlineWeather():
    callback_data = CallbackData("weather", "action")
    current_day = 0
    current_time = 0

    __instances = {}

    def __init__(self, days):
        self.days = days

    @classmethod
    def initialization(cls, days, user_id):
        cls.markup = InlineKeyboardMarkup(row_width=2)
        cls.markup.add(InlineKeyboardButton(text="<-", callback_data=cls.callback_data.new('time_down')),InlineKeyboardButton(text="->", callback_data=cls.callback_data.new('time_up')))
        cls.markup.add(InlineKeyboardButton(text="<-", callback_data=cls.callback_data.new('day_down')),InlineKeyboardButton(text="->", callback_data=cls.callback_data.new('day_up')))
        cls.__instances[user_id] = InlineWeather(days)

    @classmethod
    def update(cls, user_id, action=None):
        return cls.__instances[user_id]._update(action)

    @classmethod
    def get_markup(cls):
        return cls.markup

    def day_up(self):
        self.current_day = (self.current_day+1)%7

    def day_down(self):
        self.current_day = (self.current_day-1)%7

    def time_up(self):
        self.current_time = (self.current_time+1)%4

    def time_down(self):
        self.current_time = (self.current_time-1)%4

    def _update(self, action=None):
        cdw = self.days[self.current_day]
        day_time = [
            cdw.morning,
            cdw.day,
            cdw.evening,
            cdw.night
        ]
        if action=="time_up":
            self.time_up()
        elif action=="time_down":
            self.time_down()
        elif action=="day_up":
            self.day_up()
        elif action=="day_down":
            self.day_down()
        return self.__format(day_time[self.current_time])


    def __format(self, data):
        from markups.dicts_weather import dict_wind, dict_cond
        return \
            f"Минимальная температура: {data.temp_min}°C\n"\
            f"Максильманая температура: {data.temp_max}°C\n"\
            f"Средняя температура: {data.temp_avg}°C\n"\
            f"Температура ощущается как: {data.feels_like}°C\n"\
            f"{dict_cond[data.condition]}\n"\
            f"Ветер: {data.wind_speed} м/с\n"\
            f"Направление ветра: {dict_wind[data.wind_dir]}\n"\
            f"Влажность: {data.humidity}%\n"\
            f"Вероятность осадков: {data.prec_prob}%\n"\

