import sys 

if len(sys.argv) != 2:
    print("-1")
    sys.exit(1)


try:
    n = int(sys.argv[1])
    if n < 2 :
        print("-1")
    else:
        found = False
        while not found:
            n += 1
            for i in range (2 , int (n ** 0.5) +1):
                if n % i == 0:
                    break
            else:
                found = True
                print(n)
except ValueError:
    print("-1")