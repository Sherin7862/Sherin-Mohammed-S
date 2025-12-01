a = int(input("Enter a number: "))

limit = a if a % 2 != 0 else a - 1

result = []
num = 1

while num <= limit:
    result.append(num)
    num += 2

print(result)
