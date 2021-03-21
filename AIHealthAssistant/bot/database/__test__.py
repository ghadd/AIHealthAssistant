from peewee import *

from base import db
from user import User
from record import Record

db.connect()
db.create_tables([User, Record])
