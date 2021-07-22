import enum


class TokenType(enum.Enum):
    Invalid = -1
    Eol = 1
    Var = 2
    Eq = 3
    Print = 4
    Open = 5
    Close = 6
    Sum = 7
    Sub = 8
    Mult = 9
    Div = 10
    Int = 11
    Float = 12


class Token:
    def __init__(self, type_t, attribute_t=None):
        self.type = type_t
        self.attribute = attribute_t
