from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton('Отправить валентинку')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)

keyboard_cancel = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton('Отмена')]
    ]
)
