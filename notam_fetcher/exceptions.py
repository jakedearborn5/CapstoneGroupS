class NotamFetcherException(Exception):
    """Base exception for NotamFetcher errors."""

class NotamFetcherUnexpectedError(NotamFetcherException):
    """Raised when an unexpected error occurs"""

class NotamFetcherRequestError(NotamFetcherException):
    """Raised when NotamFetcher receives a request exception while fetching from the API"""

class NotamFetcherUnauthenticated(NotamFetcherException):
    """Raised when cliend_id or client_secret are invalid"""

