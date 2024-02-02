import sys 

import sys 

if len(sys.argv) !=2:
    print("Erreur : Veuillez fournir un seul argument .")
    sys.exit(1)
    

    
chaine = sys.argv[1]
if any(char.isdigit() for char in chaine):
    print("Erreur : Les entiers ne sont pas autorisés en argument .")
    sys.exit(1)


nouvelle_chaine = ""
compteur_lettres = 0 
for caractere in chaine: 
    if caractere.isalpha(): 
        if compteur_lettres % 2 == 0:
            nouvelle_chaine += caractere.upper()
        else:
            nouvelle_chaine += caractere
        compteur_lettres += 1
    else:
        nouvelle_chaine += caractere
print(nouvelle_chaine)

