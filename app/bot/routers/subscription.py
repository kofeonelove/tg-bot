from aiogram import Router, F
from aiogram.types import Message, CallbackQuery
from app.keyboards import plans_inline_kb
from app.config import CURRENCY

router = Router(name="subscription")

@router.message(F.text == "💎 Plans")
async def plans(m: Message):
    await m.answer("Choose a subscription length:", reply_markup=plans_inline_kb())

@router.callback_query(F.data.startswith("buy:"))
async def buy_placeholder(c: CallbackQuery):
    days = c.data.split(":")[1]
    await c.message.answer(
        f"Payment for **{days} days** is not configured yet.\n"
        f"We’ll support Telegram Stars / YooKassa later.\n"
        f"For now, contact support to complete the purchase."
    )
    await c.answer()
