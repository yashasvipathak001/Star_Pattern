space = 0
for i in range(5, 0, -1):
    print("*" * i, end="")
    print(" " * space, end="")
    print("*" * i)
    print()
    space += 2

space = 8
for i in range(1, 6):
    print("*" * i, end="")
    print(" " * space, end="")
    print("*" * i)
    print()
    space -= 2
