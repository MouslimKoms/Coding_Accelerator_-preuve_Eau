import sys

if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir un seul argument .")
    sys.exit(1)

chaine = sys.argv[1]
if any(char.isdigit() for char in chaine):
    print("Erreur : Les entiers ne sont pas autorisées en argument .")
    sys.exit(1)
nouvelle_chaine = ""
nouveau_mot = True
for caractere in chaine:
    if caractere.isalpha():
        if nouveau_mot:
            nouvelle_chaine += caractere.upper()
            nouveau_mot = False
        else: 
            nouvelle_chaine += caractere.lower()
    else:
        nouvelle_chaine += caractere
        nouveau_mot = True
print(nouvelle_chaine)