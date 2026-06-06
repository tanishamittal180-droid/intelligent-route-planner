# backend/traffic_engine.py

import random
from datetime import datetime


class TrafficEngine:

    def __init__(self):
        pass

    def current_multiplier(self):

        hour = datetime.now().hour

        # Morning rush
        if 7 <= hour <= 10:
            return 1.8

        # Evening rush
        elif 17 <= hour <= 20:
            return 2.0

        # Night
        elif 22 <= hour or hour <= 5:
            return 0.8

        return 1.2

    def apply_traffic(self, G):

        base_factor = self.current_multiplier()

        for u, v, key, data in G.edges(keys=True, data=True):

            length = data.get("length", 100)

            random_factor = random.uniform(
                0.8,
                1.3
            )

            congestion = (
                base_factor *
                random_factor
            )

            data["traffic_factor"] = congestion

            data["travel_time"] = (
                length *
                congestion
            )

        return G