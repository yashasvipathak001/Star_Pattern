space = 0
for i in range(5, 0, -1):
    print("*" * i, end="")
    print(" " * space, end="")
    print("*" * i)
    space += 2
