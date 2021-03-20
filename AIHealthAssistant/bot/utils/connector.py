from typing import List
from .loader import Loader

responses = Loader.load_responses()


class Connector:
    @staticmethod
    def get_enumerated_list_stub(data: List[str]):
        assert data

        stub = "\n".join(
            [f'{idx+1}. {value}' for idx, value in enumerate(data)]
        )
        return stub

    @staticmethod
    def get_dicease_overview(users_description: str, locale: str):
        # connect from evalueated model
        diagnosis, anals, doctor = "diag", ["med1", "med2"], "doc"

        if diagnosis:
            response = responses['help_symptoms2'][locale].format(
                diagnosis=diagnosis,
                analysis=Connector.get_enumerated_list_stub(anals),
                doctor=doctor
            )
        else:
            response = responses['error']['symptoms_validation'][locale]

        return response
