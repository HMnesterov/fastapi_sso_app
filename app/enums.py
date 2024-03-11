from enum import Enum, StrEnum


class TokenType(StrEnum):
    ACCESS = "A"
    REFRESH = "R"
    UNDEFINED = "U"
