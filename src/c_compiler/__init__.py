from c_parser.ast_node import *


class Compiler:
    def __init__(self, ast: list[ASTNode]):
        self.ast = ast
        self.data_section: list[str] = []
        self.text_section: list[str] = []
        self.counter = 0
        self.symbols: set[str] = set()

    def compile(self):
        self.text_section.append("section .text")
        self.text_section.append("global _start")
        self.text_section.append("_start:")

        for node in self.ast:
            self.visit(node)

        self.text_section.append("mov rax, 60")  # syscall: exit
        self.text_section.append("xor rdi, rdi")  # exit code 0
        self.text_section.append("syscall")

        data = "\n".join(self.data_section)
        text = "\n".join(self.text_section)
        return f"{text}\n\nsection .data\n{data}"

    def visit(self, node: ASTNode):
        if isinstance(node, DeclareNode):
            if node.identifier not in self.symbols:
                self.data_section.append(f"{node.identifier} dq 0")
                self.symbols.add(node.identifier)
            else:
                raise SyntaxError(f"La variable '{node.identifier}' est déjà definie.")

            if node.value is not None:
                self.visit_assign(node)

        if isinstance(node, AssignNode):
            self.visit_assign(node)

        if isinstance(node, PrintNode):
            self.visit_print(node)

    def visit_assign(self, node: AssignNode | DeclareNode):
        if isinstance(node.value, NumberNode):
            self.text_section.append(
                f"mov qword [{node.identifier}], {node.value.value}"
            )
        if isinstance(node.value, StringNode):
            str_label = f"str_{self.counter}"
            self.data_section.append(f"{str_label} db {node.value.value}, 0")
            self.text_section.append(f"mov qword [{node.identifier}], {str_label}")
            self.counter += 1

    def visit_print(self, node: PrintNode):
        self.text_section.append(f"mov rsi, [{node.identifier}]")
        self.text_section.append("mov rdx, 1000")
        self.text_section.append("mov rax, 1")  # syscall: write
        self.text_section.append("mov rdi, 1")  # stdout
        self.text_section.append("syscall")
