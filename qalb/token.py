from enum import Enum


class TokenType(Enum):
    NONE = 0
    # --start constants--
    ENDMARKER = 0
    NAME = 1
    NUMBER = 2
    STRING = 3
    NEWLINE = 4
    INDENT = 5
    DEDENT = 6
    LPAR = 7
    RPAR = 8
    LSQB = 9
    RSQB = 10
    COLON = 11
    COMMA = 12
    SEMI = 13
    PLUS = 14
    MINUS = 15
    STAR = 16
    SLASH = 17
    VBAR = 18
    AMPER = 19
    LESS = 20
    GREATER = 21
    EQUAL = 22
    DOT = 23
    PERCENT = 24
    LBRACE = 25
    RBRACE = 26
    EQEQUAL = 27
    NOTEQUAL = 28
    LESSEQUAL = 29
    GREATEREQUAL = 30
    TILDE = 31
    CIRCUMFLEX = 32
    LEFTSHIFT = 33
    RIGHTSHIFT = 34
    DOUBLESTAR = 35
    PLUSEQUAL = 36
    MINEQUAL = 37
    STAREQUAL = 38
    SLASHEQUAL = 39
    PERCENTEQUAL = 40
    AMPEREQUAL = 41
    VBAREQUAL = 42
    CIRCUMFLEXEQUAL = 43
    LEFTSHIFTEQUAL = 44
    RIGHTSHIFTEQUAL = 45
    DOUBLESTAREQUAL = 46
    DOUBLESLASH = 47
    DOUBLESLASHEQUAL = 48
    AT = 49
    ATEQUAL = 50
    RARROW = 51
    ELLIPSIS = 52
    # Don't forget to update the table _PyParser_TokenNames in tokenizer.c!
    OP = 53
    ERRORTOKEN = 54
    # These aren't used by the C tokenizer but are needed for tokenize.py
    COMMENT = 55
    NL = 56
    ENCODING = 57
    N_TOKENS = 58
    # Special definitions for cooperation with parser
    NT_OFFSET = 256
    # --end constants--


EXACT_TOKEN_TYPES = {
    '(':   TokenType.LPAR,
    ')':   TokenType.RPAR,
    '[':   TokenType.LSQB,
    ']':   TokenType.RSQB,
    ':':   TokenType.COLON,
    ',':   TokenType.COMMA,
    ';':   TokenType.SEMI,
    '+':   TokenType.PLUS,
    '-':   TokenType.TokenType.MINUS,
    '*':   TokenType.STAR,
    '/':   TokenType.SLASH,
    '|':   TokenType.VBAR,
    '&':   TokenType.AMPER,
    '<':   TokenType.LESS,
    '>':   TokenType.GREATER,
    '=':   TokenType.EQUAL,
    '.':   TokenType.DOT,
    '%':   TokenType.PERCENT,
    '{':   TokenType.LBRACE,
    '}':   TokenType.RBRACE,
    '==':  TokenType.EQEQUAL,
    '!=':  TokenType.NOTEQUAL,
    '<=':  TokenType.LESSEQUAL,
    '>=':  TokenType.GREATEREQUAL,
    '~':   TokenType.TILDE,
    '^':   TokenType.CIRCUMFLEX,
    '<<':  TokenType.LEFTSHIFT,
    '>>':  TokenType.RIGHTSHIFT,
    '**':  TokenType.DOUBLESTAR,
    '+=':  TokenType.PLUSEQUAL,
    '-=':  TokenType.MINEQUAL,
    '*=':  TokenType.STAREQUAL,
    '/=':  TokenType.SLASHEQUAL,
    '%=':  TokenType.PERCENTEQUAL,
    '&=':  TokenType.AMPEREQUAL,
    '|=':  TokenType.VBAREQUAL,
    '^=':  TokenType.CIRCUMFLEXEQUAL,
    '<<=': TokenType.LEFTSHIFTEQUAL,
    '>>=': TokenType.RIGHTSHIFTEQUAL,
    '**=': TokenType.DOUBLESTAREQUAL,
    '//':  TokenType.DOUBLESLASH,
    '//=': TokenType.DOUBLESLASHEQUAL,
    '...': TokenType.ELLIPSIS,
    '->':  TokenType.RARROW,
    '@':   TokenType.AT,
    '@=':  TokenType.ATEQUAL,
}


class Token:
    text: str
    type: TokenType
    prev: any
    next: any

