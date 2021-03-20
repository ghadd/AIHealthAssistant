from typing import Any, Callable, List, Union


class NotValidatedError(Exception):
    def __init__(self, value: Any):
        self.text = "Value {} was not casted or validated."
        self.value = value

    def __str__(self):
        return self.text.format(self.value)


# Some default validating funcs
def MORE_THAN_ZERO(x): return x > 0


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
