# Landon Graessle
# 24 Semptember 2024
# P1HW2
# Travel expenses calculator

# Ask user info

budget = int(input("Enter Budget: "))
print()
destination = input("Enter your travel destination: ")
print()
gas = int(input("How much will you set aside for gas? "))
print()
accomodation = int(input("How much will you need for accomodations? "))
print()
food = int(input("How much will you need for food? "))

# Print travel expenses

print("----------Travel Expenses----------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accomodation:", accomodation)
print("Food:", food)

# Calculate remaining balance

balance = budget - gas - accomodation - food
print()
print("Remaining Blanace:", balance)
