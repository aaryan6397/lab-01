#  Fibonacci Series (up to 10 terms)

a, b = 0, 1
print("Fibonacci Series:")
for i in range(10):
    print(a, end=" ")
    a, b = b, a + b
print()