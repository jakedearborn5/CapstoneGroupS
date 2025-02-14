
from pytest import MonkeyPatch
import pytest
from notam_fetcher.notam_fetcher import NotamFetcher, NotamResponseDict

from typing import Any


@pytest.fixture
def mock_empty_response(monkeypatch: MonkeyPatch):

    def returnEmpty(*args: Any) -> NotamResponseDict:
        return {
                "pageSize": 50,
                "pageNum": 1,
                "totalCount": 0,
                "totalPages": 0,
                "items": []
        }
    
    monkeypatch.setattr(NotamFetcher, "_fetchNotamsByLatLong", returnEmpty)
    monkeypatch.setattr(NotamFetcher, "_fetchNotamsByAirportCode", returnEmpty)

def test_fetchNotamsByLatLong_no_notams(mock_empty_response: None):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByLatLong(32, 32, 10)
    assert(len(notams) == 0)

def test_fetchNotamsByAirportCode_no_notams(mock_empty_response: None):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByAirportcode("LAX")
    assert(len(notams) == 0)