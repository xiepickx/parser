from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import bot
from .call import *
from data.config import load_config
from .db import db_update_phrases, db_get_users, db_users
from .keyb import menu

config = load_config("data/.env")
run = False


@dp.message_handler(commands=['start'], state='*')
async def start_cmd(msg: types.Message, state: FSMContext):
    await state.finish()
    if msg.chat.type == 'private':
        if msg.from_user.id == 856554726:
            await msg.delete()
            await msg.answer(text='Меню', reply_markup=menu())


@dp.message_handler(state='addphrase')
async def addPhraseState(msg: types.Message, state: FSMContext):
    row = db_get_phrases()
    list = row[1]
    data = json.loads(list)
    mylist = data.get("list")
    mylist.append(msg.text.lower())
    data["list"] = mylist
    payload = json.dumps(data)
    db_update_phrases(payload)
    await msg.answer(text='Фразу добавлено!', reply_markup=menu())
    await state.finish()


@dp.message_handler(state='delphrase')
async def delPhraseState(msg: types.Message, state: FSMContext):
    row = db_get_phrases()
    list = row[1]
    data = json.loads(list)
    mylist = data.get("list")
    mylist.remove(msg.text.lower())
    data["list"] = mylist
    payload = json.dumps(data)
    db_update_phrases(payload)
    await msg.answer(text='Фраза удалена!', reply_markup=menu())
    await state.finish()


@dp.message_handler(content_types=['text'])
async def checkAndSend(msg: types.Message):
    if msg.chat.type != 'private':
        if run:
            row = db_get_phrases()
            list = row[1]
            data = json.loads(list)
            l = data.get("list")
            for x in l:
                if x in str(msg.text).lower():
                        try:
                            await msg.forward(chat_id=856554726)
                            await bot.send_message(chat_id=856554726,
                                                  text=f'#new\n\nНовое сообщение от @{msg.from_user.username} ({msg.from_user.id})')
                        except:
                            pass

def register_msg_handler(dp):
    dp.register_message_handler(checkAndSend)
