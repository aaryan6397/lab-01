#  Reverse a number

n = int(input("Enter number to reverse: "))
rev = 0
while n > 0:
    digit = n % 10
    rev = rev * 10 + digit
    n = n // 10
print("Reversed Number:", rev)