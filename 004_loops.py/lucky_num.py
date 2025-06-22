lucky_number = 11
user_guess = 0

while user_guess != lucky_number:
    user_guess = int(input("Guess the number: "))
    if user_guess == lucky_number:
        print("You won")

    else:
        print("Try again")
