"""
 This is a echo bot.
 It echoes any incoming text messages.
 """
 
import logging
 
from aiogram import Bot, Dispatcher, executor, types
from sympy import symbols
from sympy.parsing.sympy_parser import parse_expr

API_TOKEN = '******'

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


@dp.message_handler(commands=['sum'])
async def command_sum(message: types.Message):
    #expression =input(message.text)
    expression = '-2+x^1-3*x^2+x^2+100*x^3-2*x'
    x = symbols('x')
    formula = parse_expr(expression.replace('^', '**'), local_dict={'x': x})
    await bot.send_message(message.chat.id,formula )
    for i in range(3):
       y = formula.subs(x, i)
       await bot.send_message(message.chat.id,(f'x={i}', f'y={y}'))
@dp.message_handler()
async def echo(message: types.Message):
    # old style:
    # await bot.send_message(message.chat.id, message.text)

    await message.answer(message.text)     


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)