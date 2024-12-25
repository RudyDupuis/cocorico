import re
from lexer.token_types import TOKEN_TYPES


class Lexer:
    def __init__(self, text: str, line_index: int):
        self.text = text
        self.line_index = line_index
        self.position = 0
        self.tokens: list[tuple[str, str]] = []
        self.tokenize()

    def tokenize(self):
        while self.position < len(self.text):
            match = None
            for token_type, pattern in TOKEN_TYPES:
                regex = re.compile(pattern)
                match = regex.match(self.text, self.position)
                if match:
                    if token_type != "WHITESPACE":
                        token = (token_type, match.group(0))
                        self.tokens.append(token)
                    self.position = match.end(0)
                    break
            if not match:
                raise SyntaxError(
                    f"(Ligne {self.line_index}, Position {self.position + 1}) : Caractère {self.text[self.position]} inattendu."
                )
        self.tokens.append(("EOF", ""))

    def get_tokens(self):
        return self.tokens
