from aiogram import Dispatcher, executor, types, Bot

TOKEN_API = '6016467207:AAE4WULwZnLPIM91nctrTyR5o5kznh4EXrA'

bot = bot(token=TOKEN_API)
dp = Dispatcher(bot=bot)

if __name__ == '__main__':
    executor.start_polling(dispatcher=dp)