from c_parser.ast_node import ASTNode
from c_parser.parsing_method.parse_declaration import parse_declaration
from c_parser.parsing_method.parse_assignment import parse_assignment
from c_parser.parsing_method.parse_print import parse_print
from shared.token.token_name_enum import TokenNameEnum
from shared.token.token import Token


class Parser:
    def __init__(self, tokens: list[Token]):
        self.ast: list[ASTNode] = []
        self.tokens = tokens
        self.position_on_tokens = 0
        self.parse()

    def current_token(self):
        return self.tokens[self.position_on_tokens]

    def consume(self):
        if self.position_on_tokens < len(self.tokens) - 1:
            self.position_on_tokens += 1

    def parse(self):
        instruction: list[Token] = []

        while self.current_token().name != TokenNameEnum.EOF:
            while self.current_token().name not in [
                TokenNameEnum.EOL,
                TokenNameEnum.EOF,
            ]:
                instruction.append(self.current_token())
                self.consume()

            if len(instruction) > 0:
                self.ast.append(self._parse_instruction(instruction))
                instruction.clear()

            self.consume()

    def _parse_instruction(self, instruction: list[Token]):
        if (
            instruction[0].name == TokenNameEnum.IDENTIFIER
            and instruction[1].name == TokenNameEnum.EQUALS
        ):
            return parse_assignment(instruction)

        if (
            instruction[0].name in [TokenNameEnum.NUMBER, TokenNameEnum.STRING]
            and instruction[1].name == TokenNameEnum.IDENTIFIER
        ):
            return parse_declaration(instruction)

        if instruction[0].name == TokenNameEnum.PRINT:
            return parse_print(instruction)

        raise SyntaxError(
            f"{instruction[0].position} : Cette instruction n'est pas valide : "
            + " ".join(token.value for token in instruction)
            + "."
        )

    def get_ast(self):
        return self.ast
