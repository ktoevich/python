import asyncio
import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
from aiogram.filters import Command
from bs4 import BeautifulSoup

API_TOKEN = "8012377575:AAEGhciG9u7icMEvx5zITW9lUImsIL7aP-w"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def send_welcome(message: types.Message):
    kb = ReplyKeyboardMarkup(
        keyboard=[[KeyboardButton(text="/posts")]],
        resize_keyboard=True, 
        input_field_placeholder="Выберите пункт меню"
    )
    await message.reply("Уведомитель постов", reply_markup=kb)

@dp.message(Command("posts"))
async def send_posts(message: types.Message):
    link = "https://habr.com/ru/news/"
    print("Link is equal",link)
    response = requests.get(link) #.text
    print("Response is equal",response.status_code)
    soup = BeautifulSoup(response.text, "html.parser")
    print("soup is working")
    block = soup.find_all("div", class_="tm-article-snippet tm-article-snippet", limit=3)
    # print("Block is equal",block)
    if block:
        print("blok work")
        txt = [el.get_text(strip=True) for el in block]
        print(txt)
        await message.reply(txt)
    else:
        await message.reply("Не удалось найти посты")

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("exit")