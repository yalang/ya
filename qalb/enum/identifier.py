from enum import Enum


class Identifier(Enum):
    FALSE = 0
    TRUE = 1
    NONE = 2
    AND = 3
    AS = 4
    ASSERT = 5
    BREAK = 6
    CLASS = 7
    CONTINUE = 8
    DELETE = 9
    ELSE_IF = 10
    ELSE = 11
    EXCEPT = 12
    FINALLY = 13
    FUNCTION = 14
    FOR = 15
    FROM = 16
    GLOBAL = 17
    IF = 18
    IMPORT = 19
    IN = 20
    IS = 21
    LAMBDA = 22
    NONLOCAL = 23
    NOT = 24
    OR = 25
    PASS = 26
    RAISE = 27
    RETURN = 28
    TRY = 29
    WHILE = 30
    WITH = 31
    YIELD = 32
    LOGIC = 33
    NUMBER = 34
    DECIMAL = 35
    STRING = 36
    OPERATOR = 37


EXACT_IDENTIFIER_TYPES = {
  "زائف": "False",
  "لااحد": "None",
  "صحيح": "True",
  "و": "and",
  "مثل": "as",
  "أكد": "assert",
  "كسر": "break",
  "صنف": "class",
  "استمر": "continue",
  "وظيفة": "def",
  "حذف": "del",
  "ولو": "elif",
  "آخر": "else",
  "إلا": "except",
  "أخيرا": "finally",
  "لأن": "for",
  "من": "from",
  "عالمي": "global",
  "لو": "if",
  "استيراد": "import",
  "في": "in",
  "يساوي": "is",
  "امدا": "lambda",
  "غيرمحلي": "nonlocal",
  "لا": "not",
  "أو": "or",
  "مرر": "pass",
  "رفع": "raise",
  "إرجاع": "return",
  "حاول": "try",
  "بينما": "while",
  "مع": "with",
  "محصول": "yield",
  "منطقية": "bool",
  "عدد": "int",
  "عشري": "float",
  "خيط": "string"
}