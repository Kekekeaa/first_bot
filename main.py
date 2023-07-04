from telebot.async_telebot import AsyncTeleBot
from telebot.types import ReplyKeyboardMarkup

bot = AsyncTeleBot('5851668146:AAEv2eL_jnXbjVJa6anqYK8Hjvs-4IoIC10')


@bot.message_handler(commands=['Help', 'start'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Привет рад тебя видеть', disable_notification=True, protect_content=True)
    await bot.send_sticker(chat_id, 'CAACAgIAAxkBAAEJlH5kpAtLLne4lUcR5XTm9yGyawyqVgACXQEAAqH2jQNApKbzPe6_5y8E')

@bot.message_handler(commands=['test'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_message(chat_id, 'Кто меня создал?', disable_notification=True, protect_content=True)
    button_dict = {'Первая кнопка': 'first',
                   'Вторая кнопка': 'second',
                   'А' : 'three'
                   }
    await bot.send_message(chat_id, 'Первый вариант кнопок', reply_markup=create_keyboard_markup(button_dict))
@bot.callback_query_handler(func=lambda call: True)
async def handle_callback(call):
    chat_id = call.message.chat.id
    button_call = call.data
    if button_call == 'first':
        await bot.send_message(chat_id, 'Боже чел повеся!')
    elif button_call == 'second':
        await bot.send_message(chat_id, 'Правильно')
    elif button_call == 'three':
        await bot.send_message(chat_id, 'Неправильно')

@bot.message_handler(commands=['location'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_location(chat_id, 58.006035175949485, 56.22731177316515)

@bot.message_handler(commands=['photo'])
async def send_welcome(message):
    chat_id = message.from_user.id
    await bot.send_photo(chat_id, 'https://img.freepik.com/free-photo/lavender-field-at-sunset-near-valensole_268835-3910.jpg', caption='Тест')

@bot.message_handler(commands=['mork'])
async def send_welcome(message):
    chat_id = message.from_user.id
    markup = ReplyKeyboardMarkup()
    button1 = InLineKeyboardButton('1',callback_data='first')
    button2 = InLineKeyboardButton('2',callback_data='second')
    button3 = InLineKeyboardButton('3', callback_data='three')
    markup.add(button1)
    markup.add(button2)
    markup.add(button3)
    await bot.send


import asyncio
asyncio.run(bot.polling())

#
#https://github.com/Ivango128/FirstBOT/commit/068dd79d1e09ecd4313598268d68924e0b8c9e65
#https://github.com/Ivango128/FirstBOT/commit/35057048581a3f80b30cee4fcab857cdd7aaae85
