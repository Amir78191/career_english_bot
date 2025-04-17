from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '7623017087:AAH4hLpQgMev1UjRiEC6-7S7KqQCmcfVLdo
'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [
        "📖 Business Vocabulary",
        "📝 Writing Zone",
        "🎙 Speaking Practice",
        "🎯 Daily Quizzes",
        "💼 Interview Trainer"
    ]
    keyboard.add(*[types.KeyboardButton(text=b) for b in buttons])
    await message.answer("Добро пожаловать в Career_EnglishBot!\nВыбери модуль:", reply_markup=keyboard)

@dp.message_handler(lambda message: message.text == "📖 Business Vocabulary")
async def vocab_module(message: types.Message):
    await message.answer("Вот несколько бизнес-слов (маркетинг):\n\n- ROI — return on investment\n- KPI — key performance indicator\n- Lead — потенциальный клиент")

@dp.message_handler(lambda message: message.text == "📝 Writing Zone")
async def writing_zone(message: types.Message):
    await message.answer("Шаблон делового письма:\n\nDear [Name],\n\nI hope this message finds you well.\n\n[Body]\n\nBest regards,\n[Your Name]")

@dp.message_handler(lambda message: message.text == "🎙 Speaking Practice")
async def speaking_practice(message: types.Message):
    await message.answer("Диалог:\n\n— Could you send me the report?\n— Sure, I’ll do it by the end of the day.")

@dp.message_handler(lambda message: message.text == "🎯 Daily Quizzes")
async def daily_quiz(message: types.Message):
    await message.answer("What does 'KPI' stand for?\n\nA) Key Product Indicator\nB) Key Performance Indicator\nC) Knowledge Performance Insight")

@dp.message_handler(lambda message: message.text == "💼 Interview Trainer")
async def interview_trainer(message: types.Message):
    await message.answer("Вопрос:\n\nTell me about yourself.\n\n(Ты можешь записать свой ответ и проверить)")

@dp.message_handler()
async def fallback(message: types.Message):
    await message.answer("Пожалуйста, выбери один из модулей на клавиатуре.")

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
