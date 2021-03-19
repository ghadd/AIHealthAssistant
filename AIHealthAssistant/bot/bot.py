import os

from telebot import TeleBot
from telebot import types
from dotenv import load_dotenv, find_dotenv

from state import State
from utils import Loader

from database import User

load_dotenv(find_dotenv(), verbose=True)

bot = TeleBot(os.getenv("BOT_TOKEN"))
locale = os.getenv("LOCALE")

responses = Loader.load_responses()


@bot.message_handler(commands=['start'])
def handle_start(msg: types.Message):
    bot.send_message(
        msg.from_user.id,
        responses['start'][locale]
    )
    User.create(
        user_id=msg.from_user.id,
        state=State.NAME_INPUT
    )


@bot.message_handler(func=lambda msg: User.get_state(msg.from_user))
def handle_name_input(msg: types.Message):
    new_name = msg.text
    User.update_name(msg.from_user, new_name)

    bot.send_message(
        msg.from_user.id,
        responses['welcome'][locale].format(new_name),
        parse_mode='Markdown'
    )

    User.update_state(msg.from_user, State.NEUTRAL)
