
"""
Double List Elements
Write a function double_list that takes a list of numbers and returns a new list where each element is doubled. Use a loop instead of map().
Example:

Input: double_list([1, 2, 3])
Output: [2, 4, 6]
Input: double_list([5, 10])
Output: [10, 20]
"""


def double_list():
    numbers = [1, 2, 3, 4, 5]
    doubled_numbers = []

    for number in numbers:
        doubled_numbers.append(number * 2)

    return doubled_numbers


double_list()
print(double_list())
