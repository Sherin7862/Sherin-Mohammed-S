a = int(input("Enter a number: "))
terms = a if a % 2 != 0 else a - 1
series = [2 * i + 1 for i in range((terms + 1) // 2)]
print(", ".join(map(str, series)))
