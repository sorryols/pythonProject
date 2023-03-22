import requests
import datetime
from config import tb_bot_token, open_weather_token
from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor

bot = Bot(token=tb_bot_token)
dp = Dispatcher(bot)


@dp.message_handler(commands=["start"])
async def start_command(message: types.Message):
    await message.reply("Hy! Write me city name, and i will send you weather information")

@dp.message_handler()
async def start_command(message: types.Message):
    code_smile = {
        "Clear": "Clear \U00002600",
        "Clouds": "Clouds \U00002601",
        "Rain": "Rain \U00002614",
        "Drizzle": "Drizzle \U00002601",
        "Thunderstorm": "Thunderstorm \U000026A1",
        "Snow": "Snow \U0001F328",
        "Mist": "Mist \U0001F32B",
    }

    try:
        r = requests.get(
            f"https://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={open_weather_token}&units=metric")
        data = r.json()
        # pprint(data)

        weather_description = data["weather"][0]["main"]
        if weather_description in code_smile:
            wd = code_smile[weather_description]
        else:
            wd = "Check you window :)"

        city = data["name"]
        cur_temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        pressure = data["main"]["pressure"]
        wind = data["wind"]["speed"]
        sunrise_time = datetime.datetime.fromtimestamp(data["sys"]["sunrise"])
        sunset_time = datetime.datetime.fromtimestamp(data["sys"]["sunset"])

        await message.reply(f"_-_|{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}|_-_\n"
              f"City: {city}\nTemp: {cur_temp} C° {wd}\nHumidity: {humidity} %\nPressure: {pressure} N/m2"
              f"\nWind speed: {wind} m/s\nSunrise time: {sunrise_time}\nSunset time: {sunset_time}")

    except:
        await message.reply("\U00002620 Check city name \U00002620")

if __name__ == '__main__':
    executor.start_polling(dp)
