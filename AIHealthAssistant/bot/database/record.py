from peewee import *
from .base import BaseModel
from playhouse.mysql_ext import JSONField
import datetime


class Record(BaseModel):
    __tablename__ = "records"

    record_id = PrimaryKeyField(unique=True, primary_key=True,
                                null=False, index=True, constraints=[SQL('AUTO_INCREMENT')])
    symptoms = JSONField()
    date_create = DateTimeField(default=datetime.datetime.now)
    diagnosis = CharField()
    required_analyzes = JSONField()
    doctor = CharField()
