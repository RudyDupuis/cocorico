from c_compiler import Compiler
from c_parser.ast_node import AssignNode, DeclareNode, NumberNode, StringNode


def visit_assign(
    compiler: Compiler,
    node: AssignNode | DeclareNode,
):
    if isinstance(node.value, NumberNode):
        compiler.identifier_counter[node.identifier] = compiler.counter
        num_label = f"num_{compiler.counter}"
        str_label = f"str_{compiler.counter}"
        size_label = f"size_{compiler.counter}"

        compiler.data_section.append(f"{num_label} dq {node.value.value}")
        compiler.data_section.append(f'{str_label} db "{str(node.value.value)}", 0')
        compiler.data_section.append(f"{size_label} dq {len(str(node.value.value))}")
        compiler.text_section.append(f"mov qword [{node.identifier}], {num_label}")

    if isinstance(node.value, StringNode):
        compiler.identifier_counter[node.identifier] = compiler.counter
        str_label = f"str_{compiler.counter}"
        size_label = f"size_{compiler.counter}"

        compiler.data_section.append(f"{str_label} db {node.value.value}, 0")
        compiler.data_section.append(f"{size_label} dq {len(node.value.value)}")
        compiler.text_section.append(f"mov qword [{node.identifier}], {str_label}")

    compiler.counter += 1
