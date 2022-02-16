from loader import dp, storage, weather

from markups.inline_sellector import InlineSettlementSelector as iss
from markups.inline_weather import InlineWeather as iw

@dp.callback_query_handler(iss.callback_data.filter())
async def check(callback_query, callback_data):
    if callback_data["action"] == '':
        coord = storage.get_coordinates(callback_data['settlement_id'])
        data = weather.get_weather_data(lat=coord.lat, lon=coord.lon)
        iw.initialization(days=data, user_id=callback_query.from_user.id)
        await callback_query.message.edit_text(iw.update(user_id=callback_query.from_user.id))
        await callback_query.message.edit_reply_markup(iw.get_markup(callback_query.from_user.id))
    else:
        await callback_query.message.edit_reply_markup(iss.update(callback_query.from_user.id, callback_data["action"]))