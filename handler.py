from aiogram import F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards as kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Привет, это твой id: {message.from_user.id}",
                         reply_markup=kb.main)

@router.message(Command('help'))
async def cmd_help(message: Message):
    await message.answer("this is command help")

@router.message(F.text == "Как дела?")
async def how_are_you(message: Message):
    await message.answer("ОК!")

@router.message(F.photo)
async def get_photo(message: Message):
    await message.answer(f"ID фотографии: {message.photo[-1].file_id}")
    
@router.message(Command('get_photo'))
async def photo(message: Message):
    await message.answer_photo(photo="https://www.youtube.com/img/desktop/yt_1200.png")

    