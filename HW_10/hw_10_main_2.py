"""
 This is a echo bot.
 It echoes any incoming text messages.
 """
 
import logging
 
from aiogram import Bot, Dispatcher, executor, types
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

API_TOKEN = '5677382019:AAEHHOFd7Z_8AfPUSeZ3XMHC_oa_W1wySlc'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message: types.Message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await message.reply("Hi!\nI'm Bot!\n")


@dp.message_handler(commands=['mn'])
async def mn(message: types.Message):
    expression = [message]
    x = symbols('x')
    formula = parse_expr(expression.replace('^', '**'), local_dict={'x': x})
    await expression.reply('Формула:', formula)
    for i in range(3):
        y = formula.subs(x, i)
        await expression.reply(f'x={i}', f'y={y}')

@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)      


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)