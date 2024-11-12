# Landon Graessle
# 7 November 2024
# P4HW2
# Collect info from multiple employees and display it

# Create variables, and use a while loop to collect information from multiple people

employee_name = str(input("Enter an employee name or type 'exit' to end the program: "))
num_employees = 0
total_overtime_pay = 0
total_regular_pay = 0
total_gross = 0

while employee_name.lower() != 'exit':
    hours_worked = int(input(f"How many hours did {employee_name} work this week? "))
    pay_rate = float(input(f"What is {employee_name}'s hourly rate? "))
    if hours_worked > 40:

        # Calculate pay and overtime based off of the hours worked
        regular_pay = pay_rate * 40
        overtime = hours_worked - 40
        overtime_pay = overtime * (pay_rate * 1.5)
        gross_pay = overtime_pay + regular_pay
    else:

        # Calculate for pay
        regular_pay = pay_rate * hours_worked
        gross_pay = regular_pay
        overtime_pay = 0
        overtime = 0

    # Increment employee number and total pay
    num_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross += gross_pay

    # Print data and ask user if they want to run the program again
    print("-" * 86)
    print(f"{'Employee Name: ':<15} {employee_name:<15}")
    print(
        f"{'Hours Worked':<15} {'Pay Rate':<11} {'Overtime Hours':<17} {'Overtime Pay':<15} {'Regular pay':<14} {'Gross Pay':<9}")
    print("-" * 86)
    print(f"{hours_worked:<15,.2f} {pay_rate:<11,.2f} {overtime:<17,.2f} {overtime_pay:<15,.2f} {regular_pay:<14,.2f} {gross_pay:<9,.2f}")
    employee_name = str(input("Enter an employee name or type 'exit' to end the program: "))

print(f"Total number of employees paid: {num_employees}")
print(f"Total amount paid for overtime: {total_overtime_pay:.2f}")
print(f"Total amount paid for regular hours: {total_regular_pay:.2f}")
print(f"Total amount paid in gross: {total_gross:.2f}")
