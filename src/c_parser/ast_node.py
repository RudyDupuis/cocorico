from shared.token.token_position import TokenPosition
from shared.token.token_name_enum import TokenNameEnum


class ASTNode:
    def __init__(self, token_position: TokenPosition):
        self.position = token_position


class NumberNode(ASTNode):
    def __init__(self, value: str, token_position: TokenPosition):
        super().__init__(token_position)
        self.value = value

    def __str__(self):
        return f"NumberNode({self.value})"


class StringNode(ASTNode):
    def __init__(self, value: str, token_position: TokenPosition):
        super().__init__(token_position)
        self.value = value

    def __str__(self):
        return f"StringNode({self.value})"


class PrintNode(ASTNode):
    def __init__(self, identifier: str, token_position: TokenPosition):
        super().__init__(token_position)
        self.identifier = identifier

    def __str__(self):
        return f"PrintNode({self.identifier})"


class AssignNode(ASTNode):
    def __init__(self, identifier: str, value: ASTNode, token_position: TokenPosition):
        super().__init__(token_position)
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"AssignNode({self.identifier}, {self.value})"


class DeclareNode(ASTNode):
    def __init__(
        self,
        data_type: TokenNameEnum,
        identifier: str,
        token_position: TokenPosition,
        value: ASTNode | None = None,
    ):
        super().__init__(token_position)
        self.data_type = data_type
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"DeclareNode({self.data_type}, {self.identifier}, {self.value})"
