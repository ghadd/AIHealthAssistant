from bot import bot
from database import db, User, Record

if __name__ == "__main__":

    db.connect()
    db.create_tables([User, Record])

    bot.polling(none_stop=True)
