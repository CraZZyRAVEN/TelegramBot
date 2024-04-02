from aiogram import F, Router, types
from aiogram.filters import CommandStart

from filters.chat_types import ChatTypeFilter


user_private_router = Router()
user_private_router.message.filter(ChatTypeFilter(['private']))


@user_private_router.message(CommandStart())
async def  start__cmd(message: types.Message) -> None:
    await message.answer('Это команда старт')

    
@user_private_router.message(F.text == 'жопа')
async def  echo(message: types.Message) -> None:
    await message.answer('Это магический фильтр:' + message.text)
    