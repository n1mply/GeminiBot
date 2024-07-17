import aiogram
from aiogram import Bot, Dispatcher, types, F
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command, StateFilter
import asyncio
import logging

from ai import get_gemini_response

keep_alive()

logging.basicConfig(level=logging.INFO)
bot = Bot(token='YOUR-KEY')
dp = Dispatcher()


class WaitResponce(StatesGroup):
  answer = State()


@dp.message(Command('start'), StateFilter(None))
async def start(message: types.Message, state: FSMContext):
  await message.answer('Привет, давай поговорим!')
  await state.clear()


@dp.message(WaitResponce.answer)
async def text(message: types.Message):
  await message.answer('Не так быстро! Дождись текущего ответа...')


@dp.message(F.text)
async def answer(message: types.Message, state: FSMContext):
  await state.set_state(WaitResponce.answer)
  answer = await get_gemini_response(str(message.text))
  try:
    print("Done!")
    await message.answer(answer, parse_mode='Markdown')
  except aiogram.exceptions.TelegramBadRequest:
    print("Alt")
    await message.answer(answer)
  await state.clear()


async def main():
  await dp.start_polling(bot)


if __name__ == '__main__':
  asyncio.run(main())
