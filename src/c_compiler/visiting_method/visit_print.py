from c_compiler import Compiler
from c_parser.ast_node import PrintNode


def visit_print(compiler: Compiler, node: PrintNode):
    counter = compiler.get_identifier_counter(node.identifier)

    compiler.text_section.append(f"mov rsi, str_{counter}")
    compiler.text_section.append(f"mov rdx, [size_{counter}]")
    compiler.text_section.append("mov rax, 1")
    compiler.text_section.append("mov rdi, 1")
    compiler.text_section.append("syscall")

    # Line break
    compiler.text_section.append("mov rsi, newline")
    compiler.text_section.append("mov rdx, 1")
    compiler.text_section.append("mov rax, 1")
    compiler.text_section.append("mov rdi, 1")
    compiler.text_section.append("syscall")
