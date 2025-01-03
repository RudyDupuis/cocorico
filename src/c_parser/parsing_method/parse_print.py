from c_parser.ast_node import PrintNode
from shared.token.token_name_enum import TokenNameEnum
from shared.token.token import Token


def parse_print(instruction: list[Token]):
    if (
        len(instruction) == 4
        and instruction[1].name == TokenNameEnum.LEFT_PAREN
        and instruction[2].name
        in [
            TokenNameEnum.IDENTIFIER,
            TokenNameEnum.NUMBER_LITERAL,
            TokenNameEnum.STRING_LITERAL,
        ]
        and instruction[3].name == TokenNameEnum.RIGHT_PAREN
    ):
        return PrintNode(instruction[2].value, instruction[2].position)

    raise SyntaxError(
        f"{instruction[0].position} : La méthode afficher doit s'écrire de cette manière -> afficher(paramètre), et le paramètre doit être un nombre, un texte ou une référence."
    )
