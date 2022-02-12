from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from loader import db

users_callback = CallbackData('user', 'id', 'tg_id')


async def create_keyboard_users():
    keyboard = InlineKeyboardMarkup(row_width=2)
    users = await db.select_all_users()
    for user in users:
        keyboard.insert(
            InlineKeyboardButton(text=user['fullname'],
                                 callback_data=users_callback.new(id=user['id'], tg_id=user['tg_id']))
        )
    return keyboard
