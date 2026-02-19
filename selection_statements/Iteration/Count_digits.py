#  Count digits in a number

n = int(input("Enter number: "))
count = 0
while n > 0:
    n = n // 10
    count = count + 1
print("Number of digits:", count)