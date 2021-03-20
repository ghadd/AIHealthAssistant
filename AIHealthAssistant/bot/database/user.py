from peewee import *

from .base import BaseModel


class User(BaseModel):
    __tablename__ = "users"

    user_id = IntegerField(unique=True, primary_key=True,
                           null=False, index=True)
    name = CharField()
    age = IntegerField()
    city = CharField()
    address = CharField()
    state = IntegerField(default=0)

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
    def exists(tg_user) -> bool:
        return bool(User.get_or_none(User.user_id == tg_user.id))
