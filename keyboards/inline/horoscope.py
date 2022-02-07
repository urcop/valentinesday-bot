from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

horoscope_callback = CallbackData('sign', 'sign_name')

horoscope = InlineKeyboardMarkup(row_width=2)

capricorn = InlineKeyboardButton(text='Козерог', callback_data=horoscope_callback.new(sign_name='kozerog'))
horoscope.insert(capricorn)

aries = InlineKeyboardButton(text='Овен', callback_data=horoscope_callback.new(sign_name='oven'))
horoscope.insert(aries)

sagittarius = InlineKeyboardButton(text='Стрелец', callback_data=horoscope_callback.new(sign_name='strelec'))
horoscope.insert(sagittarius)

taurus = InlineKeyboardButton(text='Телец', callback_data=horoscope_callback.new(sign_name='telec'))
horoscope.insert(taurus)

gemini = InlineKeyboardButton(text='Близнецы', callback_data=horoscope_callback.new(sign_name='bliznecy'))
horoscope.insert(gemini)

crab = InlineKeyboardButton(text='Рак', callback_data=horoscope_callback.new(sign_name='rak'))
horoscope.insert(crab)

leo = InlineKeyboardButton(text='Лев', callback_data=horoscope_callback.new(sign_name='lev'))
horoscope.insert(leo)

virgo = InlineKeyboardButton(text='Дева', callback_data=horoscope_callback.new(sign_name='deva'))
horoscope.insert(virgo)

libra = InlineKeyboardButton(text='Высы', callback_data=horoscope_callback.new(sign_name='vesy'))
horoscope.insert(libra)

scorpio = InlineKeyboardButton(text='Скорпион', callback_data=horoscope_callback.new(sign_name='scorpion'))
horoscope.insert(scorpio)

aquarius = InlineKeyboardButton(text='Водолей', callback_data=horoscope_callback.new(sign_name='vodoley'))
horoscope.insert(aquarius)

pisces = InlineKeyboardButton(text='Рыбы', callback_data=horoscope_callback.new(sign_name='riby'))
horoscope.insert(pisces)
