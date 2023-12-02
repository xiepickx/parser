from aiogram import Bot, Dispatcher
from data.config import load_config
import logging
from aiogram.contrib.fsm_storage.memory import MemoryStorage

logging.basicConfig(level=logging.INFO)
config = load_config("data/.env")

bot = Bot(token=config.tg_bot.token)
dp = Dispatcher(bot, storage=MemoryStorage())

