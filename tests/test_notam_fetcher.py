from pytest import MonkeyPatch
import pytest
import requests
from notam_fetcher.notam_fetcher import NotamFetcher

from typing import Any


class MockResponse:
    def __init__(self, response: dict[str, Any]):
        self.response = response

    def json(self) -> dict[str, Any]:
        return self.response


@pytest.fixture
def mock_one_unexpected_response(monkeypatch: MonkeyPatch):
    def returnUnexpected(*args: Any, **kwargs: Any) -> MockResponse:
        return MockResponse(
            {
                "pageSize": 50,
                "pageNum": 1,
                "totalCount": 2,
                "totalPages": 1,
                "items": [
                    {
                        "type": "Feature",
                        "properties": {
                            "coreNOTAMData": {
                                "notamEvent": {"scenario": "6000"},
                                "notam": {
                                    "id": "NOTAM_1_73849637",
                                    "series": "A",
                                    "number": "A2157/24",
                                    "type": "N",
                                    "issued": "2024-10-02T19:54:00.000Z",
                                    "affectedFIR": "KZJX",
                                    "selectionCode": "QCBLS",
                                    "minimumFL": "000",
                                    "maximumFL": "040",
                                    "location": "ZJX",
                                    "effectiveStart": "2024-10-02T19:50:00.000Z",
                                    "effectiveEnd": "2024-10-14T22:00:00.000Z",
                                    "text": "ZJX AIRSPACE ADS-B, AUTO DEPENDENT SURVEILLANCE\nREBROADCAST (ADS-R), TFC INFO SER BCST (TIS-B), FLT INFO SER\nBCST (FIS-B) SER MAY NOT BE AVBL WI AN AREA DEFINED AS 49NM\nRADIUS OF 322403N0781209W.",
                                    "classification": "INTL",
                                    "accountId": "KZJX",
                                    "lastUpdated": "2024-10-02T19:54:00.000Z",
                                    "icaoLocation": "KZJX",
                                    "lowerLimit": "SFC",
                                    "upperLimit": "3999FT.",
                                },
                                "notamTranslation": [
                                    {
                                        "type": "ICAO",
                                        "formattedText": "A2157/24 NOTAMN\nQ) KZJX/QCBLS////000/040/\nA) KZJX\nB) 2410021950\nC) 2410142200 EST\nE) ZJX AIRSPACE ADS-B, AUTO DEPENDENT SURVEILLANCE\nREBROADCAST (ADS-R), TFC INFO SER BCST (TIS-B), FLT INFO SER\nBCST (FIS-B) SER MAY NOT BE AVBL WI AN AREA DEFINED AS 49NM\nRADIUS OF 322403N0781209W.\nF) SFC   G) 3999FT.",
                                    }
                                ],
                            }
                        },
                        "geometry": {"type": "GeometryCollection"},
                    },
                    {
                        "type": "Point",
                        "geometry": {"type": "Point", "coordinates": [0]},
                        "properties": {"name": "Dinagat Islands"},
                    },
                ],
            }
        )

    monkeypatch.setattr(requests, "get", returnUnexpected)


@pytest.fixture
def mock_unexpected_response(monkeypatch: MonkeyPatch):
    def returnUnexpected(*args: Any, **kwargs: Any) -> MockResponse:
        return MockResponse(
            {
                "pageSize": 10,
                "pageNum": 3,
                "totalCount": 124,
                "totalPages": 13,
                "items": [
                    {
                        "type": "Point",
                        "geometry": {"type": "Point", "coordinates": [0]},
                        "properties": {"name": "Dinagat Islands"},
                    }
                ],
            }
        )

    monkeypatch.setattr(requests, "get", returnUnexpected)


@pytest.fixture
def mock_empty_response(monkeypatch: MonkeyPatch):
    def returnEmpty(*args: Any, **kwargs: Any) -> MockResponse:
        return MockResponse(
            {
                "pageSize": 50,
                "pageNum": 1,
                "totalCount": 0,
                "totalPages": 0,
                "items": [],
            }
        )

    monkeypatch.setattr(requests, "get", returnEmpty)


def test_fetchNotamsByLatLong_one_unexpected_response(
    mock_one_unexpected_response: None,
):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByLatLong(32, 32, 10)
    assert len(notams) == 1
    assert (notams[0].id=="NOTAM_1_73849637")


def test_fetchNotamsByLatLong_unexpected_response(mock_unexpected_response: None):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByLatLong(32, 32, 10)
    assert len(notams) == 0


def test_fetchNotamsByLatLong_no_notams(mock_empty_response: None):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByLatLong(32, 32, 10)
    assert len(notams) == 0


def test_fetchNotamsByAirportCode_no_notams(mock_empty_response: None):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByAirportcode("LAX")
    assert len(notams) == 0
