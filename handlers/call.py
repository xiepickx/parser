import json
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from create_bot import dp, bot
from handlers.db import db_get_phrases
from handlers.keyb import def_menu, menu

@dp.callback_query_handler(text='menu', state='*')
async def ADMstop(call: types.CallbackQuery, state: FSMContext):
    await state.finish()

    await call.message.edit_text(text='Меню', reply_markup=menu())


@dp.callback_query_handler(text_contains='phrase_')
async def phraseCall(call: types.CallbackQuery, state: FSMContext):
    cid = call.data.split('_')[1]
    if cid == 'add':
        await state.set_state('addphrase')
    else:
        await state.set_state('delphrase')
    row = db_get_phrases()
    list = row[1]
    data = json.loads(list)
    mylist = data.get("list")
    txt = ''
    for x in mylist:
        txt = f'{txt}{x}, '
    await call.message.edit_text(text=f'<b>Добавленные фразы:</b> \n<i>{txt}</i>\n<b>Введите фразу:</b>', parse_mode='html', reply_markup=def_menu())


@dp.callback_query_handler(text='start')
async def Start(call: types.CallbackQuery):
    run = True
    await call.answer(text='Запущено!', show_alert=True)

def register_handlers_call(dp):
    dp.register_callback_query_handler(ADMstop, text='menu')
