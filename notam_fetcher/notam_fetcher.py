import requests
from typing import TypedDict, Any

class NotamResponseDict(TypedDict):
    pageSize: int
    pageNum: int
    totalCount: int
    totalPages: int
    items: list[dict[str, Any]]

class NotamFetcher:
    DOMAIN = "https://external-api.faa.gov/notamapi/v1/notams"

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self._pageSize = 50

    def fetchNotamsByLatLong(self, lat: float, long: float, radius: float = 100.0):
        """
        Fetches ALL notams for a particular latitude and longitude.

        Args:
            lat (float): The latitude to fetch NOTAMs from
            long (float): The longitude to fetch NOTAMs from
            radius (float): The location radius criteria. (max:100)
        
        Raises:
            requests.exceptions.RequestException: If the any of the API request fails
            requests.exceptions.ConnectionError: If there's a network connectivity issue in any request
            json.JSONDecodeError: If any response returns invalid JSON
        Returns:
            Notams (List[Notam]): A list of NOTAMs
        """

        
        notamItems: list[dict[str, Any]] = []

        first_page = self._fetchNotamsByLatLong(lat, long, radius, 1, self._pageSize)
        totalPages = first_page['totalPages']

        notamItems.extend(first_page['items'])

        for i in range(2, totalPages+1):
            nextPage = self._fetchNotamsByLatLong(lat, long, radius, i, self._pageSize)
            notamItems.extend(nextPage['items'])


        return notamItems
    
    def _fetchNotamsByLatLong(self, lat: float, long: float, radius: float, pageNum: int , pageSize: int=1000) -> NotamResponseDict:
        """
        Fetches a response from the API using latitude and longitude.

        Args:
            lat (float): The latitude to fetch NOTAMs from
            long (float): The longitude to fetch NOTAMs from
            radius (float): The location radius criteria. (max:100)
            pageNum (int): The page number of the response (min: 1)
            pageSize (int): The number of NOTAMs per page (max: 1000)

        Returns:
            dict: JSON response containing NOTAM data

        Raises:
            requests.exceptions.RequestException: If the API request fails
            requests.exceptions.ConnectionError: If there's a network connectivity issue
            json.JSONDecodeError: If the response is not valid JSON
        """

        querystring = {
            "locationLongitude": str(long),
            "locationLatitude": str(lat),
            "locationRadius": str(radius),
            "pageNum": str(pageNum),
            "pageSize": str(pageSize)
        }

        response = requests.get(
            self.DOMAIN,
            headers={"client_id": self.client_id, "client_secret": self.client_secret},
            params=querystring,
        )

        return response.json()