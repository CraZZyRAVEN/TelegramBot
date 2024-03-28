from aiogram import Router, types
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def  start__cmd(message: types.Message) -> None:
    await message.answer('Это команда старт')

@user_private_router.message(Command('жамк', prefix='!'))
async def zhamk(message: types.Message) -> None:
    await message.answer('Челик жамкнул другого челика')