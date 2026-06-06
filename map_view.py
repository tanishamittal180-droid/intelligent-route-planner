# frontend/map_view.py

import folium

from streamlit_folium import (
    folium_static
)


class MapView:

    def __init__(self):
        pass

    def draw_route(
        self,
        coordinates
    ):

        center = coordinates[0]

        fmap = folium.Map(
            location=center,
            zoom_start=13
        )

        folium.PolyLine(
            coordinates,
            weight=6,
            color="blue"
        ).add_to(fmap)

        folium.Marker(
            coordinates[0],
            popup="Start"
        ).add_to(fmap)

        folium.Marker(
            coordinates[-1],
            popup="Destination"
        ).add_to(fmap)

        return fmap