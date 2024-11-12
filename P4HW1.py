# Landon Graessle
# 5 November 2024
# P4HW1
# Get number of scores from user, drop the lowest score, and calculate new average

# Get number of scores and values of scores

num_scores = int(input("How many scores do you want to enter? "))
grades=[]

# Use loops to determine valid inputs and add them to a list

for score in range(num_scores):
    score_value = int(input(f"Enter score #{score + 1}: "))
    while score_value > 100 or score_value < 0:
        print("Invalid score!")
        print("Score should be between 0 and 100")
        score_value = int(input(f"Enter score #{score + 1}: "))
    grades.append(score_value)

print(f"{'-' * 12} Results {'-' * 12}")
print(f"{'Lowest Score:':<16} {min(grades)}")

# Remove the lowest score and print the modified list

grades.remove(min(grades))

print(f"{'Modified List: ':<16} {grades}")

# Create and print average grades in both letter and number form

average_grade = sum(grades) / len(grades)
letter_grade = ""

if average_grade >= 90:
    letter_grade = 'A'
elif average_grade >= 80:
    letter_grade = 'B'
elif average_grade >= 70:
    letter_grade = 'C'
elif average_grade >= 60:
    letter_grade = 'D'
else:
    letter_grade = 'F!'

print(f"{'Scores Average:':<16} {average_grade:<10.2f}")
print(f"{'Letter Grade:':<16} {letter_grade:<10}")
print('-' * 31)
