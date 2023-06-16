from tg_webapp_bot import bot, executor, dp
from aiogram.types import Message
from aiogram.types import WebAppInfo
import asyncio


@dp.message_handler(commands='start')
async def start(message: Message):
    await message.reply(f"Hi {message.from_user.username}!")


async def main():
    # await bot.set_chat_menu_button(menu_button=WebAppInfo(url="https://wendland0d.github.io/webapp_page/"))
    pass


if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True, reset_webhook=True)
