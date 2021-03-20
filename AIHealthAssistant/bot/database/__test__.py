from peewee import *

from .base import *
from .user import User
from .record import Record
from .base import db

db.connect()
db.create_tables([User, Record])


