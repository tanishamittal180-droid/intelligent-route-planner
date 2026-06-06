# backend/route_history.py

import json
import os


class RouteHistory:

    def __init__(
        self,
        filename="data/route_history.json"
    ):

        self.filename = filename

        os.makedirs(
            "data",
            exist_ok=True
        )

        if not os.path.exists(
            self.filename
        ):

            with open(
                self.filename,
                "w"
            ) as f:

                json.dump(
                    [],
                    f
                )

    def save_route(
        self,
        source,
        destination,
        algorithm,
        distance,
        eta
    ):

        history = self.get_history()

        history.append({

            "source": source,
            "destination": destination,
            "algorithm": algorithm,
            "distance_km": distance,
            "eta_min": eta

        })

        with open(
            self.filename,
            "w"
        ) as f:

            json.dump(
                history,
                f,
                indent=4
            )

    def get_history(self):

        try:

            with open(
                self.filename,
                "r"
            ) as f:

                return json.load(
                    f
                )

        except:

            return []

    def clear_history(self):

        with open(
            self.filename,
            "w"
        ) as f:

            json.dump(
                [],
                f
            )