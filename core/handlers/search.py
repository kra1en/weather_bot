from aiogram.types import Message

from loader import dp
from markups import InlineSettlementSelector as iss
from core.states import WeatherStates

@dp.message_handler(commands=['search', 'start'], state = '*')
async def search(message):
    await message.answer('Введите свой город')
    await WeatherStates.search_settlement.set()

