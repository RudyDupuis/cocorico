from c_parser.ast_node import *


class Compiler:
    def __init__(self, ast: list[ASTNode]):
        self.ast = ast
        self.data_section: list[str] = []
        self.text_section: list[str] = []
        self.counter = 0
        self.identifier_counter: dict[str, int] = {}

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
                raise SyntaxError(f"La variable '{node.identifier}' est déjà definie.")

            self.identifier_counter[node.identifier] = -1
            self.data_section.append(f"{node.identifier} dq 0")

            if node.value is not None:
                visit_assign(self, node)

        if isinstance(node, AssignNode):
            visit_assign(self, node)

        if isinstance(node, PrintNode):
            visit_print(self, node)

    def get_identifier_counter(self, identifier: str):
        if identifier in self.identifier_counter:
            return self.identifier_counter[identifier]
        raise SyntaxError(f"La variable '{identifier}' n'est pas déclarée.")
