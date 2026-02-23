# ---------------------------------------------------------
# File Name: increment.py
# Program: Salary Increment System
# Description:
# Calculates increment percentage based on:
# Performance rating, experience, and attendance.
# ---------------------------------------------------------

# Taking employee details
rating = int(input("Enter performance rating (1-5): "))
experience = int(input("Enter years of experience: "))
attendance = float(input("Enter attendance percentage: "))

increment = 0

# Performance based increment
if rating >= 4:
    increment += 10
elif rating == 3:
    increment += 5
else:
    increment += 2

# Experience bonus
if experience >= 5:
    increment += 5

# Attendance bonus
if attendance >= 90:
    increment += 3

print("Total Increment Percentage:", increment, "%")