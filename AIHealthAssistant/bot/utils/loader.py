import json

from typing import Dict
from telebot.types import InlineKeyboardButton, InlineKeyboardMarkup


class Loader:
    __RESPONSES_FILENAME = "./text/responses.json"
    __MARKUPS_FILENAME = "./text/markups.json"

    @staticmethod
    def load_json_file(filename) -> Dict:
        result = json.loads(open(filename).read())

        return result

    @staticmethod
    def load_responses() -> Dict:
        return Loader.load_json_file(Loader.__RESPONSES_FILENAME)

    @staticmethod
    def load_markups() -> Dict:
        return Loader.load_json_file(Loader.__MARKUPS_FILENAME)

    @staticmethod
    def load_markup(name, locale) -> InlineKeyboardMarkup:
        markups_json = Loader.load_markups()
        markup_json = markups_json[name]

        buttons = []

        for row in markup_json["buttons"]:
            buttons_row = []
            for button in row:
                button = InlineKeyboardButton(
                    button['text'][locale], callback_data=button['cb'])
                buttons_row.append(button)

            buttons.append(buttons_row)

        markup = InlineKeyboardMarkup(keyboard=buttons)
        return markup
