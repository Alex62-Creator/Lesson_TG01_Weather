# Имя бота в Telegram Weather_Bot

import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests
# Файл config с ключами необходимо создавать дополнительно
from config import TOKEN, API_KEY_WEATHER

# Создаем объекты классов Bot (отвечает за взаимодействие с Telegram bot API) и Dispatcher (управляет обработкой входящих сообщений и команд)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я бот выдающий прогноз погоды в любом городе!\nКоманды моего управления можно посмотреть в меню")

# Обработка команды /help
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start - приветствие\n/help - список команд\n/weather - прогноз погоды")

# Обработка команды /weather
@dp.message(Command('weather'))
async def weather(message: Message):
    await message.answer("Введи город:")

# Обработка любого введенного сообщения (предполагаем, что пользователь будет вводить только правильное название города)
@dp.message()
async def city(message: Message):
    # Получаем город
    city = message.text
    # Прописываем переменную, куда будет сохраняться результат из функции get_weather
    weather = get_weather(city)
    # Выводим прогноз погоды
    await message.answer(f"Погода в {weather['name']}\nТемпература: {weather['main']['temp']}\nПогода: {weather['weather'][0]['description']}")

# Функция получения прогноза погоды с сайта
def get_weather(city):
   api_key = API_KEY_WEATHER
   # Адрес сайта, по которому мы будем отправлять запрос о погоде
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"
   # Получаем результат запроса
   response = requests.get(url)
   # Прописываем формат возврата результата json
   return response.json()

# Создаем асинхронную функцию main, которая будет запускать наш бот
async def main():
    await dp.start_polling(bot)

# Запускаем асинхронную функцию main
if __name__ == "__main__":
    asyncio.run(main())