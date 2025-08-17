from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
from app.config import PRICES, CURRENCY

main_menu = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text="Plans")],
        [KeyboardButton(text="My keys"), KeyboardButton(text="My account")],
        [KeyboardButton(text="Guide"), KeyboardButton(text="Help")],
        [KeyboardButton(text="Partners")],
    ],
    resize_keyboard=True
)

def plans_inline_kb() -> InlineKeyboardMarkup:
    rows = []
    for days, price in PRICES.items():
        rows.append([InlineKeyboardButton(text=f"{days} days — {price} {CURRENCY}", callback_data=f"buy:{days}")])
    return InlineKeyboardMarkup(inline_keyboard=rows)

guide_devices_kb = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="Android", callback_data="guide:android"),
     InlineKeyboardButton(text="Windows", callback_data="guide:windows")],
    [InlineKeyboardButton(text="iPhone", callback_data="guide:ios"),
     InlineKeyboardButton(text="Mac", callback_data="guide:mac")],
])
