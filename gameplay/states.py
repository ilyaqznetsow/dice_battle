from aiogram.dispatcher.filters.state import State, StatesGroup


class GameStates(StatesGroup):
    play = State()
    rolls = State()
    get_adress = State()
