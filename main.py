import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message

from dotenv import load_dotenv
import os

load_dotenv()
TOKEN = os.getenv("TOKEN")

bot = Bot(token=TOKEN)
dp = Dispatcher()


@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Привет! Я тестовый бот для проверки работы с aiogram")


@dp.message(Command("help"))
async def help(message: Message):
    await message.answer("Список доступных команд:\n/start - начать общение с ботом\n/help - получить список доступных команд")


@dp.message(F.text.lower() == "ping")
async def ping(message: Message):
    await message.answer("pong")


async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot has been successfully stopped")