from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

MAIN_KB = get_keyboard(
    "выдать випку",
    "отмена",
    placeholder =  "Выберите действие",
    sizes = (1, 1)
)

WHOM_KB = get_keyboard(
    'одному',
    'розыгрыш',
    "назад",
    "отмена",
    placeholder="кому?",
    sizes = (2, 2)
)

TIME_KB = get_keyboard(
    'неделя',
    'месяц',
    'другое',
    "назад",
    "отмена",
    placeholder="на сколько?",
    sizes = (2, 1, 2)
)


@admin_router.message(Command('admin'))
async def admin(message: types.Message) -> None:
    await message.answer('Это админ панель', reply_markup=ADMIN_KB)
    
    
@admin_router.message(F.text == 'выдать випку')
async def add_vip(message: types.Message) -> None:
    await message.answer('Кому выдаём?', reply_markup=WHOM_KB)
    

@admin_router.message(Command('отмена'))
@admin_router.message(F.text.casefold() == 'отмена')
async def add_vip(message: types.Message) -> None:
    await message.answer('Действия отменены', reply_markup=ADMIN_KB)


@admin_router.message(Command('назад'))
@admin_router.message(F.text.casefold() == 'назад')
async def add_vip(message: types.Message) -> None:
    await message.answer('Вы вернулись к предыдущему шагу')


@admin_router.message(F.text == "одному")
async def add_chatter_name(message: types.Message) -> None:
    await message.answer('На какой срок випка?', reply_markup=TIME_KB)
    
    
@admin_router.message(F.text == "розыгрыш")
async def add_chatter_name(message: types.Message) -> None:
    await message.answer('Введите список победителей розыгрыша', reply_markup=types.ReplyKeyboardRemove())
    
    
@admin_router.message(F.text == "неделя")
async def add_chatter_name(message: types.Message) -> None:
    await message.answer('Неделя випки добавлен для юзера')
    
    
@admin_router.message(F.text == "месяц")
async def add_chatter_name(message: types.Message) -> None:
    await message.answer('Месяц випки добавлен для юзера')
    
    
@admin_router.message(F.text == "другое")
async def add_chatter_name(message: types.Message) -> None:
    await message.answer('Введите длительность в неделях', reply_markup=types.ReplyKeyboardRemove())
    