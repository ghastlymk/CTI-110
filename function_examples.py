# create user-defined functions

def my_animal(name, sound, pounds_food):
    print(f'the {name} makes a {sound} noise')
    print(f'the {name} eats {pounds_food} pounds in a day')
    print(f'the {name} eats {pounds_food * 7} pounds in a week')

# create main function

def main():
    print('the main function is executing')
    # call the my_animal function
    my_animal("lion", 'roar', 20)

# call the main function

if __name__ == '__main__':
    main()