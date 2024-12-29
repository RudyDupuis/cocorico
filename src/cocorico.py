import argparse
import os
import sys
from shared.errors_handler import print_error_message
from c_lexer import Lexer
from c_parser import Parser

parser = argparse.ArgumentParser(description="Exécuter un fichier Cocorico (.ccrc)")
parser.add_argument("fichier", help="Chemin du fichier Cocorico (.ccrc)")

args = parser.parse_args()

if not args.fichier.endswith(".ccrc"):
    print_error_message("Le fichier doit avoir l'extension '.ccrc'.")
    sys.exit()

if not os.path.exists(args.fichier):
    print_error_message(f"Le fichier {args.fichier} n'existe pas à cet endroit.")
    sys.exit()

try:
    with open(args.fichier, "r", encoding="utf-8") as file:
        lexer = Lexer(file)
        paser = Parser(lexer.get_lexer_tokens())

        # for token in lexer.get_lexer_tokens():
        #     print(token)

        for node in paser.get_program():
            print(node)


except FileNotFoundError:
    print_error_message(f"Le fichier {args.fichier} n'a pas été trouvé.")
except SyntaxError as error:
    print_error_message(f"{error}")
except Exception as error:
    print_error_message(f"Une erreur inattendue est survenue : {error}")
