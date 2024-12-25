import argparse
import os
import sys
from utils.errors_handler import print_error_message
from lexer import Lexer

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
        for index, line in enumerate(file):
            lexer = Lexer(line, index + 1)
            print(lexer.get_tokens())

except FileNotFoundError:
    print_error_message(f"Le fichier {args.fichier} n'a pas été trouvé.")
except SyntaxError as error:
    print_error_message(f"{error}")
except Exception as error:
    print_error_message(f"Une erreur inattendue est survenue : {error}")
