# backend/cache_manager.py

import joblib
import os


CACHE_DIR = "cache"


def ensure_cache():

    if not os.path.exists(CACHE_DIR):
        os.makedirs(CACHE_DIR)


def graph_cache_path(city):

    safe_name = city.replace(",", "_")
    safe_name = safe_name.replace(" ", "_")

    return os.path.join(
        CACHE_DIR,
        f"{safe_name}.pkl"
    )


def save_graph(city, graph):

    ensure_cache()

    path = graph_cache_path(city)

    joblib.dump(graph, path)

    return path


def load_graph(city):

    path = graph_cache_path(city)

    if os.path.exists(path):
        return joblib.load(path)

    return None


def cache_exists(city):

    path = graph_cache_path(city)

    return os.path.exists(path)