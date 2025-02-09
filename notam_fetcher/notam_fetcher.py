import requests


class NotamFetcher:
    DOMAIN = "https://external-api.faa.gov/notamapi/v1/notams"

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret

    def _fetchNotamsByLatLong(self, lat: float, long: float, radius: float = 100.0):
        """
        Fetches a response from the API using latitude and longitude.

        Args:
            lat (float): The latitude to fetch NOTAMs from
            long (float): The longitude to fetch NOTAMs from
            radius (float): The location radius criteria. (max:100)

        Returns:

        Raises:

        """

        querystring = {
            "locationLongitude": str(lat),
            "locationLatitude": str(long),
            "locationRadius": str(radius),
        }

        response = requests.get(
            self.DOMAIN,
            headers={"client_id": self.client_id, "client_secret": self.client_secret},
            params=querystring,
        )

        return response.json()
