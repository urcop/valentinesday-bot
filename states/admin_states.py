from aiogram.dispatcher.filters.state import StatesGroup, State


class ChangeName(StatesGroup):
    id = State()
    new_name = State()


class DeleteUser(StatesGroup):
    id = State()
