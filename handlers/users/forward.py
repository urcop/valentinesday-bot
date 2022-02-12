from aiogram import types
from aiogram.types import CallbackQuery

from keyboards.inline.users_keyboard import create_keyboard_users, users_callback
from states.user_states import Valentine

from loader import dp


@dp.message_handler(text='Отправить валентинку')
async def forward(message: types.Message):
    await message.answer('Выберите, кому хотите отправить валентинку', reply_markup=await create_keyboard_users())


@dp.callback_query_handler(users_callback.filter())
async def choice_person(call: CallbackQuery):
    user = call.data
    await call.message.answer(f'Вы выбрали - {user.split(":")[2]}')

