from aiogram import Dispatcher, executor, types, Bot
import token_api

bot = bot(token=token_api)
dp = Dispatcher(bot=bot)


if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)