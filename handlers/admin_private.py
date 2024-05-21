from aiogram import F, Router, types
from aiogram.filters import Command, StateFilter
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State

from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

MAIN_KB = get_keyboard(
    "выдать випку",
    "выйти из админки",
    placeholder =  "Выберите действие",
    sizes = (1, 1)
)

WHOM_KB = get_keyboard(
    'одному',
    'розыгрыш',
    "отмена",
    placeholder="кому?",
    sizes = (2, 1)
)

TIME_KB = get_keyboard(
    'неделя',
    'месяц',
    'другое',
    "отмена",
    placeholder="на сколько?",
    sizes = (2, 2)
)

class AddVip(StatesGroup):
    name = State()
    names_list = State()
    time = State()

@admin_router.message(Command('admin'))
async def admin(message: types.Message) -> None:
    await message.answer('Это админ панель', reply_markup=MAIN_KB)
    

@admin_router.message(F.text.casefold() == 'выйти из админки')
async def admin(message: types.Message, state: FSMContext) -> None:
    await message.answer('Админка закрыта', reply_markup=types.ReplyKeyboardRemove())
    await state.clear()


    
@admin_router.message(StateFilter(None), F.text.casefold() == 'выдать випку')
async def add_vip(message: types.Message, state: FSMContext) -> None:
    await message.answer('Кому выдаём?', reply_markup=WHOM_KB)
    

@admin_router.message(Command('отмена'))
@admin_router.message(F.text.casefold() == 'отмена')
async def cancel(message: types.Message, state: FSMContext) -> None:
    await message.answer('Действия отменены', reply_markup=MAIN_KB)


@admin_router.message(F.text.casefold() == "одному")
async def add_chatter_name(message: types.Message, state: FSMContext) -> None:
    await message.answer('Введите имя?', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddVip.name)
    
    
@admin_router.message(AddVip.name, F.text)
async def vip_time(message: types.Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    await message.answer('На какой срок випка?', reply_markup=TIME_KB)
    await state.set_state(AddVip.time)
    
@admin_router.message(F.text.casefold() == "неделя")
async def vip_for_week(message: types.Message, state: FSMContext) -> None:
    data = await state.update_data(time=7)
    await message.answer(f'Одна неделя випки добавлена для юзера {data["name"]}')
    await state.clear()
    await message.answer('Что-то ещё?', reply_markup=MAIN_KB)

    
@admin_router.message(F.text.casefold() == "месяц")
async def vip_for_month(message: types.Message, state: FSMContext) -> None:
    data = await state.update_data(time=31)
    await message.answer(f'Месяц випки добавлен для юзера {data["name"]}')
    data = await state.get_data()
    await state.clear()
    await message.answer('Что-то ещё?', reply_markup=MAIN_KB)
    
    
@admin_router.message(F.text.casefold() == "другое")
async def vip_for_other(message: types.Message, state: FSMContext) -> None:
    await message.answer('Введите длительность в неделях', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddVip.time)
    data = await state.update_data(time=message.text*7)
    await message.answer(f'{data["time"]} дней випки было добавлено для юзера {data["name"]}')
    data = await state.get_data()
    await state.clear()
    await message.answer(data)
    await message.answer(reply_markup=MAIN_KB)


@admin_router.message(F.text.casefold() == "розыгрыш")
async def raffle(message: types.Message, state: FSMContext) -> None:
    await message.answer('Введите список победителей розыгрыша', reply_markup=types.ReplyKeyboardRemove())
    await state.set_state(AddVip.names_list)
    await state.update_data(names_list=message.text)
    await state.update_data(time=31)
    data = await state.get_data()
    await state.clear()
    await message.answer(data)
    await message.answer(reply_markup=MAIN_KB)