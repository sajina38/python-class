
fruits = []

def display_menu():
    print("""
____MENU____

1. Display fruits
2. Add fruits
3. Update fruits
4. Delete fruits
5. Exit program

                    """)

def add_fruits():

    count = int(input("How many fruits do you want to enter?"))
    for i in range(1, count + 1):
        fruit_name = input("enter a fruit name: ")
        fruits.append(fruit_name)

    print("All fruits added successfully")

def display_fruits():
    for fruit in fruits:
        print(fruit)

def delete_fruits():
    display_fruits()
    deletion_index = int(input("Enter an index to delete: "))
    delete_fruits

def update_fruits():
    display_fruits()
    update_index = int(input("Enter an index to update: "))


while True:

    display_fruits()
    user_choice = input("Enter your choice")
    if user_choice == '1':
        add_fruits()

    elif user_choice == '2':
        add_fruits()

    elif user_choice == '3':
        update_fruits()

    elif user_choice == '5':
        print("Exiting program")
        break

    else:
        print("Invalid choice")