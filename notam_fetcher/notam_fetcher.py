import requests
from typing import TypedDict, Any

class NotamResponseDict(TypedDict):
    pageSize: int
    pageNum: int
    totalCount: int
    totalPages: int
    items: list[dict[str, Any]]

class NotamFetcherException(Exception):
    """Base exception for NotamFetcher errors."""

class NotamFetcherUnexpectedError(NotamFetcherException):
    """Raised when an unexpected error occurs"""

class NotamFetcherRequestError(NotamFetcherException):
    """Raised when NotamFetcher receives a request exception while fetching from the API"""

class NotamFetcherUnauthenticated(NotamFetcherException):
    """Raised when cliend_id or client_secret are invalid"""


class NotamFetcher:
    DOMAIN = "https://external-api.faa.gov/notamapi/v1/notams"

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self._pageSize = 50

    def fetchNotamsByAirportcode(self, airportCode: str):
        """
        Fetches ALL notams for a particular latitude and longitude.

        Args:
            airportCode (str): A valid airport code.
        
        Raises:
            NotamFetcherRequestError: If a request error occurs while fetching from the API.
            NotamFetcherUnexpectedError: If an unexpected error occurs.
        Returns:
            Notams (List[dict[str, Any]]): A list of NOTAM dicts
        """
        notamItems: list[dict[str, Any]] = []

        first_page = self._fetchNotamsByAirportCode(airportCode, 1, self._pageSize)
        totalPages = first_page['totalPages']

        notamItems.extend(first_page['items'])

        for i in range(2, totalPages+1):
            nextPage = self._fetchNotamsByAirportCode(airportCode, i, self._pageSize)
            notamItems.extend(nextPage['items'])
        return notamItems
    
    def fetchNotamsByLatLong(self, lat: float, long: float, radius: float = 100.0):
        """
        Fetches ALL notams for a particular latitude and longitude.

        Args:
            lat (float): The latitude to fetch NOTAMs from
            long (float): The longitude to fetch NOTAMs from
            radius (float): The location radius criteria. (max:100)
        
        Raises:
            NotamFetcherRequestError: If a request error occurs while fetching from the API.
            NotamFetcherUnexpectedError: If an unexpected error occurs.
        Returns:
            Notams (List[dict[str, Any]]): A list of NOTAM dicts
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
            NotamFetcherRequestError: If a request error occurs while fetching from the API.
            NotamFetcherUnexpectedError: If an unexpected error occurs.
        """

        querystring = {
            "locationLongitude": str(long),
            "locationLatitude": str(lat),
            "locationRadius": str(radius),
            "pageNum": str(pageNum),
            "pageSize": str(pageSize)
        }

        try:
            response = requests.get(
                self.DOMAIN,
                headers={"client_id": self.client_id, "client_secret": self.client_secret},
                params=querystring,
            )

        except requests.exceptions.RequestException as e:
            raise NotamFetcherRequestError from e

        try: 
            data = response.json()
            if data.get("error", "") == "Invalid client id or secret":
                raise(NotamFetcherUnauthenticated("Invalid client id or secret"))
            
            return data
        except requests.exceptions.JSONDecodeError:
            raise(NotamFetcherUnexpectedError(f"Response from API unexpectedly not JSON. Received text: {response.text} "))


    def _fetchNotamsByAirportCode(self, airportCode: str, pageNum: int , pageSize: int=1000) -> NotamResponseDict:
        """
        Fetches a response from the API using latitude and longitude.

        Args:
            airportCode (str): A valid airport code.
            pageNum (int): The page number of the response (min: 1)
            pageSize (int): The number of NOTAMs per page (max: 1000)

        Returns:
            dict: JSON response containing NOTAM data

        Raises:
            NotamFetcherRequestError: If a request error occurs while fetching from the API.
            NotamFetcherUnexpectedError: If an unexpected error occurs.
        """

        querystring = {
            "domesticLocation": str(airportCode),
            "pageNum": str(pageNum),
            "pageSize": str(pageSize)
        }

        try:
            response = requests.get(
                self.DOMAIN,
                headers={"client_id": self.client_id, "client_secret": self.client_secret},
                params=querystring,
            )

        except requests.exceptions.RequestException as e:
            raise NotamFetcherRequestError from e

        try: 
            data = response.json()
            if data.get("error", "") == "Invalid client id or secret":
                raise(NotamFetcherUnauthenticated("Invalid client id or secret"))
            
            return data
        except requests.exceptions.JSONDecodeError:
            raise(NotamFetcherUnexpectedError(f"Response from API unexpectedly not JSON. Received text: {response.text} "))
