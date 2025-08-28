n = 5
for i in range(n):
    print("*", end="")
    for j in range(5-2*i):
        print("_", end="")
    print("*")