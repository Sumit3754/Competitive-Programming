num = int(input("Enter a number: "))
add = 0
for i in range(2, num + 1, 2):
    print(i, end=' ')
    add += i
print()
print("Sum of even numbers:", add)