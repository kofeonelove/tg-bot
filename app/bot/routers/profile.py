from aiogram import Router, F
from aiogram.types import Message

router = Router(name="profile")

@router.message(F.text == "My keys")
async def my_keys(m: Message):
    await m.answer("Your subscription keys will appear here once you purchase a plan.")

@router.message(F.text == "My account")
async def my_account(m: Message):
    await m.answer("Account status: no active subscription.\nReferrals and trials — coming soon.")
