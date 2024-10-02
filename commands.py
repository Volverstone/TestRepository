from aiogram import types, Dispatcher
from config import bot



async def start_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='Здравствуйте вас приветствует бот - онлайн магазин ')

async def info_handler(message: types.Message):
    await bot.send_message(chat_id=message.from_user.id,
                           text='В этом магазине можно будет купить вещи '
                                'на ваш любой цвет и вкус :) ')

def register_commands(dp: Dispatcher):
    dp.register_message_handler(start_handler, commands=['start'])
    dp.register_message_handler(info_handler, commands=['info'])