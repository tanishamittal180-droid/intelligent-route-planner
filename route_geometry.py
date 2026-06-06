# backend/route_geometry.py

import osmnx as ox


class RouteGeometry:

    def __init__(self, graph):

        self.G = graph

    def extract(self, route):

        coordinates = []

        for node in route:

            lat = self.G.nodes[node]["y"]

            lon = self.G.nodes[node]["x"]

            coordinates.append(
                [lat, lon]
            )

        return coordinates