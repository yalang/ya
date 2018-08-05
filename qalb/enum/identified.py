from enum import Enum


class Identified(Enum):
    AS_NONE = 0
    AS_IF = 1
    AS_ELSE = 2
    AS_ELSE_IF = 3
    AS_FOR = 4
    AS_WHILE = 5
    AS_DELETE = 6
    AS_FUNCTION = 7
    AS_CLASS = 8
    AS_IMPORT = 9
    AS_FROM = 10
    AS_GLOBAL = 11
    AS_ASSERT = 12
    AS_TRY = 13
    AS_EXCEPT = 15
    AS_FINALLY = 16
    AS_RAISE = 17
    AS_RETURN = 18
    AS_WITH = 19
    AS_YIELD = 20
    AS_BOOL = 21
    AS_INT = 22
    AS_FLOAT = 23
    AS_STRING = 24