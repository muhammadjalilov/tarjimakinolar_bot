from aiogram import Bot
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext

from db import Database
from filters import CheckSubFilter, CheckSubFilter2
from keyboards import is_subscription_keyboard


async def echo(message: Message, bot: Bot):
    await message.copy_to(chat_id=message.from_user.id)


async def start_answer(message: Message, bot: Bot):
    user = message.from_user
    db = Database()
    is_new_user = await db.search_id_from_db(int(message.from_user.id))
    if is_new_user:
        await db.insert_user(int(message.from_user.id))
        print(int(message.from_user.id))
    await message.answer(text=f"Hello <b>{user.mention_html(f'{user.first_name}')}</b>", parse_mode="HTML")


async def help_answer(message: Message, bot: Bot):
    await message.answer("""Commands:
    /start --> Start the bot
    /help --> Help 
    """)


async def check_subscription(message: Message, bot: Bot):
    await message.answer("❌ Kechirasiz botimizdan foydalanishdan oldin ushbu\nkanallarga a'zo bo'lishingiz kerak.",
                         reply_markup=is_subscription_keyboard)


async def check_query_sub(query: CallbackQuery, bot: Bot):
    check1 = CheckSubFilter()
    check2 = CheckSubFilter2()

    is_not_subscribed_1 = await check1(query.message, bot)
    is_not_subscribed_2 = await check2(query.message, bot)
    print(is_not_subscribed_1)
    print(is_not_subscribed_2)
    if not is_not_subscribed_1 and not is_not_subscribed_2:
        await query.answer('Kanallarga obuna bolganingizdan xursandmiz', show_alert=True)
    else:
        await query.answer('Hamma kanalga obuna boling', show_alert=True)



