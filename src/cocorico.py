import argparse
import os
import sys
from utils.errors_handler import print_error_message

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
    with open(args.fichier, "r", encoding="utf-8") as f:
        for ligne in f:
            print(ligne.strip())
except FileNotFoundError:
    print_error_message(f"Le fichier {args.fichier} n'a pas été trouvé.")
except IOError as error:
    print_error_message(f"Impossible de lire le fichier : {error}")
except Exception as error:
    print_error_message(f"Une erreur inattendue est survenue : {error}")
