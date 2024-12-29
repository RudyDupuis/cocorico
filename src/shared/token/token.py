from shared.token.token_name_enum import TokenNameEnum
from shared.token.token_position import TokenPosition


class Token:
    def __init__(self, name: TokenNameEnum, value: str, position: TokenPosition):
        self.name = name
        self.value = value
        self.position = position

    def __str__(self):
        return f"({self.name}, '{self.value}', {self.position})"
