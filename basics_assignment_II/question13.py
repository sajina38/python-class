"""
Reverse All Strings
Write a function reverse_all that takes a list of strings and returns a new list where each string is reversed.
Example:

Input: reverse_all(["hello", "world"])
Output: ["olleh", "dlrow"]
Input: reverse_all(["python", "code"])
Output:
"""


def reverse_all(string_list):
    reversed_list = []
    for word in string_list:
        reversed_list.append(word[::-1])
    return reversed_list


print(reverse_all(["hello", "world"]))   # Output: ['olleh', 'dlrow']
