import sys

if len(sys.argv) == 1:
    print("Erreur : Veuillez fournir au moins un argument ")
    sys.exit(1)
elif len(sys.argv) > 3:
    print("Erreur : Trop d'arguments fournis")
    sys.exit(1)
    
for arg in sys.argv[1:]:
    if not arg.isalpha():
        print("Erreur : Les entier ne sont pas pris en charge ")
        sys.exit(1)

chaine1 = sys.argv [1]

if len(sys.argv) == 3:
    chaine2 = sys.argv[2]
else:
    chaine2 = None

if chaine2:
    if chaine1.endswith(chaine2):
        print("True")
    else:
        print("False")
else:
    print("Erreur : Veuillez fournir deux arguments . ")

    