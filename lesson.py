import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import random
# Файл config с ключами необходимо создавать дополнительно
#from config import TOKEN

# Создаем объекты классов Bot (отвечает за взаимодействие с Telegram bot API) и Dispatcher (управляет обработкой входящих сообщений и команд)
bot = Bot(token=TOKEN)
dp = Dispatcher()

# Обработка команды /start
@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я бот!\nКоманды моего управления можно посмотреть в меню")

# Обработка команды /help
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start - приветствие\n/help - список команд\n/photo - выводит рандомное фото")

@dp.message(Command('photo'))
async def photo(message: Message):
    list = ['https://www.istockphoto.com/ru/%D1%84%D0%BE%D1%82%D0%BE/mops-%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0-gm842814768-137620351',
            'https://media.istockphoto.com/id/469360172/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%BC%D0%BE%D0%BF%D1%81-%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0.jpg?s=612x612&w=0&k=20&c=9aA-wzK84lygxeN_hFj1nYGhbExG6QNPPRKvSkJg_D0=',
            'https://media.istockphoto.com/id/868008896/ru/%D1%84%D0%BE%D1%82%D0%BE/%D0%B7%D0%B0%D0%B1%D0%B0%D0%B2%D0%BD%D1%8B%D0%B9-%D1%81%D0%BE%D0%BD%D0%BD%D1%8B%D0%B9-%D0%BC%D0%BE%D0%BF%D1%81-%D1%81%D0%BE%D0%B1%D0%B0%D0%BA%D0%B0-%D1%81-%D1%80%D0%B5%D0%B7%D0%B8%D0%BD%D0%BA%D0%BE%D0%B9-%D0%B2-%D0%B3%D0%BB%D0%B0%D0%B7%D1%83-%D1%81%D0%BE%D0%BD-%D0%BE%D1%82%D0%B4%D1%8B%D1%85-%D0%BD%D0%B0-%D0%BF%D0%BE%D0%BB%D1%83.jpg?s=612x612&w=0&k=20&c=ALBi1P8Gh_Z2uMX49ft1yErVwgLaFvz3Jxji938TSv4='
            ]
    rand_photo = random.choice(list)
    await message.answer_photo(photo=rand_photo, caption='Это супер крутая картинка')

@dp.message(F.text == "Что такое ИИ?")
async def aitext(message: Message):
    await message.answer('Искусственный интеллект — это свойство искусственных интеллектуальных систем выполнять творческие функции, которые традиционно считаются прерогативой человека; наука и технология создания интеллектуальных машин, особенно интеллектуальных компьютерных программ')

@dp.message(F.photo)
async def react_photo(message: Message):
    list = ['Ого, какая фотка!', 'Непонятно, что это такое', 'Не отправляй мне такое больше']
    rand_answ = random.choice(list)
    await message.answer(rand_answ)

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())