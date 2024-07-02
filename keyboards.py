from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

is_subscription_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="➕ Obuna bo'lish", url='https://t.me/djalilovv_mukhammad')
        ],
        [
            InlineKeyboardButton(text="➕ Obuna bo'lish", url='https://t.me/test_channel_for_bot54')
        ],
        [
            InlineKeyboardButton(text="✅ Tasdiqlash", callback_data='callback_data')
        ]
    ],
)
