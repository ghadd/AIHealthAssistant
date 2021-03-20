from peewee import *

from base import db
from user import User
from record import Record

# db.connect()
# db.create_tables([User, Record])

# for i in range(5, 10):
#     Record.create(
#         record_id=i,
#         symptoms='hello',
#         diagnosis='di',
#         required_analizes='a',
#         doctor='d'
#     )



# user = User.create(
#     user_id=15,
#     name='Anna',
#     age=19,
#     address='hello',
#     state=1,
#     last_record=7
# )



user = User.select().where(User.last_record==7).first()

print(user)