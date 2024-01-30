import sys

if len(sys.argv) != 2:
    print("Erreur : Veuillez fournir un seul argument entier")
    sys.exit(1)
    
try:
    n = int(sys.argv[1])
    if n < 0 :
       print("-1")
    else:
         a , b = 0 , 1
         for _ in range (n):
             a , b = b , a + b
         print(a)
except ValueError :
       print("Erreur : L'argument doit etre un entier ")
       sys.exit(1)