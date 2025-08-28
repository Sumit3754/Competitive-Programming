num = int(input("Enter a number: "))
sub = 0
for i in range(1, num + 1, 2):
    print(i, end=' ')
    sub += i
print()
print("Sum of odd numbers:", sub)
print()