
# Question 5: Weather Advice
user_input = float(input("Enter temperature: "))

if user_input > 30:
    print("It's hot! Wear sunglasses!")

elif user_input > 15 and user_input < 30:
    print("It's nice outside! Enjoy!")

else:
    print("It's cold! Wear a jacket!")


# Question 6: Even or Odd


number = int(input("Enter a number: "))

if number % 2 == 0:
    print("Even")

else:
    print("Odd")
