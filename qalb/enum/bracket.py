from enum import Enum


class Bracket(Enum):
    NONE = 0
    IS_ROUND = 1
    IS_CURLY = 2
    IS_SQUARE = 3
