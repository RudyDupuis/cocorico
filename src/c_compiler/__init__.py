from c_parser.ast_node import *
from shared.token.token_position import TokenPosition


class Compiler:
    def __init__(self, ast: list[ASTNode]):
        self.ast = ast
        self.data_section: list[str] = []
        self.text_section: list[str] = []
        self.counter = 0
        self.identifier_counter: dict[str, int] = (
            {}
        )  # Make a object with the identifier, the counter and the type

    def compile(self):
        self.text_section.append("section .text")
        self.text_section.append("global _start")
        self.text_section.append("_start:")

        self.data_section.append("newline db 0x0A")

        for node in self.ast:
            self.visit(node)

        self.text_section.append("mov rax, 60")
        self.text_section.append("xor rdi, rdi")
        self.text_section.append("syscall")

        data = "\n".join(self.data_section)
        text = "\n".join(self.text_section)
        return f"{text}\n\nsection .data\n{data}"

    def visit(self, node: ASTNode):
        from c_compiler.visiting_method.visit_print import visit_print
        from c_compiler.visiting_method.visit_assign import visit_assign

        if isinstance(node, DeclareNode):
            if node.identifier in self.identifier_counter:
                raise SyntaxError(
                    f"{node.position} : La variable '{node.identifier}' est déjà definie."
                )

            self.identifier_counter[node.identifier] = -1
            self.data_section.append(f"{node.identifier} dq 0")

            if node.value is not None:
                visit_assign(self, node)

        if isinstance(node, AssignNode):
            visit_assign(self, node)

        if isinstance(node, PrintNode):
            visit_print(self, node)

    def get_identifier_counter(
        self, identifier: str, identifier_position: TokenPosition
    ):
        if identifier in self.identifier_counter:
            return self.identifier_counter[identifier]
        raise SyntaxError(
            f"{identifier_position} : La variable '{identifier}' n'est pas déclarée."
        )
