from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData
from markups.dicts_weather import dict_wind, dict_cond, dict_part
import datetime


class InlineWeather():
    callback_data = CallbackData("weather", "action")
    current_day = 0
    current_time = 0

    today = datetime.date.today()
    dict_date = {
    0: today + datetime.timedelta(days=current_day),
    1: today + datetime.timedelta(days=current_day + 1), 
    2: today + datetime.timedelta(days=current_day + 2), 
    3: today + datetime.timedelta(days=current_day + 3), 
    4: today + datetime.timedelta(days=current_day + 4),
    5: today + datetime.timedelta(days=current_day + 5),
    6: today + datetime.timedelta(days=current_day + 6)
    }

    __instances = {}

    def __init__(self, days):
        self.days = days

    @classmethod
    def initialization(cls, days, user_id):
        cls.__instances[user_id] = InlineWeather(days)
    @classmethod
    def update(cls, user_id, action=None):
        return cls.__instances[user_id]._update(action)

    @classmethod
    def get_markup(cls, user_id):
        return cls.__instances[user_id].__get_markup()


    def __get_markup(self):
        self.markup = InlineKeyboardMarkup(row_width=2)
        self.markup.add(InlineKeyboardButton(text=f"{dict_part[self.prev_daytime()]}", callback_data=self.callback_data.new('time_down')),InlineKeyboardButton(text=f"{dict_part[self.next_daytime()]}", callback_data=self.callback_data.new('time_up')))
        self.markup.add(InlineKeyboardButton(text=f"{self.dict_date[self.prev_date()].strftime('%d.%m')}", callback_data=self.callback_data.new('day_down')),InlineKeyboardButton(text=f"{self.dict_date[self.next_date()].strftime('%d.%m')}", callback_data=self.callback_data.new('day_up')))
        return self.markup

    def prev_date(self):
        return (self.current_day-1)%7

    def next_date(self):
        return (self.current_day+1)%7    

    def prev_daytime(self):
        return (self.current_time-1)%4

    def next_daytime(self):
        return (self.current_time+1)%4

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
        return \
            f"Дата: {self.dict_date[self.current_day].strftime('%d.%m')}\n"\
            f"Время дня: {dict_part[self.current_time]}\n"\
            f"Средняя температура: {data.temp_avg}°C\n"\
            f"Ощущается как: {data.feels_like}°C\n"\
            f"Минимальная температура: {data.temp_min}°C\n"\
            f"Максильманая температура: {data.temp_max}°C\n"\
            f"{dict_cond[data.condition]}\n"\
            f"Ветер: {data.wind_speed} м/с\n"\
            f"Направление ветра: {dict_wind[data.wind_dir]}\n"\
            f"Влажность: {data.humidity}%\n"\
            f"Вероятность осадков: {data.prec_prob}%\n"\

