
from pytest import MonkeyPatch
import pytest
from notam_fetcher.notam_fetcher import NotamFetcher, NotamResponseDict




@pytest.fixture
def mock_empty_response(monkeypatch: MonkeyPatch):

    def returnEmpty(self: NotamFetcher, lat: float, long: float, radius: float, pageNum: int , pageSize: int=1000) -> NotamResponseDict:
        return {
                "pageSize": 50,
                "pageNum": 1,
                "totalCount": 0,
                "totalPages": 0,
                "items": []
        }
    
    monkeypatch.setattr(NotamFetcher, "_fetchNotamsByLatLong", returnEmpty)

def test_fetchNotamsByLatLong_no_notams(mock_empty_response: None):
    notam_fetcher = NotamFetcher("CLIENT_ID", "CLIENT_SECRET")
    notams = notam_fetcher.fetchNotamsByLatLong(32, 32, 10)
    assert(len(notams) == 0)