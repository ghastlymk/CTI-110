# Landon Graessle
# 3 October 2024
# P2LAB2
# Use dictionaries with user values

# Create the dictionary
cars = {"Camaro":18.21, "Prius":52.36, "Model S":110, "Silverado":26}

# Display keys only

keys = cars.keys()
print(keys)
print()

# Enter car and display miles per gallon

user_car = input("Enter a vehicle to see it's miles per gallon: ")
print()

# Display miles per gallon value for selected vehicle

print(f"The {user_car} gets {cars[user_car]} miles to the gallon.")
print()

# Ask user how far they will drive and calculate the amount of gas needed

distance = float(input(f"How many miles will you drive the {user_car}? "))

gallons = distance / cars[user_car]

print (f"{gallons:.2f} gallon(s) of gas are needed to drive the {user_car} {distance:.2f} miles.")
