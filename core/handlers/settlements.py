from loader import dp, storage
from markups.inline_sellector import InlineSettlementSelector as iss

@dp.message_handler()
async def settlements(message):
    data = storage.get_settlements(message.text)
    if len(data) == 0:
        await message.answer(text="Указанный вами город не найден\nВведите город")
    else:
        iss.initialization(data, message.from_user.id)
        await message.answer(text="Выберите свой город", reply_markup=iss.update(message.from_user.id))