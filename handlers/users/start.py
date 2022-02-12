import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import keyboard
from loader import dp, db
from states.user_states import GetUser


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        await db.add_user(
            fullname=message.from_user.full_name,
            username=message.from_user.username,
            tg_id=message.from_user.id
        )
        await message.answer(f"Привет, {message.from_user.full_name}!\n"
                             f"Для начала введи свое настоящее имя,\n"
                             f"чтобы тебя было проще найти другим ;)")
        await GetUser.name.set()
    except asyncpg.exceptions.UniqueViolationError:
        await db.select_user(tg_id=message.from_user.id)
        await message.answer('Вы уже зарегистрированы :)', reply_markup=keyboard)


@dp.message_handler(state=GetUser.name)
async def new_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await db.update_user_fullname(data.get('name'), message.from_user.id)
        await state.finish()
        await message.answer('Готово!', reply_markup=keyboard)
