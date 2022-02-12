from aiogram.dispatcher.filters.state import StatesGroup, State


class GetUser(StatesGroup):
    name = State()


class Valentine(StatesGroup):
    forward_to = State()
    message = State()
