from io import TextIOWrapper
from shared.token.token_name_enum import TokenNameEnum
from shared.token.token_position import TokenPosition
from shared.token.token import Token
from c_lexer.token_regex_library import TokenRegexLibrary


class Lexer:
    def __init__(self, file: TextIOWrapper):
        self.file = file.read()
        self.line = 0
        self.position_on_file = 0
        self.position_on_line = 0
        self.token_library = TokenRegexLibrary()
        self.lexer_tokens: list[Token] = []
        self.tokenize()

    def _find_match(self):
        for token_regex in self.token_library.get_token_regexs():
            match = token_regex.regex.match(self.file, self.position_on_file)
            if match:
                return token_regex.token_name, match.group(0)
        return None

    def _update_positions(self, token_value: str, token: TokenNameEnum):
        self.position_on_file += len(token_value)
        self.position_on_line += len(token_value)

        if token == TokenNameEnum.EOL:
            self.line += 1
            self.position_on_line = 0

    def tokenize(self):
        while self.position_on_file < len(self.file):
            match = self._find_match()

            if match:
                token, token_value = match
                if token not in self.token_library.get_hidden_token_regexs():
                    self.lexer_tokens.append(
                        Token(
                            token,
                            token_value,
                            TokenPosition(self.line + 1, self.position_on_line + 1),
                        )
                    )

                self._update_positions(token_value, token)
            else:
                raise SyntaxError(
                    f"{TokenPosition(self.line + 1, self.position_on_line + 1)}: Caractère inattendu '{self.file[self.position_on_file]}'."
                )

        self.lexer_tokens.append(
            Token(
                TokenNameEnum.EOF,
                "",
                TokenPosition(self.line + 1, self.position_on_line + 1),
            )
        )

    def get_lexer_tokens(self):
        return self.lexer_tokens
