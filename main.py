import asyncio
from colored import Fore
from aiogram import executor
from create_bot import dp
from handlers import msg, call
from handlers.db import con, cur
import sqlite3
from data.config import load_config
config = load_config("data/.env")



def db():
    try:
        cur.execute('CREATE TABLE "users" ("id"	INTEGER UNIQUE, "username"	TEXT)')
        print(Fore.light_green+'[X] Users DB created!')

    except:
        print(Fore.light_red+'[X] Users DB already created!')


    try:
        cur.execute('CREATE TABLE "settings" ("key"	TEXT UNIQUE,"value"	TEXT)')
        print(Fore.light_green+'[X] settings DB created!')

    except:
        print(Fore.light_red+'[X] settings DB already created!')


def on_startup():
    db()
    print(Fore.light_green + '[X] Bot Started!')


call.register_handlers_call(dp)
msg.register_msg_handler(dp)

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=False, on_startup=on_startup(), timeout=45)
