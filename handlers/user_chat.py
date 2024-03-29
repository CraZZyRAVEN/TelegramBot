from aiogram import Router, types
from aiogram.filters import CommandStart, Command

user_chat_router = Router()


@user_chat_router.message(Command('жамк', prefix='!'))
async def zhamk(message: types.Message) -> None:
    await message.answer('Челик жамкнул другого челика')