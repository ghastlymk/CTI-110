# Landon Graessle
# 10 October 2024
# P2HW1
# Travel expenses calculator + receipt formatting

# Ask user info

destination = input("Enter your travel destination: ")
print()
budget = float(input("Enter Budget: "))
print()
gas = float(input("How much will you set aside for gas? "))
print()
accomodation = float(input("How much will you need for accomodations? "))
print()
food = float(input("How much will you need for food? "))

# Print travel expenses formatted similarly to a store receipt

print("----------Travel Expenses----------")
print(f"{'Travel Destination:':<30} {destination:<30}")
print(f"{'Initial Budget:':<30} ${budget:<30,.2f}")
print()
print(f"{'Fuel:':<30} ${gas:<30,.2f}")
print(f"{'Accomodation:':<30} ${accomodation:<30,.2f}")
print(f"{'Food:':<30} ${food:<30,.2f}")
print("-----------------------------------")

# Calculate remaining balance

balance = budget - gas - accomodation - food
print()
print(f"{'Remaining Balnace:':<30} ${balance:<30,.2f}")
