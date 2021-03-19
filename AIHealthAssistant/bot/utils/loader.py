import json

from typing import Dict


class Loader:
    __RESPONSES_FILENAME = "./text/responses.json"

    @staticmethod
    def load_responses() -> Dict:
        result = json.loads(open(Loader.__RESPONSES_FILENAME).read())

        return result
