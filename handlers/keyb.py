from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardMarkup, KeyboardButton


def def_menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.row(InlineKeyboardButton(text='Назад', callback_data='menu'))

    return kb


def menu():
    kb = InlineKeyboardMarkup(row_width=2)
    kb.row(InlineKeyboardButton(text='Добавить ключевую фразу', callback_data='phrase_add'), InlineKeyboardButton(text='Удалить ключевую фразу', callback_data='phrase_del'))
    kb.row(InlineKeyboardButton(text='Начать', callback_data='start'))

    return kb
