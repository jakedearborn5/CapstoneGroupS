from typing import Any
class NotamFetcherException(Exception):
    """Base exception for NotamFetcher errors."""

class NotamFetcherUnexpectedError(NotamFetcherException):
    """Raised when an unexpected error occurs"""

class NotamFetcherRequestError(NotamFetcherException):
    """Raised when NotamFetcher receives a request exception while fetching from the API"""

class NotamFetcherUnauthenticated(NotamFetcherException):
    """Raised when cliend_id or client_secret are invalid"""


class NotamFetcherValidationError(NotamFetcherException):
    """Raised when Pydantic could not validate the response of the API"""
    invalid_object : Any
    def __init__(self, message: str, obj: Any):
        super().__init__(message)
        self.invalid_object = obj
