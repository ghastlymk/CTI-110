# Landon Graessle
# P4LAB2
# 31 October 2024
# Create a multiplication table with loops and only allow positive integers

# Use a while loop to run the program continuously

run_again = "yes"

while run_again == "yes" or run_again == "y".lower():
    user_int = int(input("Enter an integer: "))
    print()
    if user_int >= 0:
        for num in range(1,13):
            print(f"{user_int} * {num} = {user_int * num}")
    else:
        print("This program does not handle negative numbers!")
    print()
    run_again = input("Run the program again? ").lower()
    valid_inputs = ['yes', 'y', 'no', 'n']
    while run_again not in valid_inputs:
        print("Invalid input entered! Please say Yes or No.")
        run_again = input("Run the program again? ").lower()
    
# Loop ends here

print()
print("Exiting program...")
