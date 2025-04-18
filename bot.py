import os
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor
from dotenv import load_dotenv

# загружаем токен из .env
load_dotenv()
BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

# главное меню
main_menu = ReplyKeyboardMarkup(resize_keyboard=True)
main_menu.add(
    KeyboardButton("📖 Business Vocabulary"),
    KeyboardButton("📝 Writing Zone")
).add(
    KeyboardButton("🎙 Speaking Practice"),
    KeyboardButton("🎯 Daily Quizzes")
).add(
    KeyboardButton("💼 Interview Trainer")
)

# словарь по категориям
vocab = {
    "Marketing": ["Brand awareness", "Target audience", "Lead generation"],
    "Finance": ["Assets", "Liabilities", "Equity"],
    "HR": ["Recruitment", "Onboarding", "Retention"]
}

# шаблоны фраз
writing_templates = [
    "Dear Sir or Madam, ...",
    "I am writing to apply for the position of...",
    "Please find attached my CV...",
    "Looking forward to your reply.",
    "Best regards, ..."
]

# бизнес-фразы и диалоги
speaking_phrases = [
    "Let's touch base next week.",
    "Could you clarify that, please?",
    "What are the next steps?",
    "I'm afraid I don't have that information right now.",
    "That sounds like a great idea!"
]

# викторины
quizzes = [
    {"q": "What does 'B2B' mean?", "a": "Business to Business"},
    {"q": "Translate: 'Return on Investment'", "a": "окупаемость инвестиций"},
    {"q": "What is a CV?", "a": "Curriculum Vitae"}
]

# собеседование
interview_questions = [
    "Tell me about yourself.",
    "Why do you want to work here?",
    "What are your strengths and weaknesses?",
    "Describe a challenging situation at work and how you handled it.",
    "Where do you see yourself in 5 years?"
]

# приветствие
@dp.message_handler(commands=['start'])
async def start_command(message: types.Message):
    await message.answer("Добро пожаловать в Career_EnglishBot! Выбери раздел:", reply_markup=main_menu)

# обработка кнопок
@dp.message_handler(lambda message: message.text == "📖 Business Vocabulary")
async def business_vocab(message: types.Message):
    text = "Выбери тему словаря:\n"
    for topic in vocab:
        text += f"- {topic}\n"
    await message.answer(text)

@dp.message_handler(lambda message: message.text == "📝 Writing Zone")
async def writing_zone(message: types.Message):
    await message.answer("Вот несколько полезных фраз для деловой переписки:")
    for phrase in writing_templates:
        await message.answer(phrase)

@dp.message_handler(lambda message: message.text == "🎙 Speaking Practice")
async def speaking_zone(message: types.Message):
    await message.answer("Тренируйся с этими фразами:")
    for phrase in speaking_phrases:
        await message.answer(phrase)

@dp.message_handler(lambda message: message.text == "🎯 Daily Quizzes")
async def quizzes_zone(message: types.Message):
    for quiz in quizzes:
        await message.answer(f"❓ {quiz['q']}\n✅ Ответ: {quiz['a']}")

@dp.message_handler(lambda message: message.text == "💼 Interview Trainer")
async def interview_zone(message: types.Message):
    await message.answer("Примерные вопросы на интервью:")
    for question in interview_questions:
        await message.answer(f"💼 {question}")

# обработка остальных сообщений
@dp.message_handler()
async def echo(message: types.Message):
    await message.answer("Выбери одну из кнопок в меню ниже.", reply_markup=main_menu)

# запуск бота
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)