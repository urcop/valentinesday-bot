import logging

from aiogram import executor

from loader import dp, db
import middlewares, filters, handlers
from utils.notify_admins import on_startup_notify
from utils.set_bot_commands import set_default_commands


async def on_startup(dispatcher):
    logging.info('Подключение к бд')
    await db.create()
    logging.info('Создание таблицы пользователей')
    await db.create_table_users()
    logging.info('Создание таблицы валентинок гороскопа')
    await db.create_table_horoscope()
    logging.info('Создание таблицы валентинок преподавателям')
    await db.create_table_teacher()
    logging.info('Создание таблицы валентинок для бывшего')
    await db.create_table_ex()
    logging.info('Создание таблицы валентинок с приколом')
    await db.create_table_joke()
    logging.info('Создание таблицы валентинок для любимого')
    await db.create_table_love()
    logging.info('Создание таблицы валентинок картинкой')
    await db.create_table_photo()
    logging.info('готово')
    await set_default_commands(dispatcher)

    # Уведомляет про запуск
    # await on_startup_notify(dispatcher)


if __name__ == '__main__':
    executor.start_polling(dp, on_startup=on_startup)

