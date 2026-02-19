#  Simple Calculator (Using if-elif)

num1 = float(input("Enter first: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second: "))
if op == '+':
     print("Result:", num1 + num2)
elif op == '-': 
     print("Result:", num1 - num2)
elif op == '*':
     print("Result:", num1 * num2)
elif op == '/':
     print("Result:", num1 / num2)
else:
     print("Invalid Operator")