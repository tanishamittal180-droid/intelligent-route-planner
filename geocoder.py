# backend/geocoder.py

from geopy.geocoders import Nominatim


class Geocoder:

    def __init__(self):

        self.geolocator = Nominatim(
            user_agent="route_planner_pro"
        )

    def search(self, location_name):

        try:

            location = self.geolocator.geocode(
                location_name
            )

            if location:

                return {
                    "name": location.address,
                    "latitude": location.latitude,
                    "longitude": location.longitude
                }

            return None

        except Exception as e:

            print(e)

            return None