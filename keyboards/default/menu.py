from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton('Гороскоп'),
        ],
        [
            KeyboardButton('Бывшему'),
            KeyboardButton('Прпеподавателю'),
        ],
        [
            KeyboardButton('Любимому(й)'),
            KeyboardButton('С приколом'),
        ],
        [
            KeyboardButton('Картинкой'),
        ]
    ],
    resize_keyboard=True
)
