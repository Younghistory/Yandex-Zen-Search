import string
import aiogram
from aiogram import types,executor, Dispatcher,Bot
from aiogram.types import InlineKeyboardButton,InlineKeyboardMarkup
from aiogram.types.web_app_info import WebAppInfo
from aiogram.utils import executor
import os,json,string
import emoji
TOKEN="5776463050:AAF10wHhqH3MX43wSPAt0n7-8Yi7YsYq4Q8"

bot= Bot(token=TOKEN)
dp= Dispatcher(bot)



@dp.message_handler(commands=['start'])
async def button_1(message: types.Message):
    markup=InlineKeyboardMarkup()
    button=InlineKeyboardButton(text="Главная Дзена со статьями📜",web_app=WebAppInfo(url="https://zen.yandex.ru/"))
    markup.add(button)
    await  bot.send_message(message.chat.id,"*Здравствуйте,уважаемый пользователь.Яндекс Дзен-это платформа просмотра и создания контента от увлечённых своим делом людей.*",reply_markup=markup,parse_mode="markdown")

@dp.message_handler(commands=['begin'])
async def button_2(message: types.Message):
     markup = InlineKeyboardMarkup()
     button = InlineKeyboardButton(text="Дзен-Видео🎬",web_app=WebAppInfo(url="https://zen.yandex.ru/video"))
     markup.add(button)
     await  bot.send_message(message.chat.id,"*Данная ссылка ведёт вас на видеораздел Яндекс Дзена.*",reply_markup=markup,parse_mode="markdown")

@dp.message_handler(commands=['discover'])
async def button_3(message: types.Message):
     markup = InlineKeyboardMarkup()
     button = InlineKeyboardButton(text="Подборки🤯",web_app=WebAppInfo(url="https://zen.yandex.ru/discover"))
     markup.add(button)
     await  bot.send_message(message.chat.id,"*Данная ссылка ведёт вас на раздел Яндекс Дзена,с рекомендательными подборками.*",reply_markup=markup,parse_mode="markdown")

@dp.message_handler(commands=['shorts'])
async def button_4(message: types.Message):
     markup = InlineKeyboardMarkup()
     button = InlineKeyboardButton(text="Короткие видео🤪",web_app=WebAppInfo(url="https://zen.yandex.ru/shorts"))
     markup.add(button)
     await  bot.send_message(message.chat.id,"*Если вы с ТикТока,то вам сюда.*",reply_markup=markup,parse_mode="markdown")

@dp.message_handler(commands=['Profile'])
async def button_5(message: types.Message):
     markup = InlineKeyboardMarkup()
     button = InlineKeyboardButton(text="Ваша Дзен-Студия💾",web_app=WebAppInfo(url="https://zen.yandex.ru/profile/editor/id/5efd9d51828bb93a0ac11bfd"))
     markup.add(button)
     await  bot.send_message(message.chat.id,"*Здесь находиться ваш профиль Дзена.*",reply_markup=markup,parse_mode="markdown")


@dp.message_handler(commands=['Books'])
async def button_6(message: types.Message):
     markup = InlineKeyboardMarkup()
     button = InlineKeyboardButton(text="Самый популярный сайт с бесплатными книгами📚",web_app=WebAppInfo(url="https://b-ok.asia/"))
     markup.add(button)
     await  bot.send_message(message.chat.id,"*Сайт с Книгами.*",reply_markup=markup,parse_mode="markdown")




executor.start_polling(dp, skip_updates=True)