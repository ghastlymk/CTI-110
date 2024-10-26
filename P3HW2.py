# Landon Graessle
# 23 Oct 2024
# P3HW2
# Calculate pay and overtime with

# Get data from user and calculate overtime and pay

employee_name = str(input("Enter employee's name: "))
hours_worked = int(input("Enter number of hours worked: "))
pay_rate = float(input("Enter employee's pay rate: "))
overtime_pay = float()
overtime = float()
reghour_pay = float()

if hours_worked > 40:
    reghour_pay = pay_rate * 40
    overtime = hours_worked - 40
    overtime_pay = overtime * (pay_rate * 1.5)
    gross_pay = overtime_pay + reghour_pay
else:
    reghour_pay = pay_rate * hours_worked
    overtime == 0
    overtime_pay == 0
    gross_pay = reghour_pay

# Print information in a neat format

print("-" * 86)
print(f"{'Employee Name: ':<15} {employee_name:<15}")
print(f"{'Hours Worked':<15} {'Pay Rate':<11} {'Overtime Hours':<17} {'Overtime Pay':<15} {'Regular pay':<14} {'Gross Pay':<9}")
print("-" * 86)
print(f"{hours_worked:<15,.2f} {pay_rate:<11,.2f} {overtime:<17,.2f} {overtime_pay:<15,.2f} {reghour_pay:<14,.2f} {gross_pay:<9,.2f}")
