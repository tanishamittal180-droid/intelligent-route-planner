# backend/alternative_routes.py

import networkx as nx


class AlternativeRoutes:

    def __init__(self, graph):

        self.G = graph

    def get_routes(
        self,
        source,
        target,
        k=3
    ):

        routes = list(
            nx.shortest_simple_paths(
                self.G,
                source,
                target,
                weight="travel_time"
            )
        )

        return routes[:k]