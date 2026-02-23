# ---------------------------------------------------------
# File Name: triage.py
# Program: Hospital Emergency Triage System
# Description:
# Categorizes patient as Critical, Moderate, or Normal.
# Upgrades priority if age > 65 and condition is moderate.
# ---------------------------------------------------------

# Taking patient details
heart_rate_abnormal = input("Is heart rate abnormal? (yes/no): ").lower()
severe_injury = input("Is there severe injury? (yes/no): ").lower()
age = int(input("Enter patient age: "))

# Determine patient category
if heart_rate_abnormal == "yes" or severe_injury == "yes":
    category = "Critical"

else:
    category = "Moderate"

# Upgrade priority rule
if category == "Moderate" and age > 65:
    category = "Critical"

print("Patient Category:", category)