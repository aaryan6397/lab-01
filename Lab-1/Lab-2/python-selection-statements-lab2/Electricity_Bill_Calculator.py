# ---------------------------------------------------------
# File Name: bill.py
# Program: Electricity Bill Calculator
# Description:
# Calculates electricity bill based on unit slabs.
# Applies 10% discount if user is senior citizen.
# ---------------------------------------------------------

# Taking units consumed input
units = float(input("Enter electricity units consumed: "))

# Checking if user is senior citizen
senior = input("Are you a senior citizen? (yes/no): ").lower()

# Initialize bill amount
bill = 0

# Applying slab rates
if units <= 100:
    bill = units * 5

elif units <= 300:
    bill = (100 * 5) + ((units - 100) * 7)

else:
    bill = (100 * 5) + (200 * 7) + ((units - 300) * 10)

# Applying 10% discount for senior citizen
if senior == "yes":
    bill = bill * 0.90  # 10% discount

# Display final bill
print("Total Electricity Bill: ₹", bill)