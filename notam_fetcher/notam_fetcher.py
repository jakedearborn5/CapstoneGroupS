import requests
from datetime import datetime


from typing import Literal, Any, Optional
from pydantic import BaseModel, Field

from .exceptions import NotamFetcherRequestError, NotamFetcherUnauthenticated, NotamFetcherUnexpectedError



class NotamTranslationObject(BaseModel):
    pass

class LocalFormatTranslationObject(NotamTranslationObject):
    type: Literal["LOCAL_FORMAT"]
    simpleText: str

class ICAOTranslationObject(NotamTranslationObject):
    type: Literal["ICAO"]
    formattedText: str    

    
class Notam(BaseModel):
    id: str
    number: str
    type: str
    issued: datetime
    selectionCode: Optional[str] = Field(default=None)
    location: str
    effectiveStart: datetime
    effectiveEnd: datetime | str
    text: str
    classification: str
    accountId: str
    lastUpdated: datetime
    icaoLocation: str

class NotamEvent(BaseModel):
    scenario: str

class CoreNotamData(BaseModel):
    notamEvent: NotamEvent
    notam: Notam
    notamTranslation: list[ICAOTranslationObject| LocalFormatTranslationObject]

class NotamApiItemProperties(BaseModel):
    coreNOTAMData: CoreNotamData


class ResponseItem(BaseModel):
    pass

class OtherResponseItem(ResponseItem):
    type: str
    properties: dict[str, Any]
    geometry: dict[str, Any] 
    
class NotamApiItem(ResponseItem):
    type: Literal["Feature"]
    properties: NotamApiItemProperties
    geometry: dict[str, Any] 


class NotamAPIResponse(BaseModel):
    pageSize: int
    pageNum: int
    totalCount: int
    totalPages: int
    items: list[NotamApiItem | OtherResponseItem]


class NotamFetcher:
    DOMAIN = "https://external-api.faa.gov/notamapi/v1/notams"

    def __init__(self, client_id: str, client_secret: str):
        self.client_id = client_id
        self.client_secret = client_secret
        self._pageSize = 1000

    def fetchNotamsByAirportcode(self, airportCode: str):
        """
        Fetches ALL notams for a particular latitude and longitude.

        Args:
            airportCode (str): A valid airport code.
        
        Raises:
            NotamFetcherRequestError: If a request error occurs while fetching from the API.
            NotamFetcherUnexpectedError: If an unexpected error occurs.
        Returns:
            Notams (List[Notam]): A list of NOTAMs
        """
        notamItems: list[Notam]= []

        first_page = self._fetchNotamsByAirportCode(airportCode, 1, self._pageSize)

        notamItems.extend([item.properties.coreNOTAMData.notam for item in first_page.items if isinstance(item, NotamApiItem)])

        for i in range(2, first_page.totalPages+1):
            nextPage = self._fetchNotamsByAirportCode(airportCode, i, self._pageSize)
            notamItems.extend([item.properties.coreNOTAMData.notam for item in nextPage.items if isinstance(item, NotamApiItem)])
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
            Notams (List[Notam]): A list of NOTAMs
        """
        notamItems: list[Notam] = []

        first_page = self._fetchNotamsByLatLong(lat, long, radius, 1, self._pageSize)

        notamItems.extend([item.properties.coreNOTAMData.notam for item in first_page.items if isinstance(item, NotamApiItem)])

        for i in range(2, first_page.totalPages+1):
            nextPage = self._fetchNotamsByLatLong(lat, long, radius, i, self._pageSize)
            notamItems.extend([item.properties.coreNOTAMData.notam for item in nextPage.items if isinstance(item, NotamApiItem)])


        return notamItems
    
    def _fetchNotamsByLatLong(self, lat: float, long: float, radius: float, pageNum: int , pageSize: int=1000) -> NotamAPIResponse:
        """
        Fetches a response from the API using latitude and longitude.

        Args:
            lat (float): The latitude to fetch NOTAMs from
            long (float): The longitude to fetch NOTAMs from
            radius (float): The location radius criteria. (max:100)
            pageNum (int): The page number of the response (min: 1)
            pageSize (int): The number of NOTAMs per page (max: 1000)

        Returns:
            NotamAPIResponse: A Notam API Response

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
            
            valid_response = NotamAPIResponse.model_validate(data)
            return valid_response
        except requests.exceptions.JSONDecodeError:
            raise(NotamFetcherUnexpectedError(f"Response from API unexpectedly not JSON. Received text: {response.text} "))


    def _fetchNotamsByAirportCode(self, airportCode: str, pageNum: int , pageSize: int=1000) -> NotamAPIResponse:
        """
        Fetches a response from the API using latitude and longitude.

        Args:
            airportCode (str): A valid airport code.
            pageNum (int): The page number of the response (min: 1)
            pageSize (int): The number of NOTAMs per page (max: 1000)

        Returns:
            NotamAPIResponse: A Notam API Response

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
            
            
            return NotamAPIResponse.model_validate(data)
        except requests.exceptions.JSONDecodeError:
            raise(NotamFetcherUnexpectedError(f"Response from API unexpectedly not JSON. Received text: {response.text} "))
