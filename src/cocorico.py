import argparse
import os
import sys
import subprocess
from shared.errors_handler import print_error_message
from c_lexer import Lexer
from c_parser import Parser
from c_compiler import Compiler

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

        # for token in lexer.get_lexer_tokens():
        #     print(token)

        paser = Parser(lexer.get_lexer_tokens())

        # for node in paser.get_ast():
        #     print(node)

        compiler = Compiler(paser.get_ast())

        with open("build/output.asm", "w", encoding="utf-8") as file:
            file.write(compiler.compile())
        subprocess.run(
            ["nasm", "-f", "elf64", "build/output.asm", "-o", "build/output.o"],
            check=True,
        )
        subprocess.run(
            ["ld", "-s", "-o", "build/program", "build/output.o"], check=True
        )
        subprocess.run(["./build/program"], check=True)

except FileNotFoundError:
    print_error_message(f"Le fichier {args.fichier} n'a pas été trouvé.")
except SyntaxError as error:
    print_error_message(f"{error}")
except subprocess.CalledProcessError as error:
    print(f"Erreur dans le processus de compilation: {error}")
except Exception as error:
    print_error_message(f"Une erreur inattendue est survenue : {error}")
