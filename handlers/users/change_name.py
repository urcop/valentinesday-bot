from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command

from loader import dp, db
from states.user_states import GetUser


@dp.message_handler(Command(['change_my_name']))
async def change_name(message: types.Message):
    await GetUser.name.set()
    await message.answer('Введите новое имя')


@dp.message_handler(state=GetUser.name)
async def new_name_user(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['name'] = message.text
        await db.update_user_fullname(data.get('name'), int(message.from_user.id))
        await state.finish()
