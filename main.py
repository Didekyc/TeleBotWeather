import telebot
import requests


url = 'http://api.openweathermap.org/data/2.5/weather'
api_weather = 'e8e48950a7f0f22ecba29d13a396226d'
bot = telebot.TeleBot('1368230328:AAEUSFdoY1Wj6viKDGBZFNFtly6G5F3UWT0')


@bot.message_handler(commands=['start'])
def start_command(message):
    bot.send_message(message.chat.id,
                     "Здравствуйте! Вас приветствует бот, который подскажет вам погоду на сегодняйший день."
                     " Напишите /help и я покажу, что умею.")


@bot.message_handler(commands=['help'])
def help_command(message):
    bot.send_message(message.chat.id, "/start - начать работу с ботом.\n"
                                      "/help - посмотреть, что умеет бот.\n"
                                      "/city - посмотреть погоду в любом городе.")


@bot.message_handler(commands=['city'])
def city_command(message):
    bot.send_message(message.chat.id, "Напиши название любого города и я скажу тебе какая там сейчас погодка.")


@bot.message_handler(content_types=['text'])
def weather_command(message):
        city = message.text
        try:
            params = {'APPID': api_weather, 'q': city, 'units': 'metric'}
            result = requests.get(url, params=params)
            weather = result.json()

            bot.send_message(message.chat.id,
                             "В городе " + str(weather["name"]) + " температура " + str(float(weather["main"]['temp'])) + "\n" +
                             "Максимальная температура " + str(float(weather['main']['temp_max'])) + "\n" +
                             "Минимальная температура " + str(float(weather['main']['temp_min'])) + "\n" +
                             "Скорость ветра " + str(float(weather['wind']['speed'])) + "\n" +
                             "Давление " + str(float(weather['main']['pressure'])) + "\n" +
                             "Влажность " + str(float(weather['main']['humidity'])) + "\n")
        except:
            bot.send_message(message.chat.id, "Город " + city + " не найден! Проверьте правильность ввода названия или"
                                                                " попробуйте другой.")


if __name__ == '__main__':
    bot.polling(none_stop=True)
