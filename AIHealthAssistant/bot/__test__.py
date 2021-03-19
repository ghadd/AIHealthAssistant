from bot import bot
from importlib import import_module

database = import_module("../database", "user")

if __name__ == "__main__":
    print(database)
    # bot.polling(none_stop=True)
