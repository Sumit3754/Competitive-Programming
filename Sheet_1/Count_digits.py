num = int(input("Enter a number: "))
if num % 10 == 0:
    count = 0
    while num > 0:
        digit = num % 10
        if digit != 0:
            count += 1
            num = num // 10 
        else:
            