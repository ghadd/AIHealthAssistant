from typing import List
from .loader import Loader
from .models import predictor

clf = predictor.load_model("./utils/models/model_.dump")
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
        desease = predictor.get_prediction(clf, users_description)
        print(users_description)
        print(desease)

        # connect from evalueated model
        response_args = {
            "symptoms": ["a", "b"],
            "diagnosis": " | ".join(desease),
            "analysis": ["med1", "med2"],
            "doctor": "doc"
        }
        _, diagnosis, anals, doctor = response_args.values()

        if diagnosis:
            response = responses['help_symptoms2'][locale].format(
                diagnosis=diagnosis,
                analysis=Connector.get_enumerated_list_stub(anals),
                doctor=doctor
            )
        else:
            response = responses['error']['symptoms_validation'][locale]

        return response_args, response
