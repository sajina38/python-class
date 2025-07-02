"""
FizzBuzz with a Twist (Loops and Conditionals)
Write a program that prints numbers from 1 to 50. For multiples of 3, print "Fizz"; for multiples of 5,
print "Buzz"; for multiples of both, print "FizzBuzz". Additionally, if the number is even, append "Even" to the output (e.g., 15 should print "FizzBuzzEven"). 
Use loops and conditionals to implement this.
"""

for i in range(1, 51):
    if i % 3 == 0:
        print("FIzz")

    if i % 5 == 0:
        print("Buzz")

    if i % 3 == 0 and i % 5 == 0:
        print("FizzBuzz")

    if i % 2 == 0:
        print("FizzBuzzEven")

    else:
        print(i)
