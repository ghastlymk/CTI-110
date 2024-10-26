# Landon Graessle
# 22 Oct 2024
# P3LAB
# Get coin amounts and values from user input

# Get money from user

money = float(input("Enter the amount of money you have: $"))

# Convert money to whole number

money = round(money * 100)

# Calculate the amount of whole dollars

num_dollars = money // 100

# Remove dollars and change from money variable

money = money - num_dollars * 100

num_quarters = money // 25
money = money - num_quarters * 25

num_dimes = money // 10
money = money - num_dimes * 10

num_nickles = money // 5
money = money - num_nickles * 5

num_pennies = money
money = money - num_pennies

if num_dollars > 0:
    if num_dollars == 1:
        print(f"{num_dollars} dollar")
    else:
        print(f"{num_dollars} dollars")

if num_quarters > 0:
    if num_quarters == 1:
        print(f"{num_quarters} quarter")
    else:
        print(f"{num_quarters} quarters")

if num_dimes > 0:
    if num_dimes == 1:
        print(f"{num_dimes} dime")
    else:
        print(f"{num_dimes} dimes")

if num_nickles> 0:
    if num_nickles == 1:
        print(f"{num_nickles} nickle")
    else:
        print(f"{num_nickles} nickles")

if num_pennies > 0:
    if num_pennies == 1:
        print(f"{num_pennies} penny")
    else:
        print(f"{num_pennies} pennies")
