from c_parser.ast_node import AssignNode, NumberNode, StringNode
from shared.token.token_name_enum import TokenNameEnum
from shared.token.token import Token


def parse_assignment(instruction: list[Token]):
    if len(instruction) == 3:
        if instruction[2].name == TokenNameEnum.NUMBER_LITERAL:
            return AssignNode(instruction[0].value, NumberNode(instruction[2].value))
        if instruction[2].name == TokenNameEnum.STRING_LITERAL:
            return AssignNode(instruction[0].value, StringNode(instruction[2].value))

    raise SyntaxError(
        f'{instruction[0].position} : La modification d\'une référence se fait de cette manière -> nom = valeur, et la valeur doit être un texte délimité par "" ou un nombre.'
    )
