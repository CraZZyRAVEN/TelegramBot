from aiogram import F, Router, types, Bot
from aiogram.filters import Command

from common.restricted_words import restricted_words
from filters.chat_types import ChatTypeFilter


user_chat_router = Router()
user_chat_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_chat_router.message(Command('admin'))
async def get_adminns(message: types.Message, bot: Bot) -> None:
    chat_id = message.chat.id
    admins_list = await bot.get_chat_administrators(chat_id)
    print(admins_list)
    admins_list = [admin.user.id for admin in admins_list if admin.status == 'creator' or admin.status == 'administrator']
    print(admins_list)
    bot.my_admins_list = admins_list
    if message.from_user.id in admins_list:
        await message.delete()
    else:
        await message.answer('Личные данные пользователей чата были пересланы вам в личные сообщения.')

@user_chat_router.edited_message()
@user_chat_router.message()
async def cleaner(message: types.Message) -> None:
    if restricted_words.intersection(message.text.casefold().split()):
        await message.answer(f'{message.from_user.first_name}, это запрещенное слово')
        await message.delete()
    

@user_chat_router.message(Command('жамк', prefix='!'))
async def zhamk(message: types.Message) -> None:
    await message.answer('Челик жамкнул другого челика')