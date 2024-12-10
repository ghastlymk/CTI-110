# in class examples

def getUserSelection():

    num_items = int(input("How many items will you purchase? "))
    store_items = ['pencil', 'paper', 'notebook', 'folder', 'soda', \
                'graphics card', 'processor', 'case']
    print(*store_items)
    cart = []

    for item in range(num_items):
        user_input = input(f"Enter item #{item + 1}: ")
        while user_input not in store_items:
            print(f"{user_input} is not sold here!")
            user_input = input(f"Enter item #{item + 1}: ")
        cart.append(user_input)
    return(cart)    

def displayItems(cart):

    print()
    print("You are done shopping.")
    print()
    print('Here are the items you purchased: ')

    for i in cart:
        print(i)

# create main function

def main():
    print('welcome to the store')
    print()
    myCart = getUserSelection()
    displayItems(myCart)

# call main

if __name__ == '__main__':
    main()