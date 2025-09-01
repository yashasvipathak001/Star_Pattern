for i in range(1, 6):
    n = 1
    for j in range(1, i+1):
        if j % 2 == 1:
            print(n, end=" ")
            n += 2
        else:
            print("*", end=" ")
    print()