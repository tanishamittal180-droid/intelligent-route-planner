# backend/graph_loader.py

import osmnx as ox

from backend.cache_manager import (
    save_graph,
    load_graph,
    cache_exists
)


class GraphLoader:

    def __init__(self):

        self.graph = None

    def load_city(self, city):

        if cache_exists(city):

            print("Loading graph from cache...")

            self.graph = load_graph(city)

            return self.graph

        print("Downloading OSM graph...")

        self.graph = ox.graph_from_place(
            city,
            network_type="drive"
        )

        save_graph(
            city,
            self.graph
        )

        return self.graph

    def get_graph(self):

        return self.graph

    def graph_info(self):

        if self.graph is None:

            return None

        return {
            "nodes": len(self.graph.nodes),
            "edges": len(self.graph.edges)
        }