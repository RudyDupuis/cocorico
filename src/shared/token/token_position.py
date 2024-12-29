class TokenPosition:
    def __init__(self, line: int, position_on_line: int):
        self.line = line
        self.position_on_line = position_on_line

    def __str__(self):
        return f"(Ligne {self.line}, Position {self.position_on_line})"
