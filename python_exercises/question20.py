# Write a Python program that executes an operation on a list and handles
#  an IndexError exception if the index is out of range.

my_list = [1, 2, 3]

try:
    print(my_list[5])
except IndexError:
    print("That index is out of range")