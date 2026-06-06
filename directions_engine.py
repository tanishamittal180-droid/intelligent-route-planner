# backend/directions_engine.py

class DirectionsEngine:

    def __init__(self, graph):

        self.G = graph

    def generate(self, route):

        directions = []

        if len(route) < 2:
            return directions

        directions.append(
            "Start Navigation"
        )

        for i in range(
            len(route) - 1
        ):

            current = route[i]

            nxt = route[i + 1]

            edge = self.G.get_edge_data(
                current,
                nxt
            )

            first_edge = (
                list(edge.values())[0]
            )

            distance = first_edge.get(
                "length",
                0
            )

            road_name = first_edge.get(
                "name",
                "Road"
            )

            directions.append(
                f"Continue on "
                f"{road_name} "
                f"for "
                f"{round(distance)} m"
            )

        directions.append(
            "Destination Reached"
        )

        return directions