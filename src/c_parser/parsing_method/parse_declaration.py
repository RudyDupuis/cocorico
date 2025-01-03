from c_parser.ast_node import DeclareNode, NumberNode, StringNode
from shared.token.token_name_enum import TokenNameEnum
from shared.token.token import Token


def parse_declaration(instruction: list[Token]):
    if len(instruction) == 4 and instruction[2].name == TokenNameEnum.EQUALS:
        if instruction[3].name == TokenNameEnum.NUMBER_LITERAL:
            return DeclareNode(
                instruction[0].name,
                instruction[1].value,
                instruction[1].position,
                NumberNode(instruction[3].value, instruction[3].position),
            )
        if instruction[3].name == TokenNameEnum.STRING_LITERAL:
            return DeclareNode(
                instruction[0].name,
                instruction[1].value,
                instruction[1].position,
                StringNode(instruction[3].value, instruction[3].position),
            )

    if len(instruction) == 2:
        return DeclareNode(
            instruction[0].name, instruction[1].value, instruction[1].position
        )

    raise SyntaxError(
        f'{instruction[0].position} : La déclaration d\'une référence se fait de cette manière -> type nom = valeur, et la valeur doit être un texte délimité par "" ou un nombre.'
    )
