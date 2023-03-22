import requests
import datetime

from pprint import pprint

from config import open_weather_token

def get_weather(city, open_weather_token):

    code_smile = {
        "Clear": "Ясно \U00002600",
        "Clouds": "Хмарно \U00002601",
        "Rain": "Дождь \U00002614",
        "Drizzle": "Дождь \U00002601",
        "Thunderstorm": "Гроза \U000026A1",
        "Snow": "Сніг \U0001F328",
        "Mist": "Туман \U0001F32B",
    }

    try:
        r = requests.get(f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric")
        data = r.json()
        #pprint(data)

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

        print(f"_-_|{datetime.datetime.now().strftime('%Y-%m-%d %H:%M')}|_-_\n"
              f"City: {city}\nTemp: {cur_temp} C° {wd}\nHumidity: {humidity} %\nPressure: {pressure} N/m2"
              f"\nWind speed: {wind} m/s\nSunrise time: {sunrise_time}\nSunset time: {sunset_time}")

    except Exception as ex:
        print("Check city name")


def main():
    city = input("Enter city: ")
    get_weather(city, open_weather_token)

if __name__=='__main__':
    main()