import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from data.config import ADMINS
from keyboards.inline.users_keyboard import create_keyboard_users
from loader import dp, db
from states.admin_states import ChangeName


@dp.message_handler(Command(['users']))
async def all_users(message: types.Message):
    await message.answer(text="все пользователи", reply_markup=await create_keyboard_users())


@dp.message_handler(Command(['change_name']))
async def change_name(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer('Введи id пользователя которому заменить имя')
        await ChangeName.id.set()
    else:
        await message.answer('Вам нельзя менять имена пользователей :(')


@dp.message_handler(state=ChangeName.id)
async def get_id(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        await message.answer('Введи имя')
        data['id'] = message.text
        await ChangeName.next()


@dp.message_handler(state=ChangeName.new_name)
async def new_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_name'] = message.text
        await db.update_user_fullname(data.get('new_name'), int(data.get('id')))
        await state.finish()
        await message.answer('Имя успешно заменено')
