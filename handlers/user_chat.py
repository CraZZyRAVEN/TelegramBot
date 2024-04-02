from aiogram import F, Router, types
from aiogram.filters import Command

from common.restricted_words import restricted_words
from filters.chat_types import ChatTypeFilter


user_chat_router = Router()
user_chat_router.message.filter(ChatTypeFilter(['group', 'supergroup']))


@user_chat_router.edited_message()
@user_chat_router.message()
async def cleaner(message: types.Message) -> None:
    if restricted_words.intersection(message.text.lower().split()):
        await message.answer(f'{message.from_user.first_name}, это запрещенное слово')
        await message.delete()
    

@user_chat_router.message(Command('жамк', prefix='!'))
async def zhamk(message: types.Message) -> None:
    await message.answer('Челик жамкнул другого челика')