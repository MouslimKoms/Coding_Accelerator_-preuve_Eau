import sys

if len(sys.argv) <3:
    print("Erreur : Veuillez fournir au moins deux arguments")
    sys.exit(1)
    
tableau = sys.argv[1:-1]

recherche = sys.argv[-1]

trouve = False 
for i in range(len(tableau)):
    if tableau[i] == recherche:
        print("L'élement",recherche,"a été trouvé à l'index ",i)
        trouve = True
        break

if not trouve:
    print("Lélément",recherche,"n'a pas été trouvé dans le tableau. -1")