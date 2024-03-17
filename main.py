import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart

bot = Bot(token='7149615033:AAEEg7ueM7jFODl0OeIS_6ZMurcs1-o3b1g')

dp = Dispatcher()


@dp.message(CommandStart())
async def  start__cmd(message: types.Message) -> None:
    await message.answer('Это команда старт.')

@dp.message()
async def defname(message: types.Message) -> None:
    await message.answer(message.text)

async def main() -> None:
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot) 
    

asyncio.run(main())