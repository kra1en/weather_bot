from loader import dp

@dp.message_handler(commands=["start"])
async def command_start(message):
    await message.answer(text=f"Привет, {message.from_user.full_name}. Введите город")