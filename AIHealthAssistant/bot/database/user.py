from peewee import *

from .base import BaseModel
from .record import Record


class User(BaseModel):
    __tablename__ = "users"

    user_id = IntegerField(unique=True, primary_key=True,
                           null=False, index=True)
    name = CharField()
    age = IntegerField()
    address = CharField()
    state = IntegerField(default=0)
    last_record = ForeignKeyField(Record, backref='users')

    @staticmethod
    def _set_property(tg_user, prop_name, property_value):
        user = User.get_or_none(User.user_id == tg_user.id)
        if not user:
            raise ValueError("User could not be found.")

        setattr(user, prop_name, property_value)
        user.save()

    @staticmethod
    def _get_property(tg_user, prop_name):
        user = User.get_or_none(User.user_id == tg_user.id)
        if not user:
            raise ValueError("User could not be found.")

        return getattr(user, prop_name)

    @staticmethod
    def update_state(tg_user, new_state):
        User._set_property(tg_user, "state", new_state)

    @staticmethod
    def get_state(tg_user):
        return User._get_property(tg_user, "state")

    @staticmethod
    def update_name(tg_user, new_name):
        User._set_property(tg_user, "name", new_name)

    @staticmethod
    def get_name(tg_user):
        return User._get_property(tg_user, "name")

    @staticmethod
    def update_age(tg_user, new_age):
        User._set_property(tg_user, "age", new_age)

    @staticmethod
    def get_age(tg_user):
        return User._get_property(tg_user, "age")

    @staticmethod
    def update_address(tg_user, new_address):
        User._set_property(tg_user, "address", new_address)

    @staticmethod
    def get_address(tg_user):
        return User._get_property(tg_user, "address")

    @staticmethod
    def update_last_record(tg_user, new_record):
        User._set_property(tg_user, "last_record", new_record)

    @staticmethod
    def get_last_record(tg_user):
        return User._get_property(tg_user, "last_record")

    @staticmethod
    def exists(tg_user) -> bool:
        return bool(User.get_or_none(User.user_id == tg_user.id))
