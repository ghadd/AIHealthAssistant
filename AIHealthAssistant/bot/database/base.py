from peewee import *
from .config import *

db = MySQLDatabase(DB_NAME, user=DB_USER, password=DB_PASS, host=DB_HOST, port=DB_PORT)

class BaseModel(Model):
    class Meta:
        database = db