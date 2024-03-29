from aiogram import Router, types
from aiogram.filters import CommandStart, Command

user_private_router = Router()


@user_private_router.message(CommandStart())
async def  start__cmd(message: types.Message) -> None:
    await message.answer('Это команда старт')

    
@user_private_router.message()
async def  echo(message: types.Message) -> None:
    await message.answer(message.text)
    