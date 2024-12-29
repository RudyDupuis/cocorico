import re
from shared.token.token_name_enum import TokenNameEnum


class TokenRegex:
    def __init__(self, token_name: TokenNameEnum, regex: str):
        self.token_name = token_name
        self.regex = re.compile(regex)
