"""
Write a program that uses a for loop to print the numbers 1 to 10, and for each number, 
print that many stars (*).For example, for the number 3, print ***.
 """
# for i in range(0, 10):
#     i += 1
#     print(i * "*")


""" 
Write a program that asks the user to enter a number between 1 and 10 using a while loop. 
Keep asking until they enter a number in that range. 
Once they do, print "Great choice!" and stop.
"""

user_input = 0

while user_input < 1 or user_input > 10:

    user_input = int(input("Enter any number: "))

    if user_input > 1 or user_input < 10:
        print("great")
    else:
        print(f"That's not between 1 and 10! Try again: {user_input}")
