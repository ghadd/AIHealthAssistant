from peewee import *

from base import BaseModel
import datetime


class Record(BaseModel):
    __tablename__ = "records"

    record_id = IntegerField(unique=True, primary_key=True,
                           null=False, index=True)
    symptoms = TextField()
    date_create = DateTimeField(default=datetime.datetime.now)
    diagnosis = CharField()
    required_analizes = CharField()
    doctor = CharField()

    # @staticmethod
    # def _set_property(tg_user, prop_name, property_value):
    #     user = User.get_or_none(User.user_id == tg_user.id)
    #     if not user:
    #         raise ValueError("User could not be found.")

    #     setattr(user, prop_name, property_value)
    #     user.save()

    # @staticmethod
    # def _get_property(tg_user, prop_name):
    #     user = User.get_or_none(User.user_id == tg_user.id)
    #     if not user:
    #         raise ValueError("User could not be found.")

    #     return getattr(user, prop_name)
