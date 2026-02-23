# ---------------------------------------------------------
# File Name: login.py
# Program: Smart Login System
# Description:
# Validates username & password.
# Locks account after 3 failed attempts.
# ---------------------------------------------------------

# Predefined credentials
correct_username = "admin"
correct_password = "1234"

attempts = 0  # Counter for failed attempts

# Allow maximum 3 attempts
while attempts < 3:
    username = input("Enter username: ")
    password = input("Enter password: ")

    if username == correct_username and password == correct_password:
        print("Login Successful!")
        break
    else:
        attempts += 1
        print("Invalid credentials. Attempts left:", 3 - attempts)

# Lock account after 3 failed attempts
if attempts == 3:
    print("Account locked due to 3 failed attempts.")