from typing import Any, Callable, List
import re

class NotValidatedError(Exception):
    def __init__(self, value: Any):
        self.text = "Value {} was not casted or validated."
        self.value = value

    def __str__(self):
        return self.text.format(self.value)


# Some default validating funcs
def MORE_THAN_ZERO(x): return x > 0


def BOUNDED(x, min_value: float,
            max_value: float): return min_value < x < max_value

def TEXT_ONLY(x): return re.match("^[A-Za-zА-Яа-я ]*$", x) is not None



class Validator:
    @staticmethod
    def validate_and_cast_numeric(value: Any, wanted_type: Any = float, constraints: List[Callable] = [MORE_THAN_ZERO]):
        assert wanted_type in [int, float]

        try:
            numerical_value = wanted_type(value)
        except ValueError:
            raise NotValidatedError(value)

        for constraint in constraints:
            if not constraint(numerical_value):
                raise NotValidatedError(value)

        return numerical_value

    @staticmethod
    def validate_and_cast_string(value: Any, wanted_type: Any = str, constraints: List[Callable] = [TEXT_ONLY]):
        assert wanted_type in [str]

        try:
            str_value = wanted_type(value)
        except ValueError:
            raise NotValidatedError(value)

        for constraint in constraints:
            if not constraint(str_value):
                raise NotValidatedError(value)

        return str_value
