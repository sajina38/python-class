"""
ilter Even Numbers
Write a function get_evens that takes a list of numbers and returns a new list containing only the even numbers. Use a loop instead of filter().
Example:

Input: get_evens([1, 2, 3, 4])
Output: [2, 4]
Input: get_evens([5, 6, 7, 8])
Output: [6, 8]
"""


def get_evens(numbers):
    even_numbers = []
    for number in numbers:
        if number % 2 == 0:
            even_numbers.append(number)
    return even_numbers


print(get_evens([1, 2, 3, 4]))
