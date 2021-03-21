from bot import bot
# from database import db, User, Record
# from utils import Connector

if __name__ == "__main__":
    # res = Connector.get_dicease_overview("Боль внизу живота", 'ru')
    # print(res)

    # db.connect()
    # db.create_tables([User, Record])

    bot.polling(none_stop=True)
