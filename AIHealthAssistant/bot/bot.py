import os
from threading import local

from telebot import TeleBot
from telebot import types
from dotenv import load_dotenv, find_dotenv
from functools import partial

from state import State
from utils import Loader, Validator, Connector, NotValidatedError, BOUNDED, TEXT_ONLY

from database import User

load_dotenv(find_dotenv(), verbose=True)

bot = TeleBot(os.getenv("BOT_TOKEN"))
# temporary solution for multilingual support
locale = os.getenv("LOCALE")

responses = Loader.load_responses()


@bot.message_handler(commands=['start'])
def handle_start(msg: types.Message):
    if not User.exists(msg.from_user):
        bot.send_message(
            msg.from_user.id,
            responses['start'][locale]
        )

        User.create(
            user_id=msg.from_user.id,
            state=State.NAME_INPUT
        )
    else:
        bot.send_message(
            msg.from_user.id,
            responses['known_user'][locale].format(
                User.get_name(msg.from_user)),
            reply_markup=Loader.load_markup("main_menu", locale)
        )


@bot.callback_query_handler(func=lambda cb: cb.data == "/update_user_data")
def handle_help_symptoms(cb):
    bot.send_message(
        cb.from_user.id,
        responses['update_user_data'][locale]
    )

    User.update_state(
        cb.from_user, 
        State.NAME_INPUT
    )

@bot.message_handler(func=lambda msg: User.get_state(msg.from_user) == State.NAME_INPUT)
def handle_name_input(msg: types.Message):
    try:
        new_name = Validator.validate_and_cast_string(
            msg.text,
            wanted_type=str,
            constraints=[partial(TEXT_ONLY)]
        )
        response = responses['welcome1'][locale]
        User.update_state(msg.from_user, State.AGE_INPUT)
        User.update_name(msg.from_user, new_name)

    except NotValidatedError:
        response = responses['error']['name_validation'][locale]


    bot.send_message(
        msg.from_user.id,
        response,
        parse_mode='Markdown'
    )


@bot.message_handler(func=lambda msg: User.get_state(msg.from_user) == State.AGE_INPUT)
def handle_age_input(msg: types.Message):
    try:
        new_age = Validator.validate_and_cast_numeric(
            msg.text,
            wanted_type=int,
            constraints=[partial(BOUNDED, min_value=1, max_value=120)]
        )
        response = responses['welcome2'][locale]
        User.update_state(msg.from_user, State.ADDRESS_INPUT)
        User.update_age(msg.from_user, new_age)

    except NotValidatedError:
        response = responses['error']['age_validation'][locale]

    bot.send_message(
        msg.from_user.id,
        response
    )


@bot.message_handler(func=lambda msg: User.get_state(msg.from_user) == State.ADDRESS_INPUT)
def handle_address_input(msg: types.Message):
    new_address = msg.text
    User.update_address(msg.from_user, new_address)

    reply_markup = Loader.load_markup("main_menu", locale)

    bot.send_message(
        msg.from_user.id,
        responses['welcome3'][locale],
        parse_mode='Markdown',
        reply_markup=reply_markup
    )

    User.update_state(msg.from_user, State.NEUTRAL)

@bot.callback_query_handler(func=lambda cb: cb.data == "/help_symptoms")
def handle_help_symptoms(cb):

    bot.send_message(
        cb.from_user.id,
        responses['help_symptoms1'][locale]
    )
    bot.delete_message(cb.from_user.id, cb.message.message_id)

    User.update_state(cb.from_user, State.SYMPTOMS_INPUT)


@bot.message_handler(func=lambda msg: User.get_state(msg.from_user) == State.SYMPTOMS_INPUT)
def handle_symptoms_input(msg):
    response = Connector.get_dicease_overview(msg.text, locale)

    bot.send_message(
        msg.from_user.id,
        response,
        parse_mode="Markdown"
    )
    handle_start(msg)

    User.update_state(msg.from_user, State.NEUTRAL)
