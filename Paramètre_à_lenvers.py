import sys
arguments = sys.argv[1:]

if len(arguments)< 1:
    print("Erreur :Aucun argument fourni")
    sys.exit(1)
for arg in arguments[::-1]:
 print(arg, end=" ")