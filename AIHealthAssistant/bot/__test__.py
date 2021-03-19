from bot import bot
from database import User, db

if __name__ == "__main__":
    User.create(user_id=123)
    # db.connect()
    # db.create_tables([User])
    # print(user)
    # bot.polling(none_stop=True)
