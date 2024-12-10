# Landon Graessle
# 20 November 2024
# P5HW
# Make a game using multiple functions

import random
import time

# Create characters and assign random health and attack numbers
def char_create():
    character = {
        'name': input("Enter your character's name: "),
        'health': random.randint(75, 200),
        'attack': random.randint(25, 75)
    }
    return character

# Display characters
def display_char(character):
    for key, value in character.items():
        print(f'{key}: {value}')

# Simulate the battle
def battle_turn(attacker, victim):
    print(f"{attacker['name']} struck {victim['name']}!")
    print()
    # Calculate damage
    damage = random.randint(0, attacker['attack'])
    print(f"{attacker['name']} did {damage} damage to {victim['name']}")
    # Apply damage to the victim's health
    victim['health'] -= damage
    # Ensure health doesn't go below zero
    victim['health'] = max(0, victim['health'])
    # Return the updated victim dictionary
    return attacker, victim

def display_menu():
    print('Choose your next action:')
    print('[1] Attack')
    print('[2] Heal')
    print('[3] Run')
    user_choice = int(input('Enter your choice: '))
    return user_choice

def heal():
    health_gained = random.randint(15,35)
    char1['health'] += health_gained
    print(f'{char1['name']} gained {health_gained}.')
    return char1

def main():
    print('Welcome!')

if __name__ == '__main__':
    main()
    char1 = char_create()
    char2 = char_create()
    print()
    display_char(char1)
    display_char(char2)
    print()
    user_choice = display_menu()
    # Loop that only runs while characters are alive (I don't know what's happening here)
    while char1['health'] > 0 and char2['health'] > 0:
        if user_choice == 1:
            # Simulate a battle turn
            time.sleep(5)
            char1, char2 = battle_turn(char1, char2)
            print()
            char2, char1 = battle_turn(char2, char1)
            display_char(char1)
            display_char(char2)
            user_choice = display_menu()
        if user_choice == 2:
            char1 = heal()
            display_char(char1)
            user_choice = display_menu()
        if user_choice == 3:
            char1['health'] = 0
            print(f'{char1['name']} fled the battle! {char2['name']} wins.')
        
    print('Game over.')