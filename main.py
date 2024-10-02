import logging

import FSM_client
from config import dp, bot
from aiogram.utils import executor
import commands, FSM_products, FSM_client
from db import db_main

from config import staff

async def on_startup(_):
    for i in staff:
        await bot.send_message(chat_id=i, text='Бот включен!')
        await db_main.sql_create()
async def on_shutdown(_):
    for i in staff:
        await bot.send_message(chat_id=i, text='Бот выключен!')

commands.register_commands(dp)
FSM_products.product_fsm(dp)
FSM_client.client_fsm(dp)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    executor.start_polling(dp, skip_updates=True, on_startup=on_startup,
                           on_shutdown=on_shutdown)
