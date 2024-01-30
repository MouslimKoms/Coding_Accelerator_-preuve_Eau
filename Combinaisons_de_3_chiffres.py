for i in range(10):
    for j in range(10):
        for k in range(10):
            if i <= j and j <= k :
                if i != j and j != k and i != k:
                    print(f"{i}{j}{k}")