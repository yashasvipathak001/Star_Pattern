space = 4
for i in range(5, 0, -1):
    print("*", end="")
    for j in range(1, space):
        print(" ", end="")
    if i != 1:
        print("*", end="")
    print()
    space -= 1
