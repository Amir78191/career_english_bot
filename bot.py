import logging
import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ParseMode
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils import executor
from dotenv import load_dotenv

# Загружаем токен из файла .env
load_dotenv()
API_TOKEN = os.getenv("BOT_TOKEN")

# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Создание бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

# Включаем логирование
dp.middleware.setup(LoggingMiddleware())

# Команда /start
@dp.message_handler(commands=['start'])
async def cmd_start(message: types.Message):
    await message.reply("Привет! Я Career_EnglishBot. Я помогу тебе улучшить твой бизнес-английский!")

# Команда /help
@dp.message_handler(commands=['help'])
async def cmd_help(message: types.Message):
    await message.reply("Я помогу тебе с бизнес-лексикой, шаблонами для писем и даже проведу с тобой собеседования! Напиши мне, чтобы начать.")

# Вопросы для викторины
@dp.message_handler(commands=['quiz'])
async def cmd_quiz(message: types.Message):
    await message.reply("Какие выражения используются для начала деловой переписки?")

# Получаем ответы
@dp.message_handler()
async def echo(message: types.Message):
    user_answer = message.text.lower()
    correct_answers = ["dear", "hello", "greetings"]
    if any(answer in user_answer for answer in correct_answers):
        await message.reply("Правильно! 😊")
    else:
        await message.reply("Попробуй снова! ❌")

# Запуск бота
if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)