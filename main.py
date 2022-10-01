from imaplib import Commands
import telebot
import json
import os
import datetime
import imghdr
import logging
import mimetypes
import time
from pathlib import Path
from typing import Any, List, Optional, Type, Union
import telegram.ext
import validators
from apscheduler.schedulers.base import BaseScheduler
from telegram import Bot, Chat, ChatAction, InlineKeyboardMarkup, Message, ReplyKeyboardMarkup
from telegram.error import Unauthorized
from telegram.ext import CallbackQueryHandler, CommandHandler, Dispatcher, MessageHandler
from telegram.ext.callbackcontext import CallbackContext
from telegram.parsemode import ParseMode
from telegram.update import Update
from telegram.utils.request import Request
from aiogram import types, executor, Dispatcher, Bot
from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram_menu import MenuButton
from aiogram import Bot
from telegram_menu import BaseMessage, TelegramMenuSession, NavigationHandler
from aiogram.types import BotCommand
from rich import print
import wget
import emoji
from aiogram.utils import executor
from aiogram.types.web_app_info import WebAppInfo
import string
import aiogram
import anyio
import janitor
import klib
TOKEN = "5776463050:AAF10wHhqH3MX43wSPAt0n7-8Yi7YsYq4Q8"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def button_1(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Главная Дзена со статьями и новостями📜", web_app=WebAppInfo(url="https://zen.yandex.ru/"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Здравствуйте,уважаемый пользователь.Яндекс Дзен-это платформа просмотра и создания контента от увлечённых своим делом людей*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/bdv-bribesdevies-new-post-nouvel-article-gif-18064743', None, 'Text')


@dp.message_handler(commands=['video'])
async def button_2(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Дзен-Видео🎬", web_app=WebAppInfo(url="https://zen.yandex.ru/video"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Данная ссылка ведёт вас на видеораздел Яндекс Дзена*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/video-video-games-video-vakti-video%C3%A7ekelim-video-yap-gif-19933981', None, 'Text')


@dp.message_handler(commands=['discover'])
async def button_3(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Подборки🤯", web_app=WebAppInfo(
        url="https://zen.yandex.ru/discover"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Данная ссылка ведёт вас на раздел Яндекс Дзена,с рекомендательными подборками*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/sthc-smile-together-smile-together-nft-clean-nft-smile-together-happy-club-gif-22345391', None, 'Text')


@dp.message_handler(commands=['shorts'])
async def button_4(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Короткие видео🤪", web_app=WebAppInfo(url="https://zen.yandex.ru/shorts"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Если вы с ТикТока/Инсты,то вам сюда*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/rarity-my-little-pony-rarity-discord-mlp-my-little-pony-rocking-gif-24230547', None, 'Text')


@dp.message_handler(commands=['Profile'])
async def button_5(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(text="Ваша Дзен-Студия💾", web_app=WebAppInfo(
        url="https://zen.yandex.ru/profile/editor/id/5efd9d51828bb93a0ac11bfd"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Здесь находиться ваш профиль Дзена*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/your-favorite-martian-gif-26079162', None, 'Text')


@dp.message_handler(commands=['Books'])
async def button_6(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Самый популярный сайт с бесплатными книгами📚", web_app=WebAppInfo(url="https://b-ok.asia/"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Сайт с Книгами*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/books-libros-cute-kawaii-love-gif-9448750', None, 'Text')


@dp.message_handler(commands=['Music'])
async def button_7(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Известный сайт с разнообразной музыкой🎶", web_app=WebAppInfo(url="https://z2.fm/"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Сайт с Музыкой*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/dj-mlp-my-little-pony-music-vibing-gif-17244265', None, 'Text')


@dp.message_handler(commands=['Anime'])
async def button_8(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Сайт для просмотра аниме", web_app=WebAppInfo(url="https://amedia.online/"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Аниме*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/lvdc-gif-25698367', None, 'Text')


@dp.message_handler(commands=['Second'])
async def button_8(message: types.Message):
    markup = InlineKeyboardMarkup()
    button = InlineKeyboardButton(
        text="Сайт для просмотра аниме 2", web_app=WebAppInfo(url="https://jut.su/anime/"))
    markup.add(button)
    await bot.send_message(message.chat.id, "*Аниме 2*", reply_markup=markup, parse_mode="markdown")
    await bot.send_video(message.chat.id, 'https://tenor.com/view/menhera-chan-chibi-menhera-angry-anime-girl-gif-24076530', None, 'Text')

executor.start_polling(dp, skip_updates=True)
