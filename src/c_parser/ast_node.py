from shared.token.token_name_enum import TokenNameEnum


class ASTNode:
    pass


class NumberNode(ASTNode):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"NumberNode({self.value})"


class StringNode(ASTNode):
    def __init__(self, value: str):
        self.value = value

    def __str__(self):
        return f"StringNode({self.value})"


class PrintNode(ASTNode):
    def __init__(self, identifier: str):
        self.identifier = identifier

    def __str__(self):
        return f"PrintNode({self.identifier})"


class AssignNode(ASTNode):
    def __init__(self, identifier: str, value: ASTNode):
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"AssignNode({self.identifier}, {self.value})"


class DeclareNode(ASTNode):
    def __init__(
        self,
        data_type: TokenNameEnum,
        identifier: str,
        value: ASTNode | None = None,
    ):
        self.data_type = data_type
        self.identifier = identifier
        self.value = value

    def __str__(self):
        return f"DeclareNode({self.data_type}, {self.identifier}, {self.value})"
