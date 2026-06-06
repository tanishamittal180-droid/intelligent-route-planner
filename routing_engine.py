# backend/routing_engine.py

import osmnx as ox
import networkx as nx
from math import radians, sin, cos, sqrt, atan2


class RoutingEngine:

    def __init__(self, graph):
        self.G = graph

    # ====================================
    # NODE LOOKUP
    # ====================================

    def nearest_node(
        self,
        latitude,
        longitude
    ):

        return ox.distance.nearest_nodes(
            self.G,
            longitude,
            latitude
        )

    # ====================================
    # EDGE HELPER
    # ====================================

    def edge_data(
        self,
        u,
        v
    ):

        edge = self.G.get_edge_data(
            u,
            v
        )

        if edge is None:
            return {}

        if isinstance(edge, dict):

            if 0 in edge:
                return edge[0]

            return list(edge.values())[0]

        return edge

    # ====================================
    # DISTANCE
    # ====================================

    def route_distance(
        self,
        route
    ):

        distance = 0

        for u, v in zip(
            route[:-1],
            route[1:]
        ):

            edge = self.edge_data(
                u,
                v
            )

            distance += edge.get(
                "length",
                0
            )

        return distance

    # ====================================
    # ETA
    # ====================================

    def route_eta(
        self,
        route
    ):

        eta = 0

        for u, v in zip(
            route[:-1],
            route[1:]
        ):

            edge = self.edge_data(
                u,
                v
            )

            eta += edge.get(
                "travel_time",
                edge.get(
                    "length",
                    0
                )
            )

        return eta

    # ====================================
    # TOLLS
    # ====================================

    def route_tolls(
        self,
        route
    ):

        tolls = 0

        for u, v in zip(
            route[:-1],
            route[1:]
        ):

            edge = self.edge_data(
                u,
                v
            )

            tolls += edge.get(
                "toll",
                0
            )

        return tolls

    # ====================================
    # ECO SCORE
    # ====================================

    def eco_score(
        self,
        route
    ):

        distance = self.route_distance(
            route
        )

        eta = self.route_eta(
            route
        )

        return (
            0.6 * eta +
            0.4 * distance
        )

    # ====================================
    # DIJKSTRA
    # ====================================

    def dijkstra(
        self,
        source,
        target
    ):

        return nx.shortest_path(
            self.G,
            source,
            target,
            weight="travel_time"
        )

    # ====================================
    # A STAR
    # ====================================

    def astar(
        self,
        source,
        target
    ):

        def heuristic(a, b):

            lat1 = self.G.nodes[a]["y"]
            lon1 = self.G.nodes[a]["x"]

            lat2 = self.G.nodes[b]["y"]
            lon2 = self.G.nodes[b]["x"]

            return self.haversine(
                lat1,
                lon1,
                lat2,
                lon2
            )

        return nx.astar_path(
            self.G,
            source,
            target,
            heuristic=heuristic,
            weight="travel_time"
        )

    # ====================================
    # SHORTEST DISTANCE
    # ====================================

    def shortest_distance(
        self,
        source,
        target
    ):

        return nx.shortest_path(
            self.G,
            source,
            target,
            weight="length"
        )

    # ====================================
    # ECO ROUTE
    # ====================================

    def eco_route(
        self,
        source,
        target
    ):

        def eco_weight(
            u,
            v,
            attrs
        ):

            distance = attrs.get(
                "length",
                1
            )

            traffic = attrs.get(
                "traffic_factor",
                1
            )

            return (
                distance *
                traffic
            )

        return nx.shortest_path(
            self.G,
            source,
            target,
            weight=eco_weight
        )

    # ====================================
    # K ALTERNATIVE ROUTES
    # ====================================

    def alternative_routes(
        self,
        source,
        target,
        k=3
    ):

        try:

            routes = list(
                nx.shortest_simple_paths(
                    self.G,
                    source,
                    target,
                    weight="travel_time"
                )
            )

            return routes[:k]

        except Exception:

            return []

    # ====================================
    # ROUTE STATS
    # ====================================

    def route_summary(
        self,
        route
    ):

        return {

            "distance_km":
                round(
                    self.route_distance(
                        route
                    ) / 1000,
                    2
                ),

            "eta_min":
                round(
                    self.route_eta(
                        route
                    ) / 60,
                    2
                ),

            "tolls":
                self.route_tolls(
                    route
                ),

            "eco_score":
                round(
                    self.eco_score(
                        route
                    ),
                    2
                ),

            "nodes":
                len(route)
        }

    # ====================================
    # PLACE TO PLACE
    # ====================================

    def route_from_places(
        self,
        src_lat,
        src_lon,
        dst_lat,
        dst_lon,
        algorithm="A*"
    ):

        source = self.nearest_node(
            src_lat,
            src_lon
        )

        target = self.nearest_node(
            dst_lat,
            dst_lon
        )

        if algorithm == "Dijkstra":

            route = self.dijkstra(
                source,
                target
            )

        elif algorithm == "Eco":

            route = self.eco_route(
                source,
                target
            )

        elif algorithm == "Shortest":

            route = self.shortest_distance(
                source,
                target
            )

        else:

            route = self.astar(
                source,
                target
            )

        return route

    # ====================================
    # HAVERSINE
    # ====================================

    def haversine(
        self,
        lat1,
        lon1,
        lat2,
        lon2
    ):

        R = 6371000

        dlat = radians(
            lat2 - lat1
        )

        dlon = radians(
            lon2 - lon1
        )

        a = (
            sin(dlat / 2) ** 2
            + cos(radians(lat1))
            * cos(radians(lat2))
            * sin(dlon / 2) ** 2
        )

        c = 2 * atan2(
            sqrt(a),
            sqrt(1 - a)
        )

        return R * c