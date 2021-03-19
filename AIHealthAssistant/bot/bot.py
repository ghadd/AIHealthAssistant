import os

from telebot import TeleBot
from telebot import types
from dotenv import load_dotenv, find_dotenv

from state import State
from utils import Loader

load_dotenv(find_dotenv(), verbose=True)

bot = TeleBot(os.getenv("BOT_TOKEN"))
locale = os.getenv("LOCALE")

responses = Loader.load_responses()


@bot.message_handler(commands=['start'])
def start(msg: types.Message):
    bot.send_message(
        msg.from_user.id,
        responses['start'][locale]
    )
    # set users state to State.NAME_INPUT
