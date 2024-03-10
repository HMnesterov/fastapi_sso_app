from enum import Enum, StrEnum


class TokenType(StrEnum):
    access = "access"
    refresh = "refresh"
    undefined = "undefined"
