# Sum of first N natural numbers

limit = int(input("Enter limit: "))
total = 0
for i in range(1, limit + 1):
    total = total + i
print("Total Sum is:", total)
