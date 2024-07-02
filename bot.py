from aiogram import Bot, Dispatcher, F
from asyncio import run
from os import getenv
from dotenv import load_dotenv
from aiogram.types import BotCommand
from aiogram.filters import Command, CommandStart
from filters import CheckSubFilter, CheckSubFilter2

from functions import echo, start_answer, help_answer, check_subscription, check_query_sub

load_dotenv()

TOKEN = getenv('bot_token')
chat_id = getenv('chat_id')

dp = Dispatcher()


async def start(bot: Bot):
    await bot.send_message(chat_id=chat_id, text='Bot ishga tushdi ✅')


async def stop(bot: Bot):
    await bot.send_message(chat_id=chat_id, text='Bot ishdan toxtadi ❕')


async def main(dp_) -> None:
    bot = Bot(token=TOKEN)
    dp_.startup.register(start)
    dp_.message.register(start_answer, Command('start'))
    dp_.message.register(help_answer, Command('help'))
    dp_.message.register(check_subscription, CheckSubFilter())
    dp_.message.register(check_subscription, CheckSubFilter2())
    dp_.callback_query.register(check_query_sub, F.data == "callback_data")
    dp_.message.register(echo)
    dp_.shutdown.register(stop)

    await bot.set_my_commands(
        commands=[
            BotCommand(command='/start', description='Start the bot'),
            BotCommand(command='/help', description='Commands')
        ]
    )

    await dp_.start_polling(bot, polling_timeout=1)


if __name__ == '__main__':
    run(main(dp))
