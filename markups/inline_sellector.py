from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData


class InlineSettlementSelector():
    callback_data = CallbackData("settlements", "action", "settlement_id")
    _start = 0
    _end = 5

    __instances = {}

    def __init__(self, settlements):
        self.settlements = settlements

    def __create_markup(self, markup):
        for d in sorted(self.settlements[self._start:self._end], key=lambda d: d.region == d.name, reverse=True):
            format_text = f"{d.name}, {d.region}"
            settlement_id = d.id
            markup.add(InlineKeyboardButton(
                text=format_text, callback_data=self.callback_data.new('', settlement_id)))

    @classmethod
    def initialization(cls, settlements, user_id):
        cls.__instances[user_id] = InlineSettlementSelector(settlements)

    @classmethod
    def update(cls, user_id, action=None):
        return cls.__instances[user_id]._update(action)

    def _update(self, action=None):
        markup = InlineKeyboardMarkup(row_width=2)
        if not action:
            self.__create_markup(markup)
        elif action == "forward":
            self._start += 5
            self._end += 5
            self.__create_markup(markup)
        else:
            self._start -= 5
            self._end -= 5
            self.__create_markup(markup)
        if len(self.settlements) > 5:
            if self._start == 0:
                markup.add(InlineKeyboardButton(
                    text="->", callback_data=self.callback_data.new('forward', '')))
            elif self._end >= len(self.settlements):
                markup.add(InlineKeyboardButton(
                    text="<-", callback_data=self.callback_data.new('back', '')))
            else:
                markup.add(InlineKeyboardButton(text="<-", callback_data=self.callback_data.new('back', '')),
                           InlineKeyboardButton(text="->", callback_data=self.callback_data.new('forward', '')))
        return markup
