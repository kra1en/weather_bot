from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

class InlineSettlementSelector():
    callback_data = CallbackData("settlements", "action", "settlement_id")
    _start = 0
    _end = 5

    @classmethod
    def init(cls, settlements):
        cls.settlements = settlements

        

    @classmethod
    def update(cls, action=None):
        markup = InlineKeyboardMarkup(row_width=2)
        if not action:
            for d in sorted(cls.settlements[cls._start:cls._end], key=lambda d: d.region == d.name, reverse=True):
                format_text = f"{d.name} {d.region}"
                callback_id = d.id
                markup.add(InlineKeyboardButton(
                    text=format_text, callback_data=callback_id))
        elif action == "forward":
            cls._start+=5
            cls._end+=5
            for d in sorted(cls.settlements[cls._start:cls._end], key=lambda d: d.region == d.name, reverse=True):
                format_text = f"{d.name} {d.region}"
                callback_id = d.id
                markup.add(InlineKeyboardButton(
                    text=format_text, callback_data=callback_id))
        else:
            cls._start-=5
            cls._end-=5
            for d in sorted(cls.settlements[cls._start:cls._end], key=lambda d: d.region == d.name, reverse=True):
                format_text = f"{d.name} {d.region}"
                callback_id = d.id
                markup.add(InlineKeyboardButton(
                    text=format_text, callback_data=callback_id))
        if len(cls.settlements) > 5:
            if cls._start==0:
                markup.add(InlineKeyboardButton(text="->", callback_data=cls.callback_data.new('forward', '')))
            elif cls._end >= len(cls.settlements):
                markup.add(InlineKeyboardButton(text="<-", callback_data=cls.callback_data.new('back', '')))
            else:
                markup.add(InlineKeyboardButton(text="<-", callback_data=cls.callback_data.new('back', '')),
                InlineKeyboardButton(text="->", callback_data=cls.callback_data.new('forward', '')))
        return markup