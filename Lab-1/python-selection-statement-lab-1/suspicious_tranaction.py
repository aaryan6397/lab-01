# ---------------------------------------------------------
# Program Name: suspicious_transaction.py
# Title: Banking – Suspicious Transaction Detection
# Description: This program checks whether a transaction
#              should be flagged for manual verification.
# Conditions:
#   1. Amount > 2,00,000
#   2. Account age < 6 months
#   3. Transaction is international
# ---------------------------------------------------------

# Taking transaction amount input from user
amount = float(input("Enter transaction amount: "))

# Taking account age in months
account_age = int(input("Enter account age in months: "))

# Checking whether transaction is international
international = input("Is the transaction international? (yes/no): ").lower()

# Applying selection statement with AND condition
if amount > 200000 and account_age < 6 and international == "yes":
    print("Transaction flagged for manual verification.")
else:
    print("Transaction is normal.")