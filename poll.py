import logging
import asyncio
from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from buttons import *

API_TOKEN = 'lox, use your token'

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    await message.answer("Mars botiga xush kelibsiz! Iltimos, variatni tanlang",
                         reply_markup=bosh_menu_keyboard)

from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton




bosh_menu_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Я родитель", callback_data="Я родитель"),
            InlineKeyboardButton(text="Ученик", callback_data="Ученик"),
            InlineKeyboardButton(text="Гость", callback_data="Гость"),
        ]
    ]
)

@dp.callback_query_handler(text="Я родитель")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Добро пожаловать в бот Mars! Пожалуйста, выберите опцию", reply_markup=parents_keyboard)


@dp.callback_query_handler(text="Ученик")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Welcome back, my Lord! Enter your modme id", reply_markup=student_keyboard)

@dp.message_handler(text="🧑‍🎓 Профиль")
async def echo(message: types.Message):
     await message.reply(text="""
     Имя: Shoxrux
Фамилия: Sobirov
Язык: ru
Телефон: 901210909
Город: Ташкент
Учебный центр: YUNUSABAD""")



@dp.message_handler(text="🪙 Мои монеты")
async def echo(message: types.Message):
     await message.reply(text="Мои марс монеты: 695")

@dp.callback_query_handler(text="💥 Space Shop")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Выберите приз", reply_markup=space_shop_keyboard)
    await call.message.delete()


@dp.message_handler(text="💥 Space Shop")
async def echo(message: types.Message):
     await message.reply_photo("https://static.tildacdn.com/tild3939-3062-4336-b334-393735306135/Artboard_2_5.png")






@dp.callback_query_handler(text="Гость")
async def echo(call: types.CallbackQuery):
    await call.message.answer("Добро пожаловать в бот Mars! Пожалуйста, выберите опцию")





@dp.message_handler()
async def echo(message: types.Message):
    await message.answer(message.text)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)


