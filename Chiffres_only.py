import sys
if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir un seul argument ")


chaine = sys.argv[1]
est_uniquement_chiffres = True
for caractere in chaine : 
    if not caractere.isdigit():
        est_uniquement_chiffres = False
        break
if est_uniquement_chiffres : 
    print("True \n La chaine ne contient que des chiffres .")
else: 
    print("False \n La chaine ne contient pas des chiffres .")