from enum import Enum


class TokenError(Enum):
    INCOMPLETE_STRING = "INCOMPLETE_STRING هناك مشكلة"
    INVALID_TOKEN = "هناك مشكلة INVALID_TOKEN"
    DEFAULT = "هناك مشكلة DEFAULT"
