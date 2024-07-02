import os
from typing import Any, Union, Dict

from aiogram import Bot
from aiogram.filters import Filter
from aiogram.types import Message


class CheckSubFilter(Filter):

    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        channel_id = os.getenv("channel_id")
        user = await bot.get_chat_member(chat_id=channel_id, user_id=message.from_user.id)
        if user.status in ["member", "administrator", "creator"]:
            return False
        else:
            return True


class CheckSubFilter2(Filter):

    async def __call__(self, message: Message, bot: Bot) -> Union[bool, Dict[str, Any]]:
        channel_id2 = os.getenv("channel_id2")
        user = await bot.get_chat_member(chat_id=channel_id2, user_id=message.from_user.id)
        if user.status in ["member", "administrator", "creator"]:
            return False
        else:
            return True
