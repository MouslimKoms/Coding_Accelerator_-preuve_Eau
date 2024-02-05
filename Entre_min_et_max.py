import sys
try:
    min_val = int(input("Entrer une valeur minimum ."))
    max_val = int(input("Entrer une valeur maximum ."))
except ValueError:
    print("Erreur : entrer invalide .")
    sys.exit()
    
if min_val >= max_val : 
    print("Erreur : La Valeur minimale doit ettre inférieur à la valeur maximale ")
    sys.exit()
else: 
    for i in range(min_val ,max_val):
        print(i, end=" ")