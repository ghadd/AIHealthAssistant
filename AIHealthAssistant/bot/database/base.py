import os

from peewee import *
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv(), verbose=True)

db = MySQLDatabase(
    os.getenv("DB_NAME"),
    user=os.getenv("DB_USER"),
    password=os.getenv("DB_PASS"),
    host=os.getenv("DB_HOST"),
    port=int(os.getenv("DB_PORT"))
)


class BaseModel(Model):
    class Meta:
        database = db
