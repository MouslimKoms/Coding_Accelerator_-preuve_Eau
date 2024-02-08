import sys 

if len(sys.argv) < 2 :
    print("Erreur : Veuillez fournir au moins un élément à trier ")
    sys.exit(1)

elements = sys.argv[1:]

for i in range(len(elements)):
    min_index = i 
    for j in range(i+1, len(elements)):
        if elements[j] < elements[min_index] :
            min_index = j 
    elements[i], elements[min_index] = elements[min_index], elements[i]
print("Elements triés par ordre ASCII :",elements)