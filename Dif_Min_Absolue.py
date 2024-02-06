import sys

if len(sys.argv) < 3 :
    print("Erreur : Veuillez fournir au moins deux nombres")
    sys.exit(1)


    
tableau = [int (x) for x in sys.argv[1:]]
diff_min_abs = abs(tableau[0] - tableau[1])
for i in range(len(tableau)):
    for j in range(i+1, len(tableau)):
        diff = abs(tableau[i] - tableau[j])
        if diff < diff_min_abs:
            diff_min_abs = diff


print("La différence minimale absolue est :", diff_min_abs)
