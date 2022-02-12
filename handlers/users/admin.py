import logging

from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import CallbackQuery

from data.config import ADMINS
from keyboards.inline.users_keyboard import create_keyboard_users, users_callback
from loader import dp, db, bot
from states.admin_states import ChangeName, DeleteUser


@dp.message_handler(Command(['users']))
async def all_users(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer(text="все пользователи", reply_markup=await create_keyboard_users())
    else:
        await message.answer('у вас нет доступа к этой команде!')


@dp.message_handler(Command(['change_name']))
async def change_name(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await message.answer('Выбери пользователя которому заменить имя',
                             reply_markup=await create_keyboard_users())
        await ChangeName.id.set()
    else:
        await message.answer('Вам нельзя менять имена пользователей :(')


@dp.callback_query_handler(users_callback.filter(), state=ChangeName.id)
async def get_id(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = call.data.split(":")[2]
        await call.message.answer('Какое имя?')
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await ChangeName.next()


@dp.message_handler(state=ChangeName.new_name)
async def new_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['new_name'] = message.text
        await db.update_user_fullname(data.get('new_name'), int(data.get('id')))
        await state.finish()
        await message.answer('Имя успешно заменено')


@dp.message_handler(Command(['delete_user']))
async def del_user(message: types.Message):
    if str(message.from_user.id) in ADMINS:
        await DeleteUser.id.set()
        await message.answer('Кого удаляем?', reply_markup=await create_keyboard_users())
    else:
        await message.answer('у вас нет доступа к этой команде!')


@dp.callback_query_handler(users_callback.filter(), state=DeleteUser.id)
async def get_user(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        data['id'] = call.data.split(":")[2]
        await db.delete_user(int(data['id']))
        await bot.delete_message(call.from_user.id, call.message.message_id)
        await call.message.answer('успешно удален!')


@dp.message_handler(Command(['admin_help']))
async def admin_help(message: types.Message):
    await message.answer('админ команды\n'
                         '/delete_user - удаление пользователя из бд\n'
                         '/users - показывает всех пользователей\n'
                         '/change_name - меняет имя пользователю')
