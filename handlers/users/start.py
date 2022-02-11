import asyncpg.exceptions
from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp, db


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    try:
        user = await db.add_user(
            fullname=message.from_user.full_name,
            username=message.from_user.username,
            tg_id=message.from_user.id
        )
    except asyncpg.exceptions.UniqueViolationError:
        user = db.select_user(tg_id=message.from_user.id)

    await message.answer(f"Привет, {message.from_user.full_name}!\n"
                         f"Какого типа отправить валентинку?", reply_markup=menu)
