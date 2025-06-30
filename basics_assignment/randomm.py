"""
Question 9: Random Compliment
Create a list of 5 nice compliments (like "You are awesome!" or "Great job!"). 
Use the random module (specifically random.choice()) to pick one compliment randomly and print it.
"""
import random

compliments = ["You can do it!",
"You're awesome",
"Don't give up!",
"You inspire me",
"Great job!"]

print(random.choice(compliments))


"""
Question 10: Dice Roller
Write a program that simulates rolling a six-sided die. 
Use random.randint(1, 6) to pick a random number between 1 and 6.
Ask the user how many times they want to roll the die, then print the result of each roll.
"""


rolls = int(input("How many times do you want to roll the dice? "))

for i in range(1, rolls + 1):
    output = random.randint(1, 6)
    print(f"Roll {i}: {output}")
