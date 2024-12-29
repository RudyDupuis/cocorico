from enum import Enum


class TokenNameEnum(Enum):
    NUMBER = "NUMBER"
    STRING = "STRING"
    PRINT = "PRINT"
    IDENTIFIER = "IDENTIFIER"
    NUMBER_LITERAL = "NUMBER_LITERAL"
    STRING_LITERAL = "STRING_LITERAL"
    EQUALS = "EQUALS"
    LEFT_PAREN = "LEFT_PAREN"
    RIGHT_PAREN = "RIGHT_PAREN"
    COMMA = "COMMA"
    EOL = "EOL"
    COMMENT = "COMMENT"
    WHITESPACE = "WHITESPACE"
    EOF = "EOF"

    def __str__(self):
        return self.value
