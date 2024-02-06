import sys

def my_bulle_sort(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

if len(sys.argv) < 2: 
    print("Erreur : Veuillez fournir au moins un nombre")
    sys.exit(1)


try:
    numbers = [int(x) for x in sys.argv[1:]]
except ValueError:
    print("Erreur : Les argument doivent etre des nombres")
    sys.exit(1)
    
result = my_bulle_sort(numbers)
print("Liste triée :", result)