import folium
from folium.plugins import HeatMap


class TrafficHeatmap:

    def create(
        self,
        coordinates
    ):

        fmap = folium.Map(
            location=coordinates[0],
            zoom_start=12
        )

        HeatMap(
            coordinates
        ).add_to(
            fmap
        )

        return fmap