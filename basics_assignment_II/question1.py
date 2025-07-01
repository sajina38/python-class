"""
Reverse a String
Write a function reverse_string that takes a string as input and 
returns the string reversed.
Example:

Input: reverse_string("hello")
Output: "olleh"
Input: reverse_string("Python")
Output: "nohtyP"
"""

# user_input = input("Enter a string to reverse: ")

# reverse_string = user_input[::-1]
# print(reverse_string)


# def reverse_string(user_input):
#     return user_input[::-1]


# user_input = input("Enter a string to reverse: ")
# print(reverse_string(user_input))

def reverse_string(any_string):
    return any_string[::-1]


words = ["python", "hello", "Sajina"]
for i in words:
    print(reverse_string(i))
