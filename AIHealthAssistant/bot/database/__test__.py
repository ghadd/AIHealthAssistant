from peewee import *

from base import db
from user import User
from record import Record

# db.connect()
# db.create_tables([User, Record])

class TGUser:
    id = 20

# user = User.create(
#     user_id=20,
#     name='Dasha',
#     age=17,
#     address='hello',
#     state=2
# )

tg_user = TGUser() 

record = Record.create(
    symptoms="SYMPTOM2",
    diagnosis="D",
    required_analyzes="A",
    doctor="Doc"
)

User.update_last_record(
    tg_user, 
    record
)