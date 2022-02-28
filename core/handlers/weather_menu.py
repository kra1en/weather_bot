from loader import dp
from markups.inline_weather import InlineWeather as iw
from core.states import WeatherStates

@dp.callback_query_handler(iw.callback_data.filter(), state = WeatherStates.show_weather)
async def weather_menu(callback_query, callback_data):
    await callback_query.message.edit_text(iw.update(user_id=callback_query.from_user.id, action=callback_data["action"]))
    await callback_query.message.edit_reply_markup(iw.get_markup(callback_query.from_user.id))