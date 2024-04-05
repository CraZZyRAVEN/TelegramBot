from aiogram import F, Router, types
from aiogram.filters import Command

from filters.chat_types import ChatTypeFilter, IsAdmin
from keyboards.reply import get_keyboard

admin_router = Router()
admin_router.message.filter(ChatTypeFilter(['private']), IsAdmin())

ADMIN_KB = get_keyboard(
    
)


@admin_router.message(Command('admin'))
async def admin(message: types.Message) -> None:
    await message.answer('Это админ панель', reply_markup=ADMIN_KB)
    
    
@admin_router.message(F.text == 'добавить випку')
async def add_vip(message: types.Message) -> None:
    await message.answer('Это команда добавить випку')
    

@admin_router.message(Command('отмена'))
@admin_router.message(F.text.casefold() == 'отмена')
async def add_vip(message: types.Message) -> None:
    await message.answer('Действия отменены', reply_markup=ADMIN_KB)


@admin_router.message(Command('назад'))
@admin_router.message(F.text.casefold() == 'назад')
async def add_vip(message: types.Message) -> None:
    await message.answer('Вы вернулись к предыдущему шагу')


@admin_router.message(F.text)
async def add_chatter_name(message: types.Message) -> None:
    await message.answer('Это команда добавить випку')