
# Write a Python program to handle a ZeroDivisionError exception
#  when dividing a number by zero.
try:
    num = 10
    result = num / 0
except ZeroDivisionError:
    print("Not divisible by zero!")
