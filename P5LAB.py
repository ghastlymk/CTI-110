# Landon Graessle
# 14 November 2024
# P5LAB
# Get coin amounts and values from user input

import random

def calcCashBack():
    total_owed = round(random.uniform(0.01, 100.00), 2)
    print(f'You owe ${total_owed:.2f}')
    cash = float(input(f'How much cash will you pay? $'))
    cashBack = cash - total_owed
    return(cashBack)

def disperseCashback(cashBack):
    
    change = round(cashBack * 100)
    
    num_dollars = change // 100
    
    change = change - num_dollars * 100
    
    num_quarters = change // 25
    change = change - num_quarters * 25
    
    num_dimes = change // 10
    change = change - num_dimes * 10
    
    num_nickles = change // 5
    change = change - num_nickles * 5
    
    num_pennies = change
    change = change - num_pennies
    
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
            print(f"{num_nickles} nickel")
        else:
            print(f"{num_nickles} nickels")
    
    if num_pennies > 0:
        if num_pennies == 1:
            print(f"{num_pennies} penny")
        else:
            print(f"{num_pennies} pennies")

# Create main function

def main():
    print('Thank you for shopping!')
    cashBack = calcCashBack()
    print(f'Your change is: ${cashBack:.2f}')
    disperseCashback(cashBack)

# Call the main function

if __name__ == '__main__':
    main()