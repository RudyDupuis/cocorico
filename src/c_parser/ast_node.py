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
    def __init__(self, identifier: str, type_node: ASTNode):
        self.identifier = identifier
        self.type_node = type_node

    def __str__(self):
        return f"AssignNode({self.identifier}, {self.type_node})"
