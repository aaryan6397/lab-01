#  Sum of digits

n = int(input("Enter number: "))
sum_d = 0
while n > 0:
    sum_d += n % 10
    n //= 10
print("Sum of digits:", sum_d)