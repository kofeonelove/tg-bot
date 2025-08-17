import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN", "")
SUPPORT_USERNAME = os.getenv("SUPPORT_USERNAME", "@username")

CURRENCY = os.getenv("CURRENCY", "RUB")
PRICES = {
    30: int(os.getenv("PRICE_30", 70)),
    60: int(os.getenv("PRICE_60", 120)),
    180: int(os.getenv("PRICE_180", 300)),
    365: int(os.getenv("PRICE_365", 600)),
}