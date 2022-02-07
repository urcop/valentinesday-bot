from aiogram.types import Message

from keyboards.inline.horoscope import horoscope
from loader import dp


@dp.message_handler(text='Гороскоп')
async def get_horoscope(message: Message):
    await message.answer('Выберите знак зодиака, который нужен', reply_markup=horoscope)
