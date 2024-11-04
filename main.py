import asyncio
from config import TOKEN

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message

dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
    args = message.text.split(maxsplit=1)[1] if len(message.text.split(maxsplit=1)) > 1 else None

    if args:
        await message.answer(f'Аргумент: {args}')
    else:
        await message.answer(f'Аргументов нет.')

async def main() -> None:
    bot = Bot(TOKEN, DefaultBotProperties=ParseMode.HTML)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())
