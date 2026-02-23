# ---------------------------------------------------------
# File Name: atm.py
# Program: ATM Withdrawal System
# Description:
# Checks balance, daily limit, and ATM cash availability.
# Displays appropriate failure message.
# ---------------------------------------------------------

# Taking account details
balance = float(input("Enter account balance: "))
withdraw_amount = float(input("Enter withdrawal amount: "))
atm_cash = float(input("Enter ATM available cash: "))

daily_limit = 50000  # Daily withdrawal limit

# Checking conditions
if withdraw_amount > balance:
    print("Transaction Failed: Insufficient account balance.")

elif withdraw_amount > daily_limit:
    print("Transaction Failed: Exceeds daily withdrawal limit (₹50,000).")

elif withdraw_amount > atm_cash:
    print("Transaction Failed: ATM has insufficient cash.")

else:
    balance -= withdraw_amount
    print("Withdrawal Successful!")
    print("Remaining Balance: ₹", balance)