n = int(input("Enter number (1-7): "))
days = {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday",
        5: "Thursday", 6: "Friday", 7: "Saturday"}
print(days.get(n, "Invalid input"))
