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
  "زائف": Identifier.FALSE,
  "لااحد": Identifier.NONE,
  "صحيح": Identifier.TRUE,
  "و": Identifier.AND,
  "مثل": Identifier.AS,
  "أكد": Identifier.ASSERT,
  "كسر": Identifier.BREAK,
  "صنف": Identifier.CLASS,
  "استمر": Identifier.CONTINUE,
  "وظيفة": Identifier.FUNCTION,
  "حذف": Identifier.DELETE,
  "ولو": Identifier.ELSE_IF,
  "آخر": Identifier.ELSE,
  "إلا": Identifier.EXCEPT,
  "أخيرا": Identifier.FINALLY,
  "لأن": Identifier.FOR,
  "من": Identifier.FROM,
  "عالمي": Identifier.GLOBAL,
  "لو": Identifier.IF,
  "استيراد": Identifier.IMPORT,
  "في": Identifier.IN,
  "يساوي": Identifier.IS,
  "امدا": Identifier.LAMBDA,
  "غيرمحلي": Identifier.NONLOCAL,
  "لا": Identifier.NOT,
  "أو": Identifier.OR,
  "مرر": Identifier.PASS,
  "رفع": Identifier.RAISE,
  "إرجاع": Identifier.RAISE,
  "حاول": Identifier.TRY,
  "بينما": Identifier.WHILE,
  "مع": Identifier.WITH,
  "محصول": Identifier.YIELD,
  "منطقية": Identifier.LOGIC,
  "عدد": Identifier.NUMBER,
  "عشري": Identifier.DELETE,
  "خيط": Identifier.STRING
}