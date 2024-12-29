from shared.token.token_name_enum import TokenNameEnum
from c_lexer.token_regex import TokenRegex


class TokenRegexLibrary:
    def __init__(self):
        self.hidden_tokens_regex: list[TokenNameEnum] = [
            TokenNameEnum.WHITESPACE,
            TokenNameEnum.COMMENT,
        ]
        self.tokens_regex: list[TokenRegex] = [
            TokenRegex(TokenNameEnum.NUMBER, r"nombre"),
            TokenRegex(TokenNameEnum.STRING, r"texte"),
            TokenRegex(TokenNameEnum.PRINT, r"afficher"),
            TokenRegex(
                TokenNameEnum.IDENTIFIER,
                r"[a-zA-Z\u00C0-\u00FF_][a-zA-Z0-9\u00C0-\u00FF_]*",
            ),
            TokenRegex(TokenNameEnum.NUMBER_LITERAL, r"\d+"),
            TokenRegex(TokenNameEnum.STRING_LITERAL, r'"[^"]*"'),
            TokenRegex(TokenNameEnum.EQUALS, r"="),
            TokenRegex(TokenNameEnum.LEFT_PAREN, r"\("),
            TokenRegex(TokenNameEnum.RIGHT_PAREN, r"\)"),
            TokenRegex(TokenNameEnum.COMMA, r","),
            TokenRegex(TokenNameEnum.EOL, r"\n"),
            TokenRegex(TokenNameEnum.WHITESPACE, r"\s+"),
            TokenRegex(TokenNameEnum.COMMENT, r"#.*"),
        ]

    def get_hidden_token_regexs(self):
        return self.hidden_tokens_regex

    def get_token_regexs(self):
        return self.tokens_regex
