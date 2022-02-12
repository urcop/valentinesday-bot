from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.types import CallbackQuery

from keyboards.inline.users_keyboard import create_keyboard_users, users_callback
from states.user_states import Valentine

from loader import dp, db, bot


@dp.message_handler(text='Отправить валентинку')
async def forward(message: types.Message):
    await message.answer('Выберите, кому хотите отправить валентинку', reply_markup=await create_keyboard_users())
    await Valentine.forward_to.set()


@dp.callback_query_handler(users_callback.filter(), state=Valentine.forward_to)
async def choice_person(call: CallbackQuery, state: FSMContext):
    async with state.proxy() as data:
        user = call.data
        pined_user = await db.select_user(tg_id=int(user.split(":")[2]))
        data['forward_to'] = user.split(":")[2]
        await call.message.answer(f'Вы выбрали - {pined_user["fullname"]}')
        await call.message.answer('Напишите сообщение этому человеку или отправьте картинку')
        await Valentine.next()


@dp.message_handler(state=Valentine.message, content_types=["text"])
async def write_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.text
        text = '[ Вам анонимное сообщение ]\n\n' \
               f'{data["message"]}'

        await bot.send_message(data['forward_to'], text)
        await message.answer('Отправлено!')
        await state.finish()


@dp.message_handler(state=Valentine.message, content_types=["photo"])
async def write_message(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['message'] = message.photo[-1].file_id
        await bot.send_message(data['forward_to'], text='[ Вам анонимное сообщение ]')
        await bot.send_photo(data['forward_to'], data['message'])
        await message.answer('Отправлено!')
        await state.finish()
