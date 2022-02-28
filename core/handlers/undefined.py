from aiogram.types import Message

from loader import dp
from markups import InlineSettlementSelector as iss
from core.states import WeatherStates

@dp.message_handler(state = '*')
async def search(message):
    await message.answer('Команда не распознана. Если хотите начать поиск города - введите /search')

