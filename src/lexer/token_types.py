DATA_TYPES = [
    ("NUMBER", r"nombre"),
    ("STRING", r"chaîne"),
    ("BOOLEAN", r"booléen"),
    ("LIST", r"liste"),
]

DECLARATIONS = [
    ("FUNCTION", r"fonction"),
    ("CONST", r"const"),
]

CONTROL_FLOW = [
    ("IF", r"si"),
    ("ELSE", r"sinon"),
    ("WHILE", r"tant que"),
    ("FOR", r"pour"),
    ("IN", r"dans"),
    ("RETURN", r"retour"),
    ("BREAK", r"arrêter"),
    ("CONTINUE", r"continuer"),
]

BOOLEAN_LOGIC = [
    ("TRUE", r"vrai"),
    ("FALSE", r"faux"),
    ("AND", r"et"),
    ("OR", r"ou"),
    ("NOT", r"non"),
]

FUNCTIONS = [
    ("PRINT", r"afficher"),
]

KEYWORDS = DATA_TYPES + DECLARATIONS + CONTROL_FLOW + BOOLEAN_LOGIC + FUNCTIONS

IDENTIFIERS_LITERALS = [
    ("IDENTIFIER", r"[a-zA-Z\u00C0-\u00FF_][a-zA-Z0-9\u00C0-\u00FF_]*"),
    ("INTEGER", r"\d+"),
    ("COMMA", r","),
    ("STRING_LITERAL", r'"[^"]*"'),
]

OPERATORS = [
    ("EQUALS", r"="),
    ("PLUS", r"\+"),
    ("MINUS", r"-"),
    ("MULTIPLY", r"\*"),
    ("DIVIDE", r"/"),
    ("MODULO", r"%"),
    ("LESS_THAN", r"<"),
    ("LESS_THAN_OR_EQUAL", r"<="),
    ("GREATER_THAN", r">"),
    ("GREATER_THAN_OR_EQUAL", r">="),
    ("EQUAL_EQUAL", r"=="),
    ("BANG_EQUAL", r"!="),
]

DELIMITERS = [
    ("LEFT_PAREN", r"\("),
    ("RIGHT_PAREN", r"\)"),
    ("LEFT_BRACE", r"\{"),
    ("RIGHT_BRACE", r"\}"),
    ("LEFT_BRACKET", r"\["),
    ("RIGHT_BRACKET", r"\]"),
]

MISC = [
    ("COMMENT", r"#.*"),
    ("WHITESPACE", r"\s+"),
]

TOKEN_TYPES = KEYWORDS + IDENTIFIERS_LITERALS + OPERATORS + DELIMITERS + MISC
