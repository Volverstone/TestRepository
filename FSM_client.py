from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from config import staff
from config import dp, bot


class FSM_client(StatesGroup):
    id_product = State(),
    size_product = State(),
    count_product = State(),
    contact_client = State()


async def fsm_start(message: types.Message):
    await message.answer(text='Введите артикул товара который хотите купить: ', )

    await FSM_client.id_product.set()


async def id_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_client:
        data_client['id_product'] = message.text

    await FSM_client.next()
    await message.answer(text='Укажите размер товара: ')


async def sizes_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_client:
        data_client['size_product'] = message.text

    await FSM_client.next()
    await message.answer(text='Укажите количество товара: ')


async def count_product(message: types.Message, state: FSMContext):
    async with state.proxy() as data_client:
        data_client['count_product'] = message.text

    await FSM_client.next()
    await message.answer(text='Оставьте свой номер телефона: ')


async def contact(message: types.Message, state: FSMContext):
    async with state.proxy() as data_client:
        data_client['contact_client'] = message.text

    await message.answer(text='Завершение')
    async with state.proxy() as data_client:
        for i in staff:
            await bot.send_message(chat_id=i,
                                   text=f"Данные клиента"
                                        f"{data_client['id_product']}\n"
                                        f"{data_client['size_product']}\n"
                                        f"{data_client['count_product']}\n"
                                        f"{data_client['contact_client']}")

    await state.finish()


def client_fsm(dp: Dispatcher):
    dp.register_message_handler(fsm_start, commands=['client'])
    dp.register_message_handler(id_product, state=FSM_client.id_product)
    dp.register_message_handler(sizes_product, state=FSM_client.size_product)
    dp.register_message_handler(count_product, state=FSM_client.count_product)
    dp.register_message_handler(contact, state=FSM_client.contact_client)
