# Landon Graessle
# 17 October 2024
# P3HW1
# Calculate grades, and print with a letter grade

# Get grade floats from user

mod1_grade = float(input('Enter grade for Module 1: '))
mod2_grade = float(input('Enter grade for Module 2: '))
mod3_grade = float(input('Enter grade for Module 3: '))
mod4_grade = float(input('Enter grade for Module 4: '))
mod5_grade = float(input('Enter grade for Module 5: '))
mod6_grade = float(input('Enter grade for Module 6: '))

grades = []

# Add grades to list

grades.append(mod1_grade)
grades.append(mod2_grade)
grades.append(mod3_grade)
grades.append(mod4_grade)
grades.append(mod5_grade)
grades.append(mod6_grade)

# Print average, maximum, minimum, and sum

length = len(grades)
avg = sum(grades) / length

print(grades)
print("----------Results----------")
print(f"{'Lowest Grade:':<20} {min(grades):<20,.2f}")
print(f"{'Highest Grade:':<20} {max(grades):<20,.2f}")
print(f"{'Sum of Grades:':<20} {sum(grades):<20,.2f}")
print(f"{'Average:':<20} {avg:<20,.2f}")
print("-" * 27)

# Calculate letter grade based on avergae grade

letter = ''

if avg >= 90:
    letter = 'A'
elif avg >= 80:
    letter = 'B'
elif avg >= 70:
    letter = 'C'
elif avg >= 60:
    letter = 'D'
else:
    letter = 'F!'

print(f"{'Your grade is:':<20} {letter:<20}")
